from flask import Blueprint

teams_bp = Blueprint('teams_bp', __name__,
    template_folder='templates',
    static_folder='static', static_url_path='assets')

@teams_bp.route('/view/<int:team_id>', methods=['GET'])
def view(team_id):
    print("hello", team_id)
    return "Hello World"