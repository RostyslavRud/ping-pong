from customtkinter import*


class ConnectWindow(CTk):
    def __init__(self):
        super().__init__()
        def open_game(self):
            self.destroy()

        play_button =  CTkButton(self, text = 'приєднатися', command = self.open_game, height = 50)
        self.play_button.pack()
        self.setting_button = CTkButton(self, text = 'налаштування')
        self.setting_button.pack()
        self.exit_button = CTkButton(self, text = 'вийти')
        self.exit_button.pack()
    
    
