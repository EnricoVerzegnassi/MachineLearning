
from sklearn.naive_bayes import GaussianNB
import numpy
from sklearn.feature_extraction.text import TfidfVectorizer
from AppAnalysis import AppAnalysis
path_base="/home/verz/Documenti/Studio/Università Sapienza/Corsi/3° Semestre/Machine Learning/HW/Code/data"


reducedMap={}


learningApps = AppAnalysis()
learningApps.read_list_app(path_base + '/app/', path_base + '/sha256_family.csv');

clf = GaussianNB()
X = numpy.array(learningApps.apps)
Y = numpy.array(learningApps.malware_index)
clf.fit(X,Y)

testApps = AppAnalysis()
testApps.read_list_app(path_base+'/testApp/',path_base+ '/sha256_family.csv')
print("TEST APPS:")
print(clf.predict(testApps.apps))