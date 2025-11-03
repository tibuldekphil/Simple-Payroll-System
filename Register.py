from Theme import *
import tkinter as tk
from utility import clear_Frame
from tkinter import messagebox
from MyDB import insert_Company
import re
#Font is left empty for now
F = None


# ---------------------------- Register Page ----------------------------
def create_register_page(container_Frame):
    clear_Frame(container_Frame)

    page = tk.Frame(container_Frame, bg=BACKGROUND_MAIN)
    page.pack(expand=True, fill="both")

    tk.Label(page, 
            text="Enter Company Details",
            font=F["SUBSECTION"],
            bg=BACKGROUND_MAIN,
            fg=TEXT_LIGHT
    ).pack(pady=(0,20))

    form_Frame = tk.Frame(page, bg=BACKGROUND_FRAME, padx=40, pady=30)
    form_Frame.pack()

    # fields
    tk.Label(form_Frame,
             text="Company Name:",
             font=F["SMALL_TEXT"],
             bg=BACKGROUND_FRAME,
             fg=TEXT_DARK
    ).grid(row=0, column=0, sticky="e", pady=5, padx=(0, 10))
    company_entry = tk.Entry(form_Frame,
                             font=F["SMALL_TEXT"],
                             width=30,
                             relief="flat",
                             bd=2
    )
    company_entry.grid(row=0, column=1, pady=5, sticky="w")

    tk.Label(form_Frame,
             text="Address:",
             font=F["SMALL_TEXT"],
             bg=BACKGROUND_FRAME,
             fg=TEXT_DARK
             ).grid(row=1, column=0, sticky="e", pady=5, padx=(0, 10))
    address_entry = tk.Entry(form_Frame,
                             font=F["SMALL_TEXT"],
                             width=30,
                             relief="flat",
                             bd=2
                             )
    address_entry.grid(row=1, column=1, pady=5, sticky="w")

    tk.Label(form_Frame,
             text="Email:",
             font=F["SMALL_TEXT"],
             bg=BACKGROUND_FRAME,
             fg=TEXT_DARK
             ).grid(row=2, column=0, sticky="e", pady=5, padx=(0, 10))
    email_entry = tk.Entry(form_Frame,
                           font=F["SMALL_TEXT"],
                           width=30, 
                           relief="flat",
                           bd=2
                           )
    email_entry.grid(row=2, column=1, pady=5, sticky="w")

    tk.Label(form_Frame,
             text="Tel. Number:",
             font=F["SMALL_TEXT"],
             bg=BACKGROUND_FRAME,
             fg=TEXT_DARK
             ).grid(row=3, column=0, sticky="e", pady=5, padx=(0, 10))
    
    tel_entry = tk.Entry(form_Frame,
                         font=F["SMALL_TEXT"],
                         width=30,
                         relief="flat",
                         bd=2
                         )
    
    tel_entry.grid(row=3, column=1, pady=5, sticky="w")

    
    # Buttons
    button_Frame = tk.Frame(page, bg=BACKGROUND_MAIN)
    button_Frame.pack(pady=10)

    #=== Back Button ===
    from mMenu import show_main_menu
    back_btn = tk.Button(button_Frame,
                         text="Back",
                         bg=BTN_COLOR,
                         fg=TEXT_LIGHT,
                         font=F["SMALL_TEXT"],
                         width=10,
                         relief="flat",
                         command=lambda: show_main_menu(container_Frame)
                         )
    back_btn.pack(side="left", padx=10)
    add_hover_effect(back_btn)

    #=== Submit Button ===
    #--- Submit Function: Variable, validation ---
    
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    def _submit_register():
        company = company_entry.get().strip()
        address = address_entry.get().strip()
        email = email_entry.get().strip()
        tel = tel_entry.get().strip()
       
        # Required fields
        if not company:
            messagebox.showerror("Validation Error", "Company Name is required.")
        elif not email:
            messagebox.showerror("Validation Error", "Email Address is required.")
        # Email format
        elif not re.match(email_pattern, email):
            messagebox.showerror("Validation Error", "Invalid email format.")
        # Telephone checks
        elif tel and not tel.isdigit():
            messagebox.showerror("Validation Error", "Telephone number must contain digits only.")
        elif tel and len(tel) < 7:
            messagebox.showerror("Validation Error", "Telephone number is too short.")
        # Success
        else:
            insert_Company(company_entry.get().strip(),
                           address_entry.get().strip(),
                           email_entry.get().strip(),
                           tel_entry.get().strip())
       
    #--- The exact Button to press ---
    register_btn = tk.Button(button_Frame,
                             text="Register",
                             bg=BTN_COLOR,
                             fg=TEXT_LIGHT,
                             font=F["SMALL_TEXT"],
                             width=10,
                             relief="flat",
                             command=_submit_register
    )
    register_btn.pack(side="left", padx=10)
    add_hover_effect(register_btn)
