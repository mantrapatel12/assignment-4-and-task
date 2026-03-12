# Python File Handling Assignments

## Introduction

This project contains two simple Python programs that demonstrate basic **file handling** concepts. The goal of these tasks is to understand how Python works with files — how to read data from a file, write data into a file, append additional information, and handle possible errors such as missing files.

These exercises helped in practicing fundamental Python concepts like **user input, loops, file modes, and error handling**.

---

# Task 1: Read a File and Handle Errors

## Objective

The purpose of this task is to create a Python program that reads a text file and prints its content line by line. The program should also handle situations where the file does not exist.

## Description

The program attempts to open a file named **sample.txt** and read its content. Each line of the file is displayed with a line number to make the output clearer.

To make the program more reliable, error handling is implemented using **try and except**. If the file does not exist, the program prints a clear error message instead of crashing.

## Features

* Opens and reads a text file.
* Displays the file content line by line.
* Shows line numbers for better readability.
* Handles the **FileNotFoundError** if the file is missing.

## Example Output

If the file exists:

```
Reading file content:
Line 1: This is a sample text file.
Line 2: It contains multiple lines.
```

If the file does not exist:

```
Error: The file 'sample.txt' was not found.
```

## Concepts Used

* File opening (`open`)
* Read mode (`"r"`)
* Loop for reading lines
* Exception handling (`try-except`)

---

# Task 2: Write, Append, and Read a File

## Objective

The goal of this task is to create a Python program that:

1. Takes user input and writes it to a file.
2. Appends additional information to the same file.
3. Reads and displays the final content of the file.

## Description

The program first asks the user to enter some text. This text is written to a file named **output.txt** using write mode.

Next, the program asks for additional text and appends it to the same file using append mode.

Finally, the program opens the file again in read mode and displays the complete content to the user.

## Features

* Accepts input from the user.
* Writes data into a file.
* Appends additional data without deleting previous content.
* Reads and displays the final file content.

## Example Output

```
Enter text to write to the file: Hello, Python!
Data successfully written to output.txt.

Enter additional text to append: Learning file handling in Python.
Data successfully appended.

Final content of output.txt:
Hello, Python!
Learning file handling in Python.
```

## Concepts Used

* User input (`input()`)
* File write mode (`"w"`)
* File append mode (`"a"`)
* File read mode (`"r"`)
* Displaying file content

---

# Conclusion

These tasks provide a basic understanding of **file handling in Python**. By completing them, we learn how to read files, write data, append new information, and manage errors effectively. These skills are essential when working with real-world applications where programs often need to store and retrieve data from files.

Overall, these exercises are a good starting point for building confidence with Python’s file operations.
