from flask import Flask,jsonify
from view import endpoints
app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"app" : "SENDIT APPLICATION"})


if __name__ == "__main__":
    app.run(debug=True)



   

   


   
# if __name__ =='__main__':
#     endpoints.app.run(debug=True, port=8080)