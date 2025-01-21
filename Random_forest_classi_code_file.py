from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.preprocessing import LabelEncoder
# step no 2
data = {'Age' : [25,35,45,20,30,50,40,55,60,35],
        'Gender' : ['M', 'F', 'M','M','F','F','M','F','M','F'],
        'EstimatedSalary': [30000,40000,60000,20000,35000,80000,45000,90000,100000,50000],
       'Purchased': [0,0,1,0,1,1,0,1,1,0]}
df = pd.DataFrame(data)
print(df)
label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'])
x = df.drop('Purchased',axis=1)
y = df['Purchased']
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 42)
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(x_train, y_train)
y_pred = rf_classifier.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"accuracy of random forest: {accuracy}")
# user input
user_age = int(input("Enter your age: "))
user_gender = input("Enter your gender M/F: ")
user_salary = int(input("Enter your salary: "))

user_gender_encoder = label_encoder.transform([user_gender])[0]
user_data = [[user_age, user_gender_encoder, user_salary]]

prediction = rf_classifier.predict(user_data)
if prediction[0] == 1:
    print("This person is likely to purchase the product.")
else:
    print("This person is not likely to purchase the product.")
