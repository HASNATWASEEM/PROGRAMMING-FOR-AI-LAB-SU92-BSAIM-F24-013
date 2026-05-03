import re
import numpy as np
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss

# ------------------ 1. Chhota embedded hadith dataset (no clone) ------------------
sample_hadiths = [
    "It was narrated that Ibn ‘Abbas said: “Your Prophet (ﷺ) was enjoined to do fifty prayers but he returned to your Lord to make (i.e., reduce) them to five prayers.”",
    "Abu Huraira reported Allah's Messenger (ﷺ) as saying: Prayer said in a congregation is equivalent to twenty-five (prayers) as compared with the prayer said by a single person.",
    "Narrated `Abdullah bin `Umar: Allah's Messenger (ﷺ) said, \"The prayer in congregation is twenty seven times superior to the prayer offered by person alone.\"",
    "It was narrated from Abu Hurairah that: The Messenger of Allah said: \"The prayer in congregation is twenty-five times more virtuous than the prayer of anyone of you on his own.\"",
    "Narrated Abdullah ibn Umar: There were fifty prayers (obligatory in the beginning); and (in the beginning of Islam) washing seven times because of sexual defilement (was obligatory); and washing the urine from the cloth seven times (was obligatory). The Apostle of Allah (ﷺ) kept on praying to Allah until the number of prayers was reduced to five...",
    "Aisha reported: The Prophet said, 'The most beloved actions to Allah are those performed consistently, even if they are few.'",
    "Abu Huraira narrated: The Messenger of Allah said, 'Fasting is a shield. When anyone of you is fasting, he should not use obscene language or raise his voice. If anyone reviles him or tries to quarrel with him, he should say: I am fasting.'",
]
hadith_df = pd.DataFrame(sample_hadiths, columns=['English_Hadith'])

# ------------------ 2. Clean text function (notebook wali) ------------------
def clean_text(text):
    if isinstance(text, str):
        text = text.lower()
        text = re.sub(r'[^a-zA-Z0-9\\s]', '', text)
        text = re.sub(r'\\s+', ' ', text)
    else:
        text = ''
    return text

hadith_df['Cleaned_Hadith'] = hadith_df['English_Hadith'].apply(clean_text)

# ------------------ 3. MiniLM embeddings ------------------
model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
embeddings = model.encode(hadith_df['Cleaned_Hadith'].tolist(), show_progress_bar=True)
embeddings = np.array(embeddings)

# ------------------ 4. FAISS index ------------------
dim = embeddings.shape[1]
index = faiss.IndexFlatL2(dim)
index.add(embeddings)

# ------------------ 5. Search function ------------------
def get_similar_hadith(query, k=5):
    query_clean = clean_text(query)
    query_vec = model.encode([query_clean])
    distances, indices = index.search(query_vec, k)
    print(f"Query: {query}\n")
    for i in range(k):
        print(f"Hadith {i+1}, Distance: {distances[0][i]:.4f}")
        print(hadith_df['English_Hadith'].iloc[indices[0][i]])
        print()

# ------------------ 6. Sample queries ------------------
get_similar_hadith("How many prayers are there?")
get_similar_hadith("What is the reward of fasting?")
get_similar_hadith("Tell me about prayer in congregation")