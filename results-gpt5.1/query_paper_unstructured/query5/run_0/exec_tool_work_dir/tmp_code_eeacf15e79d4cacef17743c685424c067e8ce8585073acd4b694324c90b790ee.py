code = """import json, pandas as pd
from pathlib import Path

# Load full citations result from file
path = Path(var_call_V9Hp81xS11QJFI0RIwP1fRoT)
with path.open() as f:
    citations = json.load(f)

cit_df = pd.DataFrame(citations)
chi_filenames = [d['filename'] for d in var_call_gsL9uEg7zKvWSW97fnGhsUw7]
chi_titles = [fn.replace('.txt','') for fn in chi_filenames]

chi_cit = cit_df[cit_df['title'].isin(chi_titles)]

result = int(chi_cit['total_citations'].astype(int).sum())

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_V9Hp81xS11QJFI0RIwP1fRoT': 'file_storage/call_V9Hp81xS11QJFI0RIwP1fRoT.json', 'var_call_gsL9uEg7zKvWSW97fnGhsUw7': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
