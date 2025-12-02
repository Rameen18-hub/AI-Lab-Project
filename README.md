# **STUDENT RESULT DATABASE SYSTEM**

A Machine Learning–powered Flask web application that **collects and analyzes AI job market data**, applies ML models to **predict future demand trends**, and presents **key insights through visualizations**.

---

## 📌 **Project Overview**

This project focuses on analyzing AI job market data and predicting future trends using a complete ML pipeline. The project includes:

* ✔ Data collection & preprocessing
* ✔ Exploratory Data Analysis (EDA)
* ✔ Feature engineering
* ✔ ML model training using RandomForest
* ✔ Model evaluation (Accuracy / RMSE)
* ✔ Saving a trained pipeline using `pickle`
* ✔ Flask-based interactive web application
* ✔ HTML form input for predictions

---

## 🧠 **Machine Learning Workflow**

1. Load dataset
2. Clean missing and invalid values
3. Perform label encoding and one-hot encoding
4. Split dataset (80% training, 20% testing)
5. Build ML pipeline (Preprocessing + Model)
6. Train the model using RandomForest (Regressor or Classifier auto-detected)
7. Test and evaluate performance
8. Save pipeline -> `/static/model/best_regression_.pkl`

---

## 📊 **Technologies Used**

| Category      | Tools                   |
| ------------- | ----------------------- |
| Backend       | Flask                   |
| ML            | Scikit-Learn            |
| Data Handling | Pandas, NumPy           |
| Frontend      | HTML, CSS               |
| Render / PythonAnywhere |
| Model Saving  | Pickle                  |

---

## 📁 **Project Directory Structure**

```
/project-folder
│
├── app.py
├── requirements.txt
│
├── static/
│   └── model/
│       └── pipeline.pkl
│
└── templates/
    └── index.html
```

---

## 🧪 **Model Evaluation**

The project automatically detects whether the task is classification or regression and evaluates the model using:

* **Classification:** Accuracy, Classification Report
* **Regression:** RMSE, R² Score

---

## 🚀 **Running the Project Locally**

```

### **2. Create Virtual Environment:**

```
python -m venv venv
venv/Scripts/activate       # Windows
```

### **3. Install Dependencies:**

```
pip install -r requirements.txt
```

### **4. Run Flask App:**

```
python app.py
```

### **5. Open Browser:**

```
http://127.0.0.1:8501
```

---

```
Flask
scikit-learn
pandas
numpy


```



