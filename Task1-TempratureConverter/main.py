"""Author: Rawan Khaled"""

import tkinter as tk

def convert_temperature():
    try:
        if conversion_choice.get() == "Fahrenheit to Celsius":
            fahrenheit = float(entry_temperature.get())
            celsius = (fahrenheit - 32) * 5/9
            result_label.config(text=f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius")
        elif conversion_choice.get() == "Celsius to Fahrenheit":
            celsius = float(entry_temperature.get())
            fahrenheit = (celsius * 9/5) + 32
            result_label.config(text=f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a valid temperature.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("410x220")
root.config(bg="purple")
custom_font = ("Times New Roman", 14, "bold")
custom_font2 = ("Times New Roman", 10, "bold")

# Create a label
label = tk.Label(root, text="Select Conversion:", bg="purple", font=custom_font)
label.pack( pady=5)

# Create a dropdown menu for conversion choice
conversion_choices = ["Fahrenheit to Celsius", "Celsius to Fahrenheit"]
conversion_choice = tk.StringVar()
conversion_choice.set(conversion_choices[0])  # Set the default choice
conversion_dropdown = tk.OptionMenu(root, conversion_choice, *conversion_choices)
conversion_dropdown.pack( pady=5)

# Create an entry field for temperature input
entry_label = tk.Label(root, text="Enter Temperature:", bg="purple", font=custom_font2)
entry_label.pack(pady=5)
entry_temperature = tk.Entry(root)
entry_temperature.pack(pady=5)

# Create a button to perform the conversion
convert_button = tk.Button(root, text="Convert", command=convert_temperature, bg="black",fg="white", width=10, height=2, font=custom_font2)
convert_button.pack(pady=10)

# Create a label to display the result
result_label = tk.Label(root, text="", font=("Helvetica", 14), bg="white", width=50 )
result_label.pack()

# Start the GUI main loop
root.mainloop()
