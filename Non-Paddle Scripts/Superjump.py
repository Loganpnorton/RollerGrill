import keyboard
import time
import pyautogui

def turbo_jump():
    # Simulate pressing the 'e' key
    keyboard.press('e')
    keyboard.release('e')
    # Wait for 0.25 seconds
    time.sleep(0.05)
    # Simulate a big mouse scroll down
    pyautogui.scroll(-1000)
    pyautogui.scroll(-1000)
    pyautogui.scroll(-1000)
    pyautogui.scroll(-1000)

def main():
    print("Press '8' to perform the turbo jump...")
    # Listen for keypress events
    keyboard.on_press_key('8', lambda _: turbo_jump())
    # Keep the script running
    keyboard.wait('esc')

if __name__ == "__main__":
    main()
