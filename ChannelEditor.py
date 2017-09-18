import glob
from Tkinter import *
from RasPiVideoRandomizer import play_raspivideorandomizer

window = Tk();

channels_listbox = Listbox(window)
channels_listbox.pack()

channels = glob.glob("Channels/*.json")
for channel in channels:
    channels_listbox.insert(END, channel)

b = Button(window, text = "Play Channel", command = window.quit)
b.pack()

window.mainloop()

selected_channel = channels_listbox.get(channels_listbox.curselection())
print selected_channel
window.destroy()

play_raspivideorandomizer(selected_channel)
