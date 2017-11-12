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
                    #print("Malware !!! " + filename)
                else:
                    self.malware_index.append(0)
                    #print("Good App")


                limit = 4
                for line in f.read().splitlines():
                    arguments = line.split("::")

                    #if (arguments[0] in ["permission","url","api_call","real_permission","intent"]):
                    #    app.append(arguments[1])
                    app.append(arguments[1])

                self.apps.append(app)

