from Theme import *
import tkinter as tk
from utility import clear_Frame, POSITIONS, DEDUCTIONS
from utility import _center_toplevel, _valid_email, _valid_phone
from tkinter import messagebox


F = None
# ---------------------------- Register Page ----------------------------

def create_register_page(container_Frame):
    clear_Frame(container_Frame)

    page = tk.Frame(container_Frame, bg=BACKGROUND_MAIN)
    page.pack(expand=True, fill="both")

    form_Frame = tk.Frame(page, bg=BACKGROUND_FRAME, padx=40, pady=30)
    form_Frame.pack()

    header_label = tk.Label(form_Frame, 
                            text="Enter Company Details",
                            font=F["SUBSECTION"],
                            bg=BACKGROUND_FRAME,
                            fg=TEXT_DARK
                            )
    header_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

    # fields -- positions & deductions replaced with buttons
    tk.Label(form_Frame,
             text="Company Name:",
             font=F["BODY_TEXT"],
             bg=BACKGROUND_FRAME,
             fg=TEXT_DARK
             ).grid(row=1, column=0, sticky="e", pady=5, padx=(0, 10))
    company_entry = tk.Entry(form_Frame,
                             font=F["BODY_TEXT"],
                             width=30,
                             relief="flat",
                             bd=2
                             )
    company_entry.grid(row=1, column=1, pady=5, sticky="w")

    tk.Label(form_Frame,
             text="Address:",
             font=F["BODY_TEXT"],
             bg=BACKGROUND_FRAME,
             fg=TEXT_DARK
             ).grid(row=2, column=0, sticky="e", pady=5, padx=(0, 10))
    address_entry = tk.Entry(form_Frame,
                             font=F["BODY_TEXT"],
                             width=30,
                             relief="flat",
                             bd=2
                             )
    address_entry.grid(row=2, column=1, pady=5, sticky="w")

    tk.Label(form_Frame,
             text="Email:",
             font=F["BODY_TEXT"],
             bg=BACKGROUND_FRAME,
             fg=TEXT_DARK
             ).grid(row=3, column=0, sticky="e", pady=5, padx=(0, 10))
    email_entry = tk.Entry(form_Frame,
                           font=F["BODY_TEXT"],
                           width=30, 
                           relief="flat",
                           bd=2
                           )
    email_entry.grid(row=3, column=1, pady=5, sticky="w")

    tk.Label(form_Frame,
             text="Tel:",
             font=F["BODY_TEXT"],
             bg=BACKGROUND_FRAME,
             fg=TEXT_DARK
             ).grid(row=4, column=0, sticky="e", pady=5, padx=(0, 10))
    tel_entry = tk.Entry(form_Frame,
                         font=F["BODY_TEXT"],
                         width=30,
                         relief="flat",
                         bd=2
                         )
    tel_entry.grid(row=4, column=1, pady=5, sticky="w")

    # Positions button
    tk.Label(form_Frame,
             text="Positions:",
             font=F["BODY_TEXT"],
             bg=BACKGROUND_FRAME,
             fg=TEXT_DARK
             ).grid(row=5, column=0, sticky="e", pady=5, padx=(0, 10))
    pos_btn = tk.Button(form_Frame,
                        text="Manage Positions",
                        bg=BACKGROUND_FRAME,
                        fg=BTN_COLOR,
                        relief="flat",
                        command=lambda: open_position_window(container_Frame)
                        )
    pos_btn.grid(row=5, column=1, pady=5, sticky="w")

    # Deductions button
    tk.Label(form_Frame,
             text="Deductions:",
             font=F["BODY_TEXT"],
             bg=BACKGROUND_FRAME,
             fg=TEXT_DARK
             ).grid(row=6, column=0, sticky="e", pady=5, padx=(0, 10))
    ded_btn = tk.Button(form_Frame,
                        text="Manage Deductions",
                        bg=BACKGROUND_FRAME,
                        fg=BTN_COLOR,
                        relief="flat",
                        command=lambda: open_deduction_window(container_Frame)
                        )
    ded_btn.grid(row=6, column=1, pady=5, sticky="w")

    tk.Label(form_Frame,
             text="Admin:",
             font=F["BODY_TEXT"],
             bg=BACKGROUND_FRAME,
             fg=TEXT_DARK
             ).grid(row=7, column=0, sticky="e", pady=5, padx=(0, 10))
    admin_entry = tk.Entry(form_Frame,
                           font=F["BODY_TEXT"], 
                           width=30,
                           relief="flat",
                           bd=2
                           )
    admin_entry.grid(row=7, column=1, pady=5, sticky="w")

    tk.Label(form_Frame,
             text="Password:",
             font=F["BODY_TEXT"],
             bg=BACKGROUND_FRAME,
             fg=TEXT_DARK
             ).grid(row=8, column=0, sticky="e", pady=5, padx=(0, 10))
    password_entry = tk.Entry(form_Frame,
                              show="*",
                              font=F["BODY_TEXT"],
                              width=30,
                              relief="flat", bd=2)
    password_entry.grid(row=8, column=1, pady=5, sticky="w")

    show_pass_var = tk.BooleanVar()
    tk.Checkbutton(form_Frame,
                   text="Show Password",
                   font=F["SMALL_TEXT"],
                   bg=BACKGROUND_FRAME,
                   fg=TEXT_DARK,
                   variable=show_pass_var,
                   command=lambda: password_entry.config(show="" if show_pass_var.get() else "*")
    ).grid(row=9, column=1, sticky="w", pady=(5, 15))

    # Buttons
    button_Frame = tk.Frame(form_Frame, bg=BACKGROUND_FRAME)
    button_Frame.grid(row=10, column=0, columnspan=2, pady=(10, 0))

    from mMenu import show_main_menu
    back_btn = tk.Button(button_Frame,
                         text="Back",
                         bg=BTN_COLOR,
                         fg=TEXT_LIGHT,
                         font=F["BODY_TEXT"],
                         width=10,
                         relief="flat",
                         command=lambda: show_main_menu(container_Frame)
                         )
    back_btn.pack(side="left", padx=10)

    def _submit_register():
        company = company_entry.get().strip()
        address = address_entry.get().strip()
        email = email_entry.get().strip()
        tel = tel_entry.get().strip()
        admin = admin_entry.get().strip()
        pwd = password_entry.get()

        if not company:
            messagebox.showerror("Validation", "Company name is required.")
            return
        if not _valid_email(email):
            messagebox.showerror("Validation", "Please enter a valid email address.")
            return
        if not _valid_phone(tel):
            messagebox.showerror("Validation", "Please enter a valid telephone number (7-15 digits).")
            return

        # placeholder: save company details logic
        messagebox.showinfo("Registered", f"{company} registered successfully (placeholder).\nPositions: {len(POSITIONS)}\nDeductions: {len(DEDUCTIONS)}")

    register_btn = tk.Button(button_Frame, text="Register", bg=BTN_COLOR, fg=TEXT_LIGHT, font=F["BODY_TEXT"], width=10, relief="flat", command=_submit_register)
    register_btn.pack(side="left", padx=10)


