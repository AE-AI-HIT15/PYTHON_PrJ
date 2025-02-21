import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from functools import cached_property

class AlgorithmModel:
    @cached_property
    def model(self):
        train_data = pd.read_csv('D:\desktop\Python\Project-HIT PYTHON\test\home-data-for-ml-course\train.csv', index_col="Id")
        test_data = pd.read_csv('D:\desktop\Python\Project-HIT PYTHON\test\home-data-for-ml-course\test.csv', index_col="Id")

        # Select features
        features = ["LotArea", "YearBuilt", "GrLivArea", "BedroomAbvGr", "TotRmsAbvGrd"]
        X = train_data[features]
        y = train_data["SalePrice"]

        # Split datas
        X_train, X_val, y_train, y_val = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=42)

        # Train the linear regression model
        lr_model = LinearRegression()
        lr_model.fit(X_train, y_train)

        return lr_model
    
    
    def predict(self, x: np.ndarray) -> float:
        return self.model.predict(x)

    


