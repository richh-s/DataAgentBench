code = """import re, json
from pathlib import Path

# Load full Mongo results
path = Path(var_call_OQUPHlIocDiEW6f9Yvk1644G)
import pandas as pd
mongo_records = pd.read_json(path).to_dict(orient='records')

# Function to extract year and domain heuristically
results = []
for doc in mongo_records:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    # year: look for 2016
    year = None
    if re.search(r"2016", text):
        year = 2016
    # domain physical activity
    if re.search(r"physical activity", text, re.IGNORECASE):
        domain = 'physical activity'
    else:
        domain = None
    if year == 2016 and domain == 'physical activity':
        results.append({'title': title})

# Load citations
path2 = Path(var_call_pEPldJf6LzCkKjlJLmov8qgq)
cites = pd.read_json(path2)

# Filter citations to those titles and sum total_citations (already summed per title)
pa_titles = set(r['title'] for r in results)
filtered = cites[cites['title'].isin(pa_titles)][['title','total_citations']]

answer = filtered.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(answer))"""

env_args = {'var_call_OQUPHlIocDiEW6f9Yvk1644G': 'file_storage/call_OQUPHlIocDiEW6f9Yvk1644G.json', 'var_call_pEPldJf6LzCkKjlJLmov8qgq': 'file_storage/call_pEPldJf6LzCkKjlJLmov8qgq.json'}

exec(code, env_args)
