from utility import clear_Frame
from tkinter import messagebox
from Theme import *
import tkinter as tk
 



# ---------------------------- Login Page ----------------------------

def create_login_page(container_Frame):
    clear_Frame(container_Frame)

    page = tk.Frame(container_Frame, bg=BACKGROUND_MAIN)
    page.pack(expand=True, fill="both")

    big_Text = tk.Label(page,
                        text="Payroll System - Login",
                        fg=TEXT_LIGHT,
                        bg=BACKGROUND_MAIN,
                        font=("Segoe UI", 30)
    )
    big_Text.pack(pady=(0,20))

    input_Frame = tk.Frame(page,
                           bg=BACKGROUND_FRAME,
                           padx=20,
                           pady=20
                           )
    input_Frame.pack(pady=10)

    tk.Label(input_Frame,
             text="Username:",
             bg=BACKGROUND_FRAME,
             fg=TEXT_DARK
             ).grid(row=0, column=0, sticky="e", padx=8, pady=6)
    username_Entry = tk.Entry(input_Frame, width=30)
    username_Entry.grid(row=0, column=1, pady=6)

    tk.Label(input_Frame,
             text="Password:",
             bg=BACKGROUND_FRAME,
             fg=TEXT_DARK
             ).grid(row=1, column=0, sticky="e", padx=8, pady=6)
    password_Entry = tk.Entry(input_Frame, show="*", width=30)
    password_Entry.grid(row=1, column=1, pady=6)

    # Show password toggle
    show_pw_var = tk.BooleanVar(value=False)

    def toggle_pw():
        password_Entry.config(show="" if show_pw_var.get() else "*")

    password_check = tk.Checkbutton(input_Frame,
                              text="Show Password",
                              variable=show_pw_var,
                              bg=BACKGROUND_FRAME,
                              activebackground=BACKGROUND_FRAME,
                              command=toggle_pw
                              )
    password_check.grid(row=2, column=1, sticky="w")

    # Buttons
    btn_frame = tk.Frame(page, bg=BACKGROUND_MAIN)
    btn_frame.pack(pady=15)

    def _do_login():
        # placeholder login logic
        username = username_Entry.get().strip()
        pwd = password_Entry.get()
        if not username or not pwd:
            messagebox.showerror("Login error", "Please enter username and password.")
            return
        messagebox.showinfo("Login", f"Logged in as {username} (placeholder)")

    login_Button = tk.Button(btn_frame,
                             text="Login",
                             bg=BTN_COLOR,
                             fg=TEXT_LIGHT,
                             font=("Segoe UI", 12),
                             relief="flat",
                             padx=12,
                             pady=6,
                             command=_do_login
                             )
    login_Button.grid(row=0, column=0, padx=10)
    add_hover_effect(login_Button)

    sign_up_Button = tk.Button(btn_frame,
                               text="Sign-up",
                               bg=BTN_COLOR,
                               fg=TEXT_LIGHT,
                               font=("Segoe UI", 12),
                               relief="flat",
                               padx=12,
                               pady=6
                               )
    sign_up_Button.grid(row=0, column=1, padx=10)
    add_hover_effect(sign_up_Button)

    from mMenu import show_main_menu
    # Back to main menu
    back_btn = tk.Button(page,
                         text="Back", 
                         bg=BACKGROUND_MAIN,
                         fg=TEXT_LIGHT,
                         relief="flat",
                         command=lambda: show_main_menu(container_Frame)
                         )
    back_btn.pack(pady=8)
