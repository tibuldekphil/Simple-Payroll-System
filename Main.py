#=== Imports ===
import tkinter as tk
from Theme import *
from Fonts import load_fonts
import mMenu

#=== Window Setup ===
window = tk.Tk()
window.title("Simple Payroll System")
window.geometry("900x650")
Icon = tk.PhotoImage(file="Picture1.png")
window.iconphoto(True, Icon)

#=== Load Fonts and pass to Pages ===
F = load_fonts()
mMenu.F = F 

#=== MASTER FRAME ===
main_Frame = tk.Frame(window, bg=BACKGROUND_MAIN)
main_Frame.pack(fill="both", expand=True)

#=== FOOTER ===
footer_Frame = tk.Frame(main_Frame, bg=BACKGROUND_FRAME)
footer_Frame.pack(fill="x", side="bottom")

footer_Label = tk.Label(
    footer_Frame,
    text="© 2025 Simple Payroll System | All Rights Reserved",
    bg=BACKGROUND_FRAME,
    fg=TEXT_DARK,
    font=F["SMALL_TEXT"]
)
footer_Label.pack(pady=10)

# === Toggle Function ===
def toggle_sidebar():
    global sidebar_visible
    if sidebar_visible:
        sidebar.place_forget()       # hides the sidebar
        sidebar_visible = False
    else:
        sidebar.place(x=0, y=100)     # shows it just below the header
        sidebar_visible = True

#=== Sidebar ===
sidebar = tk.Frame(window,
                   bg=BACKGROUND_FRAME,
                   width=200,
                   height=650,
                   highlightthickness=1,
                   highlightbackground="Gray",
                   
)
sidebar_visible = False  # track menu state

#=== HEADER ===
header_Frame = tk.Frame(main_Frame, bg=BACKGROUND_FRAME)
header_Frame.pack(fill="x", side="top")

header_Label = tk.Label(
    header_Frame,
    font=F["PAGE_HEADING"],
    bg=BACKGROUND_FRAME,
    text="BLUE PAYROLL SYSTEM",
    fg=TEXT_DARK
)

burger_btn = tk.Button(header_Frame, text="☰", font=("Arial", 25), width=5, command=toggle_sidebar)
burger_btn.pack(side="left", fill="y")
header_Label.pack(side="left", pady=10)

#=== CONTAINER (middle content) ===
body_Frame = tk.Frame(main_Frame, bg=BACKGROUND_MAIN)
body_Frame.pack(fill="both", expand=True)
container_Frame = tk.Frame(body_Frame)
container_Frame.place(relx=0.5, rely=0.5, anchor="center")
         
mMenu.show_main_menu(container_Frame)



window.mainloop()