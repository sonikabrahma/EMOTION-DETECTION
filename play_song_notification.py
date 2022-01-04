import tkinter as tk
from tkinter import messagebox
def notify():
    global result
    result=messagebox.askyesno(
        title="Message",
        message="Do you want to play songs",
        detail="Would you like some songs?"
    )
    return result

print(notify())