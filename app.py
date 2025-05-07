
import streamlit as st
import os
import openai

# Create OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="The Rhyme Roadmap 🎵", layout="centered")

st.title("🎵 The Rhyme Roadmap")
st.markdown("""
Welcome to **The Rhyme Roadmap** — a creative space where you turn academic learning into powerful songs.

Fill out the form below and get guided through brainstorming concepts, rhymes, and song themes with care, support, and creativity.
""")

with st.form("rhyme_form"):
    grade = st.text_input("What grade are you in?", placeholder="e.g. 9th grade")
    outcome = st.text_area("What learning outcome are you writing about?", placeholder="e.g. Explain the causes of WWII")
    submitted = st.form_submit_button("Generate Song Roadmap")

if submitted:
    if not grade or not outcome:
        st.warning("Please fill in both fields.")
    else:
        with st.spinner("Thinking in rhymes..."):
            prompt = f"""You are an encouraging, justice-centered songwriting coach. A {grade} student wants to write a song to show they understand this learning outcome: "{outcome}". Guide them through:

1. Brainstorming concepts and metaphors.
2. Thinking of rhyming words connected to big ideas.
3. A deeper theme that can drive a powerful song.

Be kind, supportive, and help them make sense of what they know."""

            try:
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": prompt}]
                )
                result = response.choices[0].message.content.strip()
                st.success("Here's your creative roadmap:")
                st.markdown(f"---\n{result}")
            except Exception as e:
                st.error(f"Error: {str(e)}")
