import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.metrics import mean_absolute_error, confusion_matrix

class Basics:
    def __init__ (self):
        self.titanic = sns.load_dataset('titanic')

    # Prepare dataset
    def prepare_data(self):
        print(self.titanic.head(10), "\n")
        print(self.titanic.info())

    # Helper function to impute age
    def impute_age(self, cols):
        age = cols[0]
        pclass = cols[1]

        if pd.isnull(age):
            if pclass == 1:
                return self.titanic[self.titanic['pclass'] == 1]['age'].mean()
            elif pclass == 2:
                return self.titanic[self.titanic['pclass'] == 2]['age'].mean()
            elif pclass == 3:
                return self.titanic[self.titanic['pclass'] == 3]['age'].mean()
        else:
            return age

    # Process data
    def process_data(self):
        self.titanic['age'] = self.titanic[['age', 'pclass']].apply(self.impute_age, axis = 1)
        self.titanic.drop(labels=['deck', 'embark_town', 'alive'], inplace = True, axis = 1)
        common_value = 'S'
        self.titanic['embarked'].fillna(common_value, inplace = True)
        print(self.titanic.info())
        print(self.titanic.head())

        # Convert float to integer
        self.titanic['fare'] = self.titanic['fare'].astype('int')
        self.titanic['age'] = self.titanic['age'].astype('int')
        self.titanic['pclass'] = self.titanic['pclass'].astype('int')
        print(self.titanic.info())

        # Convert categorical data into numerical data
        genders = {'male': 0, 'female': 1}
        self.titanic['sex'] = self.titanic['sex'].map(genders)
        who = {'man': 0, 'woman': 1, 'child': 2}
        self.titanic['who'] = self.titanic['who'].map(who)
        adult_male = {True: 1, False: 0}
        self.titanic['adult_male'] = self.titanic['adult_male'].map(adult_male)
        alone = {True: 1, False: 0}
        self.titanic['alone'] = self.titanic['alone'].map(alone)
        ports = {'S': 0, 'C': 1, 'Q': 2}
        self.titanic['embarked'] = self.titanic['embarked'].map(ports)
        print(self.titanic.head())

        # Drop class and who data
        self.titanic.drop(labels = ['class', 'who'], axis = 1, inplace= True)
        print(self.titanic.head())

    # Build model
    def build_model(self):
        X = self.titanic.drop('survived', axis = 1)
        y = self.titanic['survived']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
        print(X_train.shape)

        model = []
        model.append(('LR', LogisticRegression(max_iter=400)))
        model.append(('KNN', KNeighborsClassifier()))
        model.append(('DTC', DecisionTreeClassifier()))
        model.append(('GNB', GaussianNB()))
        model.append(('SVC', SVC()))

        # Train model
        for name, mod in model:
            mod.fit(X_train, y_train)
            prediction = mod.predict(X_test)
            acc_val = accuracy_score(y_test, prediction)
            f1_val = f1_score(y_test, prediction)
            prec_val = precision_score(y_test, prediction)
            rec_val = recall_score(y_test, prediction)
            print("The model is {} and Accuracy: {}, Precision: {}, Recall: {}, F1: {}".format(name, acc_val, f1_val, prec_val, rec_val), "\n")
            
            # Compute mean absolute error
            print(pd.DataFrame({
                'Actual': y_test,
                'New_pred': prediction,
                'Error': mean_absolute_error(y_test, prediction)
            }))

            # Compute confusion matrix
            print(confusion_matrix(y_test, prediction), "\n")
            

if __name__ == "__main__":
    data = Basics()

    # Prepare data
    data.prepare_data()
    
    # Process data
    data.process_data()
    
    # Build model
    data.build_model()