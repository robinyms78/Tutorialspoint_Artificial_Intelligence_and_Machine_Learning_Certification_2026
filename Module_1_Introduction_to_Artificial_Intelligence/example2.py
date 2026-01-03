import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error

class PerceptronExample:
    def __init__(self):
        self.Data = pd.read_csv(r'Module_1_Introduction_to_Artificial_Intelligence\data\FuelConsumption.csv')

    # Import data
    def import_data(self):
        print(self.Data.head())

        X = self.Data[['CYLINDERS']]
        y = self.Data['CO2EMISSIONS']
        print("X: ", X)
        print("y: ", y)

        return X, y

    # Train model
    def train_simple_model(self, X, y):
        X_train, X_test, y_train, y_test = train_test_split(X, y)
        model = Perceptron()
        model.fit(X_train, y_train)
        train_score = model.score(X_train, y_train)
        print("train_score: ", train_score, "\n")

        train_score = model.score(X_test, y_test)
        print("train_score: ", train_score, "\n")

        input_value = pd.DataFrame([[4]], columns=["CYLINDERS"])
        result = model.predict(input_value)
        print("result:", result, "\n")

    # Process data
    def process_data(self, X, y):
        X = self.Data.drop(['CO2EMISSIONS', 'MODELYEAR', 'MAKE', 'MODEL', 'VEHICLECLASS', 'TRANSMISSION', 'FUELTYPE'], axis = 1)
        print("X: ", X.head(), "\n")

        y = self.Data.CO2EMISSIONS
        print("y: ", y, "\n")

    # Train multilayer perception
    def train_multilayer_model(self, X, y):
        # Train model
        X_train, X_test, y_train, y_test = train_test_split(X, y)
        Model = MLPRegressor(max_iter=2000, hidden_layer_sizes=(10, 10, 10), early_stopping=True, activation='relu')
        Model.fit(X_train, y_train)

        # Check score
        train_result = Model.score(X_train, y_train)*100
        print("train_result: ", train_result, "\n")
        test_result = Model.score(X_test, y_test)*100
        print("test_result: ", test_result, "\n")

        # Check error
        Predict = Model.predict(X_test)
        print(pd.DataFrame({
            'Actual': y_test,
            'New_pred': Predict,
            'Error': mean_absolute_error(y_test, Predict)
        }), "\n")


if __name__ == "__main__":
    # Import data
    model = PerceptronExample()
    X, y = model.import_data()

    # Train model
    model.train_simple_model(X, y)

    # Process data
    model.process_data(X, y)

    # Train multilayer model
    model.train_multilayer_model(X, y)