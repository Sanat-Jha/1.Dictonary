from sys import version_info       #importing sys 
if version_info.major == 2:            #check version and import accordingly
    import Tkinter as tk
elif version_info.major == 3:
    import tkinter as tk
    

    
app = tk.Tk()           #initiate
labelExample = tk.Button(app, text="0")

def change_label_number(num):      #defining the function
    counter = int(str(labelExample['text']))
    counter += num
    labelExample.config(text=str(counter))
    
buttonExample = tk.Button(app, text="Increase", width=30,
                          command=lambda: change_label_number(2))

buttonExample.pack()
labelExample.pack()
app.mainloop()
