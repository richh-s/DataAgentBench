code = """import json, re
import pandas as pd

# Load citations 2020
cit_path = var_call_NpjUim6ZBQqGACLfpLmvtSuU
with open(cit_path, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
if df_cit.empty:
    out = {"total_citations_2020_CHI": 0}
    print("__RESULT__:")
    print(json.dumps(out))
    raise SystemExit

df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)

def detect_chi(text):
    if not text:
        return False
    t = text.upper()
    # Look for CHI conference markers
    patterns = [
        r"\bCHI\s*['’]\s*\d{2}\b",
        r"\bCHI\s*\d{4}\b",
        r"\bPROCEEDINGS\s+OF\s+THE\s+\bCHI\b",
        r"\bACM\s+CHI\b",
        r"\bSIGCHI\b"
    ]
    return any(re.search(p, t) for p in patterns)

# Load paper docs, build set of CHI titles
paper_path = var_call_GHe72On7cpBq6RkTeI9oy9DY
with open(paper_path, 'r', encoding='utf-8') as f:
    papers = json.load(f)

chi_titles = set()
for d in papers:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if detect_chi(d.get('text','')):
        chi_titles.add(title)

# Filter citations to CHI titles and sum
mask = df_cit['title'].isin(chi_titles)
total = int(df_cit.loc[mask, 'citation_count'].sum())
out = {"total_citations_2020_CHI": total, "num_chi_papers_cited_in_2020": int(mask.sum())}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_NpjUim6ZBQqGACLfpLmvtSuU': 'file_storage/call_NpjUim6ZBQqGACLfpLmvtSuU.json', 'var_call_GHe72On7cpBq6RkTeI9oy9DY': 'file_storage/call_GHe72On7cpBq6RkTeI9oy9DY.json'}

exec(code, env_args)
