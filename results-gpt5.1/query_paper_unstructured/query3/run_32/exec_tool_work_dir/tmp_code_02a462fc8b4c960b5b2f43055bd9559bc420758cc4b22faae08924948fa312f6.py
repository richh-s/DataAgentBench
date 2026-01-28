code = """import json, pandas as pd

with open(var_call_AUmVEBi7PU2wgq9QWaLuLDJY, 'r') as f:
    citations = json.load(f)

cites_df = pd.DataFrame(citations)
cols = list(cites_df.columns)
preview = cites_df.head(3).to_dict(orient='records')

import json as _j
out = _j.dumps({'columns': cols, 'preview': preview})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_oP8Jo2y8WWNNIfSuV5jJQzLi': 'file_storage/call_oP8Jo2y8WWNNIfSuV5jJQzLi.json', 'var_call_AUmVEBi7PU2wgq9QWaLuLDJY': 'file_storage/call_AUmVEBi7PU2wgq9QWaLuLDJY.json', 'var_call_NIR8Urddo7TNHvvT1Oos0USW': {'paper_keys': ['_id', 'filename', 'text'], 'citation_sample': {'title': '"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'total_citations': '53'}}}

exec(code, env_args)
