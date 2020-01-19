from flask import Flask, request, jsonify

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Heading 1</h1>
    <p>A prototype API</p>'''

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        return 'logging you in'
    else:
        return 'show the form'

@app.route('/resources/scripts/<script>', methods=['POST'])
def request_script():
    '''need to ask for a specific script'''
    query_parameters = request.args

    script = query_parameters.get('script')
    usertoken = query_parameters.get('usertoken')
    username = query_parameters.get('username')
    return 'doing the needful'

app.run()