code = """import json
import pandas as pd

path = var_call_PWlzJWbFK6Uq6ImdMzHSOCWD
with open(path, 'r', encoding='utf-8') as f:
    citations = json.load(f)

df = pd.DataFrame(citations)
df['citation_count'] = pd.to_numeric(df['citation_count'], errors='coerce').fillna(0).astype(int)

# Cannot reliably identify 'food' domain papers from docs (no domain labels found).
# Return explanation payload.
out = {
  'error': 'Food domain labels not found in paper_docs; unable to compute total citation count for food domain with available data.',
  'note': 'A regex search for explicit domain tags (e.g., "domain: food") returned 0 documents; a broader search for "food" finds mentions but does not indicate domain.'
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_PWlzJWbFK6Uq6ImdMzHSOCWD': 'file_storage/call_PWlzJWbFK6Uq6ImdMzHSOCWD.json', 'var_call_2fEa5cABVigGalzcOhezYFWK': [], 'var_call_Ur4y8kVTPHCCgldYqXDgvko7': 'file_storage/call_Ur4y8kVTPHCCgldYqXDgvko7.json'}

exec(code, env_args)
