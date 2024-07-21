# import necessary packages
from tkinter import ttk, messagebox
from tkinter import *
from PIL import Image, ImageTk
import json
import requests

# creating GUI window & setting configurations
window = Tk()
window.geometry("300x320")  # dimensions of application window
window.title("GUI Currency Converter")
window.resizable(False, False)  # cannot resize the application window

# colours - main colours used in application
colour0 = "misty rose"
colour1 = "#333333"  # black
colour2 = "light steel blue"

# frames
top = Frame(window, width=300, height=60, bg=colour2)
top.grid(row=0, column=0)

main = Frame(window, width=300, height=460, bg=colour0)
main.grid(row=1, column=0)


# convert function - uses API
def convert():
    # #check if all fields are filled before converting
    # if not combo1.get() or combo2.get() or value.get():
    #     messagebox.showwarning("WARNING!", "You did not fill out all the fields")

    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"
    currency1 = combo1.get() #from
    currency2 = combo2.get() #to
    amount = value.get() #amount given by user
    querystring = {"from": currency1, "to": currency2, "amount": amount}

    # to display currency symbol in result frame
    if currency2 == "USD" or currency2 == "SGD" or currency2 == "CAD":
        symbol = "$"
    elif currency2 == "INR":
        symbol = "₹"
    elif currency2 == "EUR":
        symbol = "€"
    elif currency2 == "KRW":
        symbol = "₩"
    elif currency2 == "JPY" or currency2 == "CNY":
        symbol = "¥"
    elif currency2 == "GBP":
        symbol = "£"
    elif currency2 == "SAR":
        symbol = "SR"
    headers = {
        "x-rapidapi-key": "5156b0c5d0msh47617cc482472d5p1698d1jsn4d42ca61838c",
        "x-rapidapi-host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    data = json.loads(response.text)
    convertedAmount = data["result"]["convertedAmount"]
    formatted = symbol + "{:,.2f}".format(convertedAmount)

    result["text"] = formatted

    #log this value in terminal
    print(convertedAmount, formatted)

# icon in top frame
icon = Image.open("icon.png")
icon = icon.resize((40, 40))
icon = ImageTk.PhotoImage(icon)

# top frame's label
appName = Label(top, image=icon, compound=LEFT, text="Currency Converter", height=5, padx=13, pady=30, anchor=CENTER,
                font=("Arial", 16, "bold"), bg=colour2, fg=colour1)
appName.place(x=0, y=0)

# result frame
result = Label(main, text=" ", relief=SOLID, width=16, height=2, pady=7, anchor=CENTER, font=("Ivy", 15, "bold"),
               bg=colour0, fg=colour1)
result.place(x=50, y=10)

# list of currency
currency = ['SGD', 'USD', 'INR', 'CAD', 'EUR', 'KRW', 'JPY', 'GBP', 'CNY', "SAR"]

# from label
# combobox = dropdown
fromLabel = Label(main, text="From", width=8, height=1, padx=0, pady=0, anchor=NW, font=("Ivy", 10, "bold"), bg=colour0,
                  fg=colour1)
fromLabel.place(x=48, y=90)
combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy", 12))
combo1["values"] = (currency)
combo1.place(x=50, y=115)

# to label
toLabel = Label(main, text="To", width=8, height=1, padx=0, pady=0, anchor=NW, font=("Ivy", 10, "bold"), bg=colour0,
                fg=colour1)
toLabel.place(x=158, y=90)
combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=("Ivy", 12))
combo2["values"] = (currency)
combo2.place(x=160, y=115)

# entry - enter the amount
value = Entry(main, width=22, justify=CENTER, font=("Ivy", 12, "bold"), relief=SOLID)
value.place(x=50, y=155)

# button - "convert"
button = Button(main, text="Convert", width=19, padx=5, height=1, bg=colour2, fg=colour1, font=("Ivy", 12, "bold"),
                command=convert)
button.place(x=50, y=210)

window.mainloop()