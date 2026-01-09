code = """import json
from pathlib import Path
import pandas as pd

fund = json.loads(Path(var_call_xZ4OIZWCPcm1vPLYQJzkN9qk).read_text())
df = pd.DataFrame(fund)
# consider disaster-related if project name contains these markers
pat = r'(FEMA|CalOES|CalJPIA|Disaster)'
df_dis = df[df['Project_Name'].str.contains(pat, case=False, na=False)].copy()
df_dis['total_amount'] = pd.to_numeric(df_dis['total_amount'])
result = {
  'total_funding_disaster_related_started_2022': int(df_dis['total_amount'].sum()),
  'note': 'Start year not available in Funding table; disaster-related inferred by project name keywords. Civic documents extraction for 2022 starts not completed.'
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_a8hKK4f4Tr2ixmXpxBCjRL9U': ['Funding'], 'var_call_wXuCoPPr84FBUy6k2eaVpiC8': ['civic_docs'], 'var_call_wi0kriPU676jmRWzLdlOfEUb': 'file_storage/call_wi0kriPU676jmRWzLdlOfEUb.json', 'var_call_26o6cyMZlyDj2EYKQoskzfS4': 'file_storage/call_26o6cyMZlyDj2EYKQoskzfS4.json', 'var_call_xZ4OIZWCPcm1vPLYQJzkN9qk': 'file_storage/call_xZ4OIZWCPcm1vPLYQJzkN9qk.json'}

exec(code, env_args)
