from tkinter import *
from Theme import *
import re

F = None

# In-memory storage for positions and deductions
POSITIONS = []  # list of dicts: {"name": str, "rate": float}
DEDUCTIONS = []  # list of dicts: {"name": str, "type": "%" or "whole", "value": float}


def clear_Frame(frame):
    for child in frame.winfo_children():
        child.destroy()


#---------------------------- Utilities ----------------------------

def _center_toplevel(toplevel, width=400, height=300):
    toplevel.update_idletasks()
    sw = toplevel.winfo_screenwidth()
    sh = toplevel.winfo_screenheight()
    x = (sw - width) // 2
    y = (sh - height) // 2
    toplevel.geometry(f"{width}x{height}+{x}+{y}")


def _valid_email(email: str) -> bool:
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None


def _valid_phone(phone: str) -> bool:
    # Accept digits, spaces, +, -, and parentheses but require 7-15 digits
    digits = re.sub(r"\D", "", phone)
    return 7 <= len(digits) <= 15


