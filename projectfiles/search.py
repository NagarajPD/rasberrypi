import os
from ai import audio,speak
import openai
openai.api_key = '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'
messages = [ {"role": "system", "content": "Your name is infobot and give answers in 2 lines" } ]
def info():

    message=audio().replace(" ","")

    messages.append(
        {"role": "user", "content": message},
    )

    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )

    reply = chat.choices[0].message

    print("Assistant: ", reply.content)
    speak(reply.content)

    messages.append(reply)
