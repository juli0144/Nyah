import tkinter as tk

def Convert():
    input_meter = float(input_str.get().replace(",","."))
    in_inch = input_meter * 39.37
    convert_feet = int(in_inch / 12)
    convert_inch = round(in_inch - (convert_feet * 12), 1)
    output_str.set(str(convert_feet)+" foot and "+str(convert_inch)+" inch")

window = tk.Tk()

# Headline
text_label = tk.Label\
            (window, text="Meters in Feet and inch",
             font="ComicSans, 24")
text_label.pack()

# Input
input_frame = tk.Frame(window)
input_str = tk.StringVar()
input_entry = tk.Entry(input_frame, textvariable=input_str)
input_button = tk.Button(input_frame, text="Convert", font="Calibri", command=Convert)
input_entry.pack(side="left")
input_button.pack(side="left", padx= 10)
input_frame.pack()

# Output
output_str = tk.StringVar()
output_str.set("Output")
output_label = tk.Label(window, font="Calibri, 14", textvariable=output_str)
output_label.pack()

window.mainloop()