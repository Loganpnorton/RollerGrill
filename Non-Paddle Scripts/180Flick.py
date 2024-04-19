import pydirectinput
import keyboard

def rotate_180():
    # Simulate a quick mouse movement to rotate the player's view 180 degrees horizontally
    pydirectinput.moveRel(-400, 0)  # Move the mouse to the left (adjust the values as needed)
    
def main():
    print("Press '7' to perform a 180-degree flick.")
    while True:
        if keyboard.is_pressed('7'):
            print("180-degree flick performed")
            rotate_180()

if __name__ == "__main__":
    main()
