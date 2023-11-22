from flask import Flask, request, jsonify
import openai
from dotenv import load_dotenv
import  os
load_dotenv() 

app = Flask(__name__)


@app.route('/')
def get_answer():
    user_query = request.args.get('s')
    print(user_query)
    if user_query:
        try:
            query = user_query
            openai.api_key = os.getenv("OPENAI_API_KEY")
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=query,
                max_tokens=1000
            )
            answer = response.choices[0].text.strip()
            print(answer)
            return answer+"\n\n\n\n #Made with ❤️ by @imabhisht and @devsapariya94\n"


        except Exception as e:
            return jsonify({"error": str(e)})

    else:
        return jsonify({"error": "Query parameter 's' is missing in the URL"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
