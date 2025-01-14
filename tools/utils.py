from pynput import mouse, keyboard

def on_press(key):
    try:
        if key.char == 'x':  # Check if the 'x' key is pressed
            print(f"Mouse at: {mouse_controller.position}")
    except AttributeError:
        pass
def main():
    print("Press 'x' to capture mouse location. Press 'Esc' to exit.")
    
    # Start keyboard listener
    with keyboard.Listener(on_press=on_press) as keyboard_listener:
        keyboard_listener.join()

if __name__ == "__main__":
    # Initialize mouse controller
    mouse_controller = mouse.Controller()
    main()