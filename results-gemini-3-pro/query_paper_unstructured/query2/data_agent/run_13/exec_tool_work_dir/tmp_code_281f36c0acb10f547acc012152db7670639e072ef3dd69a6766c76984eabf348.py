code = """import json
import pandas as pd

# Load citations
with open(locals()['var_function-call-12153821661542533629'], 'r') as f:
    citations_data = json.load(f)

citations_df = pd.DataFrame(citations_data)

# Load paper docs
with open(locals()['var_function-call-12153821661542534380'], 'r') as f:
    papers_data = json.load(f)

# Identify ACM papers
acm_titles = []
for paper in papers_data:
    text = paper.get('text', '')
    # Check for ACM in text. 
    # Strategy: Check for "ACM" in the text. 
    # To reduce false positives, we might check for "Copyright" and "ACM" or "Association for Computing Machinery"
    # The example text has "Copyright 2015 © ACM".
    # Another indicator: "Permission to make ... ACM".
    # Or "ACM Classification Keywords".
    # Let's check if "ACM" is present.
    if "ACM" in text:
        # Extract title from filename
        filename = paper.get('filename', '')
        if filename.endswith('.txt'):
            title = filename[:-4]
            acm_titles.append(title)

# Filter citations
# Ensure citation_count is numeric
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Filter by ACM titles
acm_citations = citations_df[citations_df['title'].isin(acm_titles)]

# Calculate average
if len(acm_citations) > 0:
    avg_citations = acm_citations['citation_count'].mean()
else:
    avg_citations = 0

print("__RESULT__:")
print(json.dumps(avg_citations))"""

env_args = {'var_function-call-12153821661542533629': 'file_storage/function-call-12153821661542533629.json', 'var_function-call-12153821661542534380': 'file_storage/function-call-12153821661542534380.json'}

exec(code, env_args)
