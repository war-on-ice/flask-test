#
# If things get really nasty, this teams module
# could become package.
#
from flask import Blueprint, jsonify

from models.team import Team

teams_api = Blueprint('teams_api', __name__)

@teams_api.route('/teams', methods=['GET'])
def index():
  cbj = Team('Columbus Blue Jackets', 'CBJ', 'blue-jackets')
  flp = Team('Florida Panthers', 'FLP', 'florida-panthers')
  return jsonify({ 'teams': [ cbj.__dict__, flp.__dict__ ] })
