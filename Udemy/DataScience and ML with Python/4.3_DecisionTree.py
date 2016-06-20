import pandas as pd
from sklearn import tree
from IPython.display import Image
from sklearn.externals.six import StringIO
import pydot
from sklearn.ensemble import RandomForestClassifier
df = pd.read_csv('./Documents/Udemy_Datascience/DataScience/PastHires.csv',header=0)
print df.head()

#convert to numerical data

d ={'Y':1,'N':0}
df['Hired'] = df['Hired'].map(d)
df['Employed?'] = df['Employed?'].map(d)
df['Top-tier school'] = df['Top-tier school'].map(d)
df['Interned'] = df['Interned'].map(d)
d={'BS':0,'MS':1,'PhD':2}
df['Level of Education'] = df['Level of Education'].map(d)
print df.head()

#observations and result
features = list(df.columns[:6])
print features
x=df[features]
y=df['Hired']

#generate the tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x,y)

#To display the tree
dot_data = StringIO()
tree.export_graphviz(clf,out_file = dot_data,feature_names = features)
graph = pydot.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())

#ensemble learning using random forest

clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(x,y)

#Predict employment of an employed 10-year veteran
print clf.predict([10,1,4,0,0,0])

#Predict employment of an unemployed 10-year veteran
print clf.predict([10,0,4,0,0,0])