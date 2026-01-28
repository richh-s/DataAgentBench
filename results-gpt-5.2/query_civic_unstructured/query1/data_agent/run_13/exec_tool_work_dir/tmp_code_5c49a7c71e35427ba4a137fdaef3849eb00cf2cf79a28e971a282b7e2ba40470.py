code = """import json, re, pandas as pd

# Load funding projects with total_amount > 50000
path = var_call_msJr1zbse4QU0iqXm8zjLWU8 if isinstance(var_call_msJr1zbse4QU0iqXm8zjLWU8, str) else None
if path:
    with open(path, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = var_call_msJr1zbse4QU0iqXm8zjLWU8

fund_projects = [r['Project_Name'] for r in funding]

# Load civic docs
docs_path = var_call_bftMp4xXqghGhzBVKtaHWkCK if isinstance(var_call_bftMp4xXqghGhzBVKtaHWkCK, str) else None
if docs_path:
    with open(docs_path, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = var_call_bftMp4xXqghGhzBVKtaHWkCK

# Build a single searchable text blob per doc, but we just need whether project appears in a 'Design' section.
# Heuristic: find lines between a header containing 'Capital Improvement Projects (Design)' or 'Disaster Recovery Projects (Design)'
# and the next header containing '(Construction)' or '(Not Started)' or 'Disaster Recovery Projects (Construction/Not Started)'.

def extract_design_lines(text):
    lines = [ln.strip() for ln in text.splitlines()]
    design_blocks = []
    i = 0
    while i < len(lines):
        ln = lines[i]
        if re.search(r'\(Design\)', ln, flags=re.IGNORECASE) and re.search(r'Projects', ln, flags=re.IGNORECASE):
            # start block after this line
            block = []
            i += 1
            while i < len(lines):
                ln2 = lines[i]
                if re.search(r'\((Construction|Not Started)\)', ln2, flags=re.IGNORECASE) and re.search(r'Projects', ln2, flags=re.IGNORECASE):
                    break
                # also stop if another major section like 'DISASTER' etc with construction/not started? keep simple
                block.append(ln2)
                i += 1
            design_blocks.append('\n'.join(block))
            continue
        i += 1
    return design_blocks

# Collect set of project names that appear in any design block
in_design = set()

# Precompile patterns for each project for faster matching: use word-boundary-ish by escaping and allowing flexible whitespace
proj_patterns = []
for p in fund_projects:
    esc = re.escape(p)
    esc = esc.replace('\\ ', r'\\s+')
    proj_patterns.append((p, re.compile(esc, flags=re.IGNORECASE)))

for d in docs:
    text = d.get('text','') or ''
    for block in extract_design_lines(text):
        for p, pat in proj_patterns:
            if p in in_design:
                continue
            if pat.search(block):
                in_design.add(p)

count = len(in_design)

print('__RESULT__:')
print(json.dumps({'count': count}))"""

env_args = {'var_call_iJVNrexEMMTVEkK9c7BVBNMe': [{'cnt': '276'}], 'var_call_bftMp4xXqghGhzBVKtaHWkCK': 'file_storage/call_bftMp4xXqghGhzBVKtaHWkCK.json', 'var_call_msJr1zbse4QU0iqXm8zjLWU8': 'file_storage/call_msJr1zbse4QU0iqXm8zjLWU8.json'}

exec(code, env_args)
