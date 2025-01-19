import pygetwindow as gw
import pytesseract
from PIL import ImageGrab
import cv2
import numpy as np
import re
import time
import interception
import subprocess
from typing import List, Tuple, Optional
from functools import wraps
from collections import defaultdict
from utils.pathfinding import a_star_map
from assets.grid import dofus_map
import ctypes

# GLOBALS
# I define window_name as a global because I don't want the llm to need to input it.
window_name = 'Iop'
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' # How to set this permanently ? 


def focus_window(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Access the global window_name variable
        try:
            result = subprocess.run(
                ["python", "utils/focus_window.py", window_name],
                capture_output=True,
                text=True,
            )
            print(result.stdout)
            if result.returncode != 0:
                print(result.stderr)
        except Exception as e:
            print(f"Error calling focus_window script: {e}")
        
        # Call the original function
        return func(*args, **kwargs)

    return wrapper



@focus_window
def get_position() -> tuple:
    """
    Get the coordinates of the player.

    Returns:
        tuple: A tuple containing the X and Y coordinates or None if coordinates are not found.
    
    Example:
        >>> get_position()
        Found coordinates: X = -5, Y = 10
        (-5, 10)
    """

    box_x=200
    box_y=150

    window = gw.getWindowsWithTitle(window_name)[0]

    left = window.left  # X coordinate of top-left corner
    top = window.top    # Y coordinate of top-left corner
    right = left + box_x   # X coordinate of the small box's bottom-right corner
    bottom = top + box_y   # Y coordinate of the small box's bottom-right corner

    # Capture a small box from the screen
    screen = np.array(ImageGrab.grab(bbox=(left, top, right, bottom)))

    # if needed to do more processing
    # screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
    # _, screen = cv2.threshold(screen, 210, 255, cv2.THRESH_BINARY)

    lower_bound = np.array([195, 195, 195])
    upper_bound = np.array([255, 255, 255])

    # # Create a mask to keep only pixels in the range
    screen = cv2.inRange(screen, lower_bound, upper_bound)

    # Dipslay image for verification
    # cv2.imshow("Captured Small Box", screen)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Perform OCR to extract text from the image
    extracted_text = pytesseract.image_to_string(screen).replace('S', '5').replace('O', '0').replace('G', '6')
    print("extracted_text", extracted_text)

    # Use regex to search for coordinates in the format "-X: -Y"
    match = re.findall(r'-?\d+\s*,\s*-?\d+', extracted_text)

    if match:
        x_coord, y_coord = match[0].split(",")
        y_coord = y_coord.strip()
        print(f"Found coordinates: X = {x_coord}, Y = {y_coord}")
    else:
        print("No coordinates found in the image.")
        
        return None

    return int(x_coord), int(y_coord)

# extracted_text = get_position()


def is_fullscreen(window):
    """
    Check if the window is in fullscreen mode.
    
    Args:
        window: pygetwindow Window object.
    
    Returns:
        bool: True if fullscreen, False otherwise.
    """
    user32 = ctypes.windll.user32
    screen_width = user32.GetSystemMetrics(0)
    screen_height = user32.GetSystemMetrics(1)

    return window.left == 0 and window.top == 0 and window.width == screen_width and window.height == screen_height

@focus_window
def get_screen_capture(window_name: str):
    """
    Captures a screenshot of the window.

    Args:
        window_name (str): The name of the window to capture from.
        
    Returns:
        numpy.ndarray: The captured screen as a NumPy array.
    """
    # Try to find the window with the given name
    window = gw.getWindowsWithTitle(window_name)[0]

    if window is None:
        print("Window not found!")
        return None

    if is_fullscreen(window):
        # Fullscreen mode, no adjustments needed
        left, top, right, bottom = window.left, window.top, window.left + window.width, window.top + window.height
    
    else: 
        title_bar_height = 0 # Typical window border height on Windows #test
        border_width = 8  # Typical window border width on Windows
        left = window.left + border_width
        top = window.top + title_bar_height
        right = window.left + window.width - border_width
        bottom = window.top + window.height - border_width

    # Capture a small box from the screen
    screen = np.array(ImageGrab.grab(bbox=(left, top, right, bottom)))

    # Convert from RGB to BGR for OpenCV
    screen_bgr = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)

    ## Display if needed
    # cv2.imshow("Captured Small Box", screen_bgr)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return screen_bgr


def load_item_image(image_folder, item_name):

    file_path = f'{image_folder}/{item_name}.png'
    try:
        template = cv2.imread(file_path)
        return template

    except:
        raise FileNotFoundError(f"Template image not found at path: {file_path}")
    
    

