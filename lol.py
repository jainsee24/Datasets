import openai

openai.api_key = 'sk-L5sNDDTkiL2CsDxpe2rBT3BlbkFJ7BGenC264zF9uT8vKZm'
msg = "what is 5+106"

messages = [{"role": "user", "content": msg}]
try:
    selected_model = "gpt-4"
    completion = openai.ChatCompletion.create(model=selected_model, messages=messages)
    gpt_response = completion.choices[0].message["content"]
    print(gpt_response)
except Exception as e:
    print(f"An error occurred: {e}")
