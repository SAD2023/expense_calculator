# imports tkinter and time
import tkinter as tk
from tkinter import ttk
import time

# create the window
window = tk.Tk()

# create the seperator for the window (horizontal line in the middle)
separator = ttk.Separator(window, orient='horizontal')

# rename the title of the window to "Calculate Expense"
window.title("Calculate Expense")

# create and pack the top label asking you to input your expenses
label = tk.Label(window, text = "Input your new expenses below:").pack(fill=tk.X, pady=20, padx=20)

# create and pack the first entry for users to input their new expenses
entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack(fill=tk.X, padx=20)

# open the text file and calculate the total 
f = open("expense.txt", "r")
total = 0
for x in f:
  if x != "":
    num = float(x)
    total += num

# create the second entry for users to input an amount to remove
entry2 = tk.Entry(fg="yellow", bg="blue", width=50)

# create label for total expenses and pack it.
label3 = tk.Label(window, text = "Your total expenses are: ")
label3['text'] = label3['text'][0:25] + str(round(total, 2))

# Function is called when the first entry is submitted
"""
  - Gets the text from the entry
  - Deletes the text from entry display
  - Tries to convert to float, open the text file and add the amount
  - If try block fails, it creates a new label asking the user to enter a 
    number, packs it in the window, and calls clear_label to get rid of it
    after 2000 ms.
  - Calculates the total in the file (to two decimal points) and displays it 
  in label3
"""
def submit(): 
    counter = 0
    text=entry.get() 
    entry.delete(0, tk.END)
    try: 
      (float(text))
      #print(float(text))
      f = open("expense.txt", "a")
      f.write(text + "\n")
      f.close()
      counter += 1

    except ValueError:  
      label2 = tk.Label(window, text = "Please enter a number!")
      label2.pack(fill=tk.X, pady=20, padx=20)
      window.after(2000, clear_label, label2)

    f = open("expense.txt", "r")
    total = 0
    for x in f:
      num = float(x)
      total += num

    label3['text'] = label3['text'][0:25] + str(round(total, 2))

# function called by submit
"""
  Takes a label as argument and destroys it.
"""
def clear_label(label2):
    label2.destroy()

"""
  Opens expense.txt and clears everything.
"""
def clear():
    f = open("expense.txt", "r+")
    f.truncate(0)
    f.close()
    label3['text'] = label3['text'][0:25] + str(0)

# Called when the second entry is submitted
"""
  - Gets the text from entry2
  - Deletes the text from entry2 display
  - Tries to convert to float, open the text file and add the amount with a 
    negative sign.
  - If try block fails, it creates a new label asking the user to enter a 
    number, packs it in the window, and calls clear_label to get rid of it
    after 2000 ms.
  - Calculates the total in the file (to two decimal points) and displays it 
  in label3
"""
def clear_amount():
  text=entry2.get() 
  entry2.delete(0, tk.END)
  try: 
    (float(text))
    #print(float(text))
    f = open("expense.txt", "a")
    f.write("-" + text + "\n")
    f.close()

  except ValueError:  
    label2 = tk.Label(window, text = "Please enter a number!")
    label2.pack(fill=tk.X, pady=20, padx=20)
    window.after(2000, clear_label, label2)

  f = open("expense.txt", "r")
  total = 0
  for x in f:
    num = float(x)
    total += num

  label3['text'] = label3['text'][0:25] + str(round(total, 2))


# the submit button for the first entry, calls submit() when clicked 
button=tk.Button(window, text = 'Submit', 
                  command = submit) 
button.pack(fill=tk.X, pady=15, padx=20)

# the button for clearing all, calls clear() when clicked
button2=tk.Button(window, text = 'Clear Total Balance', 
                  command = clear) 

# packs label3
label3.pack(fill=tk.X, padx=20, pady=10)
separator.pack(side='top', fill='x')

# label for the second entry to input an amount to clear
label4 = tk.Label(window, text = "Enter an amount to clear:").pack(fill=tk.X, padx=20, pady=10)

# packs entry2
entry2.pack(fill=tk.X, padx=20)

# creates and packs the third button, and packs the second button
button3=tk.Button(window, text = 'Clear', 
                  command = clear_amount) 
button3.pack(fill=tk.X, padx=20, pady=10)
button2.pack(fill=tk.X, padx=20, pady=10)

# runs the window
window.mainloop()