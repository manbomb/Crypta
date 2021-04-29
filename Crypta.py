class Crypta:
    def __init__(self, text, cry):
        self.__text = text.lower()
        self.__cry = cry[0:2].lower()
    def setText(text):
        self.__text = text
    def setCry(cry):
        self.__cry = cry
    def getText(self):
        return self.__text
    def getCry(self):
        return self.__cry
    def __nextChar(self, a):
        if ord(a) < 122:
            return chr(ord(a)+1)
        else:
            return "a"
    def __crySequence(self):
        alpha = list("abcdefghijklmnopqrstuvwxyz")
        posIni = ord(self.__cry[0])-97
        charIni = self.__cry[1]

        for i in range(0, 26):
            alpha[(posIni+i)%26] = charIni
            charIni = self.__nextChar(charIni)
        
        return alpha
    def cry(self):
        alpha = self.__crySequence()
        text = list(self.__text)

        for i in range(0, len(text)):
            if (ord(text[i]) >= 97 and ord(text[i]) <= 122):
                text[i] = alpha[ord(text[i])-97]
        
        return "".join(text)

print(Crypta("Salve salve galerinha", "sa").cry())