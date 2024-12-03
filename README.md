# **Outfit Size Finder**

A machine learning-powered API to predict clothing sizes based on user input features like height, weight, preference, age, and body shape. The project uses **Python**, **Scikit-learn**, **Django**, and **Django REST Framework**.

***The model is trained using synthetic data to simulate a scenarios for portfolio purposes and is not suitable for real application usage.***


---

## **Features**
- Predict clothing sizes using a logistic regression model.
- Get evaluation metrics (precision, recall, F1-score) of the trained model.
- Built-in synthetic data generation for development and testing.

---

## **Tech Stack**
- **Backend:** Django, Django REST Framework
- **Machine Learning:** Scikit-learn, Pandas
- **Other Tools:** joblib (model persistence)

---

## **Installation**

### **Clone the Repository**
```bash
git clone https://github.com/fabio-trajano/outfit-size-finder.git
cd outfit-size-finder
```

### **Set Up a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
```

### **Install Dependencies**
```bash
pip install -r requirements.txt
```

### **Run Migrations**
```bash
python manage.py migrate
```

### **Generate Synthetic Data**
```bash
python data_generation.py
```

### **Train the Model**
```bash
python ml/train.py
```

### **Run the Server**
```bash
python manage.py runserver
```

## **API Documentation**
### **1. Predict Clothing Size**
- Endpoint: `/api/predict-size/`
- Method: `POST`
- Description: Predicts the clothing size based on input features.

**Request Body:**
```bash
{
    "height": 175.0,
    "weight": 70.0,
    "preference": "tight",  // Options: "tight", "loose", "regular"
    "age": 30,
    "body_shape": "athletic"  // Options: "slim", "average", "athletic", "plus-size"
}
```
**Response:**
```bash
200 OK:
{
    "predicted_size": "M"
}
```
### **2. Get Model Metrics**
- Endpoint: `/api/model-metrics/`
- Method: `GET`
- Description: Returns the evaluation metrics (precision, recall, F1-score) of the trained model.

**Response:**
```bash
200 OK:
{
    "XXS": {
        "precision": 0.85,
        "recall": 0.80,
        "f1-score": 0.82,
        "support": 50
    },
    "accuracy": 0.87,
    "macro avg": {
        "precision": 0.86,
        "recall": 0.84,
        "f1-score": 0.85,
        "support": 500
    }
}
```

## **Project Structure**
```bash
outfit-size-finder/
│
├── api/
│   ├── migrations/
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── data/
│   └── generated_data.csv
│
├── machine_learning/
│   ├── models/
│   │   ├── model.pkl
│   │   └── metrics.json
│   ├── train.py
│   ├── data_generation.py
│
├── project_name/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
├── requirements.txt
├── README.md
```
## License

Distributed under the [MIT License](LICENSE). See the [LICENSE](LICENSE) file for more information.
