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
                max_tokens=100,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            print(start_sequence, response["choices"][0]["text"].strip())
        except Exception as exc:
            print(exc)
