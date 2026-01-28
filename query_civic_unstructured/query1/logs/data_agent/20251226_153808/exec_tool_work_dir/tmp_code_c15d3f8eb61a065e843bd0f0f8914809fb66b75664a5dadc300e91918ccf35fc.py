code = """import json

# Load funding records (> $50,000)
fp = var_call_qavtXlmiGoW9QnOA78pUlytE
with open(fp, 'r') as f:
    funding_records = json.load(f)
funded_names = set()
for r in funding_records:
    n = r.get('Project_Name')
    if isinstance(n, str):
        funded_names.add(n.strip())

# Load civic docs
cp = var_call_RZF88M1S8GL1Z6q8kFep6vBb
with open(cp, 'r') as f:
    docs = json.load(f)

header = 'capital improvement projects (design)'
stop_markers = ['capital improvement projects (construction)', 'capital improvement projects (not started)', 'disaster recovery projects']

capital_design = set()

for doc in docs:
    text = doc.get('text') or ''
    if not text:
        continue
    lines = text.split('\n')
    low = [ln.lower() for ln in lines]
    # find header indices
    starts = [i for i, ln in enumerate(low) if header in ln]
    for si in starts:
        end = len(lines)
        for j in range(si+1, len(lines)):
            lj = low[j]
            if header in lj:
                end = j
                break
            if any(m in lj for m in stop_markers):
                end = j
                break
        section = lines[si+1:end]
        sec_low = [ln.lower() for ln in section]
        n = len(section)
        # collect title-like lines followed by anchors within 4 lines
        def is_anchor(s):
            s = s.strip()
            return s.endswith('updates:') or s == 'updates:' or s == 'project updates:' or ('project schedule' in s) or ('estimated schedule' in s) or s.endswith('description:') or s == 'project description:'
        for idx in range(n):
            cand = section[idx].strip()
            l = sec_low[idx].strip()
            if not cand:
                continue
            if l.startswith('agenda item') or l.startswith('page '):
                continue
            if ':' in cand:
                continue
            found = False
            for kk in range(1,5):
                if idx+kk >= n:
                    break
                if is_anchor(sec_low[idx+kk]):
                    found = True
                    break
            if found:
                # clean simple bullets like (cid:###)
                while '(cid:' in cand:
                    s = cand
                    a = s.find('(cid:')
                    b = s.find(')', a)
                    if a != -1 and b != -1:
                        cand = (s[:a] + s[b+1:]).strip()
                    else:
                        break
                cand = ' '.join(cand.split())
                capital_design.add(cand)

matched = sorted([name for name in capital_design if name in funded_names])
res = {"count": len(matched), "matched_projects": matched}
print("__RESULT__:")
print(json.dumps(res))"""

env_args = {'var_call_emkmzpvum2bkhY3KeP5UYxCb': ['civic_docs'], 'var_call_o7fqj1i1czAOdbOZBSxsmZnL': ['Funding'], 'var_call_qavtXlmiGoW9QnOA78pUlytE': 'file_storage/call_qavtXlmiGoW9QnOA78pUlytE.json', 'var_call_RZF88M1S8GL1Z6q8kFep6vBb': 'file_storage/call_RZF88M1S8GL1Z6q8kFep6vBb.json', 'var_call_AbZ8lqeSkNP5EWX7XQhMRPdW': {'funding_count': 276, 'docs_count': 19}}

exec(code, env_args)
