from pynput import mouse, keyboard
from unidecode import unidecode
from inspect import signature

def normalize_string(input_str: str) -> str:
    """
    Normalize a string by removing accents, converting to lowercase, and removing non-alphanumeric characters.

    Args:
        input_str (str): The string to normalize.

    Returns:
        str: The normalized string.
    """

    # Remove accents
    normalized = unidecode(input_str)
    
    # Convert to lowercase
    normalized = normalized.lower()

    return normalized


def normalize_input(process_args=None):
    """
    Decorator to normalize specific string arguments by name.

    Args:
        process_args (list[str] or None): Names of arguments to normalize, or None to normalize all.

    Returns:
        callable: The wrapped function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Get the function's signature and bind arguments
            func_sig = signature(func)
            bound_args = func_sig.bind(*args, **kwargs)
            bound_args.apply_defaults()

            def normalize_value(value):
                if isinstance(value, str):
                    return normalize_string(value)
                elif isinstance(value, list):
                    return [normalize_string(v) if isinstance(v, str) else v for v in value]
                return value  # Don't process non-strings

            # Normalize arguments based on `process_args`
            for arg_name, value in bound_args.arguments.items():
                if process_args is None or arg_name in process_args:
                    bound_args.arguments[arg_name] = normalize_value(value)

            # Call the original function with normalized arguments
            return func(*bound_args.args, **bound_args.kwargs)

        return wrapper
    return decorator

def on_press(key):
    try:
        if key.char == 'x':  # Check if the 'x' key is pressed
            print(f"Mouse at: {mouse_controller.position}")
    except AttributeError:
        if key == keyboard.Key.esc:  # Check if the 'Esc' key is pressed
            print("Exiting...")
            return False
        
def main():
    print("Press 'x' to capture mouse location. Press 'Esc' to exit.")
    
    # Start keyboard listener
    with keyboard.Listener(on_press=on_press) as keyboard_listener:
        keyboard_listener.join()

if __name__ == "__main__":
    mouse_controller = mouse.Controller()
    main()