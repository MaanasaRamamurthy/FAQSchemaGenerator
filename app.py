import streamlit as st
import openai

# Set your OpenAI API key here
import os

api_key = os.getenv('OPENAI_API_KEY')

# Define your template question
template_question = "Generate FAQ Schema in HTML for the following questions and answers: '{}'"

def split_faq_input(input_text):
    faq_pairs = input_text.split('[QUESTION]')
    faq_pairs = [pair.strip() for pair in faq_pairs if pair.strip()]
    return [(pair.split('[ANSWER]')[0], pair.split('[ANSWER]')[1]) for pair in faq_pairs]

# Streamlit app code
def main():
    st.title("FAQ Schema Generator")

    # User input for the question
    user_question = st.text_area("Enter questions and answers (format: [QUESTION]Your question[ANSWER]Your answer)", "")
    faq_pairs = split_faq_input(user_question)
    # Define a system message to set the context
    system_message = "FAQ Schema Generator in HTML code in microdata format"

    if st.button("Generate FAQ Schema"):
        if user_question:
            # Use the template question to create a prompt

            prompt = template_question.format(user_question)

            # Call the OpenAI API to generate a response
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # Use the ChatGPT 3.5 engine
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt}
                ]
            )

            # Extract and display the generated translation as a code block
            translation = response.choices[0].message["content"]
            st.subheader("Generated FAQ Schema in HTML:")
            st.code(translation, language='html')
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main()
