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

f = open("expense.txt", "r")
total = 0
for x in f:
  if x != "":
    num = float(x)
    total += num

#print("The name is : " + name) 

entry2 = tk.Entry(fg="yellow", bg="blue", width=50)

label3 = tk.Label(window, text = "Your total expenses are: ")
label3['text'] = label3['text'][0:25] + str(round(total, 2))
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

      
    #print("The name is : " + name) 
    label3['text'] = label3['text'][0:25] + str(round(total, 2))
def clear_label(label2):
    label2.destroy()

def clear():
    f = open("expense.txt", "r+")
    f.truncate(0)
    f.close()
    label3['text'] = label3['text'][0:25] + str(0)

# ADD IN A NEGATIVE VALUE!
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

      
  #print("The name is : " + name) 
  label3['text'] = label3['text'][0:25] + str(round(total, 2))

button=tk.Button(window, text = 'Submit', 
                  command = submit) 
button.pack(fill=tk.X, pady=15, padx=20)


button2=tk.Button(window, text = 'Clear Total Balance', 
                  command = clear) 

label3.pack(fill=tk.X, padx=20, pady=10)
separator.pack(side='top', fill='x')



label4 = tk.Label(window, text = "Enter an amount to clear:").pack(fill=tk.X, padx=20, pady=10)

entry2.pack(fill=tk.X, padx=20)

button3=tk.Button(window, text = 'Clear', 
                  command = clear_amount) 
button3.pack(fill=tk.X, padx=20, pady=10)
button2.pack(fill=tk.X, padx=20, pady=10)

#name = entry.get()
#print(name)
window.mainloop()