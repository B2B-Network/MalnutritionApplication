from matplotlib import scale
import pandas as pd
import joblib
import matplotlib.pyplot as plt
 
 
# Load the model from a file
model = joblib.load('model.pkl')
 
# Load the dataset
data = pd.read_csv('user_details.csv')
 
# Take the last row as input
user_input = data.tail(1).values.tolist()[0]
 
# Make a prediction using the model
user_input_scaled = scale.transform([user_input])
prediction = model.predict(user_input_scaled)[0]
 
# Create a pie chart to visualize the prediction result
fig, ax = plt.subplots()
ax.pie(model.predict_proba(user_input_scaled)[0], labels=['Class 0', 'Class 1'], autopct='%1.1f%%', startangle=90)
ax.set_title('Prediction Result')
 
# Save the plot to a file
plt.savefig('static/pie_chart.png')
 
# Print the prediction
print("Prediction:", prediction)
 
# Print the URL of the saved plot
print("Chart URL:", '/static/pie_chart.png')