import openai
import re

openai.api_key = "addkeyhere"

# Initialize the conversation history
conversation_history = [
    {"role": "system", "content": "You help people plan events. Take in their theme preference, event type, food preference, number of guests, budget, date of event. Give place where theme stuff can be bought, where party can be hosted, invitation theme suggestions, where food can be ordered. Be professional."}
]


# Function to send a message and get the assistant's response
def send_message(user_input):
    # Add the user's message to the conversation history
    conversation_history.append({"role": "user", "content": user_input})
    
    # Make the API call
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Or gpt-3.5-turbo
        messages=conversation_history,
        temperature=1.0,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    
    # Get the assistant's reply
    assistant_reply = response['choices'][0]['message']['content']
    
    # Add the assistant's reply to the conversation history
    conversation_history.append({"role": "assistant", "content": assistant_reply})

    # Remove '###' and '**'
    formatted_output = re.sub(r'### |[*]{2}', '', assistant_reply)
    
    # Return the assistant's reply
    return formatted_output

print("Assistant: Hello! How can I help you today?")
while True:
    user_message = input("You: ")
    if user_message.lower() in ["exit", "quit", "bye"]:
        break
    assistant_reply = send_message(user_message)
    print(f"Assistant: {assistant_reply}")