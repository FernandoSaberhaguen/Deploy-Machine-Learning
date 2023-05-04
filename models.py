# import the necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.svm import SVR
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error, r2_score
from utils import Utils

class Models:
    
    def __init__(self):
        self.params = {
            'linear_regression': {'fit_intercept': [True, False]},
            'gradient_boosting_regressor': {'loss': ['squared_error', 'absolute_error', 'huber','quantile'],
                                            'learning_rate': [0.01, 0.05, 0.1],
                                            'n_estimators': [50, 100, 200]}
            #'support_vector_regressor': {'kernel': ['linear', 'poly', 'rbf', 'sigmoid'],
            #                             'C': [0.1, 1, 10, 100, 1000],
            #                             'gamma': ['scale', 'auto']}
        }
        self.models = {}
        
    def data_preprocessing(self, X, y):
        # split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
        
        # apply feature scaling to the training set
        sc_X = StandardScaler()
        X_train = sc_X.fit_transform(X_train)
        
        return X_train, X_test, y_train, y_test
    
    def grid_training(self, X, y):
        # perform grid search for each model and store the best estimator
        for name in self.params.keys():
            if name == 'linear_regression':
                reg = LinearRegression()
            elif name == 'gradient_boosting_regressor':
                reg = GradientBoostingRegressor()
            #elif name == 'support_vector_regressor':
            #    reg = SVR()
            
            grid_reg = GridSearchCV(reg, self.params[name], cv=3).fit(X, y.values.ravel())
            self.models[name] = grid_reg.best_estimator_
            print(f'{name}: {grid_reg.best_params_}')

            
    def evaluate_models(self, X, y):
        # evaluate the performance of each model on the testing set
        best_score = 999
        best_model = None
        for name, model in self.models.items():
            y_pred = model.predict(X)
            mse = mean_squared_error(y, y_pred)
            r2 = r2_score(y, y_pred)

            if r2 < best_score:
                best_score = r2
                best_model = grid_reg.best_params_
            
            print(f'{name}:')
            print(f'Mean Squared Error: {mse:.2f}')
            print(f'R^2 Score: {r2:.2f}')
        utils = Utils()
        utils.model_export(best_model, best_score)




