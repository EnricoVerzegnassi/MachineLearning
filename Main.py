import pandas as pd
import os
from sklearn.naive_bayes import GaussianNB
import numpy
from sklearn.feature_extraction.text import TfidfVectorizer
from Characteristics import Characteristics
path_base="/home/verz/Documenti/Studio/Università Sapienza/Corsi/3° Semestre/Machine Learning/HW/Code/data"

apps = {}
malware_index = []
c = Characteristics()  #Create the structure for characteristics
reducedMap={}

def read_list_app():
    app=[]
    malware=pd.read_csv(path_base+'/sha256_family.csv', sep=',')
    for filename in os.listdir(path_base+'/app/'):
        with open(path_base+'/app/'+filename) as f:
            if (malware['sha256'].str.contains(filename).any()):
                malware_index.append(1)
                print("Malware !!! "+filename)
            else:
                malware_index.append(0)
            for line in f.read().splitlines() :
                arguments=line.split("::")
                app.append(c.mapCharateristics(arguments[0],arguments[1]))
                apps[filename]=app
    print(malware_index)


def reduce():
    reducedMap=c.charateristicsMap['feature']





read_list_app();
reduce()


c=0
#clf = GaussianNB()
#X = numpy.array(apps)
#Y = numpy.array(malware_index)
#a=[['a','g'],['b','a'],['c','e']]
#f=[[-1, -1], [-2, -1], [-3, -2]]
#b=[1,0,1]
#X=numpy.array(a)
#Y = numpy.array(b)
#clf.fit(X,Y)
#X = vect.fit_transform(df['tweets'])
#y = df['class']