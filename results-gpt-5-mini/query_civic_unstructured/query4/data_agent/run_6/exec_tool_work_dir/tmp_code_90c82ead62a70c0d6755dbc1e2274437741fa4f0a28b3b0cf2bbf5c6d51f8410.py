code = """import json, re, string
# Load civic docs
path_docs = var_call_WQOnz4h2kKRYxFLRC3s88Esu
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)
# Load funding
path_fund = var_call_CFKJoBPrTGwuRxwH2jrhFHYg
with open(path_fund, 'r', encoding='utf-8') as f:
    funds = json.load(f)

# normalization
trans_table = str.maketrans('', '', string.punctuation.replace('&',''))

def normalize(name):
    if not name:
        return ''
    s = name.lower().strip()
    s = re.sub(r"\([^)]*\)", "", s)
    s = s.translate(trans_table)
    s = ' '.join(s.split())
    return s

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

candidates = set()
# patterns to find spring 2022 occurrences
for doc in docs:
    text = doc.get('text','')
    low = text.lower()
    # find 'spring' with '2022' within 100 chars
    for m in re.finditer(r'spring', low):
        i = m.start()
        window_start = max(0, i-300)
        window_end = min(len(low), i+300)
        window = low[window_start:window_end]
        if '2022' in window:
            # search backwards for a project title line
            before = text[window_start:i]
            # split into lines and scan backwards for a candidate title
            lines = before.splitlines()
            for ln in reversed(lines[-10:]):
                ln_strip = ln.strip()
                if not ln_strip:
                    continue
                # accept lines that contain 'project' or appear title-like (capitalized start and not long)
                if re.search(r'project', ln_strip, re.I) or (len(ln_strip) < 120 and re.match(r'[A-Z0-9][A-Za-z0-9 \-\&\,\']+', ln_strip)):
                    candidates.add(ln_strip)
                    break
    # also check months March/April/May with 2022
    for month in ('march','april','may'):
        for m in re.finditer(month, low):
            i = m.start()
            window_start = max(0, i-300)
            window_end = min(len(low), i+300)
            window = low[window_start:window_end]
            if '2022' in window:
                before = text[window_start:i]
                lines = before.splitlines()
                for ln in reversed(lines[-10:]):
                    ln_strip = ln.strip()
                    if not ln_strip:
                        continue
                    if re.search(r'project', ln_strip, re.I) or (len(ln_strip) < 120 and re.match(r'[A-Z0-9][A-Za-z0-9 \-\&\,\']+', ln_strip)):
                        candidates.add(ln_strip)
                        break

# Also search for patterns like 'Begin Construction: Spring 2022' explicitly and capture nearby title
for doc in docs:
    text = doc.get('text','')
    for m in re.finditer(r'(begin construction|advertise|complete design|complete construction|project schedule|estimated schedule)[^\n]{0,120}spring[^\n]{0,40}2022', text, flags=re.I):
        i = m.start()
        window_start = max(0, i-400)
        before = text[window_start:i]
        lines = before.splitlines()
        for ln in reversed(lines[-12:]):
            ln_strip = ln.strip()
            if not ln_strip:
                continue
            if re.search(r'project', ln_strip, re.I) or (len(ln_strip) < 120 and re.match(r'[A-Z0-9][A-Za-z0-9 \-\&\,\']+', ln_strip)):
                candidates.add(ln_strip)
                break

# Normalize candidates and try matching to funding project names
norm_to_candidate = {normalize(c): c for c in candidates if normalize(c)}
matched = set()
for norm_c, orig_c in norm_to_candidate.items():
    for pname, info in fund_map.items():
        pn = info['norm']
        if not pn:
            continue
        # match if one contains the other or shares key tokens
        if norm_c in pn or pn in norm_c:
            matched.add(pname)
        else:
            # token overlap
            tokens_c = set(norm_c.split())
            tokens_p = set(pn.split())
            if tokens_c and tokens_p and len(tokens_c & tokens_p) >= 2:
                matched.add(pname)

# Compute totals
total = sum(fund_map[p]['amount'] for p in matched)
result = {'count': len(matched), 'total_funding': total, 'matched_projects': sorted(list(matched)), 'candidates_found': sorted(list(candidates))}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_hSIn0HXpIysBJLncOq2LulYt': ['civic_docs'], 'var_call_6f74mMKpIuCBNIwpLg5yIUV5': ['Funding'], 'var_call_WQOnz4h2kKRYxFLRC3s88Esu': 'file_storage/call_WQOnz4h2kKRYxFLRC3s88Esu.json', 'var_call_CFKJoBPrTGwuRxwH2jrhFHYg': 'file_storage/call_CFKJoBPrTGwuRxwH2jrhFHYg.json', 'var_call_QN6PkRR8DLD6lgf3UJRkFZMD': {'count': 0, 'total_funding': 0, 'matched_projects': []}}

exec(code, env_args)
