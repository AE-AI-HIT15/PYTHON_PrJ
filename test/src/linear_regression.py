import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class AlgorithmModel:
    def __init__(self):
        self.model = self._train_model()

    def _train_model(self):
        # Đọc dữ liệu (xóa index_col nếu lỗi)
        train_data = pd.read_csv(r"D:\desktop\Python\project_python\test\data\train.csv")

        # Kiểm tra nếu "Id" có trong cột, đặt nó làm index
        if "Id" in train_data.columns:
            train_data.set_index("Id", inplace=True)

        # Chọn các đặc trưng để huấn luyện
        features = ["LotArea", "YearBuilt", "GrLivArea", "BedroomAbvGr", "TotRmsAbvGrd"]
        X = train_data[features]
        y = train_data["SalePrice"]

        # Chia tập dữ liệu train/test
        X_train, X_val, y_train, y_val = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=42)

        # Huấn luyện mô hình hồi quy tuyến tính
        lr_model = LinearRegression()
        lr_model.fit(X_train, y_train)

        return lr_model
    
    def predict(self, x: np.ndarray) -> float:
        x = np.array(x).reshape(1, -1)  # Đảm bảo đầu vào có đúng định dạng (1, số đặc trưng)
        return float(self.model.predict(x)[0])  # Chuyển kết quả thành float
