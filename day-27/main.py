import tkinter as tk

# window = tkinter.Tk()
# window.title("Tkinter")
# window.minsize(width=500, height=300)

# label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
# label.grid(row=1, column=1)

# def button_click():
#     new_text = input.get()
#     label.config(text=new_text)

# button1 = tkinter.Button(text="Click", command=button_click)
# button1.grid(row=2, column=2)
# button2 = tkinter.Button(text="new button")
# button2.grid(row=1, column=3)

# input = tkinter.Entry(width=10)
# input.grid(row=4, column=4)

root = tk.Tk()
root.title("Mike to Km Converter")
root.minsize(width=350, height=100)

def convert():
    miles = float(mile_input.get())
    km = miles * 1.609
    km_label.config(text=f"{km}")

mile_input = tk.Entry(width=10)
mile_input.grid(row=2, column=3)

miles_text = tk.Label(text="Miles")
miles_text.grid(row=2, column=4)

is_equal = tk.Label(text="is equal to")
is_equal.grid(row=3, column=1)

km_label = tk.Label(text="~")
km_label.grid(row=3, column=3)

convert_button = tk.Button(text="Convert", command=convert)
convert_button.grid(row=5, column=3)


root.mainloop()