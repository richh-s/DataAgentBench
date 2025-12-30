code = """import json
import pandas as pd

# Load full citations result from file
with open(var_call_CYI4abAP81GkDI6nC4UwHTEB, 'r') as f:
    citations = json.load(f)

cit_df = pd.DataFrame(citations)
chi_files = [d['filename'] for d in var_call_L6Ex73z5qfASpuzeLZKODOO4]
chi_titles = [f[:-4] if f.lower().endswith('.txt') else f for f in chi_files]

result = int(cit_df[cit_df['title'].isin(chi_titles)]['citation_count'].astype(int).sum())

import json as _json
res_json = _json.dumps(result)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_CYI4abAP81GkDI6nC4UwHTEB': 'file_storage/call_CYI4abAP81GkDI6nC4UwHTEB.json', 'var_call_L6Ex73z5qfASpuzeLZKODOO4': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}]}

exec(code, env_args)
