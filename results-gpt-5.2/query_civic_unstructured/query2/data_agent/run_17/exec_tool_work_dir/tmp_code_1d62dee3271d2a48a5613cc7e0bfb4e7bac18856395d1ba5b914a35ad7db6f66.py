code = """import json, re, pandas as pd

# load civic docs query results
civic = var_call_eIC9RQkWUxJuxTKZvSmWYoxc
if isinstance(civic, str):
    with open(civic, 'r') as f:
        civic = json.load(f)

# load funding aggregation
fund = var_call_s84kqxjOfocZJ8F4wVH0rYf8
if isinstance(fund, str):
    with open(fund, 'r') as f:
        fund = json.load(f)

df_fund = pd.DataFrame(fund)
df_fund['total_amount'] = pd.to_numeric(df_fund['total_amount'], errors='coerce').fillna(0).astype(int)
fund_map = dict(zip(df_fund['Project_Name'], df_fund['total_amount']))

# helper to extract "completed" projects in 2022 from text blocks
# We'll parse each doc for lines like "<Project Name>" then within nearby lines find "Construction was completed" or "Complete Construction" with 2022.
# Also capture park-related by requiring 'park' in project name or nearby context line.

def find_completed_2022_park_projects(text):
    lines = [ln.strip() for ln in text.splitlines()]
    projects = set()
    for i, ln in enumerate(lines):
        if not ln:
            continue
        # candidate project title line: fairly short, not a bullet label
        if len(ln) > 3 and len(ln) < 120 and not re.search(r'^(Updates|Project Schedule|Project Description|Capital Improvement Projects|Disaster Recovery Projects|RECOMMENDED ACTION|DISCUSSION|Page \d+)', ln, re.I):
            window = "\n".join(lines[i:i+20])
            # completed in 2022
            completed_2022 = bool(re.search(r'(?i)(construction\s+was\s+completed[^\n]*2022|complete\s+construction[^\n]*2022|completed[^\n]*2022)', window))
            if not completed_2022:
                continue
            # park-related: park keyword in title or in window
            park_related = ('park' in ln.lower()) or bool(re.search(r'(?i)\bpark\b', window))
            if not park_related:
                continue
            # clean title
            title = re.sub(r'\s{2,}', ' ', ln).strip(' -:\t')
            # exclude obvious non-project words
            if title.lower() in {'item', 'discussion', 'recommended action'}:
                continue
            projects.add(title)
    return projects

all_projects=set()
for doc in civic:
    all_projects |= find_completed_2022_park_projects(doc.get('text',''))

# map to funding: only include titles present in funding_map exactly
matched = {p: fund_map[p] for p in all_projects if p in fund_map}

# compute total
total = int(sum(matched.values()))

out = {
    "total_funding": total,
    "matched_projects": matched,
    "unmatched_extracted_projects": sorted([p for p in all_projects if p not in fund_map])
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_WWB5hoLLQPARfKgi6461w7sT': ['Funding'], 'var_call_18SqMu3sFkfgtuXiCBontVSP': ['civic_docs'], 'var_call_eIC9RQkWUxJuxTKZvSmWYoxc': 'file_storage/call_eIC9RQkWUxJuxTKZvSmWYoxc.json', 'var_call_s84kqxjOfocZJ8F4wVH0rYf8': 'file_storage/call_s84kqxjOfocZJ8F4wVH0rYf8.json'}

exec(code, env_args)
