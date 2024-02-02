import pandas as pd
import numpy as np
from ast import literal_eval
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv() 

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

df = pd.read_csv('processed/embeddings.csv', index_col=0)

df['embeddings'] = df['embeddings'].apply(literal_eval).apply(np.array)

df.head()

def create_context(question, df, max_len=800, size="ada"):
    """
    Create a context for a question by finding the most similar context from the dataframe
    """

    q_response = client.embeddings.create(input=question, model='text-embedding-ada-002')
    q_embeddings = q_response.data[0].embedding


    df['distances'] = df['embeddings'].apply(lambda emb: cosine_similarity(q_embeddings, emb))

    returns = []
    cur_len = 0


    for i, row in df.sort_values('distances', ascending=True).iterrows():
        cur_len += row['n_tokens'] + 4
        if cur_len > max_len:
            break
        returns.append(row["text"])


    return "\n\n###\n\n".join(returns)

def answer_question(df, model="davinci-002", question="Am I allowed to publish model outputs to Twitter, without a human review?", max_len=1800, size="ada", debug=True, max_tokens=100, stop_sequence="\n"):
    """
    Answer a question based on the most similar context from the dataframe texts
    """
    context = create_context(question, df, max_len=max_len, size=size)
    if debug:
        print("Context:\n" + context)
        print("\n\n")

    try:
        response = client.completions.create(
            prompt=f"Answer the question based on the context below, and if the question can't be answered based on the context, say 'I don't know'\n\nContext: {context}\n\n---\n\nQuestion: {question}\nAnswer:",
            temperature=0,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=stop_sequence,
            model=model,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(e)
        return ""