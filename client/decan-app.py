import tkinter as tk
from tkinter import font as tkfont
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

class CustomApp(customtkinter.CTk):
    def __init__(self, size=[800,480]):
        customtkinter.CTk.__init__(self)

        self.title_font = customtkinter.CTkFont(family='Helvetica', size=18, weight="bold")
        self.body_font = customtkinter.CTkFont(family='Helvetica', size=14)
        self.title("splash")
        self.width, self.height = size[0],size[1]

        page_container = customtkinter.CTkFrame(self)
        page_container.pack(side="top", fill="both", expand=True)
        page_container.grid_rowconfigure(0, minsize=self.height, weight=1)  # configure grid system
        page_container.grid_columnconfigure(0, minsize=self.width, weight=1)
        
        self.frames = {}
        for F in (LoginPg, DecanApplication):
            page_name = F.__name__
            frame = F(parent=page_container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0)

        self.show_frame("LoginPg")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        self.title(frame.title)

class LoginPg(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)

        # Attributes
        self.controller = controller
        self.title = 'Login Page'
        #self.label_image = tksvg.SvgImage(file="assets/orb.svg")

        label_title = customtkinter.CTkLabel(self, text="Login", font=controller.title_font).grid(row=0,column=0,columnspan=2)

        label_username = customtkinter.CTkLabel(self, text="Username", font=controller.body_font).grid(row=1,column=0,columnspan=2,sticky='w',padx=6)
        self.entry_username = customtkinter.CTkEntry(master=self, placeholder_text="Username", corner_radius=0,)
        self.entry_username.grid(row=2,column=0,columnspan=2,sticky='nsew')

        label_password = customtkinter.CTkLabel(self, text="Password", font=controller.body_font).grid(row=3,column=0,columnspan=2,sticky='w',padx=6, pady=(2,0))
        self.entry_password = customtkinter.CTkEntry(master=self, placeholder_text="Password", corner_radius=0, show='*')
        self.entry_password.grid(row=4,column=0,sticky='nsew')
        self.button_password = customtkinter.CTkButton(master=self, text='Show', corner_radius=0, command=self.change_format)
        self.button_password.grid(row=4,column=1)

        button_confirm = customtkinter.CTkButton(master=self,text="Confirm",command=self.login).grid(row=5, column=0, columnspan=2, sticky='nsew',pady=(6,0))

    def login(self):
        user = 'daniel'
        password = 'danielspassword'
        if self.entry_username.get()=='daniel' and self.entry_password.get()=='danielspassword':
            print('Correct Login')
            self.controller.show_frame("DecanApplication")
        else: 
            print('Invalid Login')


    def change_format(self):
        match self.entry_password.cget("show"):
            case '*':
                self.entry_password.configure(show='')
                self.button_password.configure(text='Hide')
            case '':
                self.entry_password.configure(show='*')
                self.button_password.configure(text='Show')

class DecanApplication(customtkinter.CTkFrame):
    def __init__(self, parent, controller):
        customtkinter.CTkFrame.__init__(self, parent)

        #Attributes
        self.controller = controller
        self.title = 'Login Page'



if __name__ == "__main__":
    print(tk.TkVersion)
    app = CustomApp()
    app.mainloop()