code = """import json, re, pandas as pd

# Load civic docs
civic_src = var_call_jroWgJMT8F7cCBC0f826dx5I
if isinstance(civic_src, str) and civic_src.endswith('.json'):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

# Load funding by project
fund_src = var_call_0mwA7xPw4fLVn1WGDZnXmja6
if isinstance(fund_src, str) and fund_src.endswith('.json'):
    with open(fund_src, 'r', encoding='utf-8') as f:
        fund_rows = json.load(f)
else:
    fund_rows = fund_src
fund_df = pd.DataFrame(fund_rows)
fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'], errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(fund_df['Project_Name'], fund_df['Total_Amount']))

# Parse docs: find disaster projects and their schedule lines
# Heuristic: within a document section titled 'Disaster Recovery Projects', parse blocks with a project name line, then look for 'Begin Construction' or 'Start' lines containing 2022.

def extract_disaster_projects_started_2022(text):
    results = []
    if not text:
        return results
    # Normalize
    t = text
    # Locate disaster section(s)
    for m in re.finditer(r'Disaster Recovery Projects.*?(?=\n\s*Capital Improvement Projects|\Z)', t, flags=re.IGNORECASE|re.DOTALL):
        sec = m.group(0)
        lines = [ln.strip() for ln in sec.splitlines()]
        # project name candidates: non-empty lines without bullets that are not headings
        # We'll scan and create blocks starting at lines that look like titles (not starting with '(' or 'cid' or 'Page' or 'Agenda' etc.)
        blocks = []
        cur_name = None
        cur_block = []
        def flush():
            nonlocal cur_name, cur_block
            if cur_name and cur_block:
                blocks.append((cur_name, '\n'.join(cur_block)))
            cur_name, cur_block = None, []
        for ln in lines:
            if not ln:
                continue
            if re.match(r'^(Disaster Recovery Projects|Agenda Item|Page \d+|RECOMMENDED ACTION|DISCUSSION|\(cid:)', ln, flags=re.I):
                continue
            # treat as new project title if line has letters and no ':' and is Title Case-ish and not starting with 'Updates' or 'Project Schedule'
            is_title = (':' not in ln and not re.match(r'^(Updates|Project Schedule|Estimated Schedule|Project Description)', ln, flags=re.I)
                        and len(ln) < 120)
            if is_title:
                # start new block
                flush()
                cur_name = ln
                cur_block = [ln]
            else:
                if cur_name:
                    cur_block.append(ln)
        flush()

        for name, block in blocks:
            # started in 2022: look for begin construction or start time includes 2022
            if re.search(r'(Begin Construction|Start)\s*:\s*.*2022', block, flags=re.I):
                results.append(name)
            # also allow patterns like 'Begin construction: April 2022'
            elif re.search(r'Begin construction\s*:\s*.*2022', block, flags=re.I):
                results.append(name)
    return results

started_2022 = set()
for doc in civic_docs:
    started_2022.update(extract_disaster_projects_started_2022(doc.get('text','')))

# Sum funding for those project names present in funding table
matched = {name: fund_map.get(name) for name in started_2022 if name in fund_map}

total = int(sum(v for v in matched.values() if v is not None))

out = {
    'total_funding_usd': total,
    'num_disaster_projects_started_2022_found_in_docs': len(started_2022),
    'num_matched_to_funding_table': len(matched),
    'matched_projects': matched
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_AcRQ6OtasNM9MGboFNwd7qNq': ['civic_docs'], 'var_call_XQWZ4a4IsKyRlEwdyWL5OCqE': ['Funding'], 'var_call_jroWgJMT8F7cCBC0f826dx5I': 'file_storage/call_jroWgJMT8F7cCBC0f826dx5I.json', 'var_call_0mwA7xPw4fLVn1WGDZnXmja6': 'file_storage/call_0mwA7xPw4fLVn1WGDZnXmja6.json'}

exec(code, env_args)
