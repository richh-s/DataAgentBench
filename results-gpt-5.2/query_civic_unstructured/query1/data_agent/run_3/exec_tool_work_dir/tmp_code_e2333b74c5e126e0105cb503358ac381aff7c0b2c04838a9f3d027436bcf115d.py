code = """import json, re, pandas as pd

# Load civic docs (may be file path)
raw_docs = var_call_1AaiwBHaTiEmTu2ZdevwhkXG
if isinstance(raw_docs, str):
    with open(raw_docs, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw_docs

# Load funded project names > 50000 (may be file path)
raw_pnames = var_call_l1BvLjYkIUZbhDfhS1RqqM2N
if isinstance(raw_pnames, str):
    with open(raw_pnames, 'r', encoding='utf-8') as f:
        pnames_recs = json.load(f)
else:
    pnames_recs = raw_pnames

funded_names = {r['Project_Name'] for r in pnames_recs if r.get('Project_Name')}

# Extract project names under sections labeled '(Design)'
# Heuristic: find lines between a header containing '(Design)' and the next header containing '(Construction)' or '(Not Started)' or 'Disaster Recovery Projects'
header_design_re = re.compile(r"\(\s*Design\s*\)", re.IGNORECASE)
stop_re = re.compile(r"\(\s*Construction\s*\)|\(\s*Not Started\s*\)|Disaster\s+Recovery\s+Projects", re.IGNORECASE)

extracted_design_names = set()
for d in docs:
    text = d.get('text','') or ''
    # normalize line endings
    lines = [ln.strip() for ln in text.splitlines()]
    # find indices where a design header occurs
    idxs = [i for i,ln in enumerate(lines) if header_design_re.search(ln)]
    for start in idxs:
        # collect subsequent lines until stop
        for j in range(start+1, len(lines)):
            ln = lines[j].strip()
            if not ln:
                continue
            if stop_re.search(ln):
                break
            # project names tend to be standalone lines without bullets and not starting with common words
            if ln.startswith(('(cid:', 'Page ', 'Agenda', 'To:', 'Prepared', 'Approved', 'Date', 'Meeting', 'Subject', 'RECOMMENDED', 'DISCUSSION', 'Updates', 'Project', 'Estimated', 'Complete', 'Advertise', 'Begin')):
                continue
            if 'cid:' in ln:
                continue
            # Exclude lines that are clearly sentences
            if len(ln) > 120:
                continue
            if re.search(r"[:\.]{1}\s", ln):
                # allow e.g., 'Malibu Canyon Road Traffic Study' (no punctuation). If punctuation likely sentence.
                continue
            # remove trailing/leading odd chars
            ln2 = re.sub(r"\s+", " ", ln).strip(' \t-•*')
            # Must contain at least 2 letters
            if not re.search(r"[A-Za-z].*[A-Za-z]", ln2):
                continue
            extracted_design_names.add(ln2)

# Intersect with funded project names
matching = sorted(extracted_design_names.intersection(funded_names))
result = {
    "count": len(matching),
    "matching_project_names": matching
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_0OWVdZ71OOhCBgdHDSyrzoTQ': [{'cnt': '276'}], 'var_call_1AaiwBHaTiEmTu2ZdevwhkXG': 'file_storage/call_1AaiwBHaTiEmTu2ZdevwhkXG.json', 'var_call_l1BvLjYkIUZbhDfhS1RqqM2N': 'file_storage/call_l1BvLjYkIUZbhDfhS1RqqM2N.json'}

exec(code, env_args)
