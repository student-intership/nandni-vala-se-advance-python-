def handle_file_exceptions():
    file = None
    try:
        filename = input("Enter the filename to open: ")
        file = open(filename, 'r')
        print("File content:")
        print(file.read())  
        
    except FileNotFoundError:
        print("Error: The file was not found. Please check the filename and try again.")

    except IOError as e:
        print(f"Error: An I/O error occurred: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        if file:
            file.close()
            print("File closed.")
        else:
            print("No file to close.")


handle_file_exceptions()
