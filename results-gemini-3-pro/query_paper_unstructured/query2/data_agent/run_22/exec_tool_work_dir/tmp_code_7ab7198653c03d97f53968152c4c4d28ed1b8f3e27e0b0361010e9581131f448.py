code = """import json
import pandas as pd

# Load citations
with open('var_function-call-12153824961248921598.json', 'r') as f:
    citations_data = json.load(f)

# Convert to DataFrame
df_citations = pd.DataFrame(citations_data)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

# Load papers
with open('var_function-call-3504692975611413674.json', 'r') as f:
    papers_data = json.load(f)

# Identify ACM papers
acm_titles = []
for p in papers_data:
    text = p.get('text', '')
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check for ACM in the first 2000 characters or specific indicators
    # The preview showed copyright info within the first few paragraphs.
    # Common indicators: "permissions@acm.org", "Copyright ... ACM", "Association for Computing Machinery"
    # Or just "ACM" in the header/copyright.
    
    head_text = text[:3000]
    if "ACM" in head_text or "permissions@acm.org" in text or "Association for Computing Machinery" in text:
        acm_titles.append(title)

# Filter citations for ACM papers
# Note: citations_data is already filtered for citation_year=2018
acm_citations = df_citations[df_citations['title'].isin(acm_titles)]

average_citation = acm_citations['citation_count'].mean()

print("__RESULT__:")
print(json.dumps(average_citation))"""

env_args = {'var_function-call-12153824961248921598': 'file_storage/function-call-12153824961248921598.json', 'var_function-call-3504692975611413674': 'file_storage/function-call-3504692975611413674.json'}

exec(code, env_args)
