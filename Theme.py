from tkinter import *
BACKGROUND_MAIN = "#1E3A8A"
BACKGROUND_FRAME = "#E2E8F0"
BTN_COLOR = "#2563EB"
HOVER_COLOR = "#1D4ED8"
TEXT_DARK = "#1F2937"
TEXT_LIGHT = "#FFFFFF"

def add_hover_effect (widget, enter_bg = HOVER_COLOR, exit_bg = BTN_COLOR):
    def on_hover(event): widget.config(bg=enter_bg)
    def on_leave(event): widget.config(bg=exit_bg)
    widget.bind("<Enter>", on_hover)
    widget.bind("<Leave>", on_leave)