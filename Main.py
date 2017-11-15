
from sklearn.naive_bayes import GaussianNB,MultinomialNB
import numpy
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import svm
from AppInfoExtraction import AppInfoExtraction

from sklearn.svm import SVC
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
predictedB = mnb.predict(X_test)


#SVM first try  -- pure il sigmoid e il rbf non riescono a classificare i malware, mentre il linear li classifica perfettamente
clf = SVC(kernel="linear")
clf.fit(X_test, y_test)
predictedSVM=clf.predict(X_test)

print ("Real Value")
print (y_test)
print ("SVM value")
print (predictedSVM)
print("My Bayes-prediction")
print(predictedB)


Real_Malware=0
NB_correct=0
SVM_correct=0

SVM_FalsePositive=0
SVM_FalseNegative=0
NB_FalsePositive=0
NB_FalseNegative=0

for i in range(len(y_test)):
    if(y_test[i]!=0):                           #False positive and false negative are not detected
        Real_Malware+=1
        if(predictedB[i]==1):
            NB_correct += 1
        else:
            NB_FalseNegative +=1
        if (predictedSVM[i] == 1):
            SVM_correct += 1
        else:
            SVM_FalseNegative
    else:
        if(predictedB[i]==1):
            NB_FalsePositive +=1

        if(predictedSVM[i]==1):
            SVM_FalsePositive +=1

print ("Accuracy SVM Score: ",str(SVM_correct / Real_Malware.__float__()*100), '%')
print ("False Positive: ",SVM_FalsePositive,"False negative: ",SVM_FalseNegative)
print ("Accuracy Bayes Score: ",NB_correct / Real_Malware.__float__()*100, '%')
print ("False Positive: ",NB_FalsePositive,"False negative: ",NB_FalseNegative)

