import time
import random
from tkinter import *
from threading import Thread


class Window:
    def __init__(self, size: str, timer: float, background_colors: tuple[str, ...]) -> None:
        self.size = size.split("x")
        self.timer = timer
        self.background_colors = background_colors
        self.root = Tk()
        self.root.title("")
        self.root.geometry(size)
        self.root.resizable(False, False)
        self.root.attributes("-topmost", True)
        self.root.protocol("WM_DELETE_WINDOW", main)

        Thread(target=self.animate_window).start() 
        Thread(target=self.create_new_window).start()

        self.root.mainloop()

    def animate_window(self) -> None:
        width_positions = [i for i in range(0, self.root.winfo_screenwidth() - int(self.size[0]), 10)]
        height_positions = [i for i in range(0, self.root.winfo_screenheight() - int(self.size[1]), 10)]

        while True:
            self.root.deiconify()
            self.root["bg"] = random.choice(self.background_colors)
            self.root.geometry(f"+{random.choice(width_positions)}+{random.choice(height_positions)}")
            time.sleep(self.timer)

    def create_new_window(self) -> None:
        time.sleep(self.timer * 5)
        main()


def main():
    rainbow_colors = ("#9400D3", "#4B0082", "#0000FF", "#00FF00", "#FFFF00", "#FF7F00", "#FF0000")
    Window("300x250", 0.5, rainbow_colors)


if __name__ == "__main__":
    main()