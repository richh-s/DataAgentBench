code = """import re, json, pandas as pd
from pathlib import Path

# Load full civic docs
path_civic = Path(var_call_6XnHRP3CC73pgbpZp1fYXrmQ)
with open(path_civic, 'r') as f:
    civic_docs = json.load(f)

# Concatenate all text
texts = ' '.join(doc['text'] for doc in civic_docs)

# There is no structured per-project start date, so we will approximate using funding names and year markers.

# Load Funding table
path_funding = Path(var_call_JmkQBnhbp6M6C4LtFDGlpvsO)
with open(path_funding, 'r') as f:
    funding_records = json.load(f)

fund_df = pd.DataFrame(funding_records)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Disaster-related projects: names contain FEMA/CalOES/CalJPIA or the word 'Disaster'
def is_disaster_name(name: str) -> bool:
    name_u = name.upper()
    if 'FEMA' in name_u or 'CALOES' in name_u or 'CALJPIA' in name_u or 'DISASTER' in name_u:
        return True
    return False

fund_df['is_disaster'] = fund_df['Project_Name'].apply(is_disaster_name)

# Projects that started in 2022: approximate by names that contain '2022 '
fund_df['start_2022'] = fund_df['Project_Name'].str.contains('2022 ')

total_amount = int(fund_df[(fund_df['is_disaster']) & (fund_df['start_2022'])]['Amount'].sum())

import json as _json
out = _json.dumps(total_amount)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_6XnHRP3CC73pgbpZp1fYXrmQ': 'file_storage/call_6XnHRP3CC73pgbpZp1fYXrmQ.json', 'var_call_JmkQBnhbp6M6C4LtFDGlpvsO': 'file_storage/call_JmkQBnhbp6M6C4LtFDGlpvsO.json'}

exec(code, env_args)
