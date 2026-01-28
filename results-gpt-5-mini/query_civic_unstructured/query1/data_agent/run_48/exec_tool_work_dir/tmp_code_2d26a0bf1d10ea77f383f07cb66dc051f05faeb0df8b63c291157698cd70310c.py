code = """import json
import re

# Load data from storage file paths
with open(var_call_rBqrP5cYtlIIK7E8axsCIupJ, 'r') as f:
    funding = json.load(f)

# civic docs may be large file path
with open(var_call_eIqu4HxwDSaSNdJTHmoLdlUB, 'r') as f:
    civic_docs = json.load(f)

# Normalize funding records and convert Amount to int
fund_records = []
for r in funding:
    name = r.get('Project_Name', '').strip()
    # Some Amounts may be strings; remove non-digits
    amt_raw = str(r.get('Amount', '0'))
    amt_digits = re.sub(r"[^0-9]", "", amt_raw)
    amt = int(amt_digits) if amt_digits else 0
    fund_records.append({'Project_Name': name, 'Amount': amt})

# Build combined civic text
texts = [d.get('text','') for d in civic_docs]

# Precompute indices of 'Capital Improvement Projects' headings for each doc
heading_phrase = 'capital improvement projects'

matches = []

for fr in fund_records:
    pname = fr['Project_Name']
    pname_l = pname.lower()
    amt = fr['Amount']
    if amt <= 50000:
        continue
    found_design = False
    # search in each document
    for text in texts:
        tl = text.lower()
        pos = tl.find(pname_l)
        if pos == -1:
            # try approximate: collapse whitespace and punctuation differences
            # also try matching only significant words (first few words)
            # fallback: continue
            continue
        # find all heading indices
        heads = [m.start() for m in re.finditer(re.escape(heading_phrase), tl)]
        # find the nearest preceding heading
        prev_head = None
        for h in heads:
            if h <= pos:
                prev_head = h
            else:
                break
        if prev_head is None:
            # no preceding 'Capital Improvement Projects' heading
            # check if nearby context contains 'design'
            context = tl[max(0,pos-200): pos+200]
            if 'design' in context:
                found_design = True
                break
            else:
                continue
        # find next head
        next_head = None
        for h in heads:
            if h > prev_head:
                next_head = h
                break
        block_end = next_head if next_head is not None else len(tl)
        block = tl[prev_head:block_end]
        # check if this block is the Design section
        if 'design' in block.splitlines()[0] or '(design)' in block or 'capital improvement projects (design)' in block[:200]:
            found_design = True
            break
        # otherwise, check if anywhere in block the word 'design' occurs near the project name
        # (e.g., 'Complete Design: Summer 2023')
        if 'design' in block:
            found_design = True
            break
    if found_design:
        matches.append({'Project_Name': pname, 'Amount': amt})

# remove duplicates by project name
seen = set()
unique_matches = []
for m in matches:
    if m['Project_Name'] not in seen:
        unique_matches.append(m)
        seen.add(m['Project_Name'])

count = len(unique_matches)

# Prepare result
result = {'count': count, 'projects': unique_matches}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_B5nTcJiryIQOYz07p5jVXT5q': ['civic_docs'], 'var_call_hsdPdQKnegi9l9CRGpLsy7MV': ['Funding'], 'var_call_eIqu4HxwDSaSNdJTHmoLdlUB': 'file_storage/call_eIqu4HxwDSaSNdJTHmoLdlUB.json', 'var_call_rBqrP5cYtlIIK7E8axsCIupJ': 'file_storage/call_rBqrP5cYtlIIK7E8axsCIupJ.json'}

exec(code, env_args)
