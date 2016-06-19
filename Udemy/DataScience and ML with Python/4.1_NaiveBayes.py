from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB 
import os
import io

def dataFrameFromDirectory(path, classification):
    rows = []
    index = []
    for filename,message in readFiles(path):
        rows.append({'message':message,'class':classification})
        index.append(filename)
    return DataFrame(rows,index=index)
def readFiles(path):
    for root,dirnames,filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root,filename)
            f=io.open(path,'r',encoding='latin1')
            lines=[]
            inBody = False
            for line in f:
                if inBody:
                    lines.append(line)
                elif (line =='\n'):
                    inBody = True
            f.close()
            message = '\n'.join(lines) 
            yield path,message  
data = DataFrame({'message':[],'class':[]})
data = data.append(dataFrameFromDirectory('./Documents/Udemy_DataScience/DataScience/emails/spam','spam'))
data = data.append(dataFrameFromDirectory('./Documents/Udemy_DataScience/DataScience/emails/ham','ham'))

print data.head()
vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(data['message'].values)

classifier= MultinomialNB()
targets = data['class'].values
classifier.fit(counts,targets)

#test the model

examples = ['Free tablets now','how about a game tomorrow?']
examples_counts = vectorizer.transform(examples)
predictions = classifier.predict(examples_counts)
print predictions

