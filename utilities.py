import fitz
import pymupdf
fitz = pymupdf
import pandas as pd
import nltk
#from gensim.models import Word2Vec   ### embedding/vector
#from nltk.tokenize import word_tokenize   ### tokens
import numpy as np

from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer ###BertModel

### load the model using nltk special punkt parameter
nltk.download('punkt')
nltk.download('punkt_tab')


def extract_text_from_pdf(pdf_path):
  pdf_doc = fitz.open(stream=pdf_path, filename="pdf")
  text= "" 
  for page in pdf_doc:
    text += page.get_text("text")

  return text


###doc = fitz.open('Resume_usha_2024.pdf')
###print(doc)

### Train the model by creating embeddings
#extracted_text = extract_text_from_pdf("/Users/ushasowmyavasamsetti/Downloads/Resume_usha_2024.pdf")

#tokens= word_tokenize(extracted_text)
#model = Word2Vec([tokens], vector_size = 5, window=2,min_count=1)

### load the retrained model with the above extractracted text inn string format


model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
### Pass text to model
def get_embedding(text):
  '''this function returns the embedding of the text'''
  return model.encode([text])[0]



def compute_similiarity(resume_text, jd_text):

  ### this function checks the cosine similarity by using cosine fucntion
  resume_embedding = get_embedding(resume_text)
  jb_embedding = get_embedding(jd_text)
  ### Reshape the embeddings to 2D before calculating cosine similarity
  #resume_embedding = resume_embedding.reshape(resume_embedding.shape[1])  # or resume_embedding[0]
  #jb_embedding = jb_embedding.reshape(jb_embedding.shape[1])
  similarity_score = cosine_similarity([resume_embedding], [jb_embedding])[0][0]
  return similarity_score