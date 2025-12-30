code = """import re, json
from pathlib import Path

# Load full Mongo results
path_docs = Path(var_call_okRSYMRUWv0jKSuwzXHxoQyV)
import pandas as pd
papers = pd.read_json(path_docs)

# Extract year from text (look for 2016) and domain via keyword 'physical activity'
physical_papers = []
for _, row in papers.iterrows():
    text = row['text'] or ''
    if re.search(r'2016', text) and re.search(r'physical activity', text, re.I):
        title = re.sub(r'\.txt$', '', row['filename'])
        physical_papers.append(title)

# Load citations
path_cit = Path(var_call_H3PD3Abg0XOGjTt9f41mt1EN)
cit = pd.read_json(path_cit)

# Filter to titles in physical_papers and sum citations
cit_filt = cit[cit['title'].isin(physical_papers)].copy()
result_df = cit_filt.groupby('title', as_index=False)['total_citations'].sum()

result = result_df.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result) )"""

env_args = {'var_call_okRSYMRUWv0jKSuwzXHxoQyV': 'file_storage/call_okRSYMRUWv0jKSuwzXHxoQyV.json', 'var_call_H3PD3Abg0XOGjTt9f41mt1EN': 'file_storage/call_H3PD3Abg0XOGjTt9f41mt1EN.json'}

exec(code, env_args)
