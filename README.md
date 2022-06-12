# password-gui

Improved password generator with new features, an OO approach, and a streamlined tkinter GUI.

Allows the user to generate a doubly-randomized password, with security ensured by the use of
the secrets module.

Gives the user the option to save the "Login Source" (e.g., the website or secure entry that the
user is attempting to access), "Existing Username", and the newly-generated password to a .txt file
so that it is not forgotten.

Uses tkinter's ttk module for improved aesthetics.

Removed the English dictionary cross-reference from the previous password generator because it is
not useful. If a word exists in the password but it was created randomly, it holds no relation to
the end user and is thus not a liability.

Included in this repository is a .exe version of the app, converted from a Python script with
PyInstaller.
