import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np
# numpy is used to convert the image symbol array for prediction 


data_dict = pickle.load(open('./data.pickle', 'rb'))

data = np.asarray(data_dict['data'])
labels = np.asarray(data_dict['labels'])

# dividing the set into training and testing set with 20%
x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle=True, stratify=labels)

# tensorflow model to get the prediction
model = RandomForestClassifier()

model.fit(x_train, y_train)

# testing the model
y_predict = model.predict(x_test)

score = accuracy_score(y_predict, y_test)

# showing the accuracy of model
print('{}% of samples were classified correctly !'.format(score * 100))

# creating and saving the model
f = open('model.p', 'wb')
pickle.dump({'model': model}, f)
f.close()
