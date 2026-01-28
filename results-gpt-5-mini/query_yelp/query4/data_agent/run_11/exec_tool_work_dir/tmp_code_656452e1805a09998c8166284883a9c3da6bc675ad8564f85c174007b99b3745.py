code = """import json
import pandas as pd
with open(var_call_9lcqa0C2p1ehoGhnkxLGVTmB, 'r') as f:
    biz = json.load(f)
df = pd.DataFrame(biz)
# Prepare summary
summary = {
    'num_records': int(len(df)),
    'columns': df.columns.tolist(),
    'sample_5': df.head(5).to_dict(orient='records')
}
import json
print("__RESULT__:")
print(json.dumps(summary))"""

env_args = {'var_call_LhTd7FhVPoct9dTI7RhOOXAk': ['business', 'checkin'], 'var_call_sOWfkyzFYP4FkbOwQlzprD6m': ['review', 'tip', 'user'], 'var_call_9lcqa0C2p1ehoGhnkxLGVTmB': 'file_storage/call_9lcqa0C2p1ehoGhnkxLGVTmB.json', 'var_call_fgTMzoFPTAhXSsJn9tUNfzGG': 'file_storage/call_fgTMzoFPTAhXSsJn9tUNfzGG.json', 'var_call_Cs1diCURYKEvnbqzq9swjPv9': {'category': None, 'business_count': 0, 'average_rating': None}}

exec(code, env_args)
