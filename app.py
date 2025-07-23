import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from deep_translator import GoogleTranslator

# Cache model loading
@st.cache_resource
def load_llama_model():
    return CTransformers(
        model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
        model_type='llama',
        config={
            'max_new_tokens': 512,
            'temperature': 0.7
        }
    )

# Function to translate the blog if needed
def translate_if_needed(blog, target_lang):
    lang_codes = {
        'Hindi': 'hi',
        'Gujarati': 'gu',
        'Spanish': 'es',
        'French': 'fr'
    }
    if target_lang != "English":
        try:
            return GoogleTranslator(source='auto', target=lang_codes.get(target_lang)).translate(blog)
        except Exception as e:
            return f"Translation Error: {e}"
    return blog

# Blog generation function
def get_blog_response(topic, word_limit, style, tone):
    llm = load_llama_model()

    template = """
    Write a blog post in English for a {style} audience on the topic: "{topic}".
    Make sure the tone of the blog is {tone} and the total word count is around {word_limit}.
    """
    
    prompt = PromptTemplate(
        input_variables=["topic", "word_limit", "style", "tone"],
        template=template
    )

    final_prompt = prompt.format(
        topic=topic,
        word_limit=word_limit,
        style=style,
        tone=tone
    )

    response = llm(final_prompt)
    return response.strip()

# Streamlit UI
st.set_page_config(page_title="AI Blog Generator", page_icon="📝", layout="centered")

st.title("📝 Advanced AI Blog Generator")
st.markdown("Generate professional blogs using LLaMA 2 and LangChain 🔥")

# Blog Inputs
topic = st.text_input("📌 Enter the blog topic")

col1, col2 = st.columns(2)

with col1:
    style = st.selectbox("🎯 Target Audience", ["Researchers", "Data Scientists", "Common People", "Students", "Entrepreneurs"])
    tone = st.selectbox("🗣️ Blog Tone", ["Formal", "Friendly", "Humorous", "Professional", "Inspirational"])

with col2:
    word_limit = st.slider("✍️ Approx. Word Count", min_value=100, max_value=1000, step=50, value=300)
    language = st.selectbox("🌐 Language", ["English", "Hindi", "Gujarati", "Spanish", "French"])

# Submit Button
if st.button("🚀 Generate Blog"):
    if topic.strip() == "":
        st.warning("Please enter a topic to generate a blog.")
    else:
        with st.spinner("Generating your blog... ⏳"):
            english_blog = get_blog_response(topic, word_limit, style, tone)
            translated_blog = translate_if_needed(english_blog, language)

            st.success("✅ Blog Generated!")
            st.markdown("---")
            st.markdown(f"### ✨ Generated Blog for **{style}** in **{language}**")
            st.markdown(translated_blog)

            st.download_button(
                label="📥 Download Blog as .txt",
                data=translated_blog,
                file_name=f"{topic}_blog.txt",
                mime="text/plain"
            )
