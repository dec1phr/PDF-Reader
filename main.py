import warnings

from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadWarning

# removes the warning and stuffs
warnings.filterwarnings("ignore", category=PdfReadWarning)


def txtCmd():
    while True:
        txtFile = input("Do you want to make a new text file?(y/n): ").lower()

        if txtFile == "y":
            return True

        elif txtFile == "n":
            return False

        else:
            print("Invalid input..")


def choice():

    while True:
        userChoice = input(
            "Do you want to make separate txt files for each pages of the PDF?(y/n): "
        ).lower()

        if userChoice == "y":
            return True

        elif userChoice == "n":
            return False

        else:
            print("Invalid input..")


def txtClear():

    while True:
        clearCommand = input(
            "Do you want to clear old contents from the text file and write new contents?(y/n): "
        ).lower

        if clearCommand == "y":
            return True

        elif clearCommand == "n":
            return False

        else:
            print("Invalid input..")


def txtFileDecisionMaker():
    txtCreate = (
        txtCmd()
    )  # Determines whether the user wants to create a new file or not
    if txtCreate == True:
        FileName = input("Name your file(without .txt extension): ").replace(
            " ", "-"
        )  # Creating new text
        with open(f"{FileName}.txt", "w") as file:
            pass
    else:
        FileName = input("Enter the address of your file: ")  # Giving an existing file

    return FileName


# ------------------Main Operations------------------
Pdf = input("Enter the path of the PDF file: ")
reader = PdfReader(Pdf)

txtFileDecision = txtFileDecisionMaker()

userStrt = int(input("Enter the index of the first page: "))
userEnd = int(input("Enter the index of the last page: "))

# --------------------------------------
# userBool = choice()
# txtClear = clearCmd()
# asdfjk
# if(usrClear==True):

# ---------------------------------------------------
with open(f"{txtFileDecision}.txt", "w", encoding="utf-8") as file:
    for i in range(userStrt - 1, userEnd):
        page = reader.pages[i]
        contents = page.extract_text().replace("\x00", "")
        file.write(contents + "\n")
