import tkinter as tk
from tkinter import colorchooser
import sys


def main():
    window = tk.Tk()
    window.geometry("400x200")
    window.resizable(False, False)
    window.title("SNES Color Picker")
    img = tk.PhotoImage(file="./SNESColorPicker.png")
    window.iconphoto(False, img)
    canvas = tk.Canvas(window, width=1000, height=1000)
    canvas.pack()
    rectangle = canvas.create_rectangle(30, 40, 110, 120, fill='red')

    def findFont():
        useros = sys.platform
        if useros == "win32":
            userfont = "Segoe UI"
            fontsize = 10
        elif useros == "darwin":
            userfont = "SF Pro"
            fontsize = 14
        elif useros == "linux":
            userfont = "Arial"
            fontsize = 12
        return userfont, fontsize

    def updateText(hexColor, r, g, b, bit):

        hexColorText.configure(state='normal')
        hexColorText.delete(1.0, tk.END)
        hexColorText.insert('end', hexColor)
        hexColorText.configure(state='disabled')

        RColorText.configure(state='normal')
        RColorText.delete(1.0, tk.END)
        RColorText.insert('end', r)
        RColorText.configure(state='disabled')

        GColorText.configure(state='normal')
        GColorText.delete(1.0, tk.END)
        GColorText.insert('end', g)
        GColorText.configure(state='disabled')

        BColorText.configure(state='normal')
        BColorText.delete(1.0, tk.END)
        BColorText.insert('end', b)
        BColorText.configure(state='disabled')

        BitColorText.configure(state='normal')
        BitColorText.delete(1.0, tk.END)
        BitColorText.insert('end', bit)
        BitColorText.configure(state='disabled')

    def pickColor():
        color = colorchooser.askcolor('red', title="Choose a Color")

        rectangle = canvas.create_rectangle(30, 40, 110, 120, fill=(str(color[1])))

        r = bin(color[0][0] // 8)[2::].rjust(5, "0")
        g = bin(color[0][1] // 8)[2::].rjust(5, "0")
        b = bin(color[0][2] // 8)[2::].rjust(5, "0")

        hex1 = hex(int('0' + b + g[0:2], 2))[2::].rjust(2, '0')
        hex2 = hex(int(g[2::] + r, 2))[2::].rjust(2, '0')
        bit = hex2 + hex1

        updateText(color[1], color[0][0], color[0][1], color[0][2], str(bit))
        return color

    userfont, fontsize = findFont()

    pickColorButton = tk.Button(window, text="Select a Color", command=pickColor)
    pickColorButton.place(x=10, y=160)

    hexColorLabel = tk.Label(window, text="Hex Color", width=8, height=1)
    hexColorLabel.place(x=170, y=20)

    hexColorText = tk.Text(window, state='disabled', width=7, height=1, font=(userfont, fontsize))
    hexColorText.place(x=270, y=20)

    RColorLabel = tk.Label(window, text="R", width=8, height=1, justify=tk.RIGHT)
    RColorLabel.place(x=195, y=50)

    RColorText = tk.Text(window, state='disabled', width=3, height=1, font=(userfont, fontsize))
    RColorText.place(x=270, y=50)

    GColorLabel = tk.Label(window, text="G", width=8, height=1, justify=tk.RIGHT)
    GColorLabel.place(x=195, y=70)

    GColorText = tk.Text(window, state='disabled', width=3, height=1, font=(userfont, fontsize))
    GColorText.place(x=270, y=70)

    BColorLabel = tk.Label(window, text="B", width=8, height=1, justify=tk.RIGHT)
    BColorLabel.place(x=195, y=90)

    BColorText = tk.Text(window, state='disabled', width=3, height=1, font=(userfont, fontsize))
    BColorText.place(x=270, y=90)

    BitColorLabel = tk.Label(window, text="15-bit", width=4, height=1, justify=tk.RIGHT)
    BitColorLabel.place(x=200, y=120)

    BitColorText = tk.Text(window, state='disabled', width=4, height=1, font=(userfont, fontsize))
    BitColorText.place(x=270, y=120)

    window.mainloop()


if __name__ == "__main__":
    main()