def find_item_coordinates(item_name:str) -> List[Tuple[int, int]]:
    """
    Finds a specific item coordinates (e.g., wheat) on the screen by template matching.

    Args:
        item_name (str): The name of the item to find, used to load the template image.

    Returns:
        List[Tuple[int, int]]: A list of tuples, each representing the coordinates of the center of 
                                detected items on the screen. If no items are found, an empty list is returned.
    Example:
        find_item_coordinates('wheat')
    """

    threshold=0.5
    nms_threshold=0.8
    color_matching=False

    # Focus on the game then take a screenshot
    time.sleep(1)
    screen = get_screen_capture(window_name)

    # cv2.imshow("Captured Small Box", screen)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    template = load_item_image('assets/objects', item_name)

    # Convert the screen to grayscale or HSV based on the color_matching flag
    if color_matching:
        # Convert both screen and template to HSV color space
        screen_hsv = cv2.cvtColor(screen, cv2.COLOR_BGR2HSV)
        template_hsv = cv2.cvtColor(template, cv2.COLOR_BGR2HSV)
    else:
        # Convert to grayscale if color matching is disabled
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # Perform template matching with either grayscale or HSV-based matching
    if color_matching:
        result = cv2.matchTemplate(screen_hsv, template_hsv, cv2.TM_CCOEFF_NORMED)
    else:
        result = cv2.matchTemplate(screen_gray, template_gray, cv2.TM_CCOEFF_NORMED)

    # cv2.rectangle(result, (320, 12), (1600, 921), (0, 255, 0), 2);
    # cv2.imshow("Captured Small Box", result)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Find locations where the result is above the threshold and in the clickable zone
    mask = np.zeros_like(result, dtype=bool)
    mask[12:921, 320:1600] = True
    locations = np.where(mask & (result >= threshold))
    coordinates = list(zip(*locations[::-1]))  # Reverse to get x, y as (x, y) tuples

    # Filter out overlapping boxes using Non-Maximum Suppression (NMS)
    boxes = []
    for (x, y) in coordinates:

        x2 = x + max(template.shape[1], 0)
        y2 = y + max(template.shape[0], 0)

        boxes.append([x, y, x2, y2])

    #     cv2.rectangle(screen, (x, y), (x2, y2), (0, 255, 0), 2);
    
    # cv2.imshow('Detected Wheat', screen)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # Apply Non-Maximum Suppression (NMS) to remove overlapping boxes
    indices = cv2.dnn.NMSBoxes(boxes, [1] * len(boxes), score_threshold=threshold, nms_threshold=nms_threshold)

    final_coordinates = []
    if len(indices) > 0:
        for i in indices.flatten():
            x1, y1, x2, y2 = boxes[i]
            # final_coordinates.append(((x1 + x2) // 2, (y1 + y2) // 2))  # Get center of each box    
            final_coordinates.append((x1, y1))
            # Optionally, you can draw rectangles on the screen to show detected wheat positions.
            cv2.rectangle(screen, (x1, y1), (x2, y2), (0, 255, 0), 2);
        
    cv2.imshow('Detected Wheat', screen)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return final_coordinates

# find_item_coordinates('ble')

@focus_window
def click_on_coordinates(list_of_coordinates: List[Tuple[int, int]]) -> str:
    """

    This function iterates through a list of (x, y) screen coordinates
    and performs a left mouse click at each specified position 
    with a delay between clicks.

    Args:
        list_of_coordinates (list): A list of tuples representing screen coordinates. 
                            Each tuple should contain two integers: 
                            the x and y positions (e.g., [(100, 200), (300, 400)])

    Returns:
        str: Return 'Done' once it clicked on everything

    """

    list_of_coordinates = eval(list_of_coordinates)

    for (x, y) in list_of_coordinates:
        interception.click(x, y, button="left", delay=2)
        print(f"Clicked at: {x}, {y}")
    
    return "Done"



@focus_window
def collect_item(item_name: str, quantity: Optional[int]=None) -> str:
    """
    Collects all available instances of a specified item on the map or a specified quantity.

    This function searches the game map for the specified item and collects it. If a quantity is specified,
    it collects up to that number of the item. Otherwise, it collects all available instances of the item.

    Args:
        item_name (str): The name of the item to collect from the map.
        quantity (Optional[int]): The number of items to collect. If not specified, collects all available items.

    Returns:
        str: A message indicating the result of the collection process. If a quantity is specified, returns
             the actual number of items collected. If all items are collected, returns a confirmation message.
    """

    if quantity is not None:
        # Get player inventory 
        initial_inventory = get_item_quantities_in_inventory([item_name])
        initial_count = initial_inventory.get(item_name, 0)
    
    item_coordinates = find_item_coordinates(item_name)

    if not item_coordinates:
        return f"No more {item_name} available on this map."

    time.sleep(0.5)

    for (x, y) in item_coordinates:        

        with interception.hold_key("shift"):
            interception.click(x, y, button="left")
            time.sleep(0.1)
            # print(f"Clicked at: {x}, {y}")

    # Wait for the collection process to complete (movement + pickup delays)
    time.sleep(3 + len(item_coordinates) *2.5)

    if quantity is not None:
        updated_inventory = get_item_quantities_in_inventory([item_name])
        final_count = updated_inventory.get(item_name, 0)
        collected_count = final_count - initial_count
        return f"Collected {collected_count} {item_name}(s)."

    return f"Collected all available {item_name} on this map."

# collect_item('ble', None)

@focus_window
def get_item_quantities_in_inventory(item_names: List[str]) -> dict:
    """
    Retrieves the quantities of specified items in the inventory.

    This function checks the inventory for the given item names and returns 
    the quantity of each item found.

    Args:
        item_names (List[str]): A list of item names to search for in the inventory.

    Returns:
        dict: A dictionary where the keys are item names and the values are 
              their corresponding quantities in the inventory.
    """

    def open_close_inventory():
        interception.press('i')

    def locate_on_screen(screen, name, debug=False):
        template = load_item_image('assets/inventory', name)
        template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
        result = cv2.matchTemplate(screen, template_gray, cv2.TM_CCOEFF_NORMED)

        location = np.where(result == np.max(result))

        [y], [x] = location

        x2 = x + template.shape[1]
        y2 = y + template.shape[0]

        if debug:
            cv2.rectangle(screen, (x, y), (x2, y2), (0, 255, 0), 2)
            cv2.imshow(f"{name}", screen)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        return x, y, x2, y2

    open_close_inventory()

    screen = get_screen_capture('Iop')
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    x_search_bar, y_search_bar, x2_search_bar, y2_search_bar = locate_on_screen(screen_gray, 'search_bar')

    # Click on the lookup bar
    interception.click(((x_search_bar + x2_search_bar) // 2, (y_search_bar + y2_search_bar) // 2)) 
    
    item_quantities = defaultdict(int)

    for item_name in item_names:

        item_quantity = 0

        # Type item name in the search bar
        for letter in item_name:
            interception.press(letter)

        # Take screenshot of the game (with inventory open and the name typed)
        screen = get_screen_capture('Iop')
        screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        
        x_item, y_item, x2_item, y2_item = locate_on_screen(screen_gray, item_name)

        region_with_text = screen[y_item:y_item + 20, x_item - 5 : x_item + 40]

        ## Remove color instead of gray might help for some items
        lower_bound = np.array([150, 150, 150])
        upper_bound = np.array([255, 255, 255])
        region_with_text = cv2.inRange(region_with_text, lower_bound, upper_bound)

        extracted_text = pytesseract.image_to_string(region_with_text, config='--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789')

        cv2.imshow('Detected Wheat', region_with_text)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print("extracted_text:", extracted_text)
        
        if not extracted_text:
            print("no text found")
        
        else:
            match = re.search(r'\b[0-9]{1,4}\b', extracted_text)
            item_quantity += int(match.group(0))
            # print("extracted_text", extracted_text)
            # print("item_quantity", item_quantity)
        item_quantities[item_name] = item_quantity

        interception.click(x2_search_bar - 10, y_search_bar)

    # Click a bit above the search bar (to unfocalise) then close inventory
    interception.click(x_search_bar, y_search_bar-50)
    open_close_inventory()

    return item_quantities

# item = get_item_quantities_in_inventory(['fer','ble', 'pain', 'ortie'])


@focus_window
def move_to(x: int, y: int) -> str:
    """
    Moves the player to the indicated coordinates

    Args:
        x (int): X coordinate of the player
        y (int): Y coordinate of the player

    Returns:
        str: A message indicating the final position of the player
    """

    current_x, current_y = get_position()

    start = (current_x, current_y)
    goal = (x ,y)
    path, visited = a_star_map(dofus_map, start, goal)

    print("path", path)

    time.sleep(1)

    for coordinates in path:

        direction = (coordinates[0] - current_x, coordinates[1] - current_y)

        # print("prochaine direction:", direction)

        if direction == (-1, 0): # left
            interception.click(221, 442, button="left")
            time.sleep(5)

        elif direction == (0, -1): # up
            interception.click(936, 29, button="left")
            time.sleep(5)

        elif direction == (1, 0): # right
            interception.click(1674, 492, button="left")
            time.sleep(5)

        elif direction == (0, 1): # down
            interception.click(676, 985, button="left")
            time.sleep(5)

        else:
            print("Wrong direction")

        current_x += direction[0]
        current_y += direction[1]

    return f"Moved to ({current_x, current_y})"

# move_to(4,-30)