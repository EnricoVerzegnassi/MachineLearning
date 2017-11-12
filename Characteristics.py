class Characteristics:

    charateristicsMap = {}
    characteristic = {}

    def mapCharateristics(self, a, b):

        if (a not in self.charateristicsMap.keys()):    #Se non esiste la classe creo un dizionario vuoto
            self.charateristicsMap[a] = {}

        characteristic = self.charateristicsMap[a]
        if (b in characteristic.keys()):  # Se esiste la caratteristica
            return characteristic[b]
        else:  # Se non esiste la caratteristica
            lenght = len(characteristic)
            characteristic[b] =  lenght + 1
            return characteristic[b]