import streamlit as st
import json
import os
import pandas as pd
import requests
from PIL import Image

#set background picture
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://wallpaperaccess.com/full/2118486.jpg");
        background-size: cover;
    }
   .sidebar .sidebar-content {
        background: url("https://d2v76fz8ke2yrd.cloudfront.net/media/hotels/slideshow_images_staged/large/1076129.jpg")
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Hotel recommender")


#load data

#dataframe "info about hotels"
df_offering = pd.read_csv('/Users/albinasitdikova/Project_5/df_offering.csv')

#dataframe "top 10 hotels for each user"
df_top_n = pd.read_csv('/Users/albinasitdikova/Project_5/df_top_n_app.csv')  

#dataframe "top 10 similar hotel for each hotel"
df_similar = pd.read_csv('/Users/albinasitdikova/Project_5/df_knn.csv')
hotel_or_user = ''


#get list of all users from dataframe "top 10 hotels for each user"
list_users = []
list_users.append('')
list_users.extend(df_top_n.user_id)

#let user choose username from selectbox (contains list of all users)
selected_user = st.selectbox('Select user (leave empty for new users):', (list_users))   

#if user choose username from the list in selectbox
if selected_user:

    df_top_n.set_index(['user_id'], inplace = True)

    #top 10 recommendations is a row with index [selected user] from dataframe "top 10 hotels for each user"
    list_top_10 = list(df_top_n.loc[selected_user])

    #just list of 10 images of hotels since I didn't webscrape images url
    list_image_user = ["https://media-cdn.tripadvisor.com/media/photo-o/12/c0/62/65/trump-international-hotel.jpg", "https://media-cdn.tripadvisor.com/media/photo-w/18/4a/d6/9f/hotel.jpg", "https://media-cdn.tripadvisor.com/media/photo-w/0e/9b/f2/61/sunset-at-four-seasons.jpg", "https://media-cdn.tripadvisor.com/media/photo-w/1b/b3/4b/28/four-seasons-hotel-baltimore.jpg", "https://media-cdn.tripadvisor.com/media/photo-w/1b/73/92/a0/spacious-pool-and-bayside.jpg", "https://media-cdn.tripadvisor.com/media/photo-w/13/eb/b0/4d/conrad-indianapolis.jpg", "https://media-cdn.tripadvisor.com/media/photo-w/0f/a4/48/66/park-junior-suite.jpg", "https://media-cdn.tripadvisor.com/media/photo-o/12/fa/7a/9e/willard-premier-room.jpg", "https://media-cdn.tripadvisor.com/media/photo-w/1b/a5/c6/3e/exterior.jpg", "https://media-cdn.tripadvisor.com/media/photo-o/1b/45/10/ea/exterior.jpg"]
    
    #print 10 top hotel recommendations with images and links
    st.title("Top 10 recommendations below for user {0}:".format(selected_user))
    for i, el in enumerate(list_top_10):
        hotel_info = df_offering[df_offering.id == el]
        st.header(hotel_info.name.values[0])
        new_url = str(hotel_info.url.values[0])
        st.write("check out this [link]({0})".format(new_url))
        st.write("City:", hotel_info.locality.values[0])
        st.image(list_image_user[i])

#if user didn't choose username from the list in selectbox just print warning:
else:
    st.warning('No option is selected')     
       

#get list of all hotels from dataframe "top 10 similar hotel for each hotel"
list_hotels = []
list_hotels.append('')
list_hotels.extend(list(df_similar.id))

#let user choose hotel from selectbox (contains list of all hotels)
selected_hotel = st.selectbox('Select hotel:', (list_hotels))

#if user choose hotel from the list in selectbox
if selected_hotel:

    df_similar.set_index(['id'], inplace = True)

    #top 10 similar hotels is a row with index [selected hotel] from dataframe "top 10 hotels for each user"
    list_similar = list(df_similar.loc[selected_hotel])

    #just list of 10 images of hotels since I didn't webscrape images url
    list_image_hotel = ["https://media-cdn.tripadvisor.com/media/photo-w/18/a0/75/24/pool.jpg", "https://media-cdn.tripadvisor.com/media/photo-w/1c/b3/1b/41/lobby.jpg", "https://media-cdn.tripadvisor.com/media/photo-w/1b/45/10/db/exterior.jpg", "https://media-cdn.tripadvisor.com/media/photo-w/1b/43/70/11/exterior-view.jpg", "https://media-cdn.tripadvisor.com/media/photo-w/1b/4d/24/f3/exterior.jpg", "https://media-cdn.tripadvisor.com/media/photo-w/1c/26/a3/6d/exterior.jpg", "https://media-cdn.tripadvisor.com/media/photo-w/12/01/70/1f/the-aviary-nyc.jpg", "https://media-cdn.tripadvisor.com/media/photo-w/1a/14/40/cb/hyatt-regency-mission.jpg", "https://media-cdn.tripadvisor.com/media/photo-w/1c/b3/23/49/marriott-greatroom.jpg", "https://media-cdn.tripadvisor.com/media/photo-w/06/af/ae/8a/the-palmer-house-hilton.jpg"]
    
    
    #print 10 top similar hotels with images and links
    st.title("Other people who like hotel {0} also like:".format(selected_hotel))

    for i, el in enumerate(list_similar):
        st.header(el)
        hotel_info = df_offering[df_offering.name == el]
        new_url = str(hotel_info.url.values[0])
        st.write("check out this [link]({0})".format(new_url))
        st.write("City:", hotel_info.locality.values[0])
        st.image(list_image_hotel[i])
        
#if user didn't choose hotel from the list in selectbox print warning:
else:
    st.warning('No option is selected')       
        



