from flask import Flask, render_template, redirect, request
from sklearn.discriminant_analysis import StandardScaler
import databases
from matplotlib import scale
import pandas as pd
import joblib
import matplotlib.pyplot as plt

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
 
#     def prediction_model():
#         # Load the model from a file
#         model = joblib.load('model.pkl')
 
# # Load the dataset
#         data = pd.read_csv('user_details.csv')
 
# # Take the last row as input
#         user_input = data.tail(1).values.tolist()[0]
 
# # Make a prediction using the model
#         user_input_scaled = scale.Transform([user_input])
#         prediction = model.predict(user_input_scaled)[0]
 
# # Create a pie chart to visualize the prediction result
#         fig, ax = plt.subplots()
#         ax.pie(model.predict_proba(user_input_scaled)[0], labels=['Class 0', 'Class 1'], autopct='%1.1f%%', startangle=90)
#         ax.set_title('Prediction Result')
 
# # Save the plot to a file
#         plt.savefig('static/pie_chart.png')
 
# # Print the prediction
#         print("Prediction:", prediction)
 
# # Print the URL of the saved plot
#         print("Chart URL:", '/static/pie_chart.png')
    
#     prediction_model()
    
#     def prediction_model():
#             # Load the model from a file
#             model = joblib.load('model.pkl')

#             # Load the dataset
#             data = pd.read_csv('user_details.csv')

# # Take the last row as input
#             user_input = data.tail(1)

#             # Scale the input data using the same scaler used to train the model
#             scaler = StandardScaler()
#             user_input_scaled = scaler.fit_transform(user_input)

# # Make a prediction using the model
#             prediction = model.predict(user_input_scaled)[0]

# # Create a pie chart to visualize the prediction result

#             try:
#                 # Create a pie chart to visualize the prediction result
#                 fig, ax = plt.subplots()
#                 ax.pie(model.predict_proba(user_input_scaled)[0], labels=['Class 0', 'Class 1'], autopct='%1.1f%%', startangle=90)
#                 ax.set_title('Prediction Result')

#                 # Save the plot to a file
#                 plt.savefig('static/pie_chart.png')
#             except Exception as e:
#                 print("Error creating plot:", e)


# # Print the prediction
#             print("Prediction:", prediction)

# # Print the URL of the saved plot
#             print("Chart URL:", '/static/pie_chart.png')

#     prediction_model()
#     return redirect('/success') 


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
    # 
    
    try:
       fig, ax = plt.subplots()
       ax.pie(model.predict_proba(user_input_scaled)[0], labels=['Class 0', 'Class 1'], autopct='%1.1f%%', startangle=90)
       ax.set_title('Prediction Result')

    # Show the plot
       plt.show()
    except Exception as e:
        print("Error creating plot:", e)


    # Return the prediction and chart URL as a response
    return f"Prediction: {prediction}"





@app.route('/success')
def success():
    return 'successfully entered'

if __name__ == '__main__':
    app.run(port=5000, debug=True)
