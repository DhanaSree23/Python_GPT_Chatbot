import openai

# Set your OpenAI API key
openai.api_key = 'API_Key'
def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=[{'role': 'user', 'content': prompt}]
        )
        if 'choices' in response and len(response['choices']) > 0:
            return response['choices'][0]['message']['content'].strip()
        else:
            return "No response found in the API call."
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == '__main__':
    while True:
        user_input = input('You: ')
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Exiting the chat. Goodbye!")
            break

        response = chat_with_gpt(user_input)
        print('Chatbot:', response)
