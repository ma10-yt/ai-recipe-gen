# 🍳 AI Recipe Generator

An AI-powered recipe assistant built for my sister, who loves cooking but often struggles to find recipes that actually work with the ingredients she has at home.

Instead of searching through YouTube videos and discovering halfway through that a recipe needs ingredients she doesn't have, she can simply **enter the ingredients she has or upload a photo of them** and get useful recipe options instantly.

## 💡 Why I Built This

My sister enjoys cooking, but her usual process was:

1. Search YouTube for a recipe.
2. Find a recipe that looks good.
3. Start checking the ingredients.
4. Realize she is missing some of them.
5. Search again for another recipe.
6. Sometimes find a recipe with unclear or inconvenient instructions.

I wanted to make that process much easier.

With this app, she can start with **what she already has**, instead of starting with a recipe.

## ✨ Features

- 🥕 Enter ingredients manually
- 📷 Upload a photo of your ingredients
- 🤖 AI-powered image understanding
- 🍽️ Get 5 recipe suggestions
- 👆 Choose the recipe you want to make
- 👨‍🍳 Get complete step-by-step instructions
- 🥗 Dietary preference selection
- 🌎 Cuisine selection
- 👥 Adjustable serving size
- ⏱️ Maximum cooking-time preference
- 🔄 Easily choose another recipe

## 🧠 How It Works

```text
        Ingredients
       /           \
   Text Input     Photo Upload
       \           /
        \         /
         AI Analysis
             ↓
      5 Recipe Suggestions
             ↓
       Choose a Recipe
             ↓
     Complete Recipe
      + Instructions
```

When a photo is uploaded, the AI analyzes the visible ingredients and combines them with any ingredients entered manually.

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Backboard**
- **Kimi K2.6**
- **OpenRouter**
- **Render**

### AI

The application uses **Kimi K2.6**, an open-weight model, through Backboard and OpenRouter. Kimi K2.6 supports image input, allowing the application to analyze uploaded ingredient photos.

### Backboard

Backboard provides the API layer used to communicate with the model and manage the application's AI requests. Its message API supports both normal text requests and file attachments.

### Deployment

The application is deployed publicly using **Render**.

## 🚀 Live Demo

👉 **[Try the AI Recipe Generator](https://ai-recipe-gen-pddb.onrender.com/)**

## 💻 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-recipe-generator.git
cd ai-recipe-generator
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

On Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Backboard API key

Set the API key as an environment variable.

PowerShell:

```powershell
$env:BACKBOARD_API_KEY="your_api_key"
```

### 5. Run the application

```powershell
python -m streamlit run main.py
```

The application will open in your browser.

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
├── README.md
└── .gitignore
```

## 🌱 Why Open Innovation Matters

This project uses an **open-weight AI model** rather than building the application around a closed model.

For this project, that provides flexibility to experiment with different models and AI providers while keeping the application architecture independent from a single proprietary model.

Using an open-weight model with image understanding also made it possible to extend the original idea from simple text-based recipe generation into a more useful workflow where users can show the AI what ingredients they actually have.

## 🎯 Hacktoberfest Weekend Challenge

This project was built for the **DEV Hacktoberfest Weekend Challenge: Build for a Friend**.

The challenge asks builders to create something with open-source AI at its core that solves a real problem for a friend or loved one.

For this project, that person is my sister, and the problem is simple:

> **She loves cooking, but finding a good recipe that matches the ingredients she actually has can take too much time.**

So I built a tool that starts with her ingredients instead of making her search for recipes first.

## 👨‍💻 Author

**MA10**

Built with ❤️ for my sister.