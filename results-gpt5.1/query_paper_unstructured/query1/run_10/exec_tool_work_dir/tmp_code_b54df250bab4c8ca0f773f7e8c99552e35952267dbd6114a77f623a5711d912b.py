code = """import json, re, pandas as pd
from pathlib import Path

# Load full results
with open(var_call_otceoLVoVgJLM1MyBwZ9JFF0, 'r') as f:
    papers = json.load(f)
with open(var_call_OKHGyyzVQfhtJjXuwZPsgLMP, 'r') as f:
    citations = json.load(f)

# Identify food-domain papers via simple heuristic on text
food_titles = set()
for doc in papers:
    filename = doc.get('filename', '')
    title = re.sub(r"\.txt$", "", filename)
    text = doc.get('text', '').lower()
    if ' food ' in text or ' diet ' in text or ' dietary ' in text or ' eating ' in text or 'meal' in text:
        food_titles.add(title)

# Build DataFrame of citations
cf = pd.DataFrame(citations)
cf['citation_count'] = cf['citation_count'].astype(int)

# Filter to food titles (titles in DB match filenames without extension)
food_citations = cf[cf['title'].isin(food_titles)]

total_citations = int(food_citations['citation_count'].sum())

res = {"total_citation_count_food_domain": total_citations}

out = json.dumps(res)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_otceoLVoVgJLM1MyBwZ9JFF0': 'file_storage/call_otceoLVoVgJLM1MyBwZ9JFF0.json', 'var_call_OKHGyyzVQfhtJjXuwZPsgLMP': 'file_storage/call_OKHGyyzVQfhtJjXuwZPsgLMP.json'}

exec(code, env_args)
