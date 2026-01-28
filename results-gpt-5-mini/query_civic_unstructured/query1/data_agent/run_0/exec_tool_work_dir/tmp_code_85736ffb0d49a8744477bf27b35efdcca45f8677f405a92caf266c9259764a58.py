code = """import json
import re

def load_var(v):
    if isinstance(v, str):
        try:
            with open(v, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception:
            return v
    return v

funding = load_var(var_call_SdeIzpwHWXTGbiSgCGNZzY8M)
docs = load_var(var_call_fJ8zcOtfuMJb3QVTDXZxf5ZV)

fund_names = [rec.get('Project_Name','').strip() for rec in funding]

def normalize(s):
    s = s.lower()
    s = re.sub('[^a-z0-9]+', ' ', s)
    s = re.sub('\s+', ' ', s).strip()
    return s

norm_fund = [normalize(n) for n in fund_names]

titles = []
for doc in docs:
    text = doc.get('text','')
    lower = text.lower()
    marker = 'capital improvement projects (design)'
    i = lower.find(marker)
    if i == -1:
        continue
    # find end
    end1 = lower.find('capital improvement projects (construction)', i+1)
    end2 = lower.find('capital improvement projects (not started)', i+1)
    ends = [pos for pos in (end1, end2) if pos != -1]
    end = min(ends) if ends else None
    section = text[i+len(marker): end] if end else text[i+len(marker):]
    parts = section.split('\n\n')
    for p in parts:
        if not p or len(p.strip())<4:
            continue
        first_line = p.strip().splitlines()[0].strip()
        fl = first_line
        low = fl.lower()
        if any(k in low for k in ['updates', 'project schedule', 'estimated schedule', 'project description', 'project updates', 'page ']):
            continue
        # filter lines that are too long
        if len(fl) > 200:
            continue
        titles.append(fl)

# dedupe
seen = set()
unique_titles = []
for t in titles:
    nt = normalize(t)
    if nt in seen:
        continue
    seen.add(nt)
    unique_titles.append(t)

# matching
def tokens(s):
    return [w for w in normalize(s).split() if w]

matched = set()
for t in unique_titles:
    nt = normalize(t)
    ttoks = set(tokens(t))
    for fn, nfn in zip(fund_names, norm_fund):
        # direct substrings
        if nt == nfn or nt in nfn or nfn in nt:
            matched.add(fn)
            continue
        ftoks = set(tokens(fn))
        if not ttoks or not ftoks:
            continue
        inter = ttoks.intersection(ftoks)
        if len(inter) >= 1:
            # ratio relative to smaller
            ratio = len(inter) / float(min(len(ttoks), len(ftoks)))
            if ratio >= 0.6:
                matched.add(fn)

result_count = len(matched)

print("__RESULT__:")
print(json.dumps(result_count))"""

env_args = {'var_call_SdeIzpwHWXTGbiSgCGNZzY8M': 'file_storage/call_SdeIzpwHWXTGbiSgCGNZzY8M.json', 'var_call_fJ8zcOtfuMJb3QVTDXZxf5ZV': 'file_storage/call_fJ8zcOtfuMJb3QVTDXZxf5ZV.json'}

exec(code, env_args)
