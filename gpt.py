import openai
openai.api_key = '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'

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Who is the PM of india"}])
print(completion.choices[0].message.content)