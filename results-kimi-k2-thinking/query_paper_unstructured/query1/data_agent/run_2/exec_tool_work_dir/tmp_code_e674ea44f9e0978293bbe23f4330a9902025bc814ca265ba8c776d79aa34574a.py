code = """import json
import os

# Load MongoDB paper documents
mongo_path = var_functions.query_db:2
print(f"Loading MongoDB data from: {mongo_path}")

if os.path.exists(mongo_path):
    with open(mongo_path, 'r') as f:
        papers = json.load(f)
    print(f"Loaded {len(papers)} papers from MongoDB")
    # Show first paper structure
    if papers:
        print("First paper keys:", papers[0].keys())
        print("First paper filename:", papers[0].get('filename'))
        # Print part of text to understand structure
        text_sample = papers[0].get('text', '')[:1000]
        print("Text sample:", text_sample[:500])
else:
    print(f"File not found: {mongo_path}")
    papers = []

# Load citations data
citations_path = var_functions.query_db:9
print(f"\nLoading citations from: {citations_path}")

if os.path.exists(citations_path):
    with open(citations_path, 'r') as f:
        citations = json.load(f)
    print(f"Loaded {len(citations)} citation records")
    if citations:
        print("First citation:", citations[0])
else:
    print(f"File not found: {citations_path}")
    citations = []

print('__RESULT__:') 
print(json.dumps({"papers_count": len(papers), "citations_count": len(citations)}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
