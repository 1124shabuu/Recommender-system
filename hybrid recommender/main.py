import streamlit as st
import pickle
import requests
import surprise

def fetch_poster(movie_id):
    response =requests.get('https://api.themoviedb.org/3/movie/{}?api_key=378f4f4546182c1e6d86cf346826043d&language=en-US'.format(movie_id))
    data =response.json()

    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

def recommend(user_id,title):
    indx = indices[title]
    tmdbId1 = linkss.loc[title]['tmdbId']
    sim_scores = list(enumerate(similarity[indx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:25]
    movie_indices = [i[0] for i in sim_scores]

    pred_movies = movies_list.iloc[movie_indices][['title', 'runtime', 'vote_average', 'tmdbId']]
    pred_movies['est'] = pred_movies['tmdbId'].apply(lambda x: svd.predict(user_id, linkss1.loc[x]['movieId']).est)
    pred_movies = pred_movies.sort_values('est', ascending=False)

    recommended_movies=[]
    recommended_movies_posters=[]
    for i in range(5):
        movie_id= pred_movies.iloc[i].tmdbId
        recommended_movies.append(pred_movies.iloc[i].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_posters


movies_list = pickle.load(open('movies.pkl','rb'))
linkss=pickle.load(open('links.pkl','rb'))
linkss1=pickle.load(open('links1.pkl','rb'))
users_list= pickle.load(open('users.pkl','rb'))
indices= pickle.load(open('indices.pkl','rb'))
similarity= pickle.load(open('matrix.pkl','rb'))
svd= pickle.load(open('svd1.pkl','rb'))
st.title('Movie Recommender System')

movie_name = st.selectbox(
    'Choose any movie you like?',(movies_list['title'].values)
)

user_name = st.selectbox(
    'Choose User Id?',(users_list['userId'].values)
)

if st.button('Recommend'):
   st.subheader('Recommended Movies are:')
   names,posters= recommend(user_name,movie_name)
   col1 , col2, col3, col4 ,col5 = st.columns(5)
   with col1:
       st.text(names[0])
       st.image(posters[0])

   with col2:
       st.text(names[1])
       st.image(posters[1])

   with col3:
       st.text(names[2])
       st.image(posters[2])

   with col4:
       st.text(names[3])
       st.image(posters[3])
   with col5:
       st.text(names[4])
       st.image(posters[4])
