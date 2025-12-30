code = """import json
import re

# Load SQLite results
with open(locals()['var_function-call-4059042724151098954'], 'r') as f:
    citations_data = json.load(f)

# Load MongoDB results
# The file contains a list of documents.
with open(locals()['var_function-call-8902021320035767090'], 'r') as f:
    mongo_docs = json.load(f)

# Create a lookup for documents by filename
docs_by_filename = {d['filename']: d['text'] for d in mongo_docs}

# Filter citations for papers that are in MongoDB and are published by ACM
acm_citations = []

for record in citations_data:
    title = record['title']
    filename = title + ".txt"
    
    if filename in docs_by_filename:
        text = docs_by_filename[filename]
        # Check for ACM
        # Simple check: is "ACM" in the text?
        # Or more specific: "Copyright" and "ACM", or "Association for Computing Machinery"
        # The prompt hints suggest just "ACM".
        # Let's check for "ACM" as a substring.
        if "ACM" in text:
            acm_citations.append(int(record['citation_count']))

# Calculate average
if acm_citations:
    avg_citation = sum(acm_citations) / len(acm_citations)
    print(f"Number of ACM papers: {len(acm_citations)}")
    print("__RESULT__:")
    print(json.dumps(avg_citation))
else:
    print("No ACM papers found.")
    print("__RESULT__:")
    print("null")"""

env_args = {'var_function-call-4059042724151098954': 'file_storage/function-call-4059042724151098954.json', 'var_function-call-2165540971690442672': 'file_storage/function-call-2165540971690442672.json', 'var_function-call-8902021320035767090': 'file_storage/function-call-8902021320035767090.json'}

exec(code, env_args)
