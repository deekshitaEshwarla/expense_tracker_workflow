def main():
    print("Welcome")
    while True:
        try:
            text = input("> ").strip()
        
        except (KeyboardInterrupt, EOFError):
            print("\nCancelled")
            break
        command = text.lower()
        if not text:
            continue
        if command in ["exit", "quit"]:
            print("Exiting now...")
            break
        if command == "help":
            print("Available commands: exit, quit, help")
        else:
            print("You said: " + text)

if __name__ == "__main__":
    main()