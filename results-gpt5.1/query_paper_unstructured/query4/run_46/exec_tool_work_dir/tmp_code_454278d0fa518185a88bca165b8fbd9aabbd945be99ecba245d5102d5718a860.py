code = """import re, json, pandas as pd
from pathlib import Path

# Load full results from files
papers = json.load(open(var_call_jVgmOa0pfUMrD3j4FIHkq14P, 'r'))
citations = json.load(open(var_call_hBa9Cnw7SFwYB0g7l26YifwI, 'r'))

# Extract metadata from text (year and domain) heuristically
records = []
for doc in papers:
    text = doc.get('text', '')
    # Heuristic for year: look for 2016 in header or copyright line
    year = None
    m = re.search(r"20(1[0-9]|2[0-9])", text[:1000])
    if m:
        year = int(m.group(0))
    # Domain: look for 'physical activity' substring
    domain_match = re.search(r"physical activity", text, re.IGNORECASE)
    domain = 'physical activity' if domain_match else None
    title = doc.get('filename', '').replace('.txt', '')
    records.append({'title': title, 'year': year, 'domain': domain})

papers_df = pd.DataFrame(records)

# Filter to 2016 and physical activity domain
pa_2016 = papers_df[(papers_df['year'] == 2016) & (papers_df['domain'] == 'physical activity')]

cites_df = pd.DataFrame(citations)
# Ensure numeric citations
cites_df['total_citations'] = pd.to_numeric(cites_df['total_citations'], errors='coerce')

# Join on title
merged = pa_2016.merge(cites_df, on='title', how='left')

result = merged[['title', 'total_citations']].to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_jVgmOa0pfUMrD3j4FIHkq14P': 'file_storage/call_jVgmOa0pfUMrD3j4FIHkq14P.json', 'var_call_hBa9Cnw7SFwYB0g7l26YifwI': 'file_storage/call_hBa9Cnw7SFwYB0g7l26YifwI.json'}

exec(code, env_args)
