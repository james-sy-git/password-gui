"""
GUI module for password generation. Creates a frame and app using tkinter and
ttk, its styling module. The app allows a user to choose the special characters
(Y/N), capital letters (Y/N), and length (integer) of their desired password.

Allows the user to save the password to a text file once the password has been
generated.

James Sy
6/10/2022
"""

from improvedpasswordgen import Password
import tkinter as tk
from tkinter import ttk

class PWFrame(ttk.Frame):
    """
    Inherits from tkinter.ttk.Frame, and creates a PWFrame object to be used as
    the main working space for the app.

    Uses the secure and doubly-randomized process in improvedpasswordgen, and assigns
    a improvedpasswordgen.Password object to the Frame's password attribute.

    Additionally looks pretty :)
    """
    def __init__(self, container):
        """
        Initializes a PWFrame object, while also using the super initializer on
        this PWFrame's container window.

        Param container: the tkinter root window for this PWFrame object
        Pre: must be a valid tkinter root window

        Att password: the password associated with the running PWFrame
        Inv: password must be a valid Password or None

        Att userentry: text entry field for the existing username, stores value
        in user
        Inv: userentry is of type ttk.Entry

        Att sourceentry: text entry field for the login source, stores value
        in source
        Inv: sourceentry is of type ttk.Entry
        """
        # Hidden Attributes:
        #
        # Att font: the default font of this PWFrame's widgets
        # Inv: font must be a tuple
        #
        # Att lvar: the variable that stores the desired password length
        # Inv: lvar is of type tk.IntVar()
        #
        # Att cvar: the variable that stores the option of capital letters
        # Inv: cvar is of type tk.IntVar()
        #
        # Att svar: the variable that stores the option of special characters
        # Inv: svar is of type tk.IntVar()
        #
        # Att user: the variable that stores the existing username to be associated
        # with the new password
        # Inv: user is of type tk.StringVar()
        #
        # Att source: the variable that stores the user-entered login source
        # Inv: user is of type tk.StringVar()
        #
        # Att llabel: the widget that labels the password length fields
        # Inv: llabel is a ttk.Label widget
        #
        # Att lbox: the password length entry field, stores value in lvar
        # Inv: lbox is a ttk.Entry widget
        #
        # Att cbox: the capital letters checkbox, stores value in cvar
        # Inv: cbox is a ttk.Checkbutton widget
        #
        # Att sbox: the special characters checkbox, stores value in cvar
        # Inv: sbox is a ttk.Checkbutton widget
        #
        # Att result: the result label box showing the password
        # Inv: result is a ttk.Label widget whose text option must either be None
        # or a password associated with this PWFrame's Password object
        #
        # Att genbutton: button whose command calls usegenerator() method
        # Inv: genbutton is a ttk.Button widget
        #
        # Att userlabel: the widget that labels the userentry box
        # Inv: userlabel is a ttk.Label widget
        #
        # Att sourcelabel: the widget that labels the sourceentry box
        # Inv: sourcelabel is a ttk.Label widget
        #
        # Att savebutton: button whose command calls save() method
        # Inv: savebutton is a ttk.Button widget
        #
        # Att lstyle: style-r for this PWFrame's labels
        # Inv: lstyle is a ttk.Style widget, and applies to TLabel widgets
        #
        # Att estyle: style widget for this PWFrame's entry fields
        # Inv: estyle is a ttk.Style widget, and applies to TEntry widgets
        #
        # Att bstyle: style widget for this PWFrame's button fields
        # Inv: bstyle is a ttk.Style widget, and applies to TButton widgets
        #
        # Att cbstyle: style widget for this PWFrame's check box fields
        # Inv: cbstyle is a ttk.Style widget, and applies to TCheckbutton widgets

        super().__init__(container)

        padding = {'padx': 4, 'pady': 4}

        self.password = None

        self.font = ('Segoe UI Emoji', 10)

        self.lvar = tk.IntVar()
        self.cvar = tk.IntVar()
        self.svar = tk.IntVar()
        self.user = tk.StringVar()
        self.source = tk.StringVar()

        self.llabel = ttk.Label(self, text='Password Length:')
        self.llabel.grid(column=1, row=5, **padding, sticky=tk.W)

        self.lbox = ttk.Entry(self, textvariable=self.lvar, width=4,
        justify=tk.CENTER)
        self.lbox.grid(column=1, row=5, **padding, sticky=tk.E)

        self.cbox = ttk.Checkbutton(self, text='Capital Letters',
        variable=self.cvar, onvalue=True, offvalue=False)
        self.cbox.grid(column=2, row=4, **padding, sticky=tk.E)

        self.sbox = ttk.Checkbutton(self, text='Special Characters',
        variable=self.svar, onvalue=True, offvalue=False)
        self.sbox.grid(column=1, row=4, **padding, sticky=tk.W)

        self.result = ttk.Label(self, text=None, borderwidth=6, relief='solid',
        width=60, style='result.TLabel', anchor=tk.CENTER)
        self.result.grid(row=2, columnspan=4, **padding, sticky=tk.S)

        self.genbutton = ttk.Button(self, text='Generate', width=30,
        command=(lambda: self.usegenerator()))
        self.genbutton.grid(row=3, column=1, columnspan=2, **padding)

        self.userentry = ttk.Entry(self, textvariable=self.user, width=30,
        justify=tk.CENTER)
        self.userentry.grid(row=1, column=2, **padding, sticky=tk.W)
        self.userlabel = ttk.Label(self, text='Existing Username:')
        self.userlabel.grid(row=1, column=1, **padding)

        self.sourceentry = ttk.Entry(self, textvariable=self.source, width=30,
        justify=tk.CENTER)
        self.sourceentry.grid(row=0, column=2, **padding, sticky=tk.W)
        self.sourceentry.focus()
        self.sourcelabel = ttk.Label(self, text='Login Source:')
        self.sourcelabel.grid(row=0, column=1, **padding)

        self.savebutton = ttk.Button(self, text='Save',
        command=(lambda: self.save()))
        self.savebutton.grid(row=5, column=2, **padding, sticky=tk.E)

        self.lstyle = ttk.Style()
        self.lstyle.configure('TLabel', font=self.font, background='#B8FFFD')
        self.lstyle.configure('result.TLabel', background='#FFFFFF')
        self.estyle = ttk.Style()
        self.estyle.configure('TEntry', font=self.font)
        self.bstyle = ttk.Style()
        self.bstyle.configure('TButton', font=self.font, background='#B8FFFD')
        self.cbstyle = ttk.Style()
        self.cbstyle.configure('TCheckbutton', font=self.font, background='#B8FFFD')

        self.pack()

    def usegenerator(self):
        """
        Creates a Password object and stores it in self.password, but only if
        self.checklength is True.
        """
        if self.checklength():
            self.password = Password(self.lvar.get(), self.cvar.get(),
            self.svar.get()).getpw()
            self.result.config(text=str(self.password))

    def checklength(self):
        """
        Returns True if self.lvar exists and is only digits, False otherwise.
        """
        check = self.lvar.get()
        if check == None:
            return False
        return str(check).isdigit()

    def save(self):
        """
        If a password has been generated, saves the source, username, and new
        password to a text file. If the file does not already exists, creates it.
        """
        if self.password != None:
            with open('savedpasswords.txt', 'a') as file:
                file.write('Login Source: ' + self.source.get())
                file.write('\n')
                file.write('Username: ' + self.user.get())
                file.write('\n')
                file.write('Password: ' + self.password)
                file.write('\n\n')

            self.clear()

    def clear(self):
        """
        Removes the password, un-checks checkboxes, and restores all Entry fields
        back to their empty state.
        """
        self.password = None
        self.result.config(text='')

        self.lvar.set(0)
        self.cvar.set(False)
        self.svar.set(False)
        self.user.set('')
        self.source.set('')


class PWGUI(tk.Tk):
    """
    The root window for this password generator. Inherits from tkinter.Tk.
    """
    def __init__(self):
        """
        Initializes a GUI window object for the password generator. Uses the
        super initializer for a tkinter root window object.
        """
        # Hidden Attributes:
        #
        # Att framestyle: the style that applies to this PWGUI's frame widget
        # Inv: framestyle is a ttk.Style widget that applies to TFrame widgets

        super().__init__()

        self.title('Password Generator')
        self.geometry('460x190')
        self.resizable(False, False)
        self.configure(background='#B8FFFD')

        self.framestyle = ttk.Style()
        self.framestyle.configure('TFrame', background='#B8FFFD')

if __name__ == "__main__":
    app = PWGUI()
    frame = PWFrame(app)
    app.mainloop()
