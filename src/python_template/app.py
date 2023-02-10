import json
from flask import jsonify, request
from python_template.sql_session_api import SQLSessionAPI
from python_template._base import db, app

# INITIALISE DATABASE
api = SQLSessionAPI(db, app)


@app.route("/home", methods=["GET", "POST", "DELETE"])
def home():
    if request.method == "POST":
        return {"res": "post"}
    elif request.method == "DELETE":
        request_data = json.loads(request.data.decode())
        return {"res": jsonify(request_data)}
    else:

        return jsonify([1, 2, 3, 4])


if __name__ == "__main__":
    app.run(debug=True)
