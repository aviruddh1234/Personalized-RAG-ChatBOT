from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os 
import pandas as pd

df = pd.read_csv("GuavaTripsRating.csv")

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chrome_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    
    for i, row in df.iterrows():
        document = Document(
            page_content=row["Title"] + " " + row["Review"],
            metadata={
                "rating": row["Rating"],
                "date": row["Date"]
            },
            id = str(i)
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name="guava_trips",
    embedding_function=embeddings,
    persist_directory=db_location,
)

if add_documents:
    vector_store.add_documents(documents, ids=ids)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 3}
)