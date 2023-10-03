import streamlit as st
import openai

# Set your OpenAI API key here
openai.api_key = ""

# Define your template question
template_question = "Translate the following French text to English: '{}'"


# Streamlit app code
def main():
    st.title("French to English")

    # User input for the question
    user_question = st.text_input("Enter your question in French:")
    # Define a system message to set the context
    system_message = "You are a French to English Translator."

    if st.button("Generate Translation"):
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

            # Extract and display the generated translation
            translation = response.choices[0].message["content"]
            st.write(f"Translation to English: {translation}")
        else:
            st.warning("Please enter a question.")


if __name__ == "__main__":
    main()

#
#
# # Extract and display the generated HTML code
# html_code = response["choices"][0]["message"]["content"]
# print(f"Generated FAQ Schema HTML Code:\n{html_code}")