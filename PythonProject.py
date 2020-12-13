# CS 3080 Course/Main Project
# NIck Barcalow
# Lynel Peregrino
# Due date: 12/14/20
# Main program that calls the other two.
import os

# Main program that calls the other two.
def main():
    os.system('python ProjectSQ.py')   # calls database program
    os.system('python ProjectUI.py')   # calls UI program


if __name__ == "__main__":
    main()
