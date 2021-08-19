import requests
from bs4 import BeautifulSoup
from tkinter import *
import os
from pandastable import Table
import pandas as pd
from tqdm import tqdm
import tkinter as tk
import glob

root = tk.Tk()
root.title('LaiSiangtho verse lak na')
root.geometry('500x700')

def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))

"""creating the canvas"""
canvas = tk.Canvas(root)
outerFrame = tk.Frame(canvas)
vscrollbar = tk.Scrollbar(root, orient='vertical', command=canvas.yview)
canvas.configure(yscrollcommand=vscrollbar.set)
vscrollbar.pack(side='right', fill='y')
canvas.pack(side='left', fill='both', expand=True)
canvas.create_window((10,10), window=outerFrame, anchor='nw')

outerFrame.bind('<Configure>', lambda event, canvas=canvas: on_configure(canvas))

"""creating the scraper"""
def urllookup():
    bookresult = requests.get(bookTextbox.get())
    chapterresult = requests.get(chapterTextbox.get())
    fromresult = requests.get(fromVerse.get())
    toresult = requests.get(toVerse.get())

    



"""Create the ui"""
book = tk.Label(outerFrame, text='Laibu min:')
book.pack()
bookTextbox = tk.Entry(outerFrame, width=30)
bookTextbox.pack()
bookTextbox.focus_set()
chapter = tk.Label(outerFrame, text='Chapter:')
chapter.pack()
chapterTextbox = tk.Entry(outerFrame, width=10)
chapterTextbox.pack()
chapterTextbox.focus_set()
fromVerse = tk.Label(outerFrame, text='Verse:')
fromVerse.pack()
fromTextbox = tk.Entry(outerFrame, width=10)
fromTextbox.pack()
fromTextbox.focus_set()
toVerse = tk.Label(outerFrame, text='Verse:')
toVerse.pack()
toTextbox = tk.Entry(outerFrame, width=10)
toTextbox.pack()
toTextbox.focus_set()

submitButton = tk.Button(outerFrame, text='Submit')
submitButton.pack()


root.mainloop()
