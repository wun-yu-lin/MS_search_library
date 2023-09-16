from flask import *
import sys
sys.path.insert(1, './')
from werkzeug.exceptions import HTTPException
app=Flask(__name__)
app.config["JSON_AS_ASCII"]=False
app.config["TEMPLATES_AUTO_RELOAD"]=True
app.config.from_object("config")
app.json.ensure_ascii = False

# Register blueprints
##api url

app.config

# Pages
@app.route("/")
def index():
	return render_template("index.html")



def main():
	try:
		app.run(host="0.0.0.0",port=3000)
	except Exception as err:
		print(err)
		main()


if __name__=="__main__":
	main()