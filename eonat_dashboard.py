import folium
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_folium import folium_static

# Bootstrap import
st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

# Navbar
st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="padding-left:400px;">
    <a class="navbar-brand" href="https://share.streamlit.io/morgan-techy/nasaapi/init/eonat_dashboard.py" target="_blank">EONAT VISUAL</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
        <li class="nav-item active">
        <a class="nav-link disabled" href="#">Home <span class="sr-only">(current)</span></a>
        </li>
        <li class="nav-item">
        <a class="nav-link" href="https://github.com/mainbtpty" target="_blank">Github</a>
        </li>
        <li class="nav-item">
        <a class="nav-link" href="https://twitter.com/charles_on56830" target="_blank">Twitter</a>
        </li>
        <li class="nav-item">
        <a class="nav-link" href="https://www.linkedin.com/in/charles-oni-b45a91253/" target="_blank">Linkedin</a>
        </li>
    </ul>
    </div>
</nav>
""", unsafe_allow_html=True)

def lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Header text
st.markdown("<h1 style='text-align: center; color: white;'>Earth Observatory Natural Event Visualization</h1>", unsafe_allow_html=True)

# Earth animation
l = lottie('https://assets9.lottiefiles.com/packages/lf20_blfn1jwy.json')
st_lottie(l, height=300, key='earth_map')

# Sidebar to hold the side page features and text
with st.sidebar:
    # Slider to allow display an event on a particular day on the map
    slider = st.slider('Day Range:', 0, 365)
    st.write('You are searching in the last:', slider, 'days')

# API url to get the data from NASA API
url1 = f'https://eonet.gsfc.nasa.gov/api/v3/events?days={slider}'
# Request the data
r = requests.get(url1)
# Convert the data to JSON format and call the events categories
p_r = r.json()
events = p_r['events']
# Create a map object
m = folium.Map(location=[15, 16], tiles="Cartodbdark_matter", zoom_start=2, min_zoom=2, max_bounds=True)

# Volcano events function
def volcano():
    for count in range(len(events)):
        for i in p_r['events'][count]['geometry']:
            cord_A = i['coordinates'][1]
            cord_B = i['coordinates'][0]
            date = i['date']
        for j in p_r['events'][count]['categories']:
            event_type = j['title']
            if event_type == 'Volcanoes':
                # Global tooltip
                tooltip = 'click for more info'
                type = p_r['events'][count]['title']
                # Create markers
                folium.Marker([cord_A, cord_B], popup=folium.Popup(f'<strong>{type}<br>{date}<\strong>', max_width=150, min_width=150), tooltip=tooltip, icon=folium.features.CustomIcon(icon_image='icon/volcano.png', icon_size=(20, 20))).add_to(m)

# Wildfire events function
def wildfire():
    for count in range(len(events)):
        for i in p_r['events'][count]['geometry']:
            cord_A = i['coordinates'][1]
            cord_B = i['coordinates'][0]
            date = i['date']
        for j in p_r['events'][count]['categories']:
            event_type = j['title']
            if event_type == 'Wildfires':
                # Global tooltip
                tooltip = 'click for more info'
                type = p_r['events'][count]['title']
                # Create markers
                folium.Marker([cord_A, cord_B], popup=folium.Popup(f'<strong>{type}<br>{date}<\strong>', max_width=150, min_width=150), tooltip=tooltip, icon=folium.features.CustomIcon(icon_image='icon/fire-solid.png', icon_size=(20, 20))).add_to(m)

# Iceberg events function
def iceberg():
    for count in range(len(events)):
        for i in p_r['events'][count]['geometry']:
            cord_A = i['coordinates'][1]
            cord_B = i['coordinates'][0]
            date = i['date']
        for j in p_r['events'][count]['categories']:
            event_type = j['title']
            if event_type == 'Sea and Lake Ice':
                # Global tooltip
                tooltip = 'click for more info'
                type = p_r['events'][count]['title']
                # Create markers
                folium.Marker([cord_A, cord_B], popup=folium.Popup(f'<strong>{type}<br>{date}<\strong>', max_width=150, min_width=150), tooltip=tooltip, icon=folium.features.CustomIcon(icon_image='icon/iceberg.png', icon_size=(20, 20))).add_to(m)

# Sidebar to hold the side page features and text
with st.sidebar:
    genre = st.radio(
        "Please select an event:",
        ('All', 'volcano', 'wildfire', 'iceberg'))

    if genre == 'volcano':
        # Call the function
        volcano()
    elif genre == 'wildfire':
        # Call the function
        wildfire()
    elif genre == 'iceberg':
        # Call the function
        iceberg()
    else:
        volcano()
        wildfire()
        iceberg()

# Display map
folium_static(m)

# Text
st.info(' Created by Charles Oni (https://www.linkedin.com/in/charles-oni-b45a91253/))')
st.info('Used API: https://eonet.gsfc.nasa.gov/api/v3/events')

# Hide Streamlit style
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# JS import
st.markdown("""
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
""", unsafe_allow_html=True)
