code = """import re, json
from pathlib import Path

# Load full mongo results
path = Path(var_call_OeQEnnGPPLkLF0ulmyECGcTN)
import pandas as pd
mongo_records = pd.read_json(path).to_dict(orient='records')

physical_2016_titles = set()
for doc in mongo_records:
    text = doc.get('text','')
    if re.search(r'2016', text) and re.search(r'physical activity', text, re.I):
        fname = doc.get('filename','')
        title = re.sub(r'\.txt$', '', fname)
        physical_2016_titles.add(title)

# Load citations aggregation
path2 = Path(var_call_LccQELcd37pp7lzJjXk8HWmf)
cit_df = pd.read_json(path2)

results = []
for title in physical_2016_titles:
    row = cit_df[cit_df['title'] == title]
    if not row.empty:
        total = int(row['total_citations'].iloc[0])
        results.append({'title': title, 'total_citations': total})

out = json.dumps(results)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_OeQEnnGPPLkLF0ulmyECGcTN': 'file_storage/call_OeQEnnGPPLkLF0ulmyECGcTN.json', 'var_call_LccQELcd37pp7lzJjXk8HWmf': 'file_storage/call_LccQELcd37pp7lzJjXk8HWmf.json'}

exec(code, env_args)
