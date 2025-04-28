import requests

def chat_with_lm_studio(prompt, server_url="http://localhost:8180/v1/chat/completions"):
    headers = {
        "Content-Type": "application/json",
      #  "Authorization": f"Bearer {YOUR_API_KEY_IF_NEEDED}"  # if needed, LM Studio often runs without auth
    }
    
    payload = {
        "model": "hermes-3-llama-3.2-3b",  # Example: "gpt-3.5-turbo" or your custom model name
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    
    response = requests.post(server_url, json=payload, headers=headers)
    
    if response.status_code == 200:
        reply = response.json()
        return reply['choices'][0]['message']['content']
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ("exit", "quit"):
            break
        
        reply = chat_with_lm_studio(user_input)
        if reply:
            print(f"AI: {reply}")
