code = """import json
import pandas as pd

# Load citations
with open('var_function-call-12560398010098331911', 'r') as f:
    citations_data = json.load(f)

citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])
citations_df['citation_year'] = pd.to_numeric(citations_df['citation_year'])

# Filter for 2018 citations
citations_2018 = citations_df[citations_df['citation_year'] == 2018].copy()

# Load papers
with open('var_function-call-11991620735686112096', 'r') as f:
    papers_data = json.load(f)

# Identify ACM papers
acm_titles = set()
for paper in papers_data:
    text = paper.get('text', '')
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check for ACM in the first 5000 characters (header/metadata/copyright)
    # Common indicators: "ACM", "permissions@acm.org", "Association for Computing Machinery"
    header_text = text[:5000]
    if "ACM" in header_text or "Association for Computing Machinery" in header_text:
        acm_titles.add(title)

# Filter citations for ACM papers
acm_citations_2018 = citations_2018[citations_2018['title'].isin(acm_titles)]

# Calculate average
if not acm_citations_2018.empty:
    average_citations = acm_citations_2018['citation_count'].mean()
else:
    average_citations = 0

print("__RESULT__:")
print(json.dumps(average_citations))"""

env_args = {'var_function-call-12560398010098331911': 'file_storage/function-call-12560398010098331911.json', 'var_function-call-11991620735686112096': 'file_storage/function-call-11991620735686112096.json'}

exec(code, env_args)
