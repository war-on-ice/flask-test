from flask import Flask, render_template

from api.teams import teams_api
from models.team import Team

#
# This would also allow db models to be shared between
# the web app and the api. The app would feed 'em to
# the template and the api would jsonize what it needed.
#

app = Flask(__name__)
app.register_blueprint(teams_api, url_prefix='/api/v1')
#
# Moving to v2 would be fairly easy
#
# Or specify a header for version desired. A little more
# hairy as you look at each request instead of using
# routing
#

@app.route("/")
def homepage():
  avs = Team('Colorado Avalanche', 'CAV', 'colorado-avalanche')
  return render_template('homepage.html', team=avs)

if __name__ == '__main__':
    app.run()
