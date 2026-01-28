code = """import json
import re

# Load full citations result
with open(var_call_VcWFdddNJ0SRgf5IMHml4JiL, 'r') as f:
    citations = json.load(f)

# Load full paper docs result
with open(var_call_3HqzeWRu2FsX9AYxZSPfgvfx, 'r') as f:
    papers = json.load(f)

# Build map from title to source by regex-searching for ACM in text
source_by_title = {}
for doc in papers:
    title = doc.get('filename', '').rsplit('.txt', 1)[0]
    text = doc.get('text', '')
    if not title:
        continue
    # Heuristic: if 'ACM' appears in the copyright/permission section, treat source as ACM
    if re.search(r'\bACM\b', text):
        source_by_title[title] = 'ACM'

# Filter citations for titles whose source is ACM
acm_counts = []
for row in citations:
    title = row.get('title')
    if not title:
        continue
    if source_by_title.get(title) == 'ACM':
        try:
            c = int(row.get('citation_count'))
        except (TypeError, ValueError):
            continue
        acm_counts.append(c)

avg = sum(acm_counts) / len(acm_counts) if acm_counts else None

result = {"average_citation_count_acm_2018": avg, "paper_count": len(acm_counts)}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_VcWFdddNJ0SRgf5IMHml4JiL': 'file_storage/call_VcWFdddNJ0SRgf5IMHml4JiL.json', 'var_call_QY1IA0Xl71JC5zMVsGBiz9U1': ['paper_docs'], 'var_call_3HqzeWRu2FsX9AYxZSPfgvfx': 'file_storage/call_3HqzeWRu2FsX9AYxZSPfgvfx.json'}

exec(code, env_args)
