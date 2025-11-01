from Theme import *
import tkinter as tk
from utility import clear_Frame
from Loginpage import create_login_page
from Register import create_register_page
import Register

F = None

# ---------------------------- Main Menu ----------------------------

def show_main_menu(container_Frame):
    clear_Frame(container_Frame)

    page = tk.Frame(container_Frame, bg=BACKGROUND_MAIN)
    page.pack(expand=True, fill="both")

    tk.Label(page, font=F["SECTION_HEADING"], bg=BACKGROUND_MAIN, text="WELCOME", fg=TEXT_LIGHT).pack(pady=10)

    menu_Frame = tk.Frame(page, bg=BACKGROUND_FRAME, padx=30, pady=30, highlightthickness=2, highlightbackground=BTN_COLOR)
    menu_Frame.pack()

    login_Button = tk.Button(menu_Frame,
                             text="LOGIN",
                             bg=BTN_COLOR,
                             fg=TEXT_LIGHT,
                             font=F["SUBSECTION"],
                             width=20,
                             command=lambda: create_login_page(container_Frame)
                            )
    login_Button.pack(pady=(0,10))
    add_hover_effect(login_Button)
    
    Register.F = F
    register_company_Button = tk.Button(menu_Frame, 
                                        text="REGISTER COMPANY", 
                                        bg=BTN_COLOR, 
                                        fg=TEXT_LIGHT,
                                        font=F["SUBSECTION"], 
                                        width=20, 
                                        command=lambda: create_register_page(container_Frame)
    )
    register_company_Button.pack()
    add_hover_effect(register_company_Button)
