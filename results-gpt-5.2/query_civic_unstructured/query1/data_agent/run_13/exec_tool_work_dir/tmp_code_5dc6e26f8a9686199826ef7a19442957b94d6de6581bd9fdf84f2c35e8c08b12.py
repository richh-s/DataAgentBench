code = """import json, re

# Load funding projects with total_amount > 50000
if isinstance(var_call_msJr1zbse4QU0iqXm8zjLWU8, str):
    with open(var_call_msJr1zbse4QU0iqXm8zjLWU8, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = var_call_msJr1zbse4QU0iqXm8zjLWU8
fund_projects = [r['Project_Name'] for r in funding]

# Load civic docs
if isinstance(var_call_bftMp4xXqghGhzBVKtaHWkCK, str):
    with open(var_call_bftMp4xXqghGhzBVKtaHWkCK, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = var_call_bftMp4xXqghGhzBVKtaHWkCK

def extract_design_blocks(text):
    lines = [ln.strip() for ln in text.splitlines()]
    blocks = []
    i = 0
    while i < len(lines):
        ln = lines[i]
        if re.search(r'\(Design\)', ln, flags=re.IGNORECASE) and re.search(r'Projects', ln, flags=re.IGNORECASE):
            i += 1
            block_lines = []
            while i < len(lines):
                ln2 = lines[i]
                if re.search(r'\((Construction|Not Started)\)', ln2, flags=re.IGNORECASE) and re.search(r'Projects', ln2, flags=re.IGNORECASE):
                    break
                block_lines.append(ln2)
                i += 1
            blocks.append('\n'.join(block_lines))
            continue
        i += 1
    return blocks

proj_patterns = []
for p in fund_projects:
    esc = re.escape(p)
    esc = esc.replace('\\ ', r'\\s+')
    proj_patterns.append((p, re.compile(esc, flags=re.IGNORECASE)))

in_design = set()
for d in docs:
    text = d.get('text', '') or ''
    for block in extract_design_blocks(text):
        for p, pat in proj_patterns:
            if p in in_design:
                continue
            if pat.search(block):
                in_design.add(p)

result = {'count': len(in_design)}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_iJVNrexEMMTVEkK9c7BVBNMe': [{'cnt': '276'}], 'var_call_bftMp4xXqghGhzBVKtaHWkCK': 'file_storage/call_bftMp4xXqghGhzBVKtaHWkCK.json', 'var_call_msJr1zbse4QU0iqXm8zjLWU8': 'file_storage/call_msJr1zbse4QU0iqXm8zjLWU8.json'}

exec(code, env_args)
