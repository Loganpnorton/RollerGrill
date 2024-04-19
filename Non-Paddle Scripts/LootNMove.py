import pyscreeze
import keyboard
import time

# Function to perform the specified movement actions
def perform_movement():
    # Alternate between moving left (A) and right (D) and jumping
    for _ in range(2):
        keyboard.press('a')  # Hold A key for a short duration
        time.sleep(0.2)  # Adjust the duration as needed
        keyboard.release('a')

        keyboard.press('space')  # Press space key (jump)
        time.sleep(0.1)  # Adjust the duration as needed
        keyboard.release('space')

        keyboard.press('d')  # Hold D key for a short duration
        time.sleep(0.2)  # Adjust the duration as needed
        keyboard.release('d')

        keyboard.press('space')  # Press space key (jump)
        time.sleep(0.1)  # Adjust the duration as needed
        keyboard.release('space')

    # Move left slightly less time and hold shift
    keyboard.press('a')  # Hold A key for a shorter duration
    time.sleep(0.15)  # Adjust the duration as needed
    keyboard.release('a')

    keyboard.press('shift')  # Press shift key
    time.sleep(0.5)  # Hold shift key for a longer duration
    keyboard.release('shift')  # Release shift key

    # Move right the same amount of slightly less time and hold shift
    keyboard.press('d')  # Hold D key for a shorter duration
    time.sleep(0.15)  # Adjust the duration as needed
    keyboard.release('d')

    keyboard.press('shift')  # Press shift key
    time.sleep(0.5)  # Hold shift key for a longer duration
    keyboard.release('shift')  # Release shift key

# Function to continuously check for the presence of the images
def check_for_images(deathbox_path, supplybox_path):
    while True:
        deathbox_position = pyscreeze.locateCenterOnScreen(deathbox_path, confidence=0.8)
        if deathbox_position:
            perform_movement()  # Perform movement actions if deathbox is found
        supplybox_position = pyscreeze.locateCenterOnScreen(supplybox_path, confidence=0.8)
        if supplybox_position:
            perform_movement()  # Perform movement actions if supplybox is found

def main():
    print("Looking for deathbox.png and supplybox.png...")
    # Paths to the image files
    deathbox_path = "deathbox.png"  # Update with the correct path
    supplybox_path = "supplybox.png"  # Update with the correct path
    # Check for the presence of the images and perform movement actions
    check_for_images(deathbox_path, supplybox_path)

if __name__ == "__main__":
    main()
