from tkinter import *


class login():
    global done
    done = False

    def show(self):
        root = Tk()
        root.title("pyDino")
        self.input_box(root)
        while not done:
            root.update()
        root.destroy()
        self.done = False
        return(True, 'main_menu', None)

    def input_box(self, master=None):
        self.font = ("Arial", "10")
        self.firstContainer = Frame(master)
        self.firstContainer["pady"] = 10
        self.firstContainer.pack()

        self.secondContainer = Frame(master)
        self.secondContainer["padx"] = 20
        self.secondContainer.pack()

        self.thirdContainer = Frame(master)
        self.thirdContainer["padx"] = 20
        self.thirdContainer.pack()

        self.fourthContainer = Frame(master)
        self.fourthContainer["pady"] = 20
        self.fourthContainer.pack()

        self.title = Label(self.firstContainer, text="Login")
        self.title["font"] = ("Arial", "10", "bold")
        self.title.pack()

        self.userLabel = Label(self.secondContainer, text="Username",
                               font=self.font)
        self.userLabel.pack(side=LEFT)

        self.user = Entry(self.secondContainer)
        self.user["width"] = 30
        self.user["font"] = self.font
        self.user.pack(side=LEFT)

        self.passwordLabel = Label(self.thirdContainer, text="Password",
                                   font=self.font)
        self.passwordLabel.pack(side=LEFT)

        self.password = Entry(self.thirdContainer)
        self.password["width"] = 30
        self.password["font"] = self.font
        self.password["show"] = "*"
        self.password.pack(side=LEFT)

        self.autenticate = Button(self.fourthContainer)
        self.autenticate["text"] = "Login"
        self.autenticate["font"] = ("Calibri", "8")
        self.autenticate["width"] = 12
        self.autenticate["command"] = self.return_menu
        self.autenticate.pack()

        self.signUp = Button(self.fourthContainer)
        self.signUp["text"] = "Sign up"
        self.signUp["font"] = ("Calibri", "8")
        self.signUp["width"] = 12
        self.signUp["command"] = self.sign_up
        self.signUp.pack()

        self.message = Label(self.fourthContainer, text="", font=self.font)
        self.message.pack()

    def return_menu(self):
        user = self.user.get()
        password = self.password.get()
        if user == "adm" and password == "adm":
            global done
            done = True
            self.message["text"] = "Sucess"
        else:
            self.message["text"] = "Username or password invalid"

    def sign_up(self):
        user = self.user.get()
        password = self.password.get()
        if user == "adm":
            self.message["text"] = "User already sign up"
