import tkinter as tk

def convert():
    inputUnit = str(unitsInput.get())
    outputUnit = str(unitsOutput.get())
    output_index = PressureUNITS.index(outputUnit)
    try:
        entry = float(entry_input.get())
        multi = UNITSMULTIPIER[inputUnit][output_index]
        answer = entry*multi
    except:
        result_output["text"] = "Invalid Input"
    else:
        result_output["text"] = str(answer)#Answer casted as float

PressureUNITS = ["m", "Km", "mile", "inches"]

UNITSMULTIPIER = {
    "m":[1, 1000, 1609, 39.3700787],
    "Km": [0.001, 1, 1.609, 39370.0787],
    "mile": [1609.344, 1.609344,1, 63360],
    "inches": [0.0254, 0.0000254, 0.00001578, 1]
    }

window = tk.Tk()
window.title("Unit Convertor")

#Frame of a container
dropdown_frame = tk.Frame(master = window)
row_frame = tk.Frame(master= window)

#Creating an input dropdown
unitsInput = tk.StringVar(dropdown_frame)
unitsInput.set(PressureUNITS[1]) #Default units of Pa
dropdownInputs = tk.OptionMenu(dropdown_frame, unitsInput, *PressureUNITS)#Functions and its parameters
dropdownInputs.config(font = ("Arial, 19"))
dropdownInputs.grid(row=0, column=0, sticky="ew")

#Creating an output dropdown
unitsOutput = tk.StringVar(dropdown_frame)
unitsOutput.set(PressureUNITS[3]) #Default units of mmHg
dropdownOutputs = tk.OptionMenu(dropdown_frame, unitsOutput, *PressureUNITS)#Functions and its parameters
dropdownOutputs.config(font = ("Arial, 19"))
dropdownOutputs.grid(row=0, column=2, sticky="ew")#Sticky = ew, means that we want to stretch the column

#Constructing a label (an arrow to visually show)
lbl_arrow = tk.Label(master = dropdown_frame, anchor ="center", text = "\N{RIGHTWARDS BLACK ARROW}") #Not in windows but in the frame
#anchor centers the arrow
lbl_arrow.config(font= ("Arial", 25))
lbl_arrow.grid(row=0, column=1, sticky="ew")

dropdown_frame.grid(row=0, column = 0, padx = 10, pady = 10)

#Creating Input and Output
label_input = tk.Label(master = row_frame, text = "Input")
entry_input= tk.Entry(master = row_frame, width = "15")#Entry is for entering info in the input

label_input.grid(row = 1, column = 0, sticky = "ew", padx = (0, 10))
#No padding on the left and 10 padding towards the right. Padding creates space between them
entry_input.grid(row = 1, column = 1, sticky = "ew")
row_frame.grid(row = 1, column = 0, padx = 10, pady = 10)#The contanier starts @ top left

label_output = tk.Label(master = row_frame, text = "Output")
result_output = tk.Label(master = row_frame, relief = tk.SUNKEN) #Created a sinking effect in the screen
label_output.grid(row = 2, column = 0, sticky = "ew", padx = (0, 10))
result_output.grid(row = 2, column = 1, sticky = "ew")

btn_convert = tk.Button(master = window, text = "Convert", command = convert)
btn_convert.grid(row = 3, column = 0, padx = 10, pady = 10)



window.mainloop() #Like a while loop always running
