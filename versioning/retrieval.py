def rl_search(query, collection):
    results = collection.query(query_texts=[query], n_results=1)
    return results['documents'][0][0]
