"""
Uses the secure randomizing algorith from the Python secrets module to
generate a random password, which is then stored in the pw attribute of a
Password object. Contains two layers of randomization to ensure
password security.

James Sy
6/10/2022
"""

import secrets

sec = secrets.SystemRandom()

ALPHA = {1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j",
11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s", 20:"t",
21:"u", 22:"v", 23:"w", 24:"x", 25:"y", 26:"z"}

CHARS = {1:"!", 2:"@", 3:"#", 4:"$", 5:"^", 6:"&", 7:"*", 8:".", 9:"-", 10:"_",
11:"+", 12:"=", 13:";", 14:":", 15:"?"}

class Password(object):

    def getpw(self):
        """
        Returns the password associated with this Password instance.
        """
        return self.pw

    def __init__(self, length, caps, spec):
        """
        Initializes the password object using the values of length, caps, and spec.

        Param length: the number of characters in the password
        Pre: boolean
        Param caps: whether or not the password contains capital letters (True if
        it does, False otherwise)
        Pre: boolean
        Param spec: whether or not the password contains special characters (True
        if it does, False otherwise)
        Pre: boolean
        """
        # Hidden Attributes: see above
        #
        # Att pw: the password that is generated using the generate() method
        # Inv: pw can only contain characters of the alphabet and the standard
        # special characters given in CHARS.

        self._length = length
        self._caps = caps
        self._spec = spec

        self.pw = self.generate()

    def generate(self):
        """
        Generates a random password.
        """
        pw = ""

        if self._spec:
            for x in range(self._length):
                choices = sec.randint(0, 2) # 0 letter, 1 number, 2 special
                if choices == 0:
                    if self._caps:
                        pw += self.case_sensitive()
                    else:
                        pw += self.case_insensitive()
                elif choices == 1:
                    pw += self.number()
                elif choices == 2:
                    pw += self.special()
        else:
            for x in range(self._length):
                choices = sec.randint(0, 1) # 0 letter, 1 number
                if choices == 0:
                    if self._caps:
                        pw += self.case_sensitive()
                    else:
                        pw += self.case_insensitive()
                else:
                    pw += self.number()
        return pw

    def case_sensitive(self):
        """
        Generates either a capital or lowercase random letter.
        """
        letter = self.case_insensitive()

        upper_lower = sec.randint(0, 1) # 0 is lower, 1 is upper
        if upper_lower == 0:
            return letter
        else:
            return letter.upper()

    def case_insensitive(self):
        """
        Generates a lowercase random letter.
        """
        key = sec.randint(1, len(ALPHA))
        return ALPHA[key]

    def number(self):
        """
        Generates a random number.
        """
        return str(sec.randint(0, 9))

    def special(self):
        """
        Generates a random special character.
        """
        key = sec.randint(1, len(CHARS))
        return CHARS[key]
