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
            for _ in range(clicks):
                pyautogui.click(position)
                pyautogui.click(position)
            return True
    except Exception as e:
        print(f"Error clicking on position: {e}")
    return False

def main_loop(image_path):
    while True:
        # Check if "shieldcore.png" image is found with a lower threshold
        position = check_for_image(image_path)
        if position:
            # If found, click on it with a lower threshold and introduce a delay
            if click_on_position(position, clicks=3, delay=0.05):
                print("Image clicked")
                # Pause the script until the "0" key is pressed again
                while True:
                    if keyboard.is_pressed('0'):
                        print("Restarting the script...")
                        break  # Exit the inner loop
                    time.sleep(0.1)
                break  # Exit the outer loop if clicked and "0" key is pressed
        else:
            print("Image not found")

def main():
    # Get the absolute file path of the image
    script_directory = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_directory, "shieldcore.png")
    
    print("Starting the script...")
    while True:
        # Call the main loop function
        main_loop(image_path)

if __name__ == "__main__":
    main()
