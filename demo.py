import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import pickle

# Đọc dữ liệu từ file CSV
data = pd.read_csv("spam.csv")

# Kiểm tra các cột có trong dữ liệu
print(data.columns)

# Chuyển đổi dữ liệu trong cột 'Category' thành giá trị số
data['class'] = data['Category'].map({'ham': 0, 'spam': 1})

# Biến đổi văn bản bằng CountVectorizer
cv = CountVectorizer()
x = data['Message']
y = data['class']
x = cv.fit_transform(x)

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Huấn luyện mô hình Naive Bayes
model = MultinomialNB()
model.fit(x_train, y_train)

# Lưu mô hình
with open('spam_model.pkl', 'wb') as file:
    pickle.dump(model, file)

with open('count_vectorizer.pkl', 'wb') as file:
    pickle.dump(cv, file)

# Kiểm tra một tin nhắn mới
msg = "Your account has been hacked, click here to reset your password."
data = [msg]
vect = cv.transform(data).toarray()
result = model.predict(vect)
print("Dự đoán:", "Spam" if result[0] == 1 else "Ham")
