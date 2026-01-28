code = """import json
with open(locals()['var_function-call-7183846072918696098'], 'r') as f:
    citation_data = json.load(f)
    
paper_titles = [item['title'] for item in citation_data]

# Construct MongoDB query for each title
# The MongoDB query should retrieve the 'text' field for each paper.
mongo_queries = []
for title in paper_titles:
    # Escape single quotes within the title for the MongoDB query string
    escaped_title = title.replace("'", "\'")
    mongo_queries.append({
        "collection": "paper_docs", 
        "filter": {"filename": f"{escaped_title}.txt"}, 
        "projection": {"text": 1}
    })

print("__RESULT__:")
print(json.dumps(mongo_queries))"""

env_args = {'var_function-call-7183846072918696098': 'file_storage/function-call-7183846072918696098.json'}

exec(code, env_args)
