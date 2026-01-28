code = """import json, re, pandas as pd
from pathlib import Path

# Load full citations aggregation
path = Path(var_call_asorXN4ntJuiv0JQNNYWRVhG)
with path.open() as f:
    citations = json.load(f)

# Get candidate titles potentially in physical activity domain based on title keywords
pa_keywords = ['physical activity', 'activity', 'exercise', 'fitness', 'sedentary', 'walk', 'walking', 'running']

pa_titles = []
for row in citations:
    title = row['title']
    lt = title.lower()
    if any(k in lt for k in pa_keywords):
        pa_titles.append(title)

result = sorted(list(set(pa_titles)))

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_qNA1tdFUSzXCSy7o31tevlkI': 'file_storage/call_qNA1tdFUSzXCSy7o31tevlkI.json', 'var_call_zJwPKjsyq2sA33K6gjp7r1ed': ['Citations', 'sqlite_sequence'], 'var_call_asorXN4ntJuiv0JQNNYWRVhG': 'file_storage/call_asorXN4ntJuiv0JQNNYWRVhG.json'}

exec(code, env_args)
