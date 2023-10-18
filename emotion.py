import streamlit as st
import openai
from langchain.memory import ChatMessageHistory

history = ChatMessageHistory()

import os

api_key = os.getenv('OPENAI_API_KEY')
# Define your template question
template_question = "Generate a targeted question to understand the problem. Talk in a way that you are talking to your friend or family member. Keep the responses short and crisp. Make the user feel comfortable and at home.: '{}'"

# Streamlit app code
def main():
    st.title("Targeted questions")

    chat_history = ChatMessageHistory()

    # User input for the question
    user_question = st.text_area("Enter questions and answers", "")

    # System message to set the context
    system_message = "Generate targeted questions to understand the problem"

    if st.button("Generating questions"):
        if user_question:
            # Use the template question to create a prompt
            prompt = template_question.format(user_question)

            # Add the chat history to the prompt
            prompt += f"\n{chat_history.messages}"

            # Call the OpenAI API to generate a response
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_message},
                    {"role": "user", "content": prompt}
                ],
            )
            history.add_user_message(user_question)
            history.add_ai_message(response.choices[0].message["content"])

            print(history.messages)
            # Extract and display the generated translation as a code block
            translation = response.choices[0].message["content"]

            # Add the response to the chat history
            chat_history.add_ai_message(translation)
            # for message in history.messages:
            #     st.write(message)
            st.write(translation)
        else:
            st.warning("Please enter a question.")

if __name__ == "__main__":
    main()
