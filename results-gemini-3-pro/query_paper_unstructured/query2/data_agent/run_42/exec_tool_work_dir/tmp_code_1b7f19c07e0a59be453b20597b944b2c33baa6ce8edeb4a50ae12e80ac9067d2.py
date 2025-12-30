code = """import json
import pandas as pd

# Load citations
with open(locals()['var_function-call-7375441648498366517'], 'r') as f:
    citations_data = json.load(f)

# Load paper docs
with open(locals()['var_function-call-12252996319457097106'], 'r') as f:
    paper_docs_data = json.load(f)

# Create a dictionary for citations: title -> citation_count
# Convert citation_count to int
citation_map = {}
for item in citations_data:
    try:
        count = int(item['citation_count'])
        citation_map[item['title']] = count
    except ValueError:
        continue # Skip if invalid

acm_citations = []

for doc in paper_docs_data:
    filename = doc.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4] # Remove .txt
    
    # Check if this paper was cited in 2018
    if title in citation_map:
        text = doc.get('text', '')
        
        # Check for ACM source
        # Using a simpler check: "ACM" in first 5000 chars. 
        # Also, check if it's NOT IEEE to be safer?
        # But the question asks for "published by ACM".
        # If "ACM" is in the first few pages, it's likely ACM.
        if "ACM" in text[:5000]:
            acm_citations.append(citation_map[title])

# Calculate average
if len(acm_citations) > 0:
    avg_citations = sum(acm_citations) / len(acm_citations)
else:
    avg_citations = 0

print("__RESULT__:")
print(json.dumps(avg_citations))"""

env_args = {'var_function-call-7375441648498366517': 'file_storage/function-call-7375441648498366517.json', 'var_function-call-12252996319457097106': 'file_storage/function-call-12252996319457097106.json'}

exec(code, env_args)
