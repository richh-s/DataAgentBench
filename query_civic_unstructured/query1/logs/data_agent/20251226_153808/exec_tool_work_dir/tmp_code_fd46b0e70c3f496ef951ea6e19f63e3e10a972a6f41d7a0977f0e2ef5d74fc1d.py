code = """import json, re

# Load funding records from storage path
funding_path = var_call_qavtXlmiGoW9QnOA78pUlytE
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

funded_names = set()
for rec in funding_records:
    name = rec.get('Project_Name')
    if isinstance(name, str):
        funded_names.add(name.strip())

# Load civic documents
civic_path = var_call_RZF88M1S8GL1Z6q8kFep6vBb
with open(civic_path, 'r') as f:
    civic_docs = json.load(f)

header = 'capital improvement projects (design)'
stop_markers = [
    'capital improvement projects (construction)',
    'capital improvement projects (not started)',
    'disaster recovery projects'
]

bullet_re = re.compile(r"\(cid:[^)]*\)")

capital_design_projects = set()

for doc in civic_docs:
    text = doc.get('text') or ''
    if not text:
        continue
    lines = text.split('\n')
    low = [ln.lower() for ln in lines]

    # find all indices where header occurs
    starts = [i for i, ln in enumerate(low) if header in ln]
    for si in starts:
        # find section end
        end = len(lines)
        for j in range(si+1, len(lines)):
            lnj = low[j]
            if header in lnj:
                end = j
                break
            if any(m in lnj for m in stop_markers):
                end = j
                break
        # parse section
        sec_lines = lines[si+1:end]
        sec_low = [ln.lower() for ln in sec_lines]
        n = len(sec_lines)
        # pattern 1: updates or description markers -> previous non-empty as name
        for idx in range(n):
            l = sec_low[idx]
            if ('updates:' in l) or ('project updates:' in l) or ('project schedule' in l) or ('estimated schedule' in l) or ('description:' in l):
                k = idx - 1
                while k >= 0 and (sec_lines[k].strip() == '' or sec_low[k].startswith('agenda item') or sec_low[k].startswith('page ')):
                    k -= 1
                if k >= 0:
                    cand = sec_lines[k].strip()
                    if cand and not cand.endswith(':'):
                        cand = bullet_re.sub('', cand).strip()
                        cand = re.sub(r"\s+", " ", cand)
                        if len(cand) > 2:
                            capital_design_projects.add(cand)
        # pattern 2: title-like line followed by updates within 5 lines
        for idx in range(n):
            cand = sec_lines[idx].strip()
            l = sec_low[idx].strip()
            if not cand:
                continue
            if l.startswith('agenda item') or l.startswith('page '):
                continue
            if ':' in cand:
                continue
            found = False
            for kk in range(1, 6):
                if idx+kk >= n:
                    break
                ahead = sec_low[idx+kk]
                if ('updates:' in ahead) or ('project updates:' in ahead) or ('project schedule' in ahead) or ('estimated schedule' in ahead) or ('description:' in ahead):
                    found = True
                    break
            if found:
                clean = bullet_re.sub('', cand).strip()
                clean = re.sub(r"\s+", " ", clean)
                if len(clean) > 2:
                    capital_design_projects.add(clean)

# Intersect with funded names
matched = sorted([n for n in capital_design_projects if n in funded_names])
result = {"count": len(matched), "matched_projects": matched}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_emkmzpvum2bkhY3KeP5UYxCb': ['civic_docs'], 'var_call_o7fqj1i1czAOdbOZBSxsmZnL': ['Funding'], 'var_call_qavtXlmiGoW9QnOA78pUlytE': 'file_storage/call_qavtXlmiGoW9QnOA78pUlytE.json', 'var_call_RZF88M1S8GL1Z6q8kFep6vBb': 'file_storage/call_RZF88M1S8GL1Z6q8kFep6vBb.json'}

exec(code, env_args)
