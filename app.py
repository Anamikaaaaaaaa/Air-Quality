from flask import Flask, request, render_template
import pickle 

app = Flask(__name__)

with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)
    
# Function to determine AQI status
def get_aqi_status(x):
    if x <= 50:
        return "Good"
    elif x > 50 and x <= 100:
        return "Moderate"
    elif x > 100 and x <= 200:
        return "Poor"
    elif x > 200 and x <= 300:
        return "Unhealthy"
    elif x > 300 and x <= 400:
        return "Very Unhealthy"
    else:
        return "Hazardous"

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to process AQI input
@app.route('/check_aqi', methods=['POST'])
def check_aqi():
    aqi_value = int(request.form['aqi_value'])
    status = get_aqi_status(aqi_value)
    return render_template('result.html', aqi_value=aqi_value, status=status)

if __name__ == '__main__':
    app.run(debug=True)
