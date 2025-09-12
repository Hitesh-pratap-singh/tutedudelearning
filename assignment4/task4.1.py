try:
    with open('assignment4/sample.txt', 'r') as file:
        lines = file.readlines()
        lineCount = 0
        print("Reading File Content:")
        for line in lines:
            lineCount += 1
            print("Line", lineCount, ":", line.strip())
except FileNotFoundError:
    print("Error: File 'sample.txt' not found.")
