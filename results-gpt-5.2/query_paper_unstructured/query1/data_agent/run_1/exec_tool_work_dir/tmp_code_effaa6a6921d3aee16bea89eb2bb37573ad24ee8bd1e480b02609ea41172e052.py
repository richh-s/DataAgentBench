code = """import json, pandas as pd, re

# Load citations per title (already aggregated)
path = var_call_YUV2LW3WLUK3uO84M00LRg3n
with open(path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

df_cit = pd.DataFrame(citations)
df_cit['total_citations'] = pd.to_numeric(df_cit['total_citations'], errors='coerce').fillna(0).astype(int)

# Determine food-domain papers by scanning Mongo docs for explicit domain tag
# Pull all docs (only filename+text) and parse domain line(s)
# If dataset is large, we will query in chunks is not supported; so we do a broad pull with projection.

# Since previous mongo query with domain:food returned none, assume domain info is encoded as e.g. 'Domains: ...' 'domain: [..]'
# We'll load all documents and parse for a domain field pattern.

print('__RESULT__:')
print(json.dumps({'status':'need_all_docs'}))"""

env_args = {'var_call_YUV2LW3WLUK3uO84M00LRg3n': 'file_storage/call_YUV2LW3WLUK3uO84M00LRg3n.json', 'var_call_D4EDiQmMZPjXOaSjl0wlvwD2': [], 'var_call_Y9GVsLxZtGNwIT0I1DqhejHX': 'file_storage/call_Y9GVsLxZtGNwIT0I1DqhejHX.json'}

exec(code, env_args)