# ---------------------------- Position TopLevel ----------------------------

def open_position_window(parent_frame):
    top = tk.Toplevel()
    top.title("Manage Positions")
    _center_toplevel(top, 420, 300)
    top.config(bg=BACKGROUND_MAIN)

    frm = tk.Frame(top, bg=BACKGROUND_FRAME, padx=12, pady=12)
    frm.pack(expand=True, fill="both", padx=8, pady=8)

    tk.Label(frm,
             text="Position Name:",
             bg=BACKGROUND_FRAME,
             fg=TEXT_DARK
             ).grid(row=0, column=0, sticky="e", padx=6, pady=6)
    name_entry = tk.Entry(frm, width=25)
    name_entry.grid(row=0, column=1, pady=6)

    tk.Label(frm,
             text="Rate:",
             bg=BACKGROUND_FRAME,
             fg=TEXT_DARK
             ).grid(row=1, column=0, sticky="e", padx=6, pady=6)
    rate_entry = tk.Entry(frm, width=25)
    rate_entry.grid(row=1, column=1, pady=6)

    def submit_position():
        name = name_entry.get().strip()
        rate = rate_entry.get().strip()
        if not name:
            messagebox.showerror("Validation", "Position name required.")
            return
        try:
            rate_val = float(rate)
        except ValueError:
            messagebox.showerror("Validation", "Rate must be a number.")
            return
        POSITIONS.append({"name": name, "rate": rate_val})
        messagebox.showinfo("Saved", f"Position '{name}' saved.")
        name_entry.delete(0, "end")
        rate_entry.delete(0, "end")

    def view_positions():
        if not POSITIONS:
            messagebox.showinfo("Positions", "No positions saved.")
            return
        vw = tk.Toplevel(top)
        vw.title("Saved Positions")
        _center_toplevel(vw, 360, 300)
        lb = tk.Listbox(vw, width=50)
        lb.pack(padx=8, pady=8, expand=True, fill="both")
        for p in POSITIONS:
            lb.insert("end", f"{p['name']} — {p['rate']}")

    btn_frm = tk.Frame(frm, bg=BACKGROUND_FRAME)
    btn_frm.grid(row=3, column=0, columnspan=2, pady=10)

    submit_btn = tk.Button(btn_frm, 
                           text="Submit",
                           bg=BTN_COLOR,
                           fg=TEXT_LIGHT,
                           command=submit_position
                           )
    submit_btn.grid(row=0, column=0, padx=6)
    add_hover_effect(submit_btn)

    view_btn = tk.Button(btn_frm,
                         text="View Saved Positions",
                         bg=BTN_COLOR,
                         fg=TEXT_LIGHT,
                         command=view_positions
                         )
    view_btn.grid(row=0, column=1, padx=6)
    add_hover_effect(view_btn)

    back_btn = tk.Button(btn_frm,
                         text="Back",
                         bg=BACKGROUND_FRAME,
                         fg=TEXT_DARK,
                         command=top.destroy
                         )
    back_btn.grid(row=0, column=2, padx=6)


