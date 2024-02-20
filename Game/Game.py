# import customtkinter as ctk
from Funktions import *


def get_game_frames():
    return [
        Fight
    ]


class Gamemanager(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.player = Player('Empty', '', 99, 99, 99)

        self.frames = {}
        container = ctk.CTkFrame(self)
        container.pack(side='top', expand=True)

        for F in get_game_frames():
            frame = F(container, self)

            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(Fight)

    def show_frame(self, cont):
        # Change active frame and set active for the update funktion
        frame = self.frames[cont]
        frame.self_init(self)
        frame.tkraise()


class Fight(ctk.CTkFrame):
    def __init__(self, parent, controller):
        ctk.CTkFrame.__init__(self, parent)
        self.start = True
        self.enemys = ctk.CTkLabel(self, text='here should be an enemy')

    def self_init(self, controller):
        self.self_init_playerstats(controller)
        self.self_init_enemys()

    def self_init_enemys(self):
        frame = ctk.CTkFrame(self)

        e_frame = ctk.CTkFrame(frame)
        self.enemys = get_enemy_start(e_frame)
        self.grid_enemys()
        e_frame.pack()

        empty_label = ctk.CTkLabel(frame, text='')
        empty_label.pack()

        frame.grid(row=0, column=0, columnspan=2)

    def self_init_playerstats(self, controller):

        self.playerhp = ctk.StringVar(self, f"{controller.player.hp} / {controller.player.max_hp}")
        self.playerstrengh = ctk.StringVar(self, f"Strength: {controller.player.base_strength}")

        playerstats = ctk.CTkFrame(self)
        name = ctk.CTkLabel(playerstats, text=controller.player.name)
        name.pack()
        hp = ctk.CTkLabel(playerstats, textvariable=self.playerhp)
        hp.pack()
        strength = ctk.CTkLabel(playerstats, textvariable=self.playerstrengh)
        strength.pack()

        effectbox = ctk.CTkFrame(playerstats)
        effecttext = ctk.CTkLabel(effectbox, text='Effects')
        effecttext.pack()
        effectbox.pack()

        playerstats.grid(column=0, row=1)

    def grid_enemys(self):
        for e in self.enemys:
            e.grid(column=0, row=0)

    def self_playerstats(self):
        pass
