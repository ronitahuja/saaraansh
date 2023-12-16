import os
import dotenv
import google.generativeai as genai

class Model:
  def model(text):
    dotenv.load_dotenv()

    genai.configure(api_key=os.getenv('API_KEY'))

    model=genai.GenerativeModel('gemini-pro')
    model=model.start_chat(history=[])
    response = model.send_message(["Summarize this ",text],stream=True)
    for chunk in response:
      yield chunk.text
if __name__ == '__main__':
    Model.model()