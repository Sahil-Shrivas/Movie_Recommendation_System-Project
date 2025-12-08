# import streamlit as st
# import pickle
# import pandas as pd
# import requests
#
# def fetch_poster(movie_id):
#     response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0085212ce0840da5ef6d4b4dae01a2b0&language=en-US'.format(movie_id))
#     data = response.json()
#     print(data)
#     return "https://image.tmdb.org/t/p/w500/"+data['poster_path']
#
#
# def recommend(movie):
#     movie_index = movies[movies['title'] == movie].index[0]
#     distances = similarity[movie_index]
#     movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
#
#     recommended_movies = []
#     recommended_movies_poster = []
#     for i in movies_list:
#         movie_id = movies.iloc[i[0]].movie_id
#
#         recommended_movies.append(movies.iloc[i[0]].title)
#         #fetch poster from API
#         recommended_movies_poster.append(fetch_poster(movie_id))
#     return recommended_movies,recommended_movies_poster
#
# movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
# movies = pd.DataFrame(movies_dict)
#
# similarity = pickle.load(open('similarity.pkl', 'rb'))
#
# st.title('Movie Recommender')
#
# selected_movie_name = st.sidebar.selectbox(
#     'Which movie do you want to recommend?',
#     movies['title'].values)
#
# if st.button('Recommend'):
#     names,posters = recommend(selected_movie_name)
#
#     col1, col2, col3, col4, col5 = st.beta_columns(5)
#     with col1:
#         st.text(names[0])
#         st.image(posters[0])
#     with col2:
#         st.text(names[1])
#         st.image(posters[1])
#     with col3:
#         st.text(names[2])
#         st.image(posters[2])
#     with col4:
#         st.text(names[3])
#         st.image(posters[3])
#     with col5:
#         st.text(names[4])
#         st.image(posters[4])
#

















# CORRECT ANSWER


#


import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(page_title="Movie Recommender 🎬", page_icon="🎥", layout="wide")


# ------------------------------ FETCH POSTER ------------------------------
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=0085212ce0840da5ef6d4b4dae01a2b0&language=en-US"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print("Poster Fetch Error:", e)
        return "https://via.placeholder.com/500x750?text=No+Image"

    if "poster_path" not in data or data["poster_path"] is None:
        return "https://via.placeholder.com/500x750?text=No+Image"

    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


# ------------------------------ RECOMMENDATION ------------------------------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_poster


# ------------------------------ LOAD FILES ------------------------------
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# ------------------------------ STYLE ------------------------------
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
        color: #1f2937;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .card {
        background: #ffffff;
        padding: 10px;
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s;
        text-align: center;
    }
    .card:hover {
        transform: translateY(-5px);
    }
    .card img {
        border-radius: 10px;
        width: 100%;
    }
    .movie-title {
        margin-top: 10px;
        font-weight: bold;
        font-size: 16px;
        color: #111827;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------------------ HEADER ------------------------------
st.markdown("<h1 style='text-align:center; color:#0ea5e9;'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>Discover amazing movies tailored for you!</p>",
            unsafe_allow_html=True)

# ------------------------------ SIDEBAR ------------------------------
st.sidebar.markdown("<h2 style='color:#0ea5e9;'>Choose a Movie</h2>", unsafe_allow_html=True)
selected_movie_name = st.sidebar.selectbox("", movies['title'].values)
st.sidebar.markdown("---")

# ------------------------------ RECOMMENDATION ------------------------------
if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.markdown(f"""
                <div class="card">
                    <img src="{posters[idx]}" alt="{names[idx]} poster">
                    <div class="movie-title">{names[idx]}</div>
                </div>
            """, unsafe_allow_html=True)

