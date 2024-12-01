import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.compose import ColumnTransformer
from sklearn.metrics import classification_report
import joblib

def train_model(data_path="data/generated_data.csv", model_path="machine_learning/models/model.pkl"):
    df = pd.read_csv(data_path)

    # Features and label
    X = df[["height", "weight", "preference", "age", "body_shape"]]
    y = df["size"]

    # Preprocessing
    preprocessor = ColumnTransformer([
        ("num", StandardScaler(), ["height", "weight", "age"]),
        ("cat", OneHotEncoder(), ["preference", "body_shape"])
    ])

    # Model pipeline
    model = make_pipeline(preprocessor, LogisticRegression(max_iter=1000))

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, model_path)

    # Evaluate
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    train_model()
