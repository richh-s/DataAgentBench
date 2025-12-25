code = """import json, pandas as pd, re

pub_path = var_call_rsLR4inHjlZynKAipYdpmjRT
with open(pub_path, 'r') as f:
    pub_data = json.load(f)

pub_df = pd.DataFrame(pub_data)

# quick inspect
import json as _json
out = _json.dumps({'columns': list(pub_df.columns), 'sample': pub_df.head(2).to_dict(orient='records')})
print("__RESULT__:")
print(out)"""

env_args = {'var_call_rsLR4inHjlZynKAipYdpmjRT': 'file_storage/call_rsLR4inHjlZynKAipYdpmjRT.json', 'var_call_aIEDwcrdwiNPeICQgcADbBR0': 'file_storage/call_aIEDwcrdwiNPeICQgcADbBR0.json', 'var_call_Wv3EauzuDayJeCTsVQKuglM4': ['symbol', 'level'], 'var_call_Gajww71rm9Y62hldEHFbtnDu': {'columns': ['symbol', 'level'], 'sample': [{'symbol': 'A41D', 'level': '5.0'}, {'symbol': 'A41C', 'level': '5.0'}, {'symbol': 'A41H', 'level': '5.0'}, {'symbol': 'A42B', 'level': '5.0'}, {'symbol': 'A42C', 'level': '5.0'}]}}

exec(code, env_args)
