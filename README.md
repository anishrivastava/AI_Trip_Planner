# 🌍 Agentic AI Travel Planner using LangGraph

An AI-powered Travel Planner built using **LangGraph**, **LangChain**, **FastAPI**, and **Streamlit** that generates intelligent, personalized travel itineraries through autonomous tool orchestration. The application leverages LLM reasoning to dynamically invoke specialized tools for weather forecasting, destination discovery, expense estimation, currency conversion, and travel recommendations, delivering context-aware travel plans in real time.

Unlike traditional chatbots, this project follows an **Agentic AI architecture**, where the LLM decides which tool to invoke based on user intent, executes external APIs, and synthesizes the retrieved information into a comprehensive travel plan.

---

## 🚀 Features

- 🤖 Agentic AI workflow powered by **LangGraph**
- 🧠 LLM Tool Calling using LangChain
- 🌦️ Real-time Weather Forecast
- 📍 Tourist Attraction Discovery
- 🍽️ Restaurant Recommendations
- 🚕 Transportation Suggestions
- 💱 Live Currency Conversion
- 💰 Travel Expense & Budget Estimation
- 🗺️ AI-generated Day-wise Travel Itinerary
- ⚡ FastAPI REST Backend
- 🎨 Interactive Streamlit Frontend
- 🔧 Modular & Scalable Project Architecture
- 🐳 Docker Ready

---

## 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| AI Framework | LangGraph, LangChain |
| LLM | Groq, OpenAI |
| Backend | FastAPI |
| Frontend | Streamlit |
| APIs | OpenWeather API, Google Places API, Tavily Search API, Exchange Rate API |
| Language | Python |
| Deployment | Docker |

---

## 📂 Project Architecture

```
User
   │
   ▼
Streamlit UI
   │
   ▼
FastAPI Backend
   │
   ▼
LangGraph Workflow
   │
   ▼
LLM Agent
   │
   ▼
Tool Router
   │
   ▼
Weather │ Places │ Currency │ Expense Tools
   │
   ▼
External APIs
   │
   ▼
Final AI Response
```

---

## 📁 Project Structure

```
AI_Trip_Planner
│
├── agent/
│   └── agentic_workflow.py
│
├── tools/
│   ├── weather_info_tool.py
│   ├── place_search_tool.py
│   ├── calculator_tool.py
│   └── currency_conversion_tool.py
│
├── utils/
│   ├── weather_info.py
│   ├── place_info_search.py
│   ├── expense_calculator.py
│   ├── currency_converter.py
│   └── model_loader.py
│
├── prompt_library/
│
├── config/
│
├── main.py
├── streamlit_app.py
├── requirements.txt
└── setup.py
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/anishrivastava/AI_Trip_Planner.git
cd AI_Trip_Planner
```

Create Virtual Environment

```bash
python -m venv env
```

Activate

**Windows**

```bash
env\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file and add your API Keys.

```env
OPENAI_API_KEY=
GROQ_API_KEY=
OPENWEATHERMAP_API_KEY=
GPLACES_API_KEY=
TAVILY_API_KEY=
EXCHANGE_RATE_API_KEY=
```

---

## ▶️ Run Backend

```bash
uvicorn main:app --reload
```

---

## ▶️ Run Frontend

```bash
streamlit run streamlit_app.py
```

---

## 📌 Future Enhancements

- Docker Deployment
- Next.js Frontend
- Authentication
- Hotel & Flight Booking APIs
- Multi-Agent Planning
- Memory-enabled Conversations
- RAG Integration
- Voice Assistant Support

---

## 👨‍💻 Author

**Anish Shrivastava**

GitHub: https://github.com/anishrivastava

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
