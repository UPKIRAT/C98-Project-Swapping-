intro = input("Hey! Welcome to SWAP THE STUFF! Click enter to continue ")
print(" ")

getting_file1 = input("Enter the first file path/name with its extension: ")
getting_file2 = input("Enter the second file path/name with its extension: " )

data_of_file1 = open(getting_file1, 'r').read()
data_of_file2 = open(getting_file2, 'r').read()

print(" ")
print("This is the data of the first file: ")
print("     " + data_of_file1)

print(" ")

print("This is the data of the second file: ")
print("     " + data_of_file2)


print(" ")

message = input("Do you want to swap the data of both the files?(yes/no) ")
print(" ")

if str(message) == "yes":
    write_to_file1 = open(getting_file1, 'w')
    write_to_file1.write(data_of_file2)

    write_to_file2 = open(getting_file2, 'w')
    write_to_file2.write(data_of_file1)
    print("Done! Data of both the files have been swapped! Go check!")