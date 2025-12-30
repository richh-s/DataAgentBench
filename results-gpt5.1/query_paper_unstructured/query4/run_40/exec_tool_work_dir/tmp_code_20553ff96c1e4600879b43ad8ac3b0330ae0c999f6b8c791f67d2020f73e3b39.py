code = """import re, json
import pandas as pd

# Load full Mongo result
path_docs = var_call_Ct8EtI4owRMFLuLauJF3E0DR
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Extract title (from filename) and year (regex for 4-digit year 2016)
records = []
for d in docs:
    text = d.get('text', '')
    # year 2016
    if '2016' not in text:
        continue
    title = d.get('filename', '').replace('.txt','')
    # filter for domain physical activity via keyword search in text
    if re.search(r'physical activity', text, re.IGNORECASE) or re.search(r'\bexercise\b', text, re.IGNORECASE):
        records.append({'title': title})

# deduplicate titles
titles_pa_2016 = sorted(set(r['title'] for r in records))

# Load citation aggregates
path_cit = var_call_6KGyzX7uUQ9insjNHK3Pdusz
with open(path_cit, 'r') as f:
    cit = json.load(f)

cit_df = pd.DataFrame(cit)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

res = cit_df[cit_df['title'].isin(titles_pa_2016)][['title','total_citations']].to_dict(orient='records')

result = json.dumps(res)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_Ct8EtI4owRMFLuLauJF3E0DR': 'file_storage/call_Ct8EtI4owRMFLuLauJF3E0DR.json', 'var_call_6KGyzX7uUQ9insjNHK3Pdusz': 'file_storage/call_6KGyzX7uUQ9insjNHK3Pdusz.json'}

exec(code, env_args)
