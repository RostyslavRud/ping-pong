from customtkinter import*


class ConnectWindow(CTk):
    def __init__(self):
        super().__init__()

        self.play_button =  CTkButton(self, text = 'приєднатися', command = self.open_game, height = 50)
        self.play_button.pack()
        self.setting_button = CTkButton(self, text = 'налаштування')
        self.setting_button.pack()
        self.exit_button = CTkButton(self, text = 'вийти', command=self.exit)
        self.exit_button.pack()

        self.flag = 0

    def open_game(self):
        self.destroy()

    def exit(self):
        self.flag = -1
        self.destroy()
    def settings(self):
        pass