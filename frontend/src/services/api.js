// Mock Database Data

let mockHistory = [
  {
    _id: "report1",
    crop: "Tomato",
    disease: "Early Blight",
    status: "Moderate",
    confidence: "88%",
    date: "2023-10-14T10:30:00Z",
  },
  {
    _id: "report2",
    crop: "Rice",
    disease: "Brown Spot",
    status: "Severe",
    confidence: "92%",
    date: "2023-09-21T14:15:00Z",
  },
];

export const saveToHistory = async (report) => {
  return new Promise((resolve) => {
    setTimeout(() => {
      const newReport = {
        _id: `report${Date.now()}`,
        crop: report.cropName || "Unknown Crop",
        disease: report.diseaseName || "Unknown Disease",
        status: report.severity || "Moderate",
        confidence: report.confidence || "0%",
        date: new Date().toISOString(),
      };
      // Add to the beginning of the array so newest is first
      mockHistory = [newReport, ...mockHistory];
      resolve({ success: true, report: newReport });
    }, 500);
  });
};

const mockLibrary = [
  {
    id: 1,
    crop: "Tomato",
    name: "Late Blight",
    symptoms:
      "Dark lesions on leaves, white fungal growth on undersides in humid weather.",
    causes: "Phytophthora infestans (fungus-like organism)",
    prevention: "Apply copper-based fungicides, avoid overhead watering.",
  },
  {
    id: 2,
    crop: "Potato",
    name: "Early Blight",
    symptoms:
      "Brown spots with concentric rings (target spots) on older leaves.",
    causes: "Alternaria solani (fungus)",
    prevention:
      "Crop rotation, ensure adequate nitrogen, apply fungicides early.",
  },
  {
    id: 3,
    crop: "Wheat",
    name: "Rust",
    symptoms: "Yellow, orange, or reddish-brown powdery pustules on leaves.",
    causes: "Puccinia spp. (fungus)",
    prevention: "Plant resistant varieties, apply foliar fungicides timely.",
  },
];

// Mock Auth
export const registerUser = async (userData) => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({
        success: true,
        user: { name: userData.name || "Farmer", email: userData.email },
      });
    }, 1000);
  });
};

export const loginUser = async (credentials) => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({
        success: true,
        user: { name: "Test Farmer", email: credentials.email },
      });
    }, 1000);
  });
};

// Real Application Services
export const predictCropDisease = async (imageFile) => {
  const formData = new FormData();
  formData.append("file", imageFile);

  try {
    const response = await fetch("http://localhost:8000/predict", {
      method: "POST",
      body: formData,
    });

    // 422 = crop validation rejected (not a leaf image)
    if (response.status === 422) {
      const errorData = await response.json();
      return {
        validationError: true,
        detail:
          errorData.detail ||
          "Image does not appear to be a crop leaf. Please upload a clear plant leaf photo.",
      };
    }

    if (!response.ok) {
      throw new Error(`Server error (${response.status}). Please try again.`);
    }

    const data = await response.json();
    // Recommendations are now returned by the backend itself;
    // fall back to generics only if absent.
    return {
      ...data,
      description:
        data.description || "AI-powered analysis from the CNN model.",
      recommendations: data.recommendations || {
        immediate: ["Consult with a local agricultural expert."],
        organic: ["Apply neem oil or other organic fungicides."],
        chemical: ["Use fungicides as per local agricultural guidelines."],
        preventive: ["Ensure proper crop rotation and soil health management."],
      },
    };
  } catch (error) {
    console.error("Prediction error:", error);
    throw new Error(
      error.message ||
        "Could not connect to the backend server. Please ensure the FastAPI server is running on port 8000."
    );
  }
};

const OPENAI_API_KEY =
  "PULL_FROM_ENV_OR_REPLACE_WITH_YOUR_KEY";

const SYSTEM_PROMPT = `You are CropCare AI, an expert agricultural assistant specializing in crop diseases, plant health, and farming best practices. You help farmers identify diseases, understand symptoms, and get actionable advice on:
- Crop disease diagnosis and treatment
- Organic and chemical remedies
- Fertilizer and soil health recommendations
- Preventive farming practices
- Weather impact on crops
Keep your answers concise, practical, and farmer-friendly. If a question is unrelated to agriculture, politely redirect the conversation back to farming topics.`;

export const chatWithBot = async (message) => {
  try {
    const response = await fetch("https://api.openai.com/v1/chat/completions", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${OPENAI_API_KEY}`,
      },
      body: JSON.stringify({
        model: "gpt-4o-mini",
        messages: [
          { role: "system", content: SYSTEM_PROMPT },
          { role: "user", content: message },
        ],
        max_tokens: 300,
        temperature: 0.7,
      }),
    });

    if (!response.ok) {
      const err = await response.json();
      throw new Error(err.error?.message || "OpenAI API error");
    }

    const data = await response.json();
    const reply = data.choices?.[0]?.message?.content?.trim();
    return { reply: reply || "Sorry, I couldn't generate a response. Please try again." };
  } catch (error) {
    console.error("Chatbot error:", error);
    return {
      reply:
        "Sorry, I'm having trouble connecting right now. Please check your internet connection and try again.",
    };
  }
};

export const getHistory = async () => {
  return new Promise((resolve) => {
    setTimeout(() => resolve(mockHistory), 800);
  });
};

export const getWeatherData = async () => {
  return new Promise((resolve) => {
    setTimeout(() => {
      resolve({
        temp: "28°C",
        humidity: "85%",
        rain: "60%",
        wind: "12 km/h",
        alert: "High humidity detected - fungal risk",
      });
    }, 500);
  });
};

export const getDiseaseLibrary = async () => {
  return new Promise((resolve) => {
    setTimeout(() => resolve(mockLibrary), 600);
  });
};

export default {
  registerUser,
  loginUser,
  predictCropDisease,
  chatWithBot,
  saveToHistory,
  getHistory,
  getWeatherData,
  getDiseaseLibrary,
};
