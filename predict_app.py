import streamlit as st
import json
import os
import pandas as pd
import requests
from PIL import Image


st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://media.cntraveler.com/photos/5d780f667ffc50000818c7c1/master/pass/Waldorf%20Astoria%20Los%20Cabos%20Pedregal_Infinity-edge,-main-Pool,--The-Resort-at-Pedregal-Crudo-view-(1).jpg");
        background-size: cover;
    }
   .sidebar .sidebar-content {
        background: url("https://d2v76fz8ke2yrd.cloudfront.net/media/hotels/slideshow_images_staged/large/1076129.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
)

#finish later
#below
# ast.core.services.other.set_logging_format()

# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
        
# def remote_css(url):
#     st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

# def icon(icon_name):
#     st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)
    
# local_css("/Users/albinasitdikova/Project_5/style.css")
# remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
#under


st.title("Hotel recommender")
#st.write("Hello world!")
button_clicked = st.button("New user")



#works:
df_top_n = pd.read_csv('/Users/albinasitdikova/Project_5/df_top_n.csv')  
#st.write(df_top_n)

list_users = df_top_n.user_id

#choose a user
option = st.selectbox(
    'Choose user',
    (list_users))

st.write('You selected user with id:', option)


df_top_n.set_index(['user_id'], inplace = True)


#top 10 recommendations
list_top_10 = list(df_top_n.loc[option])
#st.write(list_top_10[0])


#https://www.tripadvisor.com/Hotel_Review-g60763-d113317-Reviews-Casablanca_Hotel_by_Library_Hotel_Collection-New_York_City_New_York.html
#st.image("https://media-cdn.tripadvisor.com/media/photo-o/09/34/ff/aa/casablanca-hotel-times.jpg")



df_offering = pd.read_csv('/Users/albinasitdikova/Project_5/df_offering.csv')

st.title("Top 10 recommendations below:")
for el in list_top_10:
    hotel_info = df_offering[df_offering.id == el]
    #st.markdown('**Hotel**')
    st.header(hotel_info.name.values[0])
    new_url = str(hotel_info.url.values[0])
    st.write("check out this [link]({0})".format(new_url))
    st.write("City:", hotel_info.locality.values[0])
    
  


#knn
df_knn = pd.read_csv('/Users/albinasitdikova/Project_5/df_knn.csv')
list_hotels = df_knn.id

#choose a user
option = st.selectbox(
    'Choose hotel',
    (list_hotels))

st.write('You selected hotel:', option)


df_knn.set_index(['id'], inplace = True)

#top 10 recommendations
list_knn = list(df_knn.loc[option])

st.title("Top 10 recommendations below:")

for el in list_knn:
    st.header(el)
    hotel_info = df_offering[df_offering.name == el]
    new_url = str(hotel_info.url.values[0])
    st.write("check out this [link]({0})".format(new_url))
    st.write("City:", hotel_info.locality.values[0])
    
#     hotel_info = df_knn[df_knn.id == el]
#     st.write(hotel_info)
    #st.markdown('**Hotel**')
#     st.header(hotel_info.name.values[0])
#     new_url = str(hotel_info.url.values[0])
#     st.write("check out this [link]({0})".format(new_url))
#     st.write("City:", hotel_info.locality.values[0])

    
    
    
st.markdown("<font color='red'>THIS TEXT WILL BE RED</font>", unsafe_allow_html=True)


st.markdown("<mark>Marked text</mark>", unsafe_allow_html=True)

st.markdown("<span style='background-color: #FFFF00'>Marked text</span>", unsafe_allow_html=True)

st.markdown("<span style='color:blue'>some *This is Blue italic.* text</span>", unsafe_allow_html=True)


