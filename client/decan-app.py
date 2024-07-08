import tkinter as tk
from tkinter import font as tkfont
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class CustomApp(customtkinter.CTk):
    def __init__(self, size=[800,480]):
        customtkinter.CTk.__init__(self)

        self.title_font = customtkinter.CTkFont(family='Helvetica', size=18, weight="bold", slant="italic")
        self.body_font = customtkinter.CTkFont(family='Helvetica', size=14)
        self.title("splash")
        self.width, self.height = size[0],size[1]

        page_container = customtkinter.CTkFrame(self)
        page_container.pack(side="top", fill="both", expand=True)
        page_container.grid_rowconfigure(0, minsize=self.height, weight=1)  # configure grid system
        page_container.grid_columnconfigure(0, minsize=self.width, weight=1)
        
        self.frames = {}
        for F in (LoginPg, LoginPg):
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

        label = customtkinter.CTkLabel(self, text="Login", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        usernameentry = customtkinter.CTkEntry(master=self,placeholder_text="Username")
        self.passwordentry = customtkinter.CTkEntry(master=self,placeholder_text="Password",show='*')
        print(self.passwordentry.cget('show'))
        self.vh_button = customtkinter.CTkButton(master=self, text='Show Password', command=self.change_format)
        usernameentry.pack()
        self.passwordentry.pack()
        self.vh_button.pack()
    
    def change_format(self):
        match self.passwordentry.cget("show"):
            case '*':
                self.passwordentry.configure(show='')
                self.vh_button.configure(text='Hide Password')
            case '':
                self.passwordentry.configure(show='*')
                self.vh_button.configure(text='Show Password')
    
        

        



        


class MainApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self, width=800, height=480)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, minsize=480 ,weight=1)
        container.grid_columnconfigure(0, minsize=800,weight=1)

        self.frames = {}
        for F in (LoginPage,PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

class LoginPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        usernameentry = tk.Entry(master=self)
        passwordentry = tk.Entry(master=self)
        usernameentry.pack()
        passwordentry.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("LoginPage"))
        button.pack()

class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("LoginPage"))
        button.pack()



if __name__ == "__main__":
    app = CustomApp()
    app.mainloop()