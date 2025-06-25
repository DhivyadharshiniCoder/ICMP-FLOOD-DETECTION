# ICMP Flood Detection using Machine Learning

This project uses a **Random Forest Classifier** to detect ICMP flood attacks based on network traffic data. It features a user-friendly **Streamlit interface** where users can upload `.csv` files and receive real-time attack predictions.

---

## 📸 Screenshot

![imageoficmp](https://github.com/user-attachments/assets/736ccc3d-fcc0-49b1-8795-24f85aa8c303)


---

## 🔍 Project Overview

- **Goal:** Detect ICMP (Internet Control Message Protocol) flood attacks using machine learning
- **Model:** Random Forest Classifier
- **Frontend:** Built with Streamlit
- **Input:** Network traffic in CSV format
- **Output:** Tabular predictions showing each row's classification

---

## 🧰 Features

- Upload CSV files for batch prediction
- Streamlit UI with table output and result download
- Accurate detection based on trained network features

---

## 📁 Project Files

- `app.py`: Streamlit frontend
- `random_forest_model.pkl`: Pre-trained ML model
- `requirements.txt`: Python dependencies
- `imageoficmp.png`: App screenshot
- `README.md`: Project documentation

---


## 💻 How to Run the App

Install dependencies:

```bash
pip install -r requirements.txt
Then run the app:
streamlit run app.py
Open the URL shown in terminal (e.g., http://localhost:8501)

🧠 Model Training Summary
Model trained using labeled ICMP flood dataset (ICMP_flood.csv)

Preprocessing included encoding, missing value handling

Model selection based on accuracy and F1-score

Final model: Random Forest with high performance on test data

🙋‍♀️ Author
Dhivyadharshini V
https://github.com/DhivyadharshiniCoder

📜 License
This project is open source under the MIT License.

yaml
Copy
Edit

---

### ✅ Next Steps:

1. Save this as `README.md` in your project folder  
2. Make sure `imageoficmp.png` is also in the same folder  
3. Run:

```bash
git add README.md imageoficmp.png
git commit -m "Added README with screenshot"
git push
