code = """import json
import pandas as pd

food_files = [d['filename'] for d in var_call_85gi9NVeMHkcyrua9s0eQWE8]
food_titles = [f.replace('.txt','') for f in food_files]

import os
with open(var_call_U76oWQxSIiKNYaTiMScTZsfc, 'r') as f:
    citations = json.load(f)

cit_df = pd.DataFrame(citations)
cit_df['total_citations'] = cit_df['total_citations'].astype(int)

food_citations = cit_df[cit_df['title'].isin(food_titles)]['total_citations'].sum()

result = json.dumps(food_citations)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_85gi9NVeMHkcyrua9s0eQWE8': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}], 'var_call_U76oWQxSIiKNYaTiMScTZsfc': 'file_storage/call_U76oWQxSIiKNYaTiMScTZsfc.json'}

exec(code, env_args)
