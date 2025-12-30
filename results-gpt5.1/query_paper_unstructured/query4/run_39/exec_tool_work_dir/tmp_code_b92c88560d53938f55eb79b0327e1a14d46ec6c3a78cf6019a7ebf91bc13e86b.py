code = """import re, json
import pandas as pd

# Load full citation aggregates
path_citations = var_call_YwY5dVz4jnAPi4yWNJn4corI
with open(path_citations, 'r') as f:
    citations = json.load(f)

# Load paper docs preview list directly (already a list of docs)
docs = var_call_aWZLqpMpVyg6bBCzKvZYcDdK

# Helper to extract year from text
YEAR_RE = re.compile(r"(?<!\d)(20\d{2}|19\d{2})(?!\d)")

def extract_year(text):
    years = [int(y) for y in YEAR_RE.findall(text)]
    if not years:
        return None
    # Heuristic: publication year is earliest year >= 2000
    years = [y for y in years if y >= 2000]
    return min(years) if years else None

records = []
for d in docs:
    title = d['filename'].rsplit('.txt', 1)[0]
    text = d.get('text', '')
    year = extract_year(text)
    if year == 2016 and re.search(r"physical activity", text, re.I):
        records.append({'title': title, 'year': year})

# Convert citations to DataFrame
cit_df = pd.DataFrame(citations)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

res = []
for r in records:
    title = r['title']
    match = cit_df.loc[cit_df['title'] == title]
    if not match.empty:
        total = int(match['total_citations'].iloc[0])
        res.append({'title': title, 'total_citations': total})

result_json = json.dumps(res)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_aWZLqpMpVyg6bBCzKvZYcDdK': 'file_storage/call_aWZLqpMpVyg6bBCzKvZYcDdK.json', 'var_call_YwY5dVz4jnAPi4yWNJn4corI': 'file_storage/call_YwY5dVz4jnAPi4yWNJn4corI.json'}

exec(code, env_args)
