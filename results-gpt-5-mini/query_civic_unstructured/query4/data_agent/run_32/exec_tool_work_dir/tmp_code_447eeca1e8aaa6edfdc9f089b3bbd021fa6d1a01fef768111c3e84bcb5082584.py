code = """import json, re
# Load files
with open(var_call_GkmSDQTPWl4imroM1mEpmbPM, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_hmbQbJAU5DGjdddo8bqvJ75p, 'r') as f:
    funding = json.load(f)

def normalize_name(name):
    if not name:
        return ''
    s = name.lower()
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

funding_records = []
for r in funding:
    pname = r.get('Project_Name')
    amt = r.get('Amount')
    try:
        amt_val = int(str(amt))
    except:
        try:
            amt_val = int(float(str(amt)))
        except:
            amt_val = 0
    funding_records.append({'orig_name': pname, 'norm_name': normalize_name(pname), 'amount': amt_val})

funding_names = set(x['norm_name'] for x in funding_records if x['norm_name'])

# prepare docs
docs = []
for d in civic_docs:
    txt = d.get('text','')
    docs.append({'filename': d.get('filename'), 'text': txt, 'text_norm': txt.lower()})

spring_months = ['march','mar','april','apr','may']

def spring2022_in_text(t):
    t = t.lower()
    if 'spring' in t and '2022' in t:
        return True
    if '2022' in t and any(m in t for m in spring_months):
        return True
    if re.search(r'2022[-/]0?3', t) or re.search(r'2022[-/]0?4', t) or re.search(r'2022[-/]0?5', t):
        return True
    return False

found = set()
for fn in funding_names:
    if not fn:
        continue
    for doc in docs:
        if fn in doc['text_norm']:
            # check surrounding window
            idx = doc['text_norm'].find(fn)
            start = max(0, idx-300)
            end = min(len(doc['text_norm']), idx+300)
            if spring2022_in_text(doc['text_norm'][start:end]):
                found.add(fn)
                break
        else:
            # try to find indicators like "begin construction" near project name words
            words = fn.split()
            if not words:
                continue
            # search for occurrences of first word
            pos = doc['text_norm'].find(words[0])
            if pos!=-1:
                start = max(0, pos-300)
                end = min(len(doc['text_norm']), pos+300)
                window = doc['text_norm'][start:end]
                if spring2022_in_text(window) and all(w in window for w in words[:4]):
                    found.add(fn)
                    break

# also scan docs for explicit "Begin Construction" or similar with spring 2022 and capture preceding title-like lines
for doc in docs:
    text = doc['text']
    low = doc['text_norm']
    for m in re.finditer(r'(begin construction|advertise|complete design|project schedule)', low):
        start = max(0, m.start()-400)
        window = low[start:m.end()+200]
        if spring2022_in_text(window):
            # extract a candidate title before this
            snippet = text[max(0, m.start()-400):m.start()]
            lines = [ln.strip() for ln in snippet.splitlines() if ln.strip()]
            if lines:
                cand = lines[-1]
                norm = normalize_name(cand)
                if norm and norm in funding_names:
                    found.add(norm)

# compute totals
matched_records = [r for r in funding_records if r['norm_name'] in found]
count = len(found)
total = sum(r['amount'] for r in matched_records)

# prepare details mapping
details = {}
for r in matched_records:
    details.setdefault(r['norm_name'], []).append({'orig_name': r['orig_name'], 'amount': r['amount']})

res = {'count': count, 'total_funding': total, 'projects_normalized': sorted(list(found)), 'projects_details': details}

print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_call_9HODkiC8wjfGKJrxlQ5AIKcj': ['civic_docs'], 'var_call_ECY4K9fE4JT46s2M7ZcBZ68U': ['Funding'], 'var_call_GkmSDQTPWl4imroM1mEpmbPM': 'file_storage/call_GkmSDQTPWl4imroM1mEpmbPM.json', 'var_call_hmbQbJAU5DGjdddo8bqvJ75p': 'file_storage/call_hmbQbJAU5DGjdddo8bqvJ75p.json'}

exec(code, env_args)
