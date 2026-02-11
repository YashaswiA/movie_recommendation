{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "b675db4b-fee7-41f1-a8fd-5e50737d8023",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[3], line 3\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mstreamlit\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mst\u001b[39;00m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpandas\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpd\u001b[39;00m\n\u001b[1;32m----> 3\u001b[0m \u001b[38;5;28;01mfrom\u001b[39;00m \u001b[38;5;21;01mmovie_recommender\u001b[39;00m \u001b[38;5;28;01mimport\u001b[39;00m recommend\n\u001b[0;32m      5\u001b[0m st\u001b[38;5;241m.\u001b[39mtitle(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m🎬 Movie Recommendation System\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      7\u001b[0m movies \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_csv(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmovies.csv\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n",
      "File \u001b[1;32m~\\movie_recommender.py:45\u001b[0m\n\u001b[0;32m      1\u001b[0m {\n\u001b[0;32m      2\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcells\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m      3\u001b[0m   {\n\u001b[0;32m      4\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m      5\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m1\u001b[39m,\n\u001b[0;32m      6\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m152a7fd2-5d15-48c4-9a12-daca0e516870\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m      7\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m      8\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m      9\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: [\n\u001b[0;32m     10\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mimport pandas as pd\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     11\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfrom sklearn.feature_extraction.text import CountVectorizer\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     12\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfrom sklearn.metrics.pairwise import cosine_similarity\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     13\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     14\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m# Load dataset\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     15\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdf = pd.read_csv(\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mmovies.csv\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     16\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     17\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m# Replace | with space\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     18\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdf[\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mgenres\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m] = df[\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mgenres\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m].str.replace(\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m|\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m, \u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m \u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     19\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     20\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m# Vectorization\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     21\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcv = CountVectorizer()\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     22\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mgenre_matrix = cv.fit_transform(df[\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mgenres\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m])\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     23\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     24\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m# Cosine similarity\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     25\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msimilarity = cosine_similarity(genre_matrix)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     26\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     27\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m# Recommendation function\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     28\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdef recommend(movie_title):\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     29\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    if movie_title not in df[\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtitle\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m].values:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     30\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        return [\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124mMovie not found\u001b[39m\u001b[38;5;130;01m\\\"\u001b[39;00m\u001b[38;5;124m]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     31\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     32\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    idx = df[df[\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mtitle\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m] == movie_title].index[0]\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     33\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    distances = list(enumerate(similarity[idx]))\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     34\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    distances = sorted(distances, key=lambda x: x[1], reverse=True)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     35\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     36\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    recommendations = []\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     37\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    for i in distances[1:6]:\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     38\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m        recommendations.append(df.iloc[i[0]].title)\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     39\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     40\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m    return recommendations\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     41\u001b[0m    ]\n\u001b[0;32m     42\u001b[0m   },\n\u001b[0;32m     43\u001b[0m   {\n\u001b[0;32m     44\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcell_type\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcode\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[1;32m---> 45\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mexecution_count\u001b[39m\u001b[38;5;124m\"\u001b[39m: null,\n\u001b[0;32m     46\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mid\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3fd3d467-06e6-4957-a296-6e031c52b374\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     47\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {},\n\u001b[0;32m     48\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124moutputs\u001b[39m\u001b[38;5;124m\"\u001b[39m: [],\n\u001b[0;32m     49\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msource\u001b[39m\u001b[38;5;124m\"\u001b[39m: []\n\u001b[0;32m     50\u001b[0m   }\n\u001b[0;32m     51\u001b[0m  ],\n\u001b[0;32m     52\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmetadata\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m     53\u001b[0m   \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mkernelspec\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m     54\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdisplay_name\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPython 3 (ipykernel)\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     55\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlanguage\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     56\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython3\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     57\u001b[0m   },\n\u001b[0;32m     58\u001b[0m   \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mlanguage_info\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m     59\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mcodemirror_mode\u001b[39m\u001b[38;5;124m\"\u001b[39m: {\n\u001b[0;32m     60\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mipython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     61\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mversion\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m3\u001b[39m\n\u001b[0;32m     62\u001b[0m    },\n\u001b[0;32m     63\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mfile_extension\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m.py\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     64\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmimetype\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mtext/x-python\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     65\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mname\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     66\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbconvert_exporter\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpython\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     67\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mpygments_lexer\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mipython3\u001b[39m\u001b[38;5;124m\"\u001b[39m,\n\u001b[0;32m     68\u001b[0m    \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mversion\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m3.12.7\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m     69\u001b[0m   }\n\u001b[0;32m     70\u001b[0m  },\n\u001b[0;32m     71\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbformat\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m4\u001b[39m,\n\u001b[0;32m     72\u001b[0m  \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnbformat_minor\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;241m5\u001b[39m\n\u001b[0;32m     73\u001b[0m }\n",
      "\u001b[1;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "from movie_recommender import recommend\n",
    "\n",
    "st.title(\"🎬 Movie Recommendation System\")\n",
    "\n",
    "movies = pd.read_csv(\"movies.csv\")\n",
    "\n",
    "movie = st.selectbox(\n",
    "    \"Select a movie\",\n",
    "    movies['title'].values\n",
    ")\n",
    "\n",
    "if st.button(\"Recommend\"):\n",
    "    recommendations = recommend(movie)\n",
    "\n",
    "    st.subheader(\"Recommended Movies:\")\n",
    "    for m in recommendations:\n",
    "        st.write(\"👉\", m)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "abbdfb52-c733-426f-84af-207af640a43e",
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
