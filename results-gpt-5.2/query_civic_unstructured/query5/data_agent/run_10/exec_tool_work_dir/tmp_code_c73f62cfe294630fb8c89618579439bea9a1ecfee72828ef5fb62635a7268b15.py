code = """import json, re
import pandas as pd

# Load civic docs
civic_src = var_call_KwdJsR3RZqKvF24MEPG4KiER
if isinstance(civic_src, str) and civic_src.endswith('.json'):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

# Load funding
fund_src = var_call_W153OaIfEZny7OJGdLftunSK
if isinstance(fund_src, str) and fund_src.endswith('.json'):
    with open(fund_src, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = fund_src

fund_df = pd.DataFrame(funding)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

projects_2022_disaster = set()

pattern = r"Disaster Recovery Projects.*?(?=\n\s*(Capital Improvement Projects|$))"

for doc in civic_docs:
    text = doc.get('text','') or ''
    for m in re.finditer(pattern, text, flags=re.IGNORECASE|re.DOTALL):
        section = m.group(0)
        lines = [ln.strip() for ln in section.splitlines()]
        cur_proj = None
        buf = []
        for ln in lines:
            if not ln:
                continue
            is_header = bool(re.match(r"^[A-Za-z0-9].+", ln)) and not re.search(r"Updates|Project Schedule|Estimated Schedule|Project Description|RECOMMENDED ACTION|DISCUSSION", ln, re.I)
            if is_header:
                if cur_proj is not None:
                    block = "\n".join(buf)
                    if re.search(r"\b2022\b", block):
                        projects_2022_disaster.add(cur_proj)
                cur_proj = ln
                buf = []
            else:
                if cur_proj is not None:
                    buf.append(ln)
        if cur_proj is not None:
            block = "\n".join(buf)
            if re.search(r"\b2022\b", block):
                projects_2022_disaster.add(cur_proj)


def norm(s):
    s = s or ""
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip().lower()

ex_norm = set(norm(p) for p in projects_2022_disaster)

if fund_df.empty:
    total = 0
    matched_projects = []
else:
    sel_mask = fund_df['Project_Name'].apply(lambda x: norm(x) in ex_norm)
    selected = fund_df[sel_mask].copy()
    total = int(selected['total_amount'].sum()) if not selected.empty else 0
    matched_projects = sorted(set(selected['Project_Name']))

out = {"total_funding": total, "matched_project_count": int(len(matched_projects)), "matched_projects": matched_projects, "extracted_disaster_projects_2022_count": int(len(projects_2022_disaster))}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_KwdJsR3RZqKvF24MEPG4KiER': 'file_storage/call_KwdJsR3RZqKvF24MEPG4KiER.json', 'var_call_W153OaIfEZny7OJGdLftunSK': 'file_storage/call_W153OaIfEZny7OJGdLftunSK.json'}

exec(code, env_args)
