from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST', 'PUT', 'DELETE', 'PATCH'])
def index():
    print(f"Headers: {request.headers}")
    if request.data:
        try:
            jsonData = request.get_json(force=True)
            prettyJson = json.dumps(jsonData, indent=4, ensure_ascii=False)
            print(prettyJson)
        except json.JSONDecodeError:
            print("Received non-JSON data:")
            print(request.data.decode('utf-8'))
    else:
        print("No data received.")
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5173)
