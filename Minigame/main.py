import multiprocessing
import playsound
import customtkinter as ctk
from PIL import Image

from Funktions import *


# Unused funktion to load pictures for the Future
def load_image(file):
    return ctk.CTkImage(Image.open(file), size=(600, 400))
    # ImageTk.PhotoImage(Image.open(file))


def _play_audio(audiofile):
    playsound.playsound(audiofile)


class SoundPlayer:
    def __init__(self, file):
        super().__init__()
        self.process = multiprocessing.Process(target=_play_audio, args=(file,))

    def run(self):
        self.process.start()

    def stop(self):
        self.process.terminate()


class Window(ctk.CTk):  # Main (root) window and window controller
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        self.title('Nyahh')
        self.geometry('600x400')
        self.configure()
        self.sound_player = SoundPlayer('assets/neon-gaming-128925.wav')
        self.after(1000, self.play_sound)

        # creating a frame and assigning it to container
        self.frames = {}
        container = ctk.CTkFrame(self)
        container.pack(side='top', expand=True)

        for F in (MainMenu, CharSelect, Options):
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(MainMenu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def play_sound(self):
        self.sound_player.run()

    def on_closing(self):
        try:
            self.sound_player.stop()
        finally:
            self.destroy()


# Sets up the first Frame
class MainMenu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        self.configure()

        label = ctk.CTkLabel(self, text='Main Menu', height=150, width=300, font=('arial', 30))
        label.pack()

        btn_charselect = ctk.CTkButton(self, text='Start', font=('arial', 20), width=150,
                                       command=lambda: controller.show_frame(CharSelect))
        btn_options = ctk.CTkButton(self, text='Options', font=('arial', 20), width=150,
                                    command=lambda: controller.show_frame(Options))
        btn_closewindow = ctk.CTkButton(self, text='Exit Minigame', font=('arial', 20), width=150,
                                        command=controller.on_closing)

        btn_charselect.pack(padx=5, pady=5)
        btn_options.pack(padx=5, pady=5)
        btn_closewindow.pack(padx=10, pady=5)


# Character select frame
class CharSelect(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        # Headline: Character select
        label = ctk.CTkLabel(self, text="Character select")

        # Adds tabs for each character
        char_tabs = ctk.CTkTabview(self)
        for i in get_char():
            char_tabs.add(i.name)
            char_description = ctk.CTkLabel(char_tabs.tab(i.name), text=i.description, justify='left')
            char_description.grid(row=0, column=1, rowspan=2)

        # Bottom Buttons
        switch_window_button = ctk.CTkButton(self, text="Go back", command=lambda: controller.show_frame(MainMenu))
        start_button = ctk.CTkButton(self, text='Start')

        label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        char_tabs.grid(row=1, columnspan=2)
        switch_window_button.grid(row=3, column=0)
        start_button.grid(row=3, column=1)


# Options Frame
class Options(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="WIP")
        label.pack(padx=10, pady=10)
        switch_window_button = ctk.CTkButton(
            self, text="Return to menu",
            command=lambda: controller.show_frame(MainMenu)
        )
        switch_window_button.pack(side="bottom", fill=ctk.X)


if __name__ == '__main__':
    root = Window()
    root.protocol("WM_DELETE_WINDOW", root.on_closing)
    root.mainloop()
