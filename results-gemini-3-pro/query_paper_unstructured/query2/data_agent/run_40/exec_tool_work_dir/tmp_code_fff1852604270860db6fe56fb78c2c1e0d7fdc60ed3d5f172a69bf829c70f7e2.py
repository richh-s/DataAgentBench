code = """import json
import os

# Load citations
citations_path = locals()['var_function-call-7399957863239035507']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Create lookup for citations in 2018 (the query already filtered by year 2018)
# The query result has {"title": ..., "citation_count": ...}
citation_lookup = {}
for entry in citations_data:
    citation_lookup[entry['title']] = int(entry['citation_count'])

# Load paper docs
docs_path = locals()['var_function-call-7399957863239036828']
with open(docs_path, 'r') as f:
    paper_docs = json.load(f)

acm_counts = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4] # remove .txt
    
    if title in citation_lookup:
        text = doc.get('text', '')
        # Check for ACM in the first 5000 characters to avoid references
        header_text = text[:5000]
        
        # Simple heuristic: Look for "ACM" or "Association for Computing Machinery"
        # Also could look for "Copyright" line
        if "ACM" in header_text or "Association for Computing Machinery" in header_text:
            acm_counts.append(citation_lookup[title])

if len(acm_counts) > 0:
    average_citations = sum(acm_counts) / len(acm_counts)
else:
    average_citations = 0

print("__RESULT__:")
print(json.dumps({"average_citation_count": average_citations, "count_papers": len(acm_counts)}))"""

env_args = {'var_function-call-10677751840676979687': ['paper_docs'], 'var_function-call-10677751840676979600': ['Citations', 'sqlite_sequence'], 'var_function-call-7399957863239035507': 'file_storage/function-call-7399957863239035507.json', 'var_function-call-7399957863239036828': 'file_storage/function-call-7399957863239036828.json'}

exec(code, env_args)
