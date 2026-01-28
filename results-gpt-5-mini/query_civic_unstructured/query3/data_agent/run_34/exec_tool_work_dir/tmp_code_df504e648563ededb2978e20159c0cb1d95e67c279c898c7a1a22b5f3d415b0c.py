code = """import json, re

# Load stored results
with open(var_call_RpKhjqFTVlsT3xmU5phuCvLx, 'r') as f:
    funding = json.load(f)
with open(var_call_OTsZFSddYbanLEHhV1oqAEar, 'r') as f:
    civic_docs = json.load(f)

# Combine all civic texts
texts = []
for d in civic_docs:
    t = d.get('text','')
    if t:
        texts.append(t)
full_text = "\n".join(texts)
full_text_low = full_text.lower()

# Find candidate project titles by locating 'fema' or 'emergency' or 'outdoor warning' or 'sirens'
candidates = set()
for keyword in ['fema', 'emergency', 'outdoor warning', 'sirens']:
    start = 0
    while True:
        idx = full_text_low.find(keyword, start)
        if idx == -1:
            break
        # get a window before the match and extract previous non-empty line as title candidate
        before = full_text[:idx]
        lines = before.splitlines()
        # scan backwards to find a plausible title line
        for li in range(len(lines)-1, max(-1, len(lines)-8), -1):
            line = lines[li].strip()
            if not line:
                continue
            # skip lines that look like labels
            if line.lower().startswith('(cid:') or line.lower().startswith('item') or line.lower().endswith(':'):
                continue
            # limit length
            if 3 <= len(line) <= 200:
                candidates.add(line)
                break
        start = idx + len(keyword)

# normalization helper
import string

def normalize_name(n):
    if not n:
        return ''
    # remove parenthetical suffixes
    n2 = re.sub(r"\s*\(.*?\)", "", n)
    n2 = n2.lower()
    # remove punctuation
    trans = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    n2 = n2.translate(trans)
    n2 = re.sub(r"\s+", " ", n2).strip()
    return n2

norm_candidates = set(normalize_name(c) for c in candidates if c)

# function to infer status by searching civic text
def infer_status(name):
    base = normalize_name(name)
    if not base:
        return 'unknown'
    # search in full_text_low for base
    idx = full_text_low.find(base)
    snippet = ''
    if idx != -1:
        snippet = full_text_low[max(0, idx-200): idx+800]
    else:
        # try partial word match
        words = base.split()
        for w in words:
            if len(w) > 4:
                i = full_text_low.find(w)
                if i != -1:
                    snippet = full_text_low[max(0, i-200): i+800]
                    break
    s = 'unknown'
    if snippet:
        if any(p in snippet for p in ['construction was completed', 'notice of completion', 'complete construction', 'construction was completed', 'completed', 'complete construction:']):
            s = 'completed'
        elif any(p in snippet for p in ['complete design', 'preliminary design', 'final design', 'working with the consultant', 'working with the design', 'finalizing the design', 'project is in the preliminary design phase', 'design plans']):
            s = 'design'
        elif any(p in snippet for p in ['not started', 'identified', 'awaiting', 'waiting for', 'advertise:', 'begin construction:', 'begin construction']):
            s = 'not started'
        elif 'under construction' in snippet or 'currently under construction' in snippet:
            s = 'not started'
    return s

# collect matching funding records
results = []
seen = set()
for rec in funding:
    pname = rec.get('Project_Name','')
    p_low = pname.lower()
    fsrc = rec.get('Funding_Source','')
    fsrc_low = (fsrc or '').lower()
    amt = rec.get('Amount')
    try:
        amt_val = int(amt)
    except:
        try:
            amt_val = int(float(amt))
        except:
            amt_val = None

    include = False
    # direct mentions
    if 'fema' in p_low or 'fema' in fsrc_low or 'emergency' in p_low or 'emergency' in fsrc_low:
        include = True
    else:
        # compare normalized names with candidates
        np = normalize_name(pname)
        for nc in norm_candidates:
            if not nc:
                continue
            if nc in np or np in nc or nc == np:
                include = True
                break
    if include and pname not in seen:
        status = infer_status(pname)
        results.append({'Project_Name': pname, 'Funding_Source': fsrc, 'Amount': amt_val, 'Status': status})
        seen.add(pname)

# sort results
results_sorted = sorted(results, key=lambda x: x['Project_Name'].lower())

print('__RESULT__:')
print(json.dumps(results_sorted))"""

env_args = {'var_call_OTsZFSddYbanLEHhV1oqAEar': 'file_storage/call_OTsZFSddYbanLEHhV1oqAEar.json', 'var_call_RpKhjqFTVlsT3xmU5phuCvLx': 'file_storage/call_RpKhjqFTVlsT3xmU5phuCvLx.json'}

exec(code, env_args)
