{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "152a7fd2-5d15-48c4-9a12-daca0e516870",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "from sklearn.metrics.pairwise import cosine_similarity\n",
    "\n",
    "# Load dataset\n",
    "df = pd.read_csv(\"movies.csv\")\n",
    "\n",
    "# Replace | with space\n",
    "df['genres'] = df['genres'].str.replace('|', ' ')\n",
    "\n",
    "# Vectorization\n",
    "cv = CountVectorizer()\n",
    "genre_matrix = cv.fit_transform(df['genres'])\n",
    "\n",
    "# Cosine similarity\n",
    "similarity = cosine_similarity(genre_matrix)\n",
    "\n",
    "# Recommendation function\n",
    "def recommend(movie_title):\n",
    "    if movie_title not in df['title'].values:\n",
    "        return [\"Movie not found\"]\n",
    "\n",
    "    idx = df[df['title'] == movie_title].index[0]\n",
    "    distances = list(enumerate(similarity[idx]))\n",
    "    distances = sorted(distances, key=lambda x: x[1], reverse=True)\n",
    "\n",
    "    recommendations = []\n",
    "    for i in distances[1:6]:\n",
    "        recommendations.append(df.iloc[i[0]].title)\n",
    "\n",
    "    return recommendations\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3fd3d467-06e6-4957-a296-6e031c52b374",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
