code = """import json
import re
# Load data from storage file paths provided by previous tool calls
with open(var_call_VOysvHNujVd5wBjWAIXEWXNV, 'r', encoding='utf-8') as f:
    papers = json.load(f)
with open(var_call_ehI73dv3V43Z57SHMmCZK6TB, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Build mapping from paper title (filename without .txt) to text
paper_text = {}
for doc in papers:
    filename = doc.get('filename', '')
    title = filename[:-4] if filename.lower().endswith('.txt') else filename
    paper_text[title] = doc.get('text', '') or ''

# Identify food-domain papers by searching for the word 'food' in the text (case-insensitive)
food_titles = set()
pattern = re.compile(r"\bfood\b", flags=re.IGNORECASE)
for title, text in paper_text.items():
    if pattern.search(text):
        food_titles.add(title)

# Aggregate citation counts by title from citations records
from collections import defaultdict
cit_counts = defaultdict(int)
for rec in citations:
    t = rec.get('title')
    # some citation_count values may be strings; convert safely
    try:
        c = int(rec.get('citation_count') or 0)
    except:
        # try float then int
        try:
            c = int(float(rec.get('citation_count')))
        except:
            c = 0
    if t is not None:
        cit_counts[t] += c

# Sum citations for titles that are in food_titles
paper_counts = []
total = 0
for title in sorted(food_titles):
    c = cit_counts.get(title, 0)
    total += c
    paper_counts.append({"title": title, "citations": c})

# Prepare result
result = {"total_citations": total, "papers": paper_counts}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_VOysvHNujVd5wBjWAIXEWXNV': 'file_storage/call_VOysvHNujVd5wBjWAIXEWXNV.json', 'var_call_ehI73dv3V43Z57SHMmCZK6TB': 'file_storage/call_ehI73dv3V43Z57SHMmCZK6TB.json'}

exec(code, env_args)
