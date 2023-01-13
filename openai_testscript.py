# https://beta.openai.com/docs/libraries/python-bindings

import getpass
import openai

openAiApiKey = getpass.getpass("Open AI API key: ")

# Define question
question = "What is the capital of France?"

openai.api_key = openAiApiKey
# response = openai.Completion.create(model="text-davinci-003", prompt=question, temperature=0, max_tokens=7)

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=question
)

# breakpoint()

print("{len} choices found".format(len=len(response.choices)))

for x in response.choices:
    print(x.text)

input("Press Enter to continue...")
# # Call GPT-3 API
# import openai
# openai.api_key = openAiApiKey
# prompt = (f"{question}")
# completions = openai.Completion.create(
#     engine="text-davinci-002",
#     prompt=prompt,
#     max_tokens=1024,
#     n=1,
#     stop=None,
#     temperature=0.5,
# )

# Print answer
# answer = completions.choices[0].text
# print(answer)