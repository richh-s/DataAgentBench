code = """import json, re, pandas as pd

# Load mongo docs (may be file path)
md = var_call_FR997zE42xnAWHVOLo5CEg6w
if isinstance(md, str):
    with open(md, 'r', encoding='utf-8') as f:
        md = json.load(f)

cit = var_call_3B231C5JuznxO3I2TsXNrWUu
if isinstance(cit, str):
    with open(cit, 'r', encoding='utf-8') as f:
        cit = json.load(f)

# Build quick lookup for total citations by title
cit_df = pd.DataFrame(cit)
# coerce total_citations to int
cit_df['total_citations'] = pd.to_numeric(cit_df['total_citations'], errors='coerce').fillna(0).astype(int)
cit_map = dict(zip(cit_df['title'], cit_df['total_citations']))

# Identify 2016 physical activity papers from docs via simple heuristics
# Domain match: 'physical activity' phrase (case-insensitive)
# Year match: look for 2016 near header/citation lines.

def extract_year(text):
    # prefer explicit patterns like 'CHI 2016', 'UbiComp 2016', '(2016)'
    patterns = [r'(?i)\\bCHI\\s*2016\\b', r'(?i)\\bUbiComp\\s*2016\\b', r'(?i)\\bCSCW\\s*2016\\b', r'(?i)\\bDIS\\s*2016\\b', r'\\(2016\\)', r'(?i)\\b2016\\b']
    for p in patterns:
        if re.search(p, text):
            return 2016
    return None

rows = []
for d in md:
    title = re.sub(r'\\.txt$', '', d.get('filename','')).strip()
    text = d.get('text','') or ''
    if not re.search(r'(?i)physical activity', text):
        continue
    y = extract_year(text)
    if y != 2016:
        continue
    total_cit = cit_map.get(title)
    if total_cit is None:
        # try minor normalization for curly quotes etc.
        # basic: replace multiple spaces, normalize apostrophes
        def norm(s):
            return re.sub(r'\\s+', ' ', s.replace('’',"'").replace('“','"').replace('”','"')).strip()
        nt = norm(title)
        # build normalized map once
        if 'norm_map' not in globals():
            norm_map = {norm(k): v for k,v in cit_map.items()}
            globals()['norm_map'] = norm_map
        total_cit = globals()['norm_map'].get(nt, 0)
    rows.append({'title': title, 'total_citations': int(total_cit)})

out_df = pd.DataFrame(rows).drop_duplicates(subset=['title']).sort_values(['total_citations','title'], ascending=[False, True])
result = out_df.to_dict(orient='records')
print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False))"""

env_args = {'var_call_FR997zE42xnAWHVOLo5CEg6w': 'file_storage/call_FR997zE42xnAWHVOLo5CEg6w.json', 'var_call_3B231C5JuznxO3I2TsXNrWUu': 'file_storage/call_3B231C5JuznxO3I2TsXNrWUu.json'}

exec(code, env_args)
