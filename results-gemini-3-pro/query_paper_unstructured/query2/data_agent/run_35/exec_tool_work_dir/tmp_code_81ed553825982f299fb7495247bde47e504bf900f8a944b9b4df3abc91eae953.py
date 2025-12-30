code = """import json
import pandas as pd

# Load citations
with open(locals()['var_function-call-5092927225989285410'], 'r') as f:
    citations_data = json.load(f)

# Load paper docs
with open(locals()['var_function-call-2239282102762620256'], 'r') as f:
    paper_docs = json.load(f)

# Identify ACM papers
acm_titles = set()
for doc in paper_docs:
    text = doc.get('text', '')
    # Check for ACM in text. 
    # To be more precise, we might look for "Copyright" and "ACM" nearby, or just "ACM"
    # Given the instructions "extract source", and "Common sources ... ACM", 
    # simple presence is the most straightforward interpretation without regex.
    if "ACM" in text: 
        title = doc['filename'].replace('.txt', '')
        acm_titles.add(title)

# Filter citations
acm_citations = []
for cit in citations_data:
    if cit['title'] in acm_titles:
        acm_citations.append(cit['citation_count'])

# Calculate average
if acm_citations:
    avg_citation = sum(acm_citations) / len(acm_citations)
else:
    avg_citation = 0

print("__RESULT__:")
print(json.dumps(avg_citation))"""

env_args = {'var_function-call-5092927225989285410': 'file_storage/function-call-5092927225989285410.json', 'var_function-call-2239282102762620256': 'file_storage/function-call-2239282102762620256.json'}

exec(code, env_args)
