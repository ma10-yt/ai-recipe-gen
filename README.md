# 🍳 AI Recipe Generator

An AI-powered recipe assistant that helps you decide what to cook from the ingredients you already have.

You can **enter ingredients manually or upload a photo of your ingredients**. The app uses AI to suggest five recipes, lets you choose one, and then generates complete step-by-step cooking instructions.

## ✨ Features

- 🥕 Enter ingredients manually
- 📷 Upload a photo of ingredients
- 🤖 AI-powered ingredient and recipe generation
- 🍽️ Get five recipe suggestions
- 👨‍🍳 Select a recipe and receive detailed cooking instructions
- 🥗 Dietary preference support
- 🌎 Cuisine selection
- 👥 Adjustable servings
- ⏱️ Cooking-time preferences
- 🔄 Choose another recipe without restarting the app

## 🧠 How It Works

```text
Ingredients / Photo
        ↓
   AI analyzes input
        ↓
  5 recipe suggestions
        ↓
   User selects one
        ↓
 Complete recipe + instructions
```

For image uploads, the AI analyzes the uploaded photo and combines the detected ingredients with any ingredients entered manually.

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Backboard**
- **Kimi K2.6**
- **OpenRouter**

Backboard is used as the AI interface and memory layer, while Kimi K2.6 handles the recipe generation and image understanding.

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-recipe-generator.git
cd ai-recipe-generator
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your API key

Set your Backboard API key as an environment variable.

PowerShell:

```powershell
$env:BACKBOARD_API_KEY="your_api_key"
```

### 5. Start the application

```powershell
python -m streamlit run main.py
```

The app will open locally in your browser.

## 🔐 Environment Variables

The application requires:

```text
BACKBOARD_API_KEY=your_api_key
```

Never commit your API key to GitHub.

## 📁 Project Structure

```text
ai-recipe-generator/
│
├── main.py
├── backboard_client.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🌱 Open AI / Open Innovation

This project uses an open-weight AI model through Backboard and OpenRouter rather than building the application around a proprietary closed model.

Using an open-weight model makes it possible to experiment with AI capabilities while keeping the application architecture flexible and portable.

## 🎯 Hacktoberfest Weekend Challenge

This project was created for the **DEV Hacktoberfest Weekend Challenge**.

The goal is to build a practical AI-powered application that solves an everyday problem: helping people decide what to cook from the ingredients they already have.

## 📸 Demo

A live demo will be available here:

**[Live Demo](YOUR_RENDER_URL)**

## 👨‍💻 Author

**MA10**

Built with Python, Streamlit, Backboard, and Kimi K2.6.