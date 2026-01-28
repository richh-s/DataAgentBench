code = """import json
# Load civic docs
path_docs = var_call_WQOnz4h2kKRYxFLRC3s88Esu
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)
# Load funding records
path_fund = var_call_CFKJoBPrTGwuRxwH2jrhFHYg
with open(path_fund, 'r', encoding='utf-8') as f:
    funds = json.load(f)

# Find candidate project titles by locating 'spring' near '2022'
candidates = set()
for doc in docs:
    text = doc.get('text', '')
    low = text.lower()
    start = 0
    while True:
        i = low.find('spring', start)
        if i == -1:
            break
        window_start = max(0, i-200)
        window_end = min(len(low), i+200)
        window = low[window_start:window_end]
        if '2022' in window:
            prev = text[window_start:i]
            lines = prev.strip().splitlines()
            if lines:
                cand = lines[-1].strip()
                if 3 < len(cand) < 200:
                    candidates.add(cand)
        start = i + 6

# Also look for March/April/May with 2022
months = ['march', 'april', 'may']
for doc in docs:
    text = doc.get('text', '')
    low = text.lower()
    for m in months:
        start = 0
        while True:
            i = low.find(m, start)
            if i == -1:
                break
            window_start = max(0, i-200)
            window_end = min(len(low), i+200)
            window = low[window_start:window_end]
            if '2022' in window:
                prev = text[window_start:i]
                lines = prev.strip().splitlines()
                if lines:
                    cand = lines[-1].strip()
                    if 3 < len(cand) < 200:
                        candidates.add(cand)
            start = i + len(m)

# Simple normalization: lowercase, remove parentheses and punctuation
import string
trans_table = str.maketrans('', '', string.punctuation.replace("&", ""))
# keep ampersand if present

def normalize(name):
    if not name:
        return ''
    s = name.lower().strip()
    s = s.replace('(', ' ').replace(')', ' ')
    s = s.translate(trans_table)
    s = ' '.join(s.split())
    return s

norm_candidates = {normalize(c): c for c in candidates if normalize(c)}

# Prepare funding map
fund_map = {}
for r in funds:
    pname = r.get('Project_Name')
    amt = r.get('Amount')
    try:
        amt_i = int(amt)
    except:
        try:
            amt_i = int(float(amt))
        except:
            amt_i = 0
    fund_map[pname] = amt_i

# Match normalized candidates to funding project names by containment
matched = set()
for nc, orig in norm_candidates.items():
    for pname in fund_map:
        pn = normalize(pname)
        if nc and (nc in pn or pn in nc):
            matched.add(pname)
# Also try exact orig match
for nc, orig in norm_candidates.items():
    for pname in fund_map:
        if orig.lower() == pname.lower():
            matched.add(pname)

# Sum funding
total = sum(fund_map[p] for p in matched)
result = {'count': len(matched), 'total_funding': total, 'matched_projects': sorted(list(matched))}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_hSIn0HXpIysBJLncOq2LulYt': ['civic_docs'], 'var_call_6f74mMKpIuCBNIwpLg5yIUV5': ['Funding'], 'var_call_WQOnz4h2kKRYxFLRC3s88Esu': 'file_storage/call_WQOnz4h2kKRYxFLRC3s88Esu.json', 'var_call_CFKJoBPrTGwuRxwH2jrhFHYg': 'file_storage/call_CFKJoBPrTGwuRxwH2jrhFHYg.json'}

exec(code, env_args)
