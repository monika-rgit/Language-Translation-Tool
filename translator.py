from tkinter import *
from tkinter import messagebox
from deep_translator import GoogleTranslator

# Function
def translate_text():
    text = input_text.get("1.0", END).strip()

    if text == "":
        messagebox.showwarning("Warning", "Please enter some text")
        return

    try:
        translated = GoogleTranslator(source='en', target='ta').translate(text)

        output_text.delete("1.0", END)
        output_text.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Window
root = Tk()
root.title("Language Translation Tool")
root.geometry("600x450")

Label(root, text="Enter English Text", font=("Arial", 14)).pack(pady=5)

input_text = Text(root, height=6, width=60)
input_text.pack()

Button(root, text="Translate", font=("Arial", 12),
       command=translate_text).pack(pady=10)

Label(root, text="Tamil Translation", font=("Arial", 14)).pack()

output_text = Text(root, height=6, width=60)
output_text.pack()

root.mainloop()