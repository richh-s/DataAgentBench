code = """import json, re

# load spring docs
path = var_call_RrmAuwXmqg52X8TuT8IIP0jf
with open(path,'r',encoding='utf-8') as f:
    docs=json.load(f)

# extract project titles preceding 'Begin Construction: Spring 2022' by block parsing
beg_pat = re.compile(r'\bBegin\s+Construction\s*:\s*Spring\s+2022\b', re.IGNORECASE)

projects=set()

for d in docs:
    lines=[ln.rstrip() for ln in d.get('text','').splitlines()]
    # identify indices with begin construction spring 2022
    for idx, ln in enumerate(lines):
        if not beg_pat.search(ln):
            continue
        # search backwards for title: first non-empty line that is not bullet and not contains ':' and not schedule header
        for j in range(idx-1, max(-1, idx-60), -1):
            cand=lines[j].strip()
            if not cand:
                continue
            if ':' in cand:
                continue
            if cand.startswith('(cid') or cand.startswith('•') or cand.startswith('-') or cand.startswith('–'):
                continue
            low=cand.lower()
            if 'project schedule' in low or 'estimated schedule' in low:
                continue
            if low.startswith('capital improvement projects') or low.startswith('disaster projects'):
                continue
            # likely title appears before 'Updates:'
            projects.add(cand)
            break

# load funding
fpath = var_call_QaHZ0aBiwBcN90g6vApyBxXi
with open(fpath,'r',encoding='utf-8') as f:
    fund=json.load(f)

fund_map={r['Project_Name']: int(r['Total_Amount']) for r in fund}

matched=[]
missing=[]
for p in sorted(projects):
    if p in fund_map:
        matched.append((p,fund_map[p]))
    else:
        missing.append(p)

total=sum(a for _,a in matched)

print('__RESULT__:')
print(json.dumps({'projects_started_spring_2022': [p for p,_ in matched], 'count': len(matched), 'total_funding': total, 'unmatched_extracted_titles': missing}))"""

env_args = {'var_call_GU7TOrWp60QnSxcfBDDbjJb3': ['civic_docs'], 'var_call_oT345mwgQj4Nim0YXkOkj7b9': ['Funding'], 'var_call_4kyFbfoBMGRtUpextA1f4p3h': 'file_storage/call_4kyFbfoBMGRtUpextA1f4p3h.json', 'var_call_RrmAuwXmqg52X8TuT8IIP0jf': 'file_storage/call_RrmAuwXmqg52X8TuT8IIP0jf.json', 'var_call_30YBBp833KFtdaNkWsVc6Pk0': {'projects': ['advertised for construction bids shortly after this date.', 'damaged by the Woolsey Fire.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.'], 'count': 6}, 'var_call_QaHZ0aBiwBcN90g6vApyBxXi': 'file_storage/call_QaHZ0aBiwBcN90g6vApyBxXi.json'}

exec(code, env_args)
