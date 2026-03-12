text = input("Enter the text to write to File: ")
with open("output.txt", "w") as file:
    file.write(text + "\n")
print("Data successfully written to output.txt")

more_text = input("Enter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(more_text + "\n")
print("Data successfully appended to output.txt")

print("\nFinal content to output.txt:")
with open("output.txt", "r") as file:
    print(file.read())
