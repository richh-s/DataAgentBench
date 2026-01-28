code = """import json
import re

# Load data files from storage
with open(var_call_IgMGRy82fd6CM3YSp579uesP, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_bj5IIhfHCAcIpURljX3hdbZG, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Normalize title
def normalize_title(t):
    if t is None:
        return ''
    s = str(t).strip()
    s = re.sub(r"^[\"']+|[\"']+$", '', s)
    s = re.sub(r"\s+", ' ', s)
    return s.lower()

# Check if doc is 2016 and contains physical activity
def doc_is_2016_pa(doc):
    text = doc.get('text', '')
    if not isinstance(text, str):
        return False
    if '2016' not in text:
        return False
    if re.search(r'physical activity', text, re.I):
        # check that 2016 appears near top (first 1500 chars)
        header = text[:1500]
        if '2016' in header:
            return True
    return False

# Build map from normalized title to total_citations
cit_map = {}
for rec in citations:
    t = rec.get('title')
    tot = rec.get('total_citations')
    try:
        tot_i = int(tot)
    except Exception:
        tot_i = 0
    cit_map[normalize_title(t)] = tot_i

# Find matching docs
results = []
for doc in docs:
    if not doc_is_2016_pa(doc):
        continue
    filename = doc.get('filename','')
    title = re.sub(r'\.txt$', '', filename)
    norm = normalize_title(title)
    total = cit_map.get(norm, 0)
    results.append({'title': title, 'total_citations': total})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_call_GCr1zw7xx9xk1G0vBAUywNW4': ['paper_docs'], 'var_call_IgMGRy82fd6CM3YSp579uesP': 'file_storage/call_IgMGRy82fd6CM3YSp579uesP.json', 'var_call_fbCH73ERsJiR8V8GgNikjxAJ': ['Citations', 'sqlite_sequence'], 'var_call_bj5IIhfHCAcIpURljX3hdbZG': 'file_storage/call_bj5IIhfHCAcIpURljX3hdbZG.json'}

exec(code, env_args)
