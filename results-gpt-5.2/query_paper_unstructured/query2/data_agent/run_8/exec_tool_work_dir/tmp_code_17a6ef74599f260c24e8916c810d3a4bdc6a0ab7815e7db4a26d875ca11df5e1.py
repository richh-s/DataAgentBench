code = """import json, re, pandas as pd

# Load citations 2018
cit_src = var_call_hCwbb4mESee6Jr3ERgI9YHi4
if isinstance(cit_src, str):
    with open(cit_src, 'r', encoding='utf-8') as f:
        cit = json.load(f)
else:
    cit = cit_src
cit_df = pd.DataFrame(cit)
if cit_df.empty:
    out = {"average_citation_count": None, "paper_count": 0}
    print("__RESULT__:")
    print(json.dumps(out))
    raise SystemExit
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce')

# Load paper docs
docs_src = var_call_YM8iDyScfeRIQvB9YllpgPNv
if isinstance(docs_src, str):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

def title_from_filename(fn):
    return re.sub(r"\.txt$", "", fn).strip()

# Heuristic for ACM publisher
acm_patterns = [
    r"\bAssociation for Computing Machinery\b",
    r"\bACM\b",
    r"\bCopyright\s*\d{4}\s*©\s*ACM\b",
    r"\bhttp://dx\.doi\.org/10\.1145/",
    r"\bdx\.doi\.org/10\.1145/",
    r"\bpermissions@acm\.org\b",
]
acm_re = re.compile("|".join(acm_patterns), re.IGNORECASE)

rows = []
for d in docs:
    fn = d.get('filename','')
    text = d.get('text','') or ''
    title = title_from_filename(fn)
    is_acm = bool(acm_re.search(text))
    rows.append({"title": title, "is_acm": is_acm})

papers_df = pd.DataFrame(rows)

# Join and compute mean for ACM papers
joined = cit_df.merge(papers_df[papers_df.is_acm], on='title', how='inner')
mean_val = float(joined['citation_count'].mean()) if not joined.empty else None
out = {"average_citation_count": mean_val, "paper_count": int(joined.shape[0])}

print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_hCwbb4mESee6Jr3ERgI9YHi4': 'file_storage/call_hCwbb4mESee6Jr3ERgI9YHi4.json', 'var_call_YM8iDyScfeRIQvB9YllpgPNv': 'file_storage/call_YM8iDyScfeRIQvB9YllpgPNv.json'}

exec(code, env_args)
