code = """import json
import pandas as pd

# Access the file paths
citations_path = locals()['var_function-call-12560398010098331911']
papers_path = locals()['var_function-call-11991620735686112096']

# Load citations (already filtered for 2018 by SQL query)
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Load papers
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

# Identify ACM papers
acm_titles = set()
for paper in papers_data:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    header_text = text[:5000]
    if "ACM" in header_text or "Association for Computing Machinery" in header_text or "permissions@acm.org" in header_text:
        acm_titles.add(title)

# Filter citations for ACM papers
# We only care about citations for papers that are published by ACM
acm_citations = citations_df[citations_df['title'].isin(acm_titles)]

# Calculate average
if not acm_citations.empty:
    average_citations = acm_citations['citation_count'].mean()
else:
    average_citations = 0

print("__RESULT__:")
print(json.dumps(average_citations))"""

env_args = {'var_function-call-12560398010098331911': 'file_storage/function-call-12560398010098331911.json', 'var_function-call-11991620735686112096': 'file_storage/function-call-11991620735686112096.json'}

exec(code, env_args)
