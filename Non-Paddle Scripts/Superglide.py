import keyboard
import time

def press_keys():
    # Simulate pressing the space key
    keyboard.press('space')
    # Wait a very short time (one frame)
    time.sleep(1/144)  # Assuming 144 frames per second
    # Release the space key
    keyboard.release('space')

    # Simulate pressing the c key
    keyboard.press('c')
    # Wait a very short time (one frame)
    time.sleep(1/144)  # Assuming 144 frames per second
    # Release the c key
    keyboard.release('c')

def main():
    print("Press '9' to activate superglide...")
    # Listen for keypress events
    keyboard.on_press_key('9', lambda _: press_keys())
    # Keep the script running
    keyboard.wait('esc')

if __name__ == "__main__":
    main()
