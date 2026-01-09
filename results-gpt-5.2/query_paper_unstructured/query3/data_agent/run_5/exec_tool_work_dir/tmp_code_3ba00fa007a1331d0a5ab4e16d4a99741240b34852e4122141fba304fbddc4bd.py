code = """import json, re
import pandas as pd

# Load Mongo docs (may be a json file path)
docs_src = var_call_mOhHCGcPeUOlFfkRfkdNgn81
if isinstance(docs_src, str):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

# Load citations totals
cits_src = var_call_trt4Fa8bVd52lJdLSbMta5wO
if isinstance(cits_src, str):
    with open(cits_src, 'r', encoding='utf-8') as f:
        cits = json.load(f)
else:
    cits = cits_src

cit_df = pd.DataFrame(cits)
if not cit_df.empty:
    cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)

# Heuristic extraction for year and contribution

year_patterns = [
    re.compile(r'\b(?:Copyright\s*)?(?:\u00a9\s*)?(19\d{2}|20\d{2})\b'),
]

contrib_empirical_patterns = [
    re.compile(r'\bempirical\b', re.IGNORECASE),
]

venue_patterns = [
    re.compile(r"\bCHI\b"),
    re.compile(r"\bCSCW\b"),
    re.compile(r"\bUbiComp\b|\bUBICOMP\b"),
    re.compile(r"\bDIS\b"),
    re.compile(r"\bIUI\b"),
    re.compile(r"\bTEI\b"),
    re.compile(r"\bOzCHI\b"),
    re.compile(r"\bWWW\b"),
    re.compile(r"\bAH\b"),
    re.compile(r"\bPervasiveHealth\b"),
]

source_patterns = [
    re.compile(r"\bACM\b"),
    re.compile(r"\bIEEE\b"),
    re.compile(r"\bPubMed\b"),
]


def extract_year(text):
    # Prefer lines containing venue strings with year like "CHI 2018" or "'18" etc.
    # 1) look for explicit 4-digit years 2010-2026 near start
    head = text[:6000]
    years = [int(m.group(1)) for m in re.finditer(r'\b(20\d{2})\b', head)]
    if years:
        # publication year is usually the minimum 4-digit year in header (copyright/year)
        return min(years)
    # fallback broader
    years2 = [int(m.group(1)) for m in re.finditer(r'\b(19\d{2}|20\d{2})\b', text[:20000])]
    return min(years2) if years2 else None


def has_empirical(text):
    return bool(contrib_empirical_patterns[0].search(text[:30000]))

rows = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    y = extract_year(text)
    if y is None or y <= 2016:
        continue
    if not has_empirical(text):
        continue
    rows.append({'title': title, 'year': y})

papers_df = pd.DataFrame(rows).drop_duplicates(subset=['title'])

# join with citations totals
if papers_df.empty:
    out = []
else:
    merged = papers_df.merge(cit_df, on='title', how='left')
    merged['total_citations'] = merged['total_citations'].fillna(0).astype(int)
    merged = merged.sort_values(['total_citations','title'], ascending=[False, True])
    out = merged[['title','total_citations']].to_dict('records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_mOhHCGcPeUOlFfkRfkdNgn81': 'file_storage/call_mOhHCGcPeUOlFfkRfkdNgn81.json', 'var_call_trt4Fa8bVd52lJdLSbMta5wO': 'file_storage/call_trt4Fa8bVd52lJdLSbMta5wO.json'}

exec(code, env_args)
