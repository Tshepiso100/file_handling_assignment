def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with some text and numbers: 987\n")
        print("File 'my_file.txt' created successfully.")
    except Exception as e:
        print("Error occurred while creating the file:", e)
    finally:
        print("File creation process completed.")

def read_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of 'my_file.txt':")
            print(file.read())
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied to access 'my_file.txt'.")
    except Exception as e:
        print("Error occurred while reading the file:", e)

def append_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Additional line 1\n")
            file.write("Appending some more text\n")
            file.write("Appending line with numbers: 54321\n")
        print("Text appended to 'my_file.txt' successfully.")
    except Exception as e:
        print("Error occurred while appending to the file:", e)
    finally:
        print("Appending process completed.")


create_file()

read_file()

append_file()
