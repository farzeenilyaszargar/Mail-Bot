import os
import requests

API_KEY = os.getenv("DEEPSEEK_API_KEY")



def msgAI(coreMsg, emailId, user):
    url = "https://api.deepseek.com/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "You are an email writer. Just write body, no subject, avoid markdown or uncertainity eg. [name]"},
            {"role": "user", "content": f"{coreMsg}\nWrite a personalized email to {emailId} from {user}"}
        ],
        "temperature": 0.7
    }
    


    response = requests.post(url, headers=headers, json=data)

    result = response.json()

    print(API_KEY)


    print(result)  

    return result["choices"][0]["message"]["content"]


# make api call to ai which will make a custom message for the user


