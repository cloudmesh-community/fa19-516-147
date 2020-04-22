# copy content from cloud computing eng
#   to view documention http://0.0.0.0:8080/cloudmesh/v3/ui/
from flask import jsonify
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir="./")
# Read the yaml file to configure the endpoints
app.add_api("database_noSQL.yaml")


# create a URL route in our application for "/"
@app.route("/")
def home():
    msg = {"status": "ok"}
    return jsonify(msg)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
