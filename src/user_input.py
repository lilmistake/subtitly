import inquirer
from inquirer import themes
import tkinter as tk
from tkinter import filedialog

def user_input():
    """ 
    Asks user for input and returns a list of the file path and the answers to the questions

    Returns
    ---
    [file_path, answers]
    """
    root = tk.Tk()
    root.withdraw()

    def validate(x):
        try:
            int(x)
            return True
        except:
            return False

    print("Select video file")
    file_path = filedialog.askopenfilename()
    print(f"✅ Opened File: {file_path}")

    questions = [
    inquirer.List('format',
                    message="What subtitle file format do you want?",
                    choices=['.srt','.vtt'],
                ),
        inquirer.Text('size', message="Minimum audio chunk size in seconds?\nSmaller chunks process faster but may be inaccurate",
            validate=lambda _, x: validate(x) or x < 1000,  default="30"
            ),
        inquirer.Text('volume', message="Silence threshold volume in dB",
            validate=lambda _, x: validate(x) , default="-40"
            ),
        inquirer.Text('silence', message="Minimum silence length in ms?",
            validate=lambda _, x: validate(x) , default="500"
            )
    ]
    answers = inquirer.prompt(questions, theme=themes.GreenPassion() )
    return [file_path, answers]