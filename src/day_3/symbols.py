data = []

# Read the file and store each line in the data list
with open('input.txt', 'r') as file:
    data = [line.strip('\n') for line in file]

# Extract unique symbols from the data
symbols = set(char for line in data for char in line)

# Print the unique symbols
for symbol in symbols:
    if not symbol.isdigit():
        print(symbol)
