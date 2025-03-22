Require Python 3.10 Microsoft Visual Studio Tools 2022

python -m venv nonopenai

Activate it:

Windows:.\nonopenai\Scripts\activate
Install the GPT4All Installer using GUI based installers
Windows: https://gpt4all.io/installers/gpt4all-installer-win64.exe
Mac: https://gpt4all.io/installers/gpt4all-installer-darwin.dmg
Ubuntu: https://gpt4all.io/installers/gpt4all-installer-linux.run
Download the required LLM models and take note of the PATH they're installed to
Clone this repo
pip install gpt4all langchain-community streamlit
The comparison app can be started by running streamlit run app-comparison.py before you do that though, update the base ggml download path in line 16, e.g. BASE_PATH = 'C:/Users/User/AppData/Local/nomic.ai/GPT4All/' and openAI api key on line 11
References

https://www.nomic.ai/gpt4all
https://python.langchain.com/docs/integrations/llms/gpt4all/

# 🚀 Gen AI-Based Email Classification and OCR

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
A brief overview of your project and its purpose. Mention which problem statement are your attempting to solve. Keep it concise and engaging.

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  
🖼️ Screenshots:

![Screenshot 1](link-to-image)

## 💡 Inspiration
What inspired you to create this project? Describe the problem you're solving.

## ⚙️ What It Does
Explain the key features and functionalities of your project.

## 🛠️ How We Built It
Briefly outline the technologies, frameworks, and tools used in development.

## 🚧 Challenges We Faced
Describe the major technical or non-technical challenges your team encountered.

## 🏃 How to Run
1. Clone the repository  
   ```sh
   git clone https://github.com/your-repo.git
   ```
2. Install dependencies  
   ```sh
   npm install  # or pip install -r requirements.txt (for Python)
   ```
3. Run the project  
   ```sh
   npm start  # or python app.py
   ```

## 🏗️ Tech Stack
- 🔹 Frontend: React / Vue / Angular
- 🔹 Backend: Node.js / FastAPI / Django
- 🔹 Database: PostgreSQL / Firebase
- 🔹 Other: OpenAI API / Twilio / Stripe

## 👥 Team
- **Your Name** - [GitHub](#) | [LinkedIn](#)
- **Teammate 2** - [GitHub](#) | [LinkedIn](#)
