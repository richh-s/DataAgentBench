code = """import json, re
import pandas as pd

path_docs = var_call_5FRoyKoaGE92xUhwFnjuJHFV
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

path_fund = var_call_B8i9KzeWghvmclogSXmtIm7J
with open(path_fund, 'r', encoding='utf-8') as f:
    fund = json.load(f)

fund_df = pd.DataFrame(fund)
if not fund_df.empty:
    fund_df['total_amount'] = pd.to_numeric(fund_df['total_amount'], errors='coerce').fillna(0).astype(int)

spring_2022_projects = set()

start_line_re = re.compile(r'(?im)^\s*(?:Begin\s+Construction|Start(?:\s+Construction)?|Begin\s+Work|Construction\s+Start|Advertise|Bid\s+and\s+Award|Issue\s+RFP|Issue\s+RFQ|Notice\s+to\s+Proceed)\s*:\s*([^\n\r]+)')

name_re = re.compile(r'(?m)^(?!\s*(?:\(cid:|Page\s+\d+\s+of\s+\d+|Agenda\s+Item|Capital\s+Improvement\s+Projects|Disaster\s+Recovery\s+Projects|RECOMMENDED\s+ACTION|DISCUSSION|To:|Prepared\s+by:|Approved\s+by:|Date\s+prepared:|Meeting\s+date:|Subject:|Updates:|Project\s+Description:))\s*([A-Z][^\n]{2,120})\s*$')

for d in docs:
    text = d.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        m = name_re.match(line)
        if not m:
            continue
        pname = m.group(1).strip()
        if pname.endswith(':') or len(pname) < 4:
            continue
        if pname.lower() in {'discussion','recommended action'}:
            continue
        chunk = "\n".join(lines[i:i+60])
        found = False
        for sm in start_line_re.finditer(chunk):
            if re.search(r'(?i)\bSpring\s+2022\b', sm.group(1)):
                found = True
                break
        if found:
            spring_2022_projects.add(pname)

spring_list = sorted(spring_2022_projects)
joined = fund_df[fund_df['Project_Name'].isin(spring_list)] if spring_list else fund_df.iloc[0:0]

total_funding = int(joined['total_amount'].sum()) if not joined.empty else 0

result = {
    'projects_started_spring_2022_count': int(len(spring_list)),
    'total_funding_usd': total_funding,
    'projects_found': spring_list
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_5FRoyKoaGE92xUhwFnjuJHFV': 'file_storage/call_5FRoyKoaGE92xUhwFnjuJHFV.json', 'var_call_B8i9KzeWghvmclogSXmtIm7J': 'file_storage/call_B8i9KzeWghvmclogSXmtIm7J.json'}

exec(code, env_args)
