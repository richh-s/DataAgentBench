code = """import json, re, pandas as pd
from pathlib import Path

# Load full results
papers_path = Path(var_call_DNIBEPA1QybII4nOcxAjYBPX)
with open(papers_path, 'r') as f:
    papers = json.load(f)

cites_path = Path(var_call_9g8hSlNN2f2UmgNuBoMpPOd1)
with open(cites_path, 'r') as f:
    citations = json.load(f)

# Extract title from filename (remove .txt)
for p in papers:
    fn = p.get('filename','')
    title = re.sub(r"\.txt$", "", fn)
    p['title'] = title

# Identify food-domain papers: use simple heuristic based on text mentioning food/meal/eating/diet
food_keywords = re.compile(r"\b(food|eating|diet|meal|nutrition)\b", re.IGNORECASE)
food_titles = {p['title'] for p in papers if food_keywords.search(p.get('text',''))}

# Sum citations for those titles
total = 0
for row in citations:
    if row['title'] in food_titles:
        try:
            total += int(row.get('citation_count',0))
        except ValueError:
            pass

result = total

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_DNIBEPA1QybII4nOcxAjYBPX': 'file_storage/call_DNIBEPA1QybII4nOcxAjYBPX.json', 'var_call_9g8hSlNN2f2UmgNuBoMpPOd1': 'file_storage/call_9g8hSlNN2f2UmgNuBoMpPOd1.json'}

exec(code, env_args)
