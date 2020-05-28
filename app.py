from flask import Flask,render_template,jsonify,request
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/process_comment',methods=['GET'])
def predict_toxicity():
	input_text = request.args.get('text', None) 
	input_text = False
	return jsonify({'resp':input_text})
if __name__ == '__main__':
   app.run(debug = True,port=9090)