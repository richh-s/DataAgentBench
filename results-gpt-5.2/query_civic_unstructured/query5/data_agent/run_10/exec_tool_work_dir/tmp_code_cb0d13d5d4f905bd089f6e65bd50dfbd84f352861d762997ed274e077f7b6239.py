code = """import json, re
import pandas as pd

# Load civic docs result
civic_src = var_call_KwdJsR3RZqKvF24MEPG4KiER
if isinstance(civic_src, str) and civic_src.endswith('.json'):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

fund_src = var_call_W153OaIfEZny7OJGdLftunSK
if isinstance(fund_src, str) and fund_src.endswith('.json'):
    with open(fund_src, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = fund_src

fund_df = pd.DataFrame(funding)
if fund_df.empty:
    total = 0
else:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

# Extract disaster recovery project names that have start year 2022
projects_2022_disaster = set()

# helper to scan text blocks under Disaster Recovery Projects
for doc in civic_docs:
    text = doc.get('text','') or ''
    # find disaster recovery section(s)
    for m in re.finditer(r"Disaster Recovery Projects.*?(?=\n\s*(Capital Improvement Projects|$))", text, flags=re.IGNORECASE|re.DOTALL):
        section = m.group(0)
        # split into lines
        lines = [ln.strip() for ln in section.splitlines()]
        cur_proj = None
        buf = []
        for ln in lines:
            if not ln:
                continue
            # project header lines often without bullets and not starting with punctuation
            # heuristic: line not starting with '(' or 'cid' and not containing 'Updates'/'Project Schedule'
            if re.match(r"^[A-Za-z0-9].+", ln) and not re.search(r"Updates|Project Schedule|Estimated Schedule|Project Description|RECOMMENDED ACTION|DISCUSSION", ln, re.I):
                # flush previous
                if cur_proj and buf:
                    block = "\n".join(buf)
                    if re.search(r"\b2022\b", block):
                        projects_2022_disaster.add(cur_proj)
                cur_proj = ln
                buf = []
            else:
                if cur_proj:
                    buf.append(ln)
        if cur_proj and buf:
            block = "\n".join(buf)
            if re.search(r"\b2022\b", block):
                projects_2022_disaster.add(cur_proj)

# Also include disaster projects implied by name suffix in funding (FEMA/CalOES/CalJPIA) that started 2022 per docs
# Match funding project names against extracted ones loosely (exact or startswith)

# Build mapping from extracted project name to funding rows via normalization

def norm(s):
    return re.sub(r"\s+", " ", re.sub(r"\(.*?\)", "", s or "")).strip().lower()

ex_norm = {norm(p): p for p in projects_2022_disaster}

selected = fund_df[fund_df['Project_Name'].apply(lambda x: norm(x) in ex_norm)] if not fund_df.empty else fund_df

total = int(selected['total_amount'].sum()) if not selected.empty else 0

out = {"total_funding": total, "project_count": int(len(set(selected['Project_Name']))) , "matched_projects": sorted(set(selected['Project_Name']))}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_KwdJsR3RZqKvF24MEPG4KiER': 'file_storage/call_KwdJsR3RZqKvF24MEPG4KiER.json', 'var_call_W153OaIfEZny7OJGdLftunSK': 'file_storage/call_W153OaIfEZny7OJGdLftunSK.json'}

exec(code, env_args)
