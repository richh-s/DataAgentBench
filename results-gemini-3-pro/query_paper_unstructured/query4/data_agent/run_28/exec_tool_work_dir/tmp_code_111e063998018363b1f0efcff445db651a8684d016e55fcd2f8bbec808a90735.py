code = """import json
import pandas as pd

# Load citations
with open(locals()['var_function-call-14596373756638571722'], 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)
# Ensure citation_count is int
df_citations['citation_count'] = df_citations['citation_count'].astype(int)
# Group by title and sum
citation_totals = df_citations.groupby('title')['citation_count'].sum().to_dict()

# Load paper docs
with open(locals()['var_function-call-7398565704940874410'], 'r') as f:
    paper_docs = json.load(f)

results = []

for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    # Check domain
    if 'physical activity' not in text.lower():
        continue
        
    # Check year
    # Look for 2016 in the first 1000 characters
    header = text[:1000]
    if '2016' in header:
        # Check if it's the publication year. 
        # Sometimes '2016' might be part of an email or something, but usually safe in header.
        # Let's assume presence in first 1000 chars is sufficient for this task.
        
        # Get total citations
        total_citations = citation_totals.get(title, 0)
        
        results.append({
            "title": title,
            "total_citation_count": total_citations
        })

# Sort by title for consistency
results.sort(key=lambda x: x['title'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5420876219690003843': 'file_storage/function-call-5420876219690003843.json', 'var_function-call-14495357574425764744': 'file_storage/function-call-14495357574425764744.json', 'var_function-call-7398565704940874410': 'file_storage/function-call-7398565704940874410.json', 'var_function-call-14596373756638571722': 'file_storage/function-call-14596373756638571722.json'}

exec(code, env_args)
