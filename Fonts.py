from tkinter import font

def load_fonts():
    fonts = {
        "PAGE_HEADING": font.Font(family="Poppins", size=48, weight="bold"),
        "SECTION_HEADING": font.Font(family="Poppins", size=32, weight="bold"),
        "SUBSECTION": font.Font(family="Poppins", size=24),
        "BODY_TEXT": font.Font(family="Inter", size=16, weight="normal"),
        "SMALL_TEXT": font.Font(family="Inter", size=13)
    }
    return fonts

