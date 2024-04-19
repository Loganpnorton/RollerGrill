import pyautogui
import time
import pyscreeze
import keyboard
import os

def check_for_image(image_path, threshold=0.8):
    try:
        position = pyscreeze.locateCenterOnScreen(image_path, confidence=0.6)
        return position
    except Exception as e:
        print(f"Error checking for image: {e}")
        return None

def click_on_position(position, clicks=1, delay=0.05):
    try:
        if position is not None:
            time.sleep(delay)  # Introduce a delay before clicking
            pyautogui.click(position, clicks=clicks)
            pyautogui.click(position, clicks=clicks)
            pyautogui.click(position, clicks=clicks)
            pyautogui.click(position, clicks=clicks)
            pyautogui.click(position, clicks=clicks)
            pyautogui.click(position, clicks=clicks)
            pyautogui.click(position, clicks=clicks)
            pyautogui.click(position, clicks=clicks)
            return True
    except Exception as e:
        print(f"Error clicking on position: {e}")
    return False

def scroll_down():
    pyautogui.scroll(-1000)

def main_loop(image_path):
    while True:
        # Check if "shieldcore.png" image is found with a lower threshold
        position = check_for_image(image_path, threshold=0.8)
        if position:
            # If found, click on it with a lower threshold and introduce a delay
            if click_on_position(position, clicks=3, delay=0.1):
                print("Image clicked")
                # Pause the script until the "0" key is pressed again
                while True:
                    if keyboard.is_pressed('0'):
                        print("Restarting the script")
                        return  # Exit the function if "0" key is pressed again
                    time.sleep(0.1)
                break  # Exit the loop if clicked and "0" key is pressed
        else:
            print("Image not found")
            # If image is not found, scroll down
            scroll_down()
            scroll_down()

def main():
    # Get the absolute file path of the image
    script_directory = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_directory, "shieldcore.png")
    
    print("Press '0' to start the script...")
    while True:
        # Check if the "0" key is pressed to start or stop the script
        if keyboard.is_pressed('0'):
            print("Starting the script...")
            break

    while True:
        # Call the main loop function
        main_loop(image_path)

if __name__ == "__main__":
    main()
