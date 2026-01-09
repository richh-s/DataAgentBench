code = """import json, re

# Load civic docs
civic_src = var_call_J7eGwEXhjIzwwKUfPFoudyfW
if isinstance(civic_src, str) and civic_src.endswith('.json'):
    with open(civic_src, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = civic_src

# Load funding totals > 50k
fund_src = var_call_XdOjpbUIRZETuOjgdLVI09nb
if isinstance(fund_src, str) and fund_src.endswith('.json'):
    with open(fund_src, 'r', encoding='utf-8') as f:
        fund_rows = json.load(f)
else:
    fund_rows = fund_src

fund_projects = set(r['Project_Name'] for r in fund_rows)

capital_design = set()
header_re = re.compile(r"Capital Improvement Projects\s*\(Design\)", re.IGNORECASE)
stop_re = re.compile(r"\n\s*Capital Improvement Projects\s*\(Construction\)|\n\s*Disaster Recovery Projects|\n\s*Capital Improvement Projects\s*\(Not Started\)", re.IGNORECASE)
skip_re = re.compile(r"^(\(cid:|Updates\b|Project Schedule\b|Estimated Schedule\b|Complete Design\b|Advertise\b|Begin Construction\b|Final Design\b|Page\b|Agenda Item\b|DISCUSSION\b|RECOMMENDED ACTION\b)", re.IGNORECASE)

for doc in civic_docs:
    text = doc.get('text','') or ''
    for m in header_re.finditer(text):
        window = text[m.end():m.end()+6000]
        sm = stop_re.search(window)
        if sm:
            window = window[:sm.start()]
        for line in window.splitlines():
            s = line.strip()
            if not s or len(s) < 4:
                continue
            if skip_re.match(s):
                continue
            s2 = re.sub(r"\s{2,}", " ", s).strip(' -:\t')
            if len(s2) > 120:
                continue
            if '.' in s2:
                continue
            capital_design.add(s2)

result_set = sorted(capital_design.intersection(fund_projects))

print("__RESULT__:")
print(json.dumps({"count": len(result_set)}))"""

env_args = {'var_call_LOtBju6RNpgkJofPvIFclz34': [{'project_count': '276'}], 'var_call_J7eGwEXhjIzwwKUfPFoudyfW': 'file_storage/call_J7eGwEXhjIzwwKUfPFoudyfW.json', 'var_call_XdOjpbUIRZETuOjgdLVI09nb': 'file_storage/call_XdOjpbUIRZETuOjgdLVI09nb.json'}

exec(code, env_args)
