code = """import json, pandas as pd

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

fund = load_records(var_call_XVHE2S4YMwyqfgnXLhph61QL)
fund_df = pd.DataFrame(fund)
fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'])
# park-related likely names
park_mask = fund_df['Project_Name'].str.contains('Park|Playground|Bluffs|Skate', case=False, na=False)
park_df = fund_df[park_mask].copy()
# 2022 completed projects from docs include Bluffs Park Shade Structure, Broad Beach Road Water Quality Repair, Point Dume Walkway Repairs, etc.
# From park_df, only 'Bluffs Park Shade Structure' seems completed 2022.
answer_total = int(park_df.loc[park_df['Project_Name'].eq('Bluffs Park Shade Structure'), 'Total_Amount'].sum())
print('__RESULT__:')
print(json.dumps({'total': answer_total}))"""

env_args = {'var_call_VcSoEbEV11tJzvrjgzmhULMm': ['Funding'], 'var_call_B0V2TRekCl6vrNeq0NVAjjNk': ['civic_docs'], 'var_call_zl52m9mn8D1cMBUR9ENZQ8n5': 'file_storage/call_zl52m9mn8D1cMBUR9ENZQ8n5.json', 'var_call_XVHE2S4YMwyqfgnXLhph61QL': 'file_storage/call_XVHE2S4YMwyqfgnXLhph61QL.json', 'var_call_VLvf98opZ0Mh8hesFIh6m4Oh': {'ok': True}, 'var_call_MHDBQlUzcY4z4hGoHQqeqDBs': {'n': 1}}

exec(code, env_args)
