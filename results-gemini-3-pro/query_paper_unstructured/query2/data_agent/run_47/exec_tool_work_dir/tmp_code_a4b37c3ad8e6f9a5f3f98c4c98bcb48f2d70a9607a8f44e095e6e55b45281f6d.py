code = """import json
import pandas as pd

# Load citations
with open(locals()['var_function-call-3783600766859717927'], 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)

# Load paper docs
with open(locals()['var_function-call-11097278280357331485'], 'r') as f:
    paper_docs_data = json.load(f)

# Process paper docs to identify ACM papers
acm_titles = set()
for doc in paper_docs_data:
    filename = doc.get('filename', '')
    if filename.endswith('.txt'):
        title = filename[:-4]
        text = doc.get('text', '')
        # Check first 5000 chars for ACM
        # Also check for "Association for Computing Machinery"
        # The prompt implies "ACM" is the source name to look for.
        # "Copyright ... ACM" is a good indicator.
        # Simply checking "ACM" in the first chunk is a good heuristic.
        header_text = text[:5000]
        if "ACM" in header_text or "Association for Computing Machinery" in header_text:
            acm_titles.add(title)

# Filter citations
# Join on title
# df_citations has 'title', 'citation_count'
# We only want rows where title is in acm_titles
# And citation_year is 2018 (which it is, based on the query)

df_citations['is_acm'] = df_citations['title'].isin(acm_titles)
acm_citations = df_citations[df_citations['is_acm']]

# Calculate average
if len(acm_citations) > 0:
    avg_citations = acm_citations['citation_count'].astype(float).mean()
else:
    avg_citations = 0.0

print("__RESULT__:")
print(avg_citations)"""

env_args = {'var_function-call-3783600766859717927': 'file_storage/function-call-3783600766859717927.json', 'var_function-call-11097278280357331485': 'file_storage/function-call-11097278280357331485.json'}

exec(code, env_args)
