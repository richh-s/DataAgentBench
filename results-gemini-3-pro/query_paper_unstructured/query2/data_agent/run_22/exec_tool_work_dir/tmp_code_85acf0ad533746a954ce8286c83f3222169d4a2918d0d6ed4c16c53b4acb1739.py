code = """import json
import pandas as pd

# Get file paths
citations_path = locals()['var_function-call-12153824961248921598']
papers_path = locals()['var_function-call-3504692975611413674']

# Load citations
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

# Load papers
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

# Identify ACM papers
acm_titles = []
for p in papers_data:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check for ACM in the first 3000 characters
    head_text = text[:3000]
    # Check for "ACM" word with boundary or copyright/permission context
    # Simply checking "ACM" might be enough given the domain.
    # But let's be slightly more robust.
    if "ACM" in head_text or "permissions@acm.org" in text:
        acm_titles.append(title)

# Filter citations for ACM papers
# df_citations contains records for citation_year=2018
acm_citations = df_citations[df_citations['title'].isin(acm_titles)]

# Calculate average
if not acm_citations.empty:
    average_citation = acm_citations['citation_count'].mean()
else:
    average_citation = 0

print("__RESULT__:")
print(json.dumps(average_citation))"""

env_args = {'var_function-call-12153824961248921598': 'file_storage/function-call-12153824961248921598.json', 'var_function-call-3504692975611413674': 'file_storage/function-call-3504692975611413674.json'}

exec(code, env_args)