# ---------------------------- Deduction TopLevel ----------------------------

def open_deduction_window(parent_frame):
    top = tk.Toplevel()
    top.title("Manage Deductions")
    _center_toplevel(top, 460, 340)
    top.config(bg=BACKGROUND_MAIN)

    frm = tk.Frame(top,
                   bg=BACKGROUND_FRAME,
                   padx=12,
                   pady=12
                   )
    frm.pack(expand=True, fill="both", padx=8, pady=8)

    tk.Label(frm,
             text="Deduction Name:",
             bg=BACKGROUND_FRAME,
             fg=TEXT_DARK
             ).grid(row=0, column=0, sticky="e", padx=6, pady=6)
    name_entry = tk.Entry(frm, width=25)
    name_entry.grid(row=0, column=1, pady=6)

    tk.Label(frm,
             text="Deduction Type:",
             bg=BACKGROUND_FRAME,
             fg=TEXT_DARK
             ).grid(row=1, column=0, sticky="e", padx=6, pady=6)
    dtype_var = tk.StringVar(value="%")
    dtype_menu = tk.OptionMenu(frm, dtype_var, "%", "whole")
    dtype_menu.grid(row=1, column=1, sticky="w")

    tk.Label(frm,
             text="Value:",
             bg=BACKGROUND_FRAME,
             fg=TEXT_DARK
             ).grid(row=2, column=0, sticky="e", padx=6, pady=6)
    value_entry = tk.Entry(frm, width=25)
    value_entry.grid(row=2, column=1, pady=6)

    def submit_deduction():
        name = name_entry.get().strip()
        dtype = dtype_var.get()
        val = value_entry.get().strip()
        if not name:
            messagebox.showerror("Validation", "Deduction name required.")
            return
        try:
            val_num = float(val)
        except ValueError:
            messagebox.showerror("Validation", "Value must be a number.")
            return
        DEDUCTIONS.append({"name": name, "type": dtype, "value": val_num})
        messagebox.showinfo("Saved", f"Deduction '{name}' saved.")
        name_entry.delete(0, "end")
        value_entry.delete(0, "end")

    def view_deductions():
        if not DEDUCTIONS:
            messagebox.showinfo("Deductions", "No deductions saved.")
            return
        vw = tk.Toplevel(top)
        vw.title("Saved Deductions")
        _center_toplevel(vw, 420, 320)
        lb = tk.Listbox(vw, width=60)
        lb.pack(padx=8, pady=8, expand=True, fill="both")
        for d in DEDUCTIONS:
            lb.insert("end", f"{d['name']} — {d['type']} {d['value']}")

    btn_frm = tk.Frame(frm, bg=BACKGROUND_FRAME)
    btn_frm.grid(row=4, column=0, columnspan=2, pady=10)

    submit_btn = tk.Button(btn_frm,
                           text="Submit",
                           bg=BTN_COLOR,
                           fg=TEXT_LIGHT,
                           command=submit_deduction
                           )
    submit_btn.grid(row=0, column=0, padx=6)
    add_hover_effect(submit_btn)

    view_btn = tk.Button(btn_frm,
                         text="View Saved Deductions",
                         bg=BTN_COLOR,
                         fg=TEXT_LIGHT,
                         command=view_deductions
                         )
    view_btn.grid(row=0, column=1, padx=6)
    add_hover_effect(view_btn)

    back_btn = tk.Button(btn_frm,
                         text="Back",
                         bg=BACKGROUND_FRAME,
                         fg=TEXT_DARK,
                         command=top.destroy
                         )
    back_btn.grid(row=0, column=2, padx=6)
