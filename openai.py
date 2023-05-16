'''
**********************************
***     Author: @eMirror        ***
**********************************
'''

import openai

#https://platform.openai.com/account/api-keys
openai.api_key = 'Your api-key'

#Establish the context/determine how the bot will respond. Example: Answer only in Japanese
context = "Assistant"

messages = [{"role": "system",
             "content": context}]

while True:

    prompt = input("Message: ")

    if prompt == "00":
        break

    #"Role" determines who sends it. In this case, the user/prompt.
    messages.append({"role": "user",
                     "content": prompt})

    #Generate answer.
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=messages)

    #Separate and store the AI's response. 0 is the first option, it contains multiple responses, or you can request multiple responses.
    responseMessage = response.choices[0].message.content

    #Remember the answer from ChatGPT
    messages.append({"role": "assistant", "content": responseMessage})

    print("Answer: " + response.choices[0].message.content)