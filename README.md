# 📧 Spam Classifier Web App

A simple machine learning-powered web application that detects whether a message is spam or not, built using Python, Scikit-learn, and Streamlit.

![screenshot](https://via.placeholder.com/800x400.png?text=Spam+Classifier+App+Screenshot) <!-- Replace this with your own screenshot if available -->

---

## 🚀 Features

- 🧠 Trained on real SMS spam data
- ⚙️ Uses Naive Bayes and CountVectorizer
- 🌐 Interactive web interface with Streamlit
- 🗃️ Easy to run locally or deploy online

---

## 📂 Project Structure

spam-classifier-app/
├── app.py # Streamlit web app
├── model.py # ML training script
├── spam.csv # Dataset
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── .gitignore # Ignore cache and venv files


---

## 🧪 Example Inputs

### ✅ Not Spam:
- "Hey, are we still meeting at 6 PM?"
- "Happy birthday! Hope you have a great day."

### 🚨 Spam:
- "Congratulations! You've won a $1000 gift card."
- "Click here to claim your free cruise now."

---

## 💻 How to Run Locally

1. **Clone this repository**:
   ```bash
   git clone https://github.com/your-username/spam-classifier-app.git
   cd spam-classifier-app


Create and activate a virtual environment:

bash
Copy
Edit
python3 -m venv venv
source venv/bin/activate

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Train the model (only needs to be done once):

bash
Copy
Edit
python model.py
Run the web app:

bash
Copy
Edit
streamlit run app.py
The app will open in your browser at http://localhost:8501.
