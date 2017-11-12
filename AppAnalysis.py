from Characteristics import Characteristics
import pandas as pd
import os

class AppAnalysis:
    apps = []
    malware_index = []
    c = Characteristics()  # Create the structure for characteristics

    def read_list_app(self, appDir, malwareList):

        malware = pd.read_csv(malwareList, sep=',')
        for filename in os.listdir(appDir):
            app = []
            with open(appDir + filename) as f:
                if (malware['sha256'].str.contains(filename).any()):
                    self.malware_index.append(1)
                    print("Malware !!! " + filename)
                else:
                    self.malware_index.append(0)
                    print("Good App")

                counter = 0
                limit = 4
                for line in f.read().splitlines():
                    arguments = line.split("::")
                    if (arguments[0] == "url" and counter < limit):
                        app.append(self.c.mapCharateristics(arguments[0], arguments[1]))
                        counter = counter + 1

                while (len(app) < 4):  # Aggiugo numeri zero fittizi per riempire i buchi
                    app.append(0)
                self.apps.append(app)
        print(self.malware_index)
