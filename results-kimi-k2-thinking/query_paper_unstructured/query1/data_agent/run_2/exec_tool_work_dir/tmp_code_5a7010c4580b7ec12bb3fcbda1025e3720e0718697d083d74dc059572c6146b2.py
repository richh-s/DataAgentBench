code = """import json
import os

# Load MongoDB paper documents
mongo_key = "var_functions.query_db:2"
mongo_path = locals().get(mongo_key, "")
print(f"Loading MongoDB data from: {mongo_path}")

if mongo_path and os.path.exists(mongo_path):
    with open(mongo_path, 'r') as f:
        papers = json.load(f)
    print(f"Loaded {len(papers)} papers from MongoDB")
    # Show first paper structure
    if papers:
        print("First paper keys:", papers[0].keys())
        print("First paper filename:", papers[0].get('filename'))
        # Extract title from filename
        filename = papers[0].get('filename', '')
        title = filename.replace('.txt', '') if filename else ''
        print("Extracted title:", title)
else:
    print(f"File not found or invalid path: {mongo_path}")
    papers = []

# Load citations data
citations_key = "var_functions.query_db:9"
citations_path = locals().get(citations_key, "")
print(f"\nLoading citations from: {citations_path}")

if citations_path and os.path.exists(citations_path):
    with open(citations_path, 'r') as f:
        citations = json.load(f)
    print(f"Loaded {len(citations)} citation records")
    if citations:
        print("First citation:", citations[0])
        print("Citation title:", citations[0].get('title'))
else:
    print(f"File not found or invalid path: {citations_path}")
    citations = []

# Let's understand the data structure first
result = {
    "papers_count": len(papers),
    "citations_count": len(citations),
    "first_paper_title": papers[0].get('filename', '').replace('.txt', '') if papers else None,
    "first_citation_title": citations[0].get('title') if citations else None
}

print('__RESULT__:') 
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json'}

exec(code, env_args)
