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
```
### 2. Create Virtual Environment (Recommended)
```bash
python -m venv venv
# Activate:
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Download LLaMA 2 Model
Download llama-2-7b-chat.ggmlv3.q8_0.bin from a trusted source such as Hugging Face:

🔗 [Example Download - Hugging Face](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q8_0.bin)

### 🏃 How to Use
Launch the app:
```
streamlit run app.py
```

### In the App:
#### 1. Enter Blog Topic – Type your subject

#### 2. Select Target Audience – e.g., Students, Professionals

#### 3. Choose Tone – e.g., Formal, Friendly

#### 4. Set Word Count – Use the slider

#### 5. Select Language – Choose the output language

#### 6. Click “Generate Blog” – The blog will be generated

#### 7.Download Blog – Save it as a .txt file
