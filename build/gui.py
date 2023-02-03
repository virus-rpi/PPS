from pathlib import Path

from tkinter import Tk, Canvas, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Python/PPS/build/assets/frame0/")


def create():
    print("Ok")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def main():
    window = Tk()

    window.geometry("1062x569")
    window.configure(bg="#353535")

    canvas = Canvas(
        window,
        bg="#353535",
        height=569,
        width=1062,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    canvas.create_rectangle(
        0.0,
        0.0,
        166.0,
        569.0,
        fill="#4F4F4F",
        outline="")

    canvas.create_text(
        12.0,
        28.0,
        anchor="nw",
        text="Devices",
        fill="#FFFFFF",
        font=("Inter", 20 * -1)
    )

    canvas.create_rectangle(
        182.0,
        28.0,
        1038.0,
        538.0,
        fill="#454545",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=create,
        relief="flat"
    )
    button_1.place(
        x=18.0,
        y=500.0,
        width=131.0,
        height=38.0
    )
    button_1.update()
    window.resizable(False, False)

    return window
