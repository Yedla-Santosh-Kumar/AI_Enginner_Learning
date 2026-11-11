import os 
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq 
load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("API Error")
client=Groq(api_key=my_api_key)
model="openai/gpt-oss-120b"
# model="llama-3.3-70b-versatile"
role="user"
prompt="Suggest a name for my clothing company"
'''message_system={
    "role":"system",
    "content":"You are my Girfriend."}'''
'''message_system={
    "role":"system",
    "content":"You are my strict Office colleague and who is also my manager"
}'''
'''message_system={
    "role":"system",
    "content":"You are my college teacher but i am your one of the student"
}'''
message_system={
    "role":"system",
    "content":"You are my brand manager who suggests name for my company. Name should be in one word and suggest only one word."
}
message={"role":role,
         "content":prompt}
messages=[message_system,message]
'''response=client.chat.completions.create(
    model=model,
    messages=messages
)'''
response=client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=1
)
# print(response)
print("===============================================================")
answer=response.choices[0].message.content
print(answer)