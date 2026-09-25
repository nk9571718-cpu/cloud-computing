from flask import Flask
import os
app = Flask(__name__)
@app.route("/")
def home():
  return "<h1>Welcome to Rendor</h1><p>cloud computing test</p>"
  if__name__ == "__main__":
  app.run(host="0.0.0.0", port int(os.environ.get("PORT",10000)))
