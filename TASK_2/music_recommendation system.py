# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All" 
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

# Author: Zubaida Sehnaz
# run the code on kaggle as it is in jupyter notebook format as for doing on vscode you need to download the csv file first 

import numpy as np
import pandas as pds
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import matplotlib.pyplot as plt

zs_music=pds.read_csv("/kaggle/input/music-dataset-1950-to-2019/tcc_ceds_music.csv")
zs_music.head()
zs_music['lyrics']

vtf = TfidfVectorizer(stop_words='english')
zs_music['lyrics']=zs_music['lyrics'].fillna("")
music_vector_matrix= vtf.fit_transform(zs_music['lyrics'])

cos_similar=linear_kernel(music_vector_matrix, music_vector_matrix)

music_indices = pds.Series(zs_music.index, index=zs_music['track_name']).drop_duplicates()
music_indices
music_indices['patricia']

def music_recommendation(title, cos_similar=cos_similar):
    index=music_indices[title]
    similarity_score=enumerate(cos_similar[index])
    similarity_score= sorted(similarity_score, key=lambda x: x[1], reverse=True)
    
    similarity_index=[i[0] for i in similarity_score]
    print(zs_music["track_name"].iloc[similarity_index]) 

music_recommendation('patricia')

top_10_tracks = zs_music['track_name'].head(10)
colors = plt.cm.viridis(np.linspace(0, 1, 10))
plt.figure(figsize=(10, 6))
bars = plt.barh(top_10_tracks[::-1], range(1, 11), color=colors)
plt.xlabel('Rank')
plt.ylabel('Track Name')
plt.title('Top 10 Recommended Tracks')
plt.gca().invert_yaxis()