from uuid import uuid4

from flask import Flask
from flask import request

app = Flask(__name__)

pretend_db = {
                'users': {'abefa8f7-5f19-4fea-8ddd-3a93122e8e87': 
                    {
                        'username': 'john@doe.com',
                        'password':'t!@#wqrtsc0'
                    }}, 
                'jobs': ['software engineer']}

@app.route('/', methods=['get'])
def hello():
    return "Hello!"

@app.route('/create-account', methods=['post'])
def create_account():
    username = request.json['username']
    password = request.json['password']
    user_id = str(uuid4())
    print(f'USER ID: {user_id}')
    new_account = {'username': username, 'password': password}

    if user_id in pretend_db['users'].keys():
        return "Duplicate keys", 500

    pretend_db['users'][user_id] = new_account
    return 'Account created', 200

@app.route('/add-job', methods=['post'])
def add_job():
    job = request.json['job_title']
    if job in pretend_db['jobs']:
        return "Job already exists", 500
    return 'Job added', 200

@app.route('/job', methods=['get'])
def search_job():
    title = request.args.get('title')
    print(title)
    if title in pretend_db['jobs']:
        return 'Job is available', 200
    return 'No job available', 200

@app.route('/job-count', methods=['get'])
def get_job_count():
    user_count = len(pretend_db['jobs'])
    return {'user_count': user_count}, 200

@app.route('/user-count', methods=['get'])
def get_user_count():
    user_count = len(pretend_db['users'])
    return {'user_count': user_count}, 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
