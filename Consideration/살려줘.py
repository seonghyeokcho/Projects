import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# Load data and select columns
path = 'C:/_data/'
ts = 1
df = pd.read_csv(path + "아파트(매매).csv")
df = df[["거래금액(만원)","본번", "부번", "단지명", "전용면적(㎡)", "계약년월","층", "건축년도"]]
df.drop('본번', axis=1)
df.drop('부번', axis=1)
df.drop('단지명', axis=1)
df.drop('전용면적(㎡)', axis=1)
df.drop('계약년월', axis=1)
df.drop('건축년도', axis=1)
# Fit label encoders to categorical columns
label_encoders = {}
for col in df.select_dtypes(include=['object']):
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# Print label mappings for each column
for col, le in label_encoders.items():
    print(col, dict(zip(le.classes_, le.transform(le.classes_))))


# Split data into train and test sets
train_size = int(len(df) * 0.8)
train_data = df.iloc[:train_size]
test_data = df.iloc[train_size:]

# Scale data using MinMaxScaler
scaler = MinMaxScaler()
train_data = scaler.fit_transform(train_data)
test_data = scaler.transform(test_data)

# Prepare data for LSTM model
def prepare_data(data, time_steps=1):
    X, Y = [], []
    for i in range(len(data) - time_steps):
        a = data[i:(i + time_steps), :]
        X.append(a)
        Y.append(data[i + time_steps, 0])
    return np.array(X), np.array(Y)

train_X, train_Y = prepare_data(train_data)
test_X, test_Y = prepare_data(test_data)

# Build LSTM model
model = Sequential()
model.add(LSTM(10, input_shape=(ts,train_X.shape[2])))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')

# Train LSTM model
model.fit(train_X, train_Y, epochs=200, batch_size=5, verbose=2)

# Evaluate LSTM model
loss, accuracy = model.evaluate(test_X, test_Y, verbose=0)
print('mse', mse)
print('Test accuracy:', accuracy)

y_pred = model.predict(test_X)
r2 = r2_score(test_Y, y_pred)
print('r2 score:', r2)