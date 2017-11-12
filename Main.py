
from sklearn.naive_bayes import GaussianNB,MultinomialNB
import numpy
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from AppInfoExtraction import AppInfoExtraction
path_base="/home/verz/Documenti/Studio/Università Sapienza/Corsi/3° Semestre/Machine Learning/HW/Code/data"


reducedMap={}


learningApps = AppInfoExtraction()
learningApps.read_list_app(path_base + '/app/', path_base + '/sha256_family.csv');

#clf = GaussianNB()
mnb = MultinomialNB()
mlb = MultiLabelBinarizer()
X = mlb.fit_transform(learningApps.apps)
Y = numpy.array(learningApps.malware_index)
#clf.fit(X,Y)

X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.33, random_state=42)

mnb.fit(X_train,y_train)
predicted = mnb.predict(X_test)

print ("Real Value")
print (y_test)
print("My prediction")
print(predicted)

print ("Accuracy Score: ",accuracy_score(y_test, predicted))