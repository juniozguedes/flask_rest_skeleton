from flask import Blueprint
from datetime import datetime as dt
from .models import User, db

teams_bp = Blueprint('teams_bp', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='assets')

@teams_bp.route('/', methods=['POST'])
def create_team(request):
    team_data = request.json
    print(team_data)
