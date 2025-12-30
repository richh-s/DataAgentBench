code = """import json
import pandas as pd

# Load citations result
with open(locals()['var_function-call-1269001259179698706'], 'r') as f:
    citations_data = json.load(f)

# Load paper docs result
with open(locals()['var_function-call-1269001259179697405'], 'r') as f:
    paper_docs = json.load(f)

# Create a dictionary for fast lookup of citation counts by title
# Filter citations for 2018 is already done in the SQL query
citation_map = {item['title']: item['citation_count'] for item in citations_data}

acm_citations = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
    
    # Check if this paper has citations in 2018
    if title in citation_map:
        text = doc.get('text', '')
        # Check if source is ACM
        # Looking for "ACM" in the text. 
        # To be more robust, we might look for "Permission to make ... ACM" or "Copyright ... ACM"
        # But simple substring matching is often sufficient for these logical extraction tasks unless there's ambiguity.
        if "ACM" in text: 
            acm_citations.append(int(citation_map[title]))

if len(acm_citations) > 0:
    avg_citations = sum(acm_citations) / len(acm_citations)
else:
    avg_citations = 0

print("__RESULT__:")
print(avg_citations)"""

env_args = {'var_function-call-1269001259179698706': 'file_storage/function-call-1269001259179698706.json', 'var_function-call-1269001259179697405': 'file_storage/function-call-1269001259179697405.json'}

exec(code, env_args)
