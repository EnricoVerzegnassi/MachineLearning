
from sklearn.naive_bayes import GaussianNB,MultinomialNB
import numpy

from AppInfoExtraction import AppInfoExtraction
path_base="/home/verz/Documenti/Studio/Università Sapienza/Corsi/3° Semestre/Machine Learning/HW/Code/data"


reducedMap={}


learningApps = AppInfoExtraction()
learningApps.read_list_app(path_base + '/app/', path_base + '/sha256_family.csv');

clf = GaussianNB()
mnb = MultinomialNB()
X = numpy.asmatrix(learningApps.apps)
Y = numpy.array(learningApps.malware_index)
#clf.fit(X,Y)
mnb.fit(learningApps.apps,Y)
testApps = AppInfoExtraction()
testApps.read_list_app(path_base+'/testApp/',path_base+ '/sha256_family.csv')
print("TEST APPS:")
print(mnb.predict(testApps.apps))