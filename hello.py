
from flask import Flask, render_template, redirect, request
from sklearn.discriminant_analysis import StandardScaler
import databases
from matplotlib import scale
import pandas as pd
import joblib
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home_page.html')

@app.route('/<string:user_wish>')
def user(user_wish):
    return render_template(f'{user_wish}.html')

@app.route('/register',methods=['POST'])
def sign_up():
    name =  request.form.get('name')
    email =  request.form.get('email')
    password = request.form.get('password')
    phone_number =  request.form.get('phone')

    databases.sign_up_insert(name, email, password, phone_number)

    return redirect('/login')
   
@app.route('/login',methods=['POST'])
def login():
    email =  request.form.get('email')
    password = request.form.get('password')
   

    databases.insert_login_details(email, password)

    return redirect('/main') 

@app.route('/prediction',methods=['POST'])
def mal_prediction():
    age =  request.form.get('age')
    bmi = request.form.get('bmi')
    muac = request.form.get('muac')
    cc = request.form.get('cc')
    hc = request.form.get('hc')
    mw = request.form.get('mw')
    
    if 'fd' in request.form:
        fd = '1'
    else:
        fd = '0'

   

    databases.prediction(age,bmi,muac,cc,hc,mw,fd)
    return redirect('/predict')
 
@app.route('/predict')
def predict():
    # Load the model from a file
    model = joblib.load('model.pkl')

    # Load the dataset
    data = pd.read_csv('user_details.csv')

    # Take the last row as input
    user_input = data.tail(1)

    # Scale the input data using the same scaler used to train the model
    scaler = StandardScaler()
    user_input_scaled = scaler.fit_transform(user_input)

    # Make a prediction using the model
    prediction = model.predict(user_input_scaled)[0]

    # Create a pie chart to visualize the prediction result
    # try:
    fig, ax = plt.subplots()
    
    data = model.predict_proba(user_input_scaled)[0]
    labels = ['Class {}'.format(i) for i in range(len(data))]
    ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=90)

    ax.set_title('Overall Prediction Result')

        # Save the plot to a buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

        # Encode the buffer as a base64 string
    chart_data = base64.b64encode(buffer.getvalue()).decode()

        # Return the prediction and chart as an HTML template
    return render_template('prediction.html', prediction=prediction, chart_data=chart_data)

@app.route('/success')
def success():
    return 'successfully entered'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
