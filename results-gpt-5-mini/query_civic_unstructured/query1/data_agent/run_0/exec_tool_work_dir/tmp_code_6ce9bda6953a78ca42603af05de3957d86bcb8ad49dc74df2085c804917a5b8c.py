code = """import json
import re
import string

# Load stored results
with open(var_call_SdeIzpwHWXTGbiSgCGNZzY8M, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(var_call_fJ8zcOtfuMJb3QVTDXZxf5ZV, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Helper normalize
trans = str.maketrans(string.punctuation, ' ' * len(string.punctuation))

def normalize(s):
    if s is None:
        return ''
    s = s.lower()
    s = s.translate(trans)
    s = re.sub(r"\s+", ' ', s).strip()
    return s

# Extract titles from Capital Improvement Projects (Design) sections
title_set = []
for doc in docs:
    text = doc.get('text', '')
    lower = text.lower()
    marker = 'capital improvement projects (design)'
    idx = lower.find(marker)
    if idx == -1:
        continue
    # find end of section
    end_markers = ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'capital improvement projects (construction)']
    end_idx = None
    for em in end_markers:
        j = lower.find(em, idx+1)
        if j != -1 and (end_idx is None or j < end_idx):
            end_idx = j
    section = text[idx + len(marker): end_idx] if end_idx else text[idx + len(marker):]
    # split into chunks by two or more newlines
    chunks = re.split(r"\n\s*\n", section)
    for ch in chunks:
        ch = ch.strip()
        if not ch:
            continue
        # take first non-empty line as candidate title
        lines = [ln.strip() for ln in ch.splitlines() if ln.strip()]
        if not lines:
            continue
        cand = lines[0]
        # filter out lines that are clearly not titles
        low = cand.lower()
        if len(cand) < 4 or len(cand) > 200:
            continue
        if any(k in low for k in ['updates', 'project schedule', 'advertise', 'begin construction', 'page ', 'agenda item', 'recommended action', 'discussion']):
            continue
        # remove leading bullets or numbering
        cand = re.sub(r'^[\-\d\.)\s]+', '', cand)
        if cand and normalize(cand) not in [normalize(t) for t in title_set]:
            title_set.append(cand)

# Deduplicate normalized
uniq_titles = []
seen = set()
for t in title_set:
    n = normalize(t)
    if n in seen:
        continue
    seen.add(n)
    uniq_titles.append(t)

# Prepare funding list (already filtered by Amount > 50000 from earlier query)
fund_projects = []
for rec in funding:
    pname = rec.get('Project_Name', '')
    amt = rec.get('Amount', '')
    # ensure numeric
    try:
        a = int(str(amt))
    except:
        try:
            a = int(float(str(amt)))
        except:
            a = 0
    if a <= 50000:
        continue
    fund_projects.append(pname)

# Matching between titles and funding project names
matched_norms = set()
matched_pairs = []

# helper tokens
def tokens(s):
    return [w for w in normalize(s).split() if w]

for fname in fund_projects:
    # consider base name without parentheses
    base = fname.split('(')[0].strip()
    nbase = normalize(base)
    nf = normalize(fname)
    f_tokens = set(tokens(fname))
    matched = False
    for title in uniq_titles:
        nt = normalize(title)
        t_tokens = set(tokens(title))
        # direct containment
        if nt and (nt in nf or nf in nt):
            matched = True
        # base containment
        if not matched and nbase and (nbase in nt or nt in nbase):
            matched = True
        # token overlap
        if not matched and t_tokens and f_tokens:
            inter = t_tokens.intersection(f_tokens)
            if inter:
                ratio = len(inter) / float(min(len(t_tokens), len(f_tokens)))
                if ratio >= 0.6:
                    matched = True
        if matched:
            matched_norms.add(nbase)
            matched_pairs.append((fname, title))
            break

result_count = len(matched_norms)

print("__RESULT__:")
print(json.dumps(result_count))"""

env_args = {'var_call_SdeIzpwHWXTGbiSgCGNZzY8M': 'file_storage/call_SdeIzpwHWXTGbiSgCGNZzY8M.json', 'var_call_fJ8zcOtfuMJb3QVTDXZxf5ZV': 'file_storage/call_fJ8zcOtfuMJb3QVTDXZxf5ZV.json', 'var_call_IP5GqWbgBMXPgqtaW3fnctqw': {'fund_len': 276, 'docs_len': 5}}

exec(code, env_args)
