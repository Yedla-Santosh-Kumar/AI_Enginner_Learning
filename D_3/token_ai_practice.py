import os 
from pathlib import Path
from groq import Groq 
from dotenv import load_dotenv 
load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("Groq API Key is Missing")
client=Groq(api_key=my_api_key)
model="openai/gpt-oss-120b"
role="user"
message_1={
    "role":role,
    "content":"Hii How are You?"
}
message_2={
    "role":role,
    "content":"Do you know Chatrapathi Shivaji Maharaj?"
}
message_3={
    "role":role,
    "content":"In Telugu Jersey Movie what is the Moto in that movie."
}
msg=[message_1,message_2,message_3]
for message in msg:
    messages=[message]
    response=client.chat.completions.create(
                                            model=model,
                                            messages=messages,
                                            temperature=2,
                                            max_tokens=500
                                            )
    answer=response.choices[0].message.content
    print(answer)
    usage=response.usage
    print("My Tokens",usage.prompt_tokens)
    print("Prediction Tokens",usage.completion_tokens)
    print("Total Tokens",usage.total_tokens)
    print("Reason",response.choices[0].finish_reason)