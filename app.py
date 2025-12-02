
# # from flask import Flask, render_template, request
# # import numpy as np
# # import pickle
# # import os

# # app = Flask(__name__)

# # # Load model
# # model_path = os.path.join("static", "model", "best_model.pkl")
# # model = pickle.load(open(model_path, "rb"))



# # @app.route("/", methods=["GET", "POST"])
# # def index():
# #     prediction = None

# #     if request.method == "POST":

# #         try:
# #             # Collect form data in exact order of your training features
# #             features = [
# #                 int(request.form["Gender"]),
# #                 float(request.form["Ethnicity"]),
# #                 float(request.form["ParentalEducation"]),
# #                 float(request.form["StudyTimeWeekly"]),
# #                 float(request.form["Absences"]),
# #                 int(request.form["Tutoring"]),
# #                 int(request.form["ParentalSupport"]),
# #                 int(request.form["Extracurricular"]),
# #                 int(request.form["Sports"]),
# #                 int(request.form["Music"]),
# #                 int(request.form["Volunteering"]),
# #                 float(request.form["GPA"])
# #             ]

# #             final_input = np.array([features])

# #             # Predict
# #             prediction = model.predict(final_input)[0]

# #         except Exception as e:
# #             prediction = f"Error: {str(e)}"

# #     return render_template("index.html", prediction=prediction)


# # if __name__ == "__main__":
# #     app.run(debug=True)


# # from flask import Flask, render_template, request
# # import numpy as np
# # import pickle

# # app = Flask(__name__)

# # # -------------------------
# # # Load model + scaler + features
# # # -------------------------
# # with open('static/model/best_regression_model.pkl', 'rb') as f:
# #     data = pickle.load(f)

# # model = data['model']
# # scaler = data['scaler']
# # selected_features = data['selected_features']


# # # -------------------------
# # # Home Page
# # # -------------------------
# # @app.route('/')
# # def index():
# #     return render_template('index.html')


# # # -------------------------
# # # Prediction Route
# # # -------------------------
# # @app.route('/predict', methods=['POST'])
# # def predict():

# #     try:
# #         # Collect input from HTML form
# #         input_values = []

# #         for feature in selected_features:
# #             value = float(request.form.get(feature))
# #             input_values.append(value)

# #         # Convert to array
# #         final_features = np.array([input_values])

# #         # Apply same scaling as training
# #         final_scaled = scaler.transform(final_features)

# #         # Predict
# #         prediction = model.predict(final_scaled)[0]

# #         return render_template('index.html',
# #                                result=f"Predicted Result: {prediction}")

# #     except Exception as e:
# #         return render_template('index.html',
# #                                result=f"Error: {str(e)}")


# # if __name__ == "__main__":
# #     app.run(debug=True)



# from flask import Flask, render_template, request
# import numpy as np
# import pickle

# app = Flask(__name__)

# # Load only model
# model = pickle.load(open('static/model/best_regression_model.pkl', 'rb'))

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():

#     try:
#         # Manually define feature order SAME AS TRAINING
#         features = [
#             'StudyTimeWeekly',
#             'Absences',
#             'GPA'
#         ]

#         input_values = []

#         for f in features:
#             input_values.append(float(request.form.get(f)))

#         final_input = np.array([input_values])

#         prediction = model.predict(final_input)[0]

#         return render_template('index.html',
#                                result=f"Predicted Result: {prediction}")

#     except Exception as e:
#         return render_template('index.html',
#                                result=f"Error: {str(e)}")

# if __name__ == "__main__":
#     app.run(debug=True)




# from flask import Flask, render_template, request
# import pickle
# import numpy as np

# app = Flask(__name__)

# # -------------------------
# #  LOAD MODELS
# # -------------------------

# # 1. Load Regression Model (Dictionary)
# with open("best_regression_model.pkl", "rb") as f:
#     reg_data = pickle.load(f)

# reg_model = reg_data["model"]
# scaler = reg_data["scaler"]
# reg_columns = reg_data["columns"]

# # 2. Load Classification Model (Single Object)
# with open("best_classification_model.pkl", "rb") as f:
#     class_model = pickle.load(f)

# # -------------------------
# #  ROUTES
# # -------------------------

# @app.route("/")
# def home():
#     return render_template("index.html", prediction=None)

# @app.route("/predict", methods=["POST"])
# def predict():

#     # Collect input for ALL features
#     input_data = []
#     for col in reg_columns:
#         value = float(request.form[col])
#         input_data.append(value)

#     X = np.array([input_data])

#     # GPA Prediction (scaled)
#     X_scaled = scaler.transform(X)
#     gpa_pred = reg_model.predict(X_scaled)[0]

#     # Grade Prediction (NO scaling)
#     grade_pred = class_model.predict(X)[0]

#     final_output = f"GPA: {round(gpa_pred,2)} | Grade Class: {grade_pred}"

#     return render_template("index.html", prediction=final_output)


# if __name__ == "__main__":
#     app.run(debug=True)


from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# -------------------------
# LOAD MODELS
# -------------------------

# Load Regression Model (Dictionary)
with open("best_regression_model.pkl", "rb") as f:
    reg_data = pickle.load(f)

reg_model = reg_data["model"]
scaler = reg_data["scaler"]

# FIX: Use SAME 12 fields as your HTML form
reg_columns = [
    "Gender", "Ethnicity", "ParentalEducation", "StudyTimeWeekly",
    "Absences", "Tutoring", "ParentalSupport", "Extracurricular",
    "Sports", "Music", "Volunteering", "GPA"
]

# Load Classification Model
with open("best_classification_model.pkl", "rb") as f:
    class_model = pickle.load(f)

# -------------------------
# ROUTES
# -------------------------

@app.route("/")
def home():
    return render_template("index.html", prediction=None)

@app.route("/predict", methods=["POST"])
def predict():

    # Collect inputs
    input_data = []
    for col in reg_columns:
        value = float(request.form[col])
        input_data.append(value)

    X = np.array([input_data])

    # GPA Prediction
    scaled_X = scaler.transform(X)
    gpa_pred = reg_model.predict(scaled_X)[0]

    # Grade Prediction
    grade_pred = class_model.predict(X)[0]

    final_output = f"GPA: {round(gpa_pred, 2)} | Grade Class: {grade_pred}"

    return render_template("index.html", prediction=final_output)

if __name__ == "__main__":
    app.run(debug=True)
