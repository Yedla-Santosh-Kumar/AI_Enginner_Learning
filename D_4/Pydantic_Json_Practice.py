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
from pydantic import BaseModel
class Ticket(BaseModel):
    name:str
    email:str
    phone:str 
    category:str
schema=Ticket.model_json_schema()
response_format={
    "type":"json_object"
}
Text=f"Extract the personal information from the ticket strictly based on this schema {schema} and give a json output"
message_1={
    "role":"system",
    "content":Text
}
role="user"
text_1="Hello My name is Pratyush. I have an iphone which is not working at all. My address is delhi. My email is abc@gmail.com. My contact number is 82134"
prompt=f"This is a customer ticket. Please extract the personal information from this {text_1}."
message_2={
    "role":role,
    "content":prompt
}
messages=[message_1,message_2]
response=client.chat.completions.create(
    model=model,
    messages=messages,
    response_format=response_format
)
print(response)
print("=============================")
answer=response.choices[0].message.content
print(answer)

import json
raw=answer
data=json.loads(raw)
ticket=Ticket(**data)
print(ticket.name)
print(ticket.email)
print(ticket.phone)
print(ticket.category)