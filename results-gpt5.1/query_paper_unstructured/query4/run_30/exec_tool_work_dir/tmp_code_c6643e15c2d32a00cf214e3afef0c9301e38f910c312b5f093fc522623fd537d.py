code = """import re, json
import pandas as pd

# Load full mongo result
path_mongo = var_call_weqgpRSaqF41d4cJRJgJJnfy
with open(path_mongo, 'r') as f:
    mongo_records = json.load(f)

# Extract title (filename without .txt), year (first 4-digit 20xx), and domain via keyword match
physical_titles_2016 = []
for doc in mongo_records:
    text = doc.get('text', '')
    # year
    years = re.findall(r"(20[0-9]{2})", text)
    year = int(years[0]) if years else None
    if year != 2016:
        continue
    # domain: contains 'physical activity' (case-insensitive)
    if re.search(r"physical activity", text, re.IGNORECASE):
        filename = doc.get('filename', '')
        title = re.sub(r"\.txt$", "", filename)
        physical_titles_2016.append(title)

# Load citations aggregate
path_cit = var_call_LT1Tvzy78W420508pZEZsZpc
with open(path_cit, 'r') as f:
    cit_records = json.load(f)

df_cit = pd.DataFrame(cit_records)
# normalize title quoting artifacts
df_cit['title_clean'] = df_cit['title'].str.replace('"', '', regex=False)

results = []
for t in physical_titles_2016:
    match = df_cit[df_cit['title_clean'] == t]
    if not match.empty:
        total = int(match.iloc[0]['total_citations'])
    else:
        total = 0
    results.append({'title': t, 'total_citations': total})

out = json.dumps(results)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_weqgpRSaqF41d4cJRJgJJnfy': 'file_storage/call_weqgpRSaqF41d4cJRJgJJnfy.json', 'var_call_LT1Tvzy78W420508pZEZsZpc': 'file_storage/call_LT1Tvzy78W420508pZEZsZpc.json'}

exec(code, env_args)
