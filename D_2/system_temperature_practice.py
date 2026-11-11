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
prompt=input("Enter Your Prompt: ")
message_1={
    "role":"system",
    "content":"Act like You are My Father."
}
message_2={
    "role":role,
    "content":prompt
}
messages=[message_1,message_2]
response=client.chat.completions.create(
    model=model,
    messages=messages,
    temperature=2
)
print(response)
print("=============================")
answer=response.choices[0].message.content
print(answer)