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
# prompt="Do you know Virat Kohli."
prompt1="Hi!"
prompt2="Explain time travel in detail."
prompt3="Write a 1000 word essay on Machine Learning."
prompts=[prompt1,prompt2,prompt3]
for prompt in prompts:
    message={
            "role":role,
            "content":prompt}
    messages=[message]
    response=client.chat.completions.create(
                                            model=model,
                                            messages=messages,
                                            max_tokens=100)
    usage=response.usage
    print(f"Prompt:{prompt} --> your_tokens: {usage.prompt_tokens} completion_tokens: {usage.completion_tokens} total_tokens: {usage.total_tokens} Finish Reason: {response.choices[0].finish_reason}")
# print(response)
#print("===============================================================")
#answer=response.choices[0].message.content
#print(answer)