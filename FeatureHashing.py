class FeatureHashing:


    def hashingFeature(self, app, vectorLenght):
        vector = [0] * vectorLenght
        for line in app.read().splitlines():
            arguments = line.split("::")
            if (len(line) > 0):
                i = hash(arguments[1]) % vectorLenght
                vector[i] +=1

        return vector
