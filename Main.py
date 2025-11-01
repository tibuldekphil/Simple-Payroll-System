#=== Imports ===
import tkinter as tk
from Theme import *
from Fonts import load_fonts
import mMenu

#=== Window Setup ===
window = tk.Tk()
window.title("Simple Payroll System")

Icon = tk.PhotoImage(file="Picture1.png")
window.iconphoto(True, Icon)

#=== Load Fonts and pass to Pages ===
F = load_fonts()
mMenu.F = F 

#=== MASTER FRAME ===
main_Frame = tk.Frame(window, bg=BACKGROUND_MAIN)
main_Frame.pack(fill="both", expand=True)

#=== HEADER ===
header_Frame = tk.Frame(main_Frame, bg=BACKGROUND_FRAME)
header_Frame.pack(fill="x", side="top", pady=(0,50))

header_Label = tk.Label(
    header_Frame,
    font=F["PAGE_HEADING"],
    bg=BACKGROUND_FRAME,
    text="BLUE PAYROLL SYSTEM",
    fg=TEXT_DARK
)
header_Label.pack(pady=10)

#=== CONTAINER (middle content) ===
container_Frame = tk.Frame(main_Frame, bg=BACKGROUND_MAIN)
container_Frame.pack(fill="both", expand=True, pady=(10, 10))
         
mMenu.show_main_menu(container_Frame)


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

window.mainloop()
