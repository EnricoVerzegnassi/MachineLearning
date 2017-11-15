
from sklearn.naive_bayes import GaussianNB,MultinomialNB
import numpy
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import svm
from AppInfoExtraction import AppInfoExtraction

from sklearn.svm import SVC
path_base="/Users/Jacopo/Desktop/Universita/SAPIENZA/ML/HW1/code/MachineLearning/data"


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
predictedB = mnb.predict(X_test)


#SVM first try  -- pure il sigmoid e il rbf non riescono a classificare i malware, mentre il linear li classifica perfettamente
clf = SVC(kernel="linear")
clf.fit(X_test, y_test)
predictedSVM=clf.predict(X_test)

print ("Real Value")
print (y_test)
print ("SVM value")
print predictedSVM
print("My Bayes-prediction")
print(predictedB)



correctB_result=0
correctSVM_result=0

for i in range(len(y_test)):
    if(y_test[i]!=0):
        if(predictedB[i]==1):
            correctB_result= correctB_result + 1
        if (predictedSVM[i] == 1):
            correctSVM_result = correctSVM_result + 1

print "Accuracy SVM Score: ",correctSVM_result / len(y_test).__float__()*100, '%'
print "Accuracy Bayes Score: ",correctB_result / len(y_test).__float__()*100, '%'



#print "Error Score: ",1-correct_result / len(y_test).__float__(), '%'
#print ("Accuracy Score: ",accuracy_score(y_test, predicted))