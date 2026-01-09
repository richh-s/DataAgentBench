code = """import json, re
import pandas as pd

def load_records(obj):
    if isinstance(obj, str):
        # file path
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

pub_recs = load_records(var_call_KKoNnOzinbnsJH3OlaSrUO18)
# active level-5 list came back empty; fall back to any level-5 symbols
lvl5 = load_records(var_call_DbA0rd8zrZGceBlUvzJcbE5k)

# parse year from natural language date
month_map = {m:i for i,m in enumerate(['january','february','march','april','may','june','july','august','september','october','november','december'], start=1)}

def extract_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\\d{2}', s)
    if not m:
        return None
    return int(m.group(0))

def parse_cpc_codes(cpc_str):
    if not cpc_str:
        return []
    try:
        arr = json.loads(cpc_str)
        codes = []
        for it in arr:
            code = it.get('code') if isinstance(it, dict) else None
            if code:
                codes.append(code.strip())
        return codes
    except Exception:
        return []

rows = []
for r in pub_recs:
    y = extract_year(r.get('filing_date'))
    if y is None:
        continue
    codes = parse_cpc_codes(r.get('cpc'))
    for c in codes:
        rows.append((y, c))

df = pd.DataFrame(rows, columns=['year','cpc'])
# keep only years up to 2022 (best year constraint)
df = df[df['year']<=2022]

# Determine level-5 codes by matching to cpc_definition level=5.
# Since active list empty, query all level 5 symbols from CPCDefinition_database is needed,
# but not available here; approximate by code length/structure? Not safe.
# We'll instead infer level-5 as having a '/' with at least one digit after and having at least 1 digit after slash (group). But that's not level.
# To comply, we will request level=5 symbols without status filter from DB in next step.

result = {'need_more_data': True, 'message': 'Need CPC level=5 symbol list (status filter returned none). Please query cpc_definition where level=5 (no status filter).'}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_DbA0rd8zrZGceBlUvzJcbE5k': [], 'var_call_KKoNnOzinbnsJH3OlaSrUO18': 'file_storage/call_KKoNnOzinbnsJH3OlaSrUO18.json'}

exec(code, env_args)
