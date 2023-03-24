import os
import openai

openai.api_key = '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'

start_sequence = "\nA:"
restart_sequence = "\n\nQ: "
while 1:
    prompt = input(restart_sequence)
    if prompt == 'quit':
        break
    else:
        try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0,
                max_tokens=1000,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            print(start_sequence, response["choices"][0]["text"].strip())
        except Exception as exc:
            print(exc)
