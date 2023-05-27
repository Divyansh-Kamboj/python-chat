import openai
openai.api_key = "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"

model_engine = "text-davinci-003"
prompt = input("Ask me a question!\n")

Completion = openai.Completion.create(
engine = model_engine,
prompt=prompt,
max_tokens=1024,
n=1,
stop=None,
temperature=0.5,
    )

response = Completion.choices[0].text
print(response)