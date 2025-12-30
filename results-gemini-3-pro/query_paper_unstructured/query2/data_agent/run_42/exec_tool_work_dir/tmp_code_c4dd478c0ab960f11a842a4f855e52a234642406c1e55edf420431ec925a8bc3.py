code = """import json
import pandas as pd
import re

# Load citations
with open(locals()['var_function-call-7375441648498366517'], 'r') as f:
    citations_data = json.load(f)

# Load paper docs
with open(locals()['var_function-call-12252996319457097106'], 'r') as f:
    paper_docs_data = json.load(f)

# Create a dictionary for citations: title -> citation_count
# The citations_data is a list of dicts.
# Note: Titles in citations_data might need normalization? 
# The hint says: "The paper title in the Citations SQLite table matches the filename (without .txt extension)"
citation_map = {item['title']: item['citation_count'] for item in citations_data}

acm_citations = []

for doc in paper_docs_data:
    filename = doc.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4] # Remove .txt
    
    # Check if this paper was cited in 2018 (i.e., exists in our citation_map)
    if title in citation_map:
        text = doc.get('text', '')
        
        # Determine source
        # Heuristic: Check for "ACM" in the first 5000 characters or Look for Copyright statement
        # Looking at the sample: "Copyright 2015 © ACM"
        # Also "Permission ... ACM"
        # I'll check for "ACM" in the first 5000 chars to cover the first page/metadata.
        # This avoids finding "ACM" in the references section at the end.
        
        is_acm = False
        if "ACM" in text[:10000]: # Increased to 10000 to be safe for first page
             is_acm = True
        
        # Double check with specific patterns if needed, but "ACM" in the header/copyright is strong.
        # Let's verify if "IEEE" is there to avoid confusion if both appear?
        # Usually one publisher per paper.
        
        if is_acm:
            count = citation_map[title]
            acm_citations.append(count)

# Calculate average
if len(acm_citations) > 0:
    avg_citations = sum(acm_citations) / len(acm_citations)
else:
    avg_citations = 0

print("__RESULT__:")
print(json.dumps(avg_citations))"""

env_args = {'var_function-call-7375441648498366517': 'file_storage/function-call-7375441648498366517.json', 'var_function-call-12252996319457097106': 'file_storage/function-call-12252996319457097106.json'}

exec(code, env_args)
