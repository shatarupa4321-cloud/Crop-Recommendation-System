# 🌱 Crop Recommendation System

A machine learning-based web application that recommends suitable crops based on soil nutrients and environmental conditions.

## 📌 Project Overview

The Crop Recommendation System helps users identify suitable crops using important agricultural parameters. It uses a trained machine learning model to generate crop recommendations from user-provided inputs.

## ✨ Features

- Enter soil nutrient values: Nitrogen (N), Phosphorus (P), and Potassium (K).
- Provide temperature, humidity, soil pH, and rainfall values.
- Predict suitable crops using a trained machine learning model.
- View recommendations through a Streamlit user interface.
- Use a Flask backend to process prediction requests.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Machine Learning:** Scikit-learn
- **Frontend:** Streamlit
- **Backend:** Flask
- **Data Processing:** Pandas
- **Tools:** Jupyter Notebook, Git, GitHub

## 📂 Project Structure

```text
Crop-Recommendation-System/
├── app_ui.py
├── farm.jpg
├── .gitignore
└── backend/
    ├── app.py
    ├── classifier.pkl
    ├── crop_recommendation.csv
    └── train_model (1).ipynb
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/shatarupa4321-cloud/Crop-Recommendation-System.git
cd Crop-Recommendation-System
```

### 2. Install dependencies

Install the Python packages required by the application:

```bash
pip install streamlit flask pandas numpy scikit-learn requests
```

### 3. Start the Flask backend

Open a terminal in the project directory and run:

```bash
python backend/app.py
```

Keep this terminal running.

### 4. Start the Streamlit application

Open a second terminal in the project directory and run:

```bash
python -m streamlit run app_ui.py
```

The application will open in your browser.

## 📸 Application Screenshots

### Crop Recommendation System — Interface

![Crop Recommendation System Interface](screenshots/Screenshot%20(257).png)

### Crop Recommendation System — Output

![Crop Recommendation System Output](screenshots/Screenshot%20(258).png)

## 🧠 How It Works

1. The user enters soil nutrient and environmental values.
2. The Streamlit interface sends the inputs to the Flask backend.
3. The trained machine learning model processes the inputs.
4. The application displays the predicted crop recommendations.

## 🎯 Project Objective

To demonstrate the application of machine learning and web development to an agricultural problem by helping users explore crop choices based on soil and environmental conditions.

---

**Developed as a machine learning project using Python.**
