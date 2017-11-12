from Characteristics import Characteristics
import pandas as pd
import os
import numpy

class AppInfoExtraction:
    apps = []
    malware_index = []
    c = Characteristics()  # Create the structure for characteristics

    def read_list_app(self, appDir, malwareList):

        malware = pd.read_csv(malwareList, sep=',')
        for filename in os.listdir(appDir):
            app = []
            feature1=[]
            feature2=[]
            with open(appDir + filename) as f:
                if (malware['sha256'].str.contains(filename).any()):
                    self.malware_index.append(1)
                    print("Malware !!! " + filename)
                else:
                    self.malware_index.append(0)
                    print("Good App")


                limit = 4
                for line in f.read().splitlines():
                    arguments = line.split("::")

                    
                    if (arguments[0] == "url" and len(feature1) < limit):
                        feature1.append(self.c.mapCharateristics(arguments[0], arguments[1]))


                    if (arguments[0] == "permission" and len(feature2) < limit):
                        feature2.append(self.c.mapCharateristics(arguments[0], arguments[1]))


                while (len(feature1) < 4):  # Aggiugo numeri zero fittizi per riempire i buchi
                    feature1.append(0)

                while (len(feature2) < 4):  # Aggiugo numeri zero fittizi per riempire i buchi
                    feature2.append(0)

                app.append(feature1)
                app.append(feature2)

                self.apps.append(numpy.array(app))

        print(self.malware_index)
