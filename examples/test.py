import openai
from constants import CHATS

for chat in CHATS:
  response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
          {
              "role": "system",
              "content": "You are a professional dating app consultant. 20 year-old male user (M) will share his their private chats and you should give three specific suggestions pointing with specific sentence/sentences from 'M' and explain why it would be better and what the user should consider for the better conversation. Format a sentence from the chat and your suggestion with bullet point (- M: 'M's sentence', - 제안: 'Your alternative suggestion', - 설명: 'Why you suggested the sentence'). You should suggest chats in the style of a 20 year old, not too formal, and don't suggest any detailed an private messages that could felt as a overwhelmed question from stranger. Answer in Korean",
          },
          {"role": "user", "content": chat},
      ],
  )

  response_message = response["choices"][0]["message"]
  print(response_message["content"])
  print("="*30)
