import streamlit as st
import pandas as pd
import numpy as np
import pickle
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=d78c2bf11649dd7572d529660a7afd30&language=en-US'.format(movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/"+data['poster_path']






def recommender(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]
    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movie_list:
        movies_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movies_id))
    return recommended_movies ,recommended_movies_poster         



movies_dict=pickle.load(open('Movies_list.pkl','rb'))
movies = pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.markdown('Movie Recommender System')
selected_movie = st.selectbox(
    'Select which Type Movie you like.. ',
    movies['title'].values)



if st.button('Recommend'):
    
    name,poster=recommender(selected_movie)
    col1, col2, col3 ,col4 ,col5 = st.beta_columns(5)
   
    with col1:
       st.markdown(name[0])
       st.image(poster[0])
    with col2:
       st.markdown(name[1])
       st.image(poster[1])
    with col3:
       st.markdown(name[2])
       st.image(poster[2])
    with col4:
       st.markdown(name[3])
       st.image(poster[3])    
    with col5:
       st.markdown(name[4])
       st.image(poster[4])  




