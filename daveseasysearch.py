from tkinter import *
import wikipedia

# backend
def get_data():
    entry_value = entry.get()
    answer.delete(1.0, END)
    try:
        answer_value = wikipedia.summary(entry_value)
        answer.insert(INSERT, answer_value)
    except:
        answer.insert(INSERT, "ERROR !\nPlease check your input and\\or internet connection.")

def author_data():
    vikas = "\nHi, I am Vikas Patel. I created this small app.\n\t***** DavesEasySearch *****\nThis small very helpful app is created for those\
 who needs to search something on internet but don't want to open the web browser."
    answer.delete(1.0, END)
    answer.insert(INSERT, vikas)
# backend complete
# app gui 
root = Tk()
root.title("DavesEasySearch - By Vikas Patel")
author_box = Frame(root)

author_box.pack(side = TOP)
# search box
search_box = Frame(root)
    # search query
entry = Entry(search_box,width = 40)
entry.pack()
search_button = Button(search_box,width = 20, text = "Search", command = get_data)
author = Button(search_box, text = "About this app", command = author_data)
search_button.pack(side = RIGHT)
author.pack(side = LEFT)
search_box.pack(side =  TOP)
# search box end

# result box
result_box = Frame(root)
    # scroll bar
scroll = Scrollbar(result_box)
scroll.pack(side = RIGHT, fill = Y)
    # answer window
answer = Text(result_box,width = 100,height = 25, yscrollcommand = scroll.set, wrap = WORD)
scroll.config(command = answer.yview)
answer.pack()
    # answer window end
result_box.pack()
root.mainloop()
