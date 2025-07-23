# 📝 Advanced AI Blog Generator

Generate professional and customized blog posts effortlessly using the power of **LLaMA 2** and **LangChain**. This Streamlit-based application enables content creation on any topic, tailored by audience, tone, word count, and language.

---

## ✨ Features

- **Custom Blog Generation** – Input topic, audience, tone, and word count for tailored content.
- **LLaMA 2 Integration** – Powered by the LLaMA 2 language model for high-quality text generation.
- **LangChain Prompt Management** – Efficient orchestration of prompts and responses.
- **Multi-language Output** – Translate blogs into Hindi, Gujarati, Spanish, or French.
- **Interactive UI** – Built with Streamlit for a simple and intuitive user experience.
- **Download Option** – Save generated blogs as `.txt` files.

---

## 🚀 Tech Stack

- **Streamlit** – Web application interface  
- **LangChain** – Prompt and model handling  
- **CTransformers** – Local model execution using `.ggml` format  
- **Deep Translator** – Blog translation into multiple languages  

---

## ⚙️ Installation Guide

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd ai-blog-generator

2. Create Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv
# Activate:
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If you don’t have requirements.txt, create one with:

txt
Copy
Edit
streamlit
langchain
ctransformers
deep_translator
4. Download LLaMA 2 Model
Download llama-2-7b-chat.ggmlv3.q8_0.bin from a trusted source such as Hugging Face:

🔗 Example Download - Hugging Face

Place the file in a models folder:

python
Copy
Edit
ai-blog-generator/
├── models/
│   └── llama-2-7b-chat.ggmlv3.q8_0.bin
├── app.py
├── requirements.txt
└── README.md
🏃 How to Use
Launch the app:

bash
Copy
Edit
streamlit run app.py
In the App:
Enter Blog Topic – Type your subject

Select Target Audience – e.g., Students, Professionals

Choose Tone – e.g., Formal, Friendly

Set Word Count – Use the slider

Select Language – Choose the output language

Click “Generate Blog” – The blog will be generated

Download Blog – Save it as a .txt file

🤝 Contributing
Fork the repository

Create your branch: git checkout -b feature/your-feature

Make your changes

Commit: git commit -m "Add your message"

Push: git push origin feature/your-feature

Open a Pull Request

📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.
```
