try:
    data = input("Enter text to write to the file: ")
    file = open('assignment4/output.txt', 'w')
    file.write(data)
    print("Data successfully written to 'output.txt'")
    file.close()

    data = input("Enter additional text to append: ")
    file = open('assignment4/output.txt', 'a')
    file.write("\n")  # Adding a newline before appending
    file.write(data)
    print("Data successfully appended")
    file.close()

    with open('assignment4/output.txt', 'r') as file:
        lines = file.readlines()
        print("Final content of output.txt:")
        for line in lines:
            print(line.strip())
except FileNotFoundError:
    print("File Not Found")