import streamlit as st
from openai import OpenAI
from langchain_experimental.llms.ollama_functions import OllamaFunctions

# initialize model
llm = OllamaFunctions(model="llama3.1")
client = OpenAI(api_key="ollama", base_url="http://localhost:11434/v1")

# magic function
def suggest(text):

    template = """
        Answer the question asked by the user based on the
            text provided. Do not give any further explanation. The answer has to be
            in a JSON format.
    """

    response = client.chat.completions.create(
        model="llama3.1",
        messages=[
            {
                "role": "system",
                "content": template,
            },
            {
                "role": "user",
                "content": [
                 {
                     "type": "text",
                     "text": f"""
                    You are a popular social media expert with many followers in both Tiktok and Instagram
                    You will receive text from users. {text}. Generate list of hashtags and captions and HOOKS ideas relevant to the text that can go VIRAL in JSON FORMAT.
                    """
                 },
                ]
            }
        ]
    )
    return response.choices[0].message.content

st.set_page_config(layout="wide", page_title="Content Grower")
st.title("Content Grower")
st.caption("🚀 A Streamlit APP for social media grow assist")

# textbot
st.write("receive suggestions")

text = st.text_area(
    "Your requirement",
)

if text:
    try:
        # get output
        output = suggest(text)
        st.write(output)
    except Exception as e:
        st.error(f"Error: {e}")

st.write("Here is what is trending now!")

