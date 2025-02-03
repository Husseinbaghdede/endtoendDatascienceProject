# Pure Palate Prediction - Machine Learning Web App

## 📌 Project Overview
This project is a **Flask-based web application** that predicts the quality of beverages based on their physicochemical properties. Users can input various attributes, and the trained machine learning model will predict the **beverage quality score**.

## ✨ Features
- **User-friendly web interface** built with Flask.
- **Machine Learning pipeline** for prediction.
- **Interactive form submission** for user input.
- **MLflow integration** for experiment tracking.
- **DagsHub integration** for model versioning.
- **Automatic error handling** with proper feedback to users.

---

## 📂 Project Structure
```
project/
│
├── .github/                        # GitHub workflows and actions
├── artifacts/                      # Stores model artifacts
│   ├── model_trainer/
│   │   └── model.joblib              # Trained model file
├── config/                         # Configuration files
├── logs/                           # Logs for debugging and tracking
├── research/                       # Jupyter notebooks or experiments
├── src/
│   ├── datascience/
│   │   ├── components/             # Modular components of the pipeline
│   │   ├── config/                 # Configuration management
│   │   ├── constants/              # Constants used across the project
│   │   ├── entity/                 # Data entities and schema
│   │   ├── pipeline/               # ML pipeline (e.g., prediction_pipeline.py)
│   │   └── utils/                  # Utility scripts
│   └── __init__.py                 # Package initializer
├── templates/                      # HTML templates for the web app
│   ├── index.html                   # User input page
│   ├── results.html                 # Prediction result page
├── venv/                           # Virtual environment
├── .env                            # Environment variables
├── .gitignore                      # Ignored files and directories
├── app.py                          # Flask application
├── Dockerfile                      # Docker configuration
├── main.py                         # Entry point for execution
├── params.yaml                     # Parameter configurations
├── README.md                       # Documentation (this file)
├── requirements.txt                # Dependencies
├── schema.yaml                     # Data schema for validation
├── setup.py                        # Setup script for packaging
├── template.py                     # Additional scripts or templates
```

---

## 🚀 Installation & Setup
### Prerequisites:
Ensure you have **Python 3.8+** installed.

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/pure-palate-prediction.git
cd pure-palate-prediction
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up Environment Variables
Create a `.env` file and add the following:
```env
MLFLOW_TRACKING_URI=https://dagshub.com/yourusername/pure-palate-project.mlflow
MLFLOW_TRACKING_USERNAME=yourusername
MLFLOW_TRACKING_PASSWORD=yourpat
```

### 4️⃣ Run the Flask Application
```bash
python app.py
```
Now, open your browser and go to **`http://127.0.0.1:5000/`**.

---

## 📝 Usage Guide
1️⃣ **Enter beverage attributes** on the homepage.
2️⃣ **Submit** the form.
3️⃣ The prediction result appears on a new page.

---

## 🏗️ Model Details
- **Algorithm Used:** ElasticNet Regression
- **Metrics Tracked:** RMSE, MAE, R2 Score
- **Tracked on:** MLflow (DagsHub)
- **Model File:** `artifacts/model_trainer/model.joblib`

---

## ⚡ API Endpoints
| Endpoint  | Method | Description |
|-----------|--------|-------------|
| `/` | GET | Home page |
| `/predict` | POST | Handles form submission and returns prediction |

---

## 📌 Screenshots
**Home Page:**
![Home Page](static/homepage.png)

**Prediction Result:**
![Result Page](static/resultpage.png)

---

## 🔥 MLflow Experiment Tracking
- This project logs metrics and model artifacts to **MLflow**, hosted on **DagsHub**.
- To track experiments, navigate to:
  **[DagsHub MLflow UI](https://dagshub.com/yourusername/pure-palate-project.mlflow)**


## 💡 Acknowledgments
- **Scikit-learn** for machine learning modeling.
- **Flask** for backend development.
- **MLflow & DagsHub** for experiment tracking.



🎯 **Happy Coding & Experimenting!**



### Workflows--ML Pipeline

1. Data Ingestion
2. Data validation
3. Data Transformation-- Feature engineering, Data Preprocessing
4. Model Trainer
5. Model Evaluation- MLFLOW, DagsHub



## Workflows

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
