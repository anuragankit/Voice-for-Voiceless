# Voice for Voiceless 🧏‍♂️📢

A Python-based application that translates sign language gestures into alphabetic characters, enabling people with speech impairments to communicate more effectively.

---

## 🚀 Features

- Real-time hand gesture recognition using computer vision
- Converts American Sign Language (ASL) letters into readable text
- Supports data collection, model training, and live inference
- Easy-to-use and customizable

---

## 🧠 Technologies Used

- Python
- OpenCV
- Mediapipe
- Scikit-learn
- NumPy
- Pickle (for saving models)

---

## 📁 Project Structure
```
Sign2Speech-mainHead/
│
├── collect_imgs.py # Script to collect training images
├── create_dataset.py # Generates dataset from collected images
├── train_classifier.py # Trains a classifier model
├── inference_classifier.py # Performs real-time inference
├── data/ # Folder where image data is stored
├── data.pickle # Dataset in pickled format
├── model.p # Trained classifier model
├── requirements.txt # Dependency file
└── README.md
```

---

## ⚙️ Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/anuragankit/Voice-for-Voiceless.git
cd Voice-for-Voiceless

python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows
```

Install Dependencies
```
bash
Copy
Edit
pip install -r requirements.txt
```
Collect Training Data 
```
bash
Copy
Edit
python collect_imgs.py
```
Create Dataset
```
bash
Copy
Edit
python create_dataset.py
```
Train the Classifier
```
bash
Copy
Edit
python train_classifier.py
```
Run Inference
```
bash
Copy
Edit
python inference_classifier.py
```
📌 Notes
Make sure your webcam is working properly.

The trained model is saved as model.p, you can retrain or use it directly.

For best results, ensure good lighting and background contrast.

🤝 Contributing
Contributions are welcome! Fork the repo and submit a pull request to improve gesture support, UI/UX, or inference performance.

🖥️ DEVELOPED BY ``` ANKIT ANURAG ```

