code = """import json, re, pandas as pd

civic = var_call_eIC9RQkWUxJuxTKZvSmWYoxc
if isinstance(civic, str):
    with open(civic, 'r') as f:
        civic = json.load(f)

fund = var_call_s84kqxjOfocZJ8F4wVH0rYf8
if isinstance(fund, str):
    with open(fund, 'r') as f:
        fund = json.load(f)

df_fund = pd.DataFrame(fund)
df_fund['total_amount'] = pd.to_numeric(df_fund['total_amount'], errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(df_fund['Project_Name'], df_fund['total_amount']))

def find_completed_2022_park_projects(text):
    lines = [ln.strip() for ln in text.splitlines()]
    projects = set()
    exclude_pat = re.compile(r'^(Updates|Project Schedule|Project Description|Capital Improvement Projects|Disaster Recovery Projects|RECOMMENDED ACTION|DISCUSSION|Page \d+)', re.I)
    comp_pat = re.compile(r'(?i)(construction\s+was\s+completed[^\n]*2022|complete\s+construction[^\n]*2022|completed[^\n]*2022)')
    park_pat = re.compile(r'(?i)\bpark\b')
    for i, ln in enumerate(lines):
        if not ln:
            continue
        if len(ln) > 3 and len(ln) < 120 and not exclude_pat.search(ln):
            window = "\n".join(lines[i:i+20])
            if not comp_pat.search(window):
                continue
            if ('park' not in ln.lower()) and (not park_pat.search(window)):
                continue
            title = re.sub(r'\s{2,}', ' ', ln).strip(' -:\t')
            if title.lower() in {'item', 'discussion', 'recommended action'}:
                continue
            projects.add(title)
    return projects

all_projects = set()
for doc in civic:
    all_projects |= find_completed_2022_park_projects(doc.get('text',''))

matched = {p: int(fund_map[p]) for p in all_projects if p in fund_map}
total = int(sum(matched.values()))

out = {'total_funding': total, 'matched_projects': matched, 'unmatched_extracted_projects': sorted([p for p in all_projects if p not in fund_map])}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WWB5hoLLQPARfKgi6461w7sT': ['Funding'], 'var_call_18SqMu3sFkfgtuXiCBontVSP': ['civic_docs'], 'var_call_eIC9RQkWUxJuxTKZvSmWYoxc': 'file_storage/call_eIC9RQkWUxJuxTKZvSmWYoxc.json', 'var_call_s84kqxjOfocZJ8F4wVH0rYf8': 'file_storage/call_s84kqxjOfocZJ8F4wVH0rYf8.json'}

exec(code, env_args)
