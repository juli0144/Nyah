import multiprocessing
from pydub import AudioSegment
from pydub.playback import play
# from PIL import Image

from Game import *


# Unused funktion to load pictures for the Future
def load_image(file):
    return ctk.CTkImage(Image.open(file))
    # ImageTk.PhotoImage(Image.open(file))


def _play_audio(audio):
    play(audio)


def get_frames():
    return [
        Startup,
        CharSelect,
        Options,
        Gamemanager
    ]


class SoundPlayer:
    def __init__(self, file, volume):
        super().__init__()
        self.song = AudioSegment.from_wav(file)
        self.song_volumed = self.song + volume
        self.play = multiprocessing.Process(target=_play_audio, args=(self.song_volumed, ))

    def run(self):
        self.play.start()

    def stop(self):
        self.play.terminate()


class Window(ctk.CTk):  # Main (root) window and window controller
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        self.title('Nyahh')
        self.geometry('600x400')
        self.configure()

        self.stats = {}
        self.frames = {}

        self.backround_music = SoundPlayer('assets/neon-gaming-128925.wav', -40)
        self.on_startup()

    def on_startup(self):
        self.backround_music.run()
        self.set_frames()

    def on_closing(self):
        try:
            self.backround_music.stop()
        finally:
            self.destroy()

    def set_frames(self):
        # creating a frame and assigning it to container
        container = ctk.CTkFrame(self)
        container.pack(side='top', expand=True)

        for F in get_frames():
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(Startup)

    def show_frame(self, cont):
        # Change active frame and set active for the update funktion
        frame = self.frames[cont]
        frame.tkraise()


# Sets up the first Frame
class Startup(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)

        self.configure()

        label = ctk.CTkLabel(self, text='Main Menu', height=100, width=300, font=('arial', 40))
        label.pack()

        btn_charselect = ctk.CTkButton(self, text='New Game', font=('arial', 20), width=150,
                                       command=lambda: controller.show_frame(CharSelect))
        btn_options = ctk.CTkButton(self, text='Options', font=('arial', 20), width=150,
                                    command=lambda: controller.show_frame(Options))
        btn_closewindow = ctk.CTkButton(self, text='Exit Minigame', font=('arial', 20), width=150,
                                        command=controller.on_closing)

        btn_charselect.pack(padx=5, pady=5)
        btn_options.pack(padx=5, pady=5)
        btn_closewindow.pack(padx=10, pady=25, side='bottom')


# Character select frame
class CharSelect(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        temp_dict = {}

        # Headline: Character select
        label = ctk.CTkLabel(self, text="Character select")

        # Adds tabs for each character
        self.char_tabs = ctk.CTkTabview(self)
        for i in get_char():
            temp_dict[i.name] = i
            self.char_tabs.add(i.name)
            char_description = ctk.CTkLabel(self.char_tabs.tab(i.name), text=i.description, justify='left')
            char_description.grid(row=0, column=1, rowspan=2)

        # Bottom Buttons
        switch_window_button = ctk.CTkButton(self, text="Go back", command=lambda: controller.show_frame(Startup))
        start_button = ctk.CTkButton(self, text='Start', command=lambda: self.init_new_game(temp_dict, controller))

        label.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
        self.char_tabs.grid(row=1, columnspan=2)
        switch_window_button.grid(row=3, column=0)
        start_button.grid(row=3, column=1)

    def init_new_game(self, dic_classes, controller):
        # Checks the choosen tab and sets the class out of the dictionary
        choosen_car_tabs = self.char_tabs.get()
        controller.frames[Gamemanager].player = dic_classes[choosen_car_tabs]
        controller.stats['difficulty'] = 'easy'
        controller.show_frame(Gamemanager)


# Options Frame
class Options(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        label = ctk.CTkLabel(self, text="WIP")
        label.pack(padx=10, pady=10)
        switch_window_button = ctk.CTkButton(
            self, text="Return to menu",
            command=lambda: controller.show_frame(Startup)
        )
        switch_window_button.pack(side="bottom", fill=ctk.X)


if __name__ == '__main__':
    root = Window()
    root.protocol("WM_DELETE_WINDOW", root.on_closing)
    root.mainloop()
