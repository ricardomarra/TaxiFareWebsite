import streamlit as st
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')


'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

pickup_datetime = st.text_input("Date", 0)
pickup_longitude = st.text_input("Pickup longitude", 0)
pickup_latitude = st.text_input("Pickup latitude", 0)
dropoff_longitude = st.text_input("Dropoff longitude", 0)
dropoff_latitude = st.text_input("Dropoff latitude", 0)
passenger_count = st.text_input("Passenger count", 0)

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://wagon-data-kutztduama-ew.a.run.app/predict_fare'

if url == 'http://taxifare.lewagon.ai/predict_fare/':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...
'''

params = {
            "key": '2013-07-06 17:18:00.000000119',
            "pickup_datetime": '2013-07-06 17:18:00 UTC',
            "pickup_longitude": float(pickup_longitude),
            "pickup_latitude": float(pickup_latitude),
            "dropoff_longitude": float(dropoff_longitude),
            "dropoff_latitude": float(dropoff_latitude),
            "passenger_count": int(passenger_count)
             }

'''
3. Let's call our API using the `requests` package...
'''

results = requests.get(url, params = params)
prediction = results.json()['prediction']


'''
4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user

'''

st.write(prediction)
