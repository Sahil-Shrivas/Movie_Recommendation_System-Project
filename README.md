# 🎬 Movie Recommendation System 

**📰 Description:**  
The **Movie Recommendation System** is a Python-based web app that suggests movies similar to the one you select. It leverages **content-based filtering** using a similarity matrix and provides recommendations with **movie posters** dynamically fetched from the **TMDb API**.  

This project combines **machine learning**, **data processing**, **API integration**, and a **modern UI** to deliver an interactive and fast movie recommendation experience.  

---

## 📖 Overview

Movies are a popular form of entertainment, but finding the right movie can be challenging. This system helps users discover new movies similar to their favorite ones.  

**Key highlights:**  

- Uses **content-based filtering** to recommend movies  
- Displays **top 5 similar movies** with posters  
- Fetches movie posters dynamically using **TMDb API**  
- Interactive and responsive **Streamlit UI**  
- Optimized for **fast performance** and minimal load times  

The recommendation is based on **similarity between movie features** such as genres, keywords, and metadata.  

---

## 🛠️ Tech Stack & Libraries

- **Language:** Python 🐍  
- **Web Framework:** Streamlit 🌐  
- **Libraries:**  
  - `pandas` & `numpy` — data handling and manipulation  
  - `scikit-learn` — compute similarity and machine learning utilities  
  - `requests` — fetch movie posters from TMDb API  
  - `pickle` — save and load preprocessed datasets and similarity matrices  
- **External API:** TMDb API for high-quality movie posters 🎥  

> Check `requirements.txt` for full dependency list.

---

## Screenshot 

![alt text](https://raw.githubusercontent.com/Sahil-Shrivas/Movie_Recommendation_System-Project/refs/heads/main/Screenshot%202025-12-18%20200028.png)
![alt text](https://raw.githubusercontent.com/Sahil-Shrivas/Movie_Recommendation_System-Project/refs/heads/main/Screenshot%202025-12-18%20200056.png)

---

## 📂 Project Structure

    Movie-Recommendation-System/
    │── movie_dict.pkl # Dictionary containing movie data
    │── similarity.pkl # Precomputed similarity matrix for movies
    │── app.py # Streamlit app code (main interface)
    │── README.md # This documentation
    │── requirements.txt # Python dependencies
    │── LICENSE # MIT License

---

**Explanation:**  
- `movie_dict.pkl` contains all movies with metadata like title, genres, and TMDb movie IDs.  
- `similarity.pkl` is a **precomputed similarity matrix** used for recommending similar movies quickly.  
- `app.py` is the **main Streamlit application** which handles UI, movie selection, and displays recommendations.  

---

## 🧩 How It Works

1. **User selects a movie** from the sidebar dropdown.  
2. The app retrieves the **movie index** from the dataset.  
3. Computes **similarity scores** with all other movies using the **similarity matrix**.  
4. Sorts movies by similarity score and picks the **top 5 recommendations**.  
5. Fetches **movie posters dynamically** using the TMDb API.  
6. Displays results in **interactive cards** with hover effects for a modern look.  

---

## 🚀 Installation & Running the App

1. **Clone the repository**

    ```bash
    git clone https://github.com/Sahil-Shrivas/Movie-Recommendation-System.git
    cd Movie-Recommendation-System

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt

3. **Run the Streamlit app**

   ```bash
   streamlit run app.py

---

## 📊 Features

- 🎨 Interactive UI: Modern layout with hover effects for movie cards

- 🎞️ Movie Posters: High-quality posters fetched dynamically

- ⚡ Fast Recommendations: Precomputed similarity matrix ensures near-instant results

- 🖥️ Responsive Layout: Works well on both desktop and mobile screens

- ✅ Easy to Extend: Can integrate more movies or update similarity metrics

  ---

## 🧠 How Recommendations Are Calculated

- The system uses content-based filtering, where each movie is represented by its features (like genre, keywords, etc.).

- Cosine similarity is used to calculate similarity between movies.

- For a selected movie, the system identifies movies with the highest similarity scores.

- Top recommendations are then displayed with posters and titles.

---

## 📬 Contact

- Author: Sahil Shrivas ✨
- GitHub: https://github.com/Sahil-Shrivas

---


