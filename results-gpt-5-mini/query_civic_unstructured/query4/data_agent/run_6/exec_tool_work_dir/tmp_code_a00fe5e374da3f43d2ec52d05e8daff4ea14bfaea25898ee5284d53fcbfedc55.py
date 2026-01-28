code = """import json, re, string
# Load civic docs
path_docs = var_call_WQOnz4h2kKRYxFLRC3s88Esu
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)
# Load funding
path_fund = var_call_CFKJoBPrTGwuRxwH2jrhFHYg
with open(path_fund, 'r', encoding='utf-8') as f:
    funds = json.load(f)

keywords = ['project','repair','improvements','improvement','study','plan','park','water','road','drain','playground','slope','resurfacing','repair','repairs']

candidates = set()
for doc in docs:
    text = doc.get('text','')
    lines = text.splitlines()
    n = len(lines)
    low_lines = [ln.lower() for ln in lines]
    # window forward check: if a candidate line is followed by a line/window containing spring and 2022 or month+2022
    for i, ln in enumerate(lines):
        ln_low = low_lines[i]
        window = ' '.join(low_lines[i:i+7])
        if ('spring' in window and '2022' in window) or any((m in window and '2022' in window) for m in ('march','april','may')):
            # if the line itself looks like a project title or contains keywords
            if any(k in ln_low for k in keywords) or len(ln.strip())>0:
                # prefer lines that contain keywords; otherwise look back a bit for a keyword line
                if any(k in ln_low for k in keywords):
                    candidates.add(lines[i].strip())
                else:
                    # search backward up to 6 lines for keyword
                    found = False
                    for j in range(max(0,i-6), i):
                        if any(k in low_lines[j] for k in keywords):
                            candidates.add(lines[j].strip())
                            found = True
                            break
                    if not found:
                        candidates.add(lines[i].strip())
    # backward check: if a line mentions spring and 2022, find previous keyword line
    for i, ln in enumerate(lines):
        ln_low = low_lines[i]
        if 'spring' in ln_low and '2022' in ln_low:
            for j in range(max(0,i-6), i)[::-1]:
                if any(k in low_lines[j] for k in keywords):
                    candidates.add(lines[j].strip())
                    break
        for m in ('march','april','may'):
            if m in ln_low and '2022' in ln_low:
                for j in range(max(0,i-6), i)[::-1]:
                    if any(k in low_lines[j] for k in keywords):
                        candidates.add(lines[j].strip())
                        break

# normalization function
punct = string.punctuation
trans = str.maketrans('', '', punct)

def normalize(s):
    if not s:
        return ''
    s2 = s.lower()
    # remove parenthetical content
    s2 = re.sub(r"\([^)]*\)", "", s2)
    # remove punctuation
    s2 = s2.translate(trans)
    s2 = ' '.join(s2.split())
    return s2

# prepare funding map
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
    fund_map[pname] = {'norm': normalize(pname), 'amount': amt_i}

# normalize candidates
norm_candidates = {normalize(c): c for c in candidates if normalize(c)}

matched = set()
for nc, orig in norm_candidates.items():
    nc_tokens = set(nc.split())
    for pname, info in fund_map.items():
        pn = info['norm']
        if not pn:
            continue
        # substring match
        if nc in pn or pn in nc:
            matched.add(pname)
            continue
        # token overlap
        pn_tokens = set(pn.split())
        if len(nc_tokens & pn_tokens) >= 2:
            matched.add(pname)

# compute totals
total = sum(fund_map[p]['amount'] for p in matched)
result = {'count': len(matched), 'total_funding': total, 'matched_projects': sorted(list(matched)), 'candidates': sorted(list(candidates))}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_hSIn0HXpIysBJLncOq2LulYt': ['civic_docs'], 'var_call_6f74mMKpIuCBNIwpLg5yIUV5': ['Funding'], 'var_call_WQOnz4h2kKRYxFLRC3s88Esu': 'file_storage/call_WQOnz4h2kKRYxFLRC3s88Esu.json', 'var_call_CFKJoBPrTGwuRxwH2jrhFHYg': 'file_storage/call_CFKJoBPrTGwuRxwH2jrhFHYg.json', 'var_call_QN6PkRR8DLD6lgf3UJRkFZMD': {'count': 0, 'total_funding': 0, 'matched_projects': []}}

exec(code, env_args)
