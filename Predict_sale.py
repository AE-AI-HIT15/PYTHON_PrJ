import numpy as np
import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# Đọc dữ liệu
train_data = pd.read_csv('train.csv', index_col="Id")
test_data = pd.read_csv('test.csv', index_col="Id")

# Chỉ lấy các giá trị có trong RL/RM
train_data = train_data[train_data["MSZoning"].isin(["RL", "RM"])]
test_data = test_data[test_data["MSZoning"].isin(["RL", "RM"])]

# Mã hóa MSZoning: RL → 0, RM → 1
zone_mapping = {"RL": 0, "RM": 1}
train_data["MSZoning"] = train_data["MSZoning"].map(zone_mapping)
test_data["MSZoning"] = test_data["MSZoning"].map(zone_mapping)

# Chọn các đặc trưng
features = ["MSZoning", "LotArea", "YearBuilt", "GrLivArea", "BedroomAbvGr", "TotRmsAbvGrd"]
X = train_data[features]
y = train_data["SalePrice"]

# Chia dữ liệu
X_train, X_val, y_train, y_val = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)

# Huấn luyện mô hình Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Dự đoán tập validation
y_preds = lr_model.predict(X_val)

# Dự đoán tập test
X_test = test_data[features]
y_preds_test = lr_model.predict(X_test)


# Huấn luyện Random Forest
rf_model = RandomForestRegressor(random_state=1)
rf_model.fit(X_train, y_train)
y_preds_rf = rf_model.predict(X_test)

# Giao diện Streamlit
st.title("Dự đoán Giá Bán Nhà")
st.write("Nhập các thông số dưới đây để dự đoán giá bán nhà:")

# Input người dùng
LotArea = st.number_input("Diện tích lô đất (m²)", min_value=0)
YearBuilt = st.number_input("Năm xây dựng", min_value=1800, max_value=2024)
MSZoning = st.selectbox("Khu vực quy hoạch", ["RL", "RM"])
GrLivArea = st.number_input("Diện tích nhà (m²)", min_value=0)
BedroomAbvGr = st.number_input("Số phòng ngủ", min_value=0)
TotRmsAbvGrd = st.number_input("Tổng số phòng", min_value=0)

# Chuyển đổi MSZoning
MSZoning = zone_mapping[MSZoning]

# Dự đoán giá khi bấm nút
if st.button("Dự đoán"):
    input_data = pd.DataFrame([[MSZoning, LotArea, YearBuilt, GrLivArea, BedroomAbvGr, TotRmsAbvGrd]],
                              columns=features).astype(float)
    prediction = lr_model.predict(input_data)
    st.write(f"Giá bán dự đoán: ${prediction[0]:,.2f}")
