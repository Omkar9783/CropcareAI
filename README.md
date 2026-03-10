# CropCare AI 🌿

CropCare AI is an advanced, full-stack agricultural support application designed to empower farmers with state-of-the-art machine learning detection and community-driven knowledge. 

By simply uploading a photo of a crop leaf, the application detects potential diseases, estimates confidence and severity, and provides immediate, organic, and chemical treatment recommendations.

---

## 🚀 Features

- **Instant AI Disease Detection**: Upload a leaf photo to diagnose diseases across 14 supported crops (Tomato, Potato, Corn, Grape, Apple, and more) using our custom-trained Convolutional Neural Network.
- **Actionable AI Recommendations**: Receive categorized advice (Immediate, Organic, Chemical, Preventive) translated directly into your preferred language.
- **Smart Local Business Model**: The platform automatically recommends specific branded fertilizers safely available in your area and lists the closest verified agro-centers where you can buy them, complete with distance tracking and call-now functionality.
- **Native Multi-language Support**: Experience the entire application (including dynamic AI scans and chatbot responses) seamlessly integrated into English, Hindi, and Marathi.
- **AI Chatbot Assistant**: Ask natural-language questions about agriculture, weather impacts, or soil health and receive context-aware advice powered by modern LLMs.

---

## 🛠 Tech Stack

**Frontend**
- **React.js (Vite)** 
- **Tailwind CSS** & **Tailwind Typography**
- **Lucide React** (Iconography)
- **i18next** (Dynamic multi-language routing)
- **React Markdown** (Native chat formatting)

**Backend / AI Engine**
- **Python 3** & **FastAPI**
- **TensorFlow / Keras** (Image classification models)
- **Deep-Translator** (Dynamic backend localization)
- **Uvicorn** (Asynchronous backend serving)
- **Pillow / Numpy** (Image tensor preprocessing)

---

## ⚙️ Getting Started

### Prerequisites
- Node.js (v18+)
- Python 3.10+
- Optional: Add your Google `Gemini` API key to `frontend/.env` to unlock advanced chatbot intelligence.

### 1. Setup the Backend
Navigate to the backend directory, install the Python requirements, and start the FastAPI server:

```bash
cd backend
python -m venv venv310
source venv310/bin/activate  # On Windows: venv310\Scripts\activate
pip install -r requirements.txt
python main.py
```
*The backend server will run on `http://localhost:8000`.*

### 2. Setup the Frontend
Open a new terminal session, navigate to the frontend directory, install the NPM dependencies, and start the Vite development server:

```bash
cd frontend
npm install
npm run dev
```
*The frontend application will run on `http://localhost:5173`.*

---

## 🌍 Language Translation Engine
The application ships with dynamically generated locale files. To modify or add new languages (e.g., Gujarati, Bengali), simply edit the base `frontend/src/locales/en.json` file and run our custom python translator script:

```bash
cd backend
python translate.py
```

---

## ⚖️ License
This project is open-source and free to distribute. Built to elevate modern agriculture through accessible intelligence.
