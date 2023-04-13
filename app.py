from flask import Flask, render_template, request
import finalparser

app = Flask(__name__,template_folder='D:/Assignment/pythonparser/frontend',static_folder='D:/Assignment/pythonparser/static')



def sendData(data):
    c_code=finalparser.preprocess(data)
    ast=finalparser.generate_ast(c_code)
    finalparser.generate_parse_tree(ast)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():
    data= request.form.get('codeBox')
    print(data)
    sendData(data)


    # Process the data here

    return render_template('index.html')
    

if __name__ == '__main__':
    app.run(debug=True)

