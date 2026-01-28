code = """import json
import re

# helper to load storage vars (which may be file paths)
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

# Get funding project names (records already filtered Amount > 50000)
fund_names = [rec.get('Project_Name','').strip() for rec in funding]

# normalization
def normalize(s):
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

norm_fund = [normalize(n) for n in fund_names]

# Extract titles from Capital Improvement Projects (Design) section
titles = []
for doc in docs:
    text = doc.get('text','')
    lower = text.lower()
    marker = 'capital improvement projects (design)'
    i = lower.find(marker)
    if i == -1:
        continue
    # find end of section
    end_markers = ['capital improvement projects (construction)', 'capital improvement projects (not started)']
    j = None
    for em in end_markers:
        k = lower.find(em, i+1)
        if k != -1 and (j is None or k < j):
            j = k
    section = text[i+len(marker): j] if j else text[i+len(marker):]
    # Split by double newlines
    parts = [p.strip() for p in re.split(r'\n\s*\n', section) if p.strip()]
    for p in parts:
        # skip if includes known headers
        lowp = p.lower()
        if any(h in lowp for h in ['updates:', 'project schedule', 'estimated schedule', 'project description', 'project updates']):
            # take the line(s) before these markers as potential title
            # find position of marker
            for marker2 in ['updates:', 'project schedule', 'estimated schedule', 'project description', 'project updates']:
                pos = lowp.find(marker2)
                if pos != -1:
                    candidate = p[:pos].strip()
                    # take last non-empty line
                    lines = [ln.strip() for ln in candidate.splitlines() if ln.strip()]
                    if lines:
                        titles.append(lines[-1])
                    break
            continue
        # otherwise, first line might be a title
        first_line = p.splitlines()[0].strip()
        # filter out lines that are too short or look like page markers
        if len(first_line) >= 4 and not re.match(r'page \d+ of', first_line.lower()):
            titles.append(first_line)

# dedupe titles
seen = set()
unique_titles = []
for t in titles:
    ts = t.strip()
    if not ts:
        continue
    key = normalize(ts)
    if key in seen:
        continue
    seen.add(key)
    unique_titles.append(ts)

# match titles to funding names by normalization and token overlap

def tokens(s):
    return [w for w in normalize(s).split() if w]

matched = set()
for t in unique_titles:
    nt = normalize(t)
    ttoks = set(tokens(t))
    for fn, nfn in zip(fund_names, norm_fund):
        # direct normalized equality or substring
        if nt == nfn or nt in nfn or nfn in nt:
            matched.add(fn)
            continue
        # token overlap
        ftoks = set(tokens(fn))
        if not ttoks or not ftoks:
            continue
        inter = ttoks.intersection(ftoks)
        ratio = len(inter) / min(len(ttoks), len(ftoks))
        if ratio >= 0.6:
            matched.add(fn)

result_count = len(matched)

print("__RESULT__:")
print(json.dumps(result_count))"""

env_args = {'var_call_SdeIzpwHWXTGbiSgCGNZzY8M': 'file_storage/call_SdeIzpwHWXTGbiSgCGNZzY8M.json', 'var_call_fJ8zcOtfuMJb3QVTDXZxf5ZV': 'file_storage/call_fJ8zcOtfuMJb3QVTDXZxf5ZV.json'}

exec(code, env_args)
