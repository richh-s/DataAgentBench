code = """import pandas as pd
import json

with open(locals()['var_function-call-13415103741321583316'], 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)

# Convert citation_count to numeric, handling potential non-numeric values
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'], errors='coerce')

# Drop rows where citation_count is NaN after conversion
df_citations.dropna(subset=['citation_count'], inplace=True)


titles = df_citations['title'].tolist()

print('__RESULT__:')
print(json.dumps(titles))"""

env_args = {'var_function-call-13415103741321583316': 'file_storage/function-call-13415103741321583316.json'}

exec(code, env_args)
