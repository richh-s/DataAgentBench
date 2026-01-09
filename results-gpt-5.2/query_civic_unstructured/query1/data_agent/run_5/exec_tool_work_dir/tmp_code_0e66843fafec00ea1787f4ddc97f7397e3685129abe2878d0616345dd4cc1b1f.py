code = """import json, re, pandas as pd

# Load civic docs (mongo query result) from file if needed
civic = var_call_dg5JVhfch06pxm1wQfiyAf8c
if isinstance(civic, str):
    with open(civic, 'r', encoding='utf-8') as f:
        civic = json.load(f)

fund = var_call_6HF3oFNFRkfp4Hk7ogXyDhPA
if isinstance(fund, str):
    with open(fund, 'r', encoding='utf-8') as f:
        fund = json.load(f)

fund_names = set(r['Project_Name'] for r in fund)

# Extract design project names from docs using section header patterns
section_re = re.compile(r'\bCapital Improvement Projects\s*\(Design\)\b', re.IGNORECASE)
end_re = re.compile(r'\bCapital Improvement Projects\s*\((?:Construction|Not Started)\)\b|\bDisaster Recovery Projects\b', re.IGNORECASE)

# Heuristic for project line: a standalone line with letters and some punctuation, not bullet/update/schedule
skip_prefixes = ('updates', 'project schedule', 'estimated schedule', 'project description', 'page ', 'agenda item', 'to:', 'prepared by', 'approved by', 'date prepared', 'meeting date', 'subject', 'recommended action', 'discussion', '(cid')

candidate_projects = set()
for doc in civic:
    text = doc.get('text','') or ''
    m = section_re.search(text)
    if not m:
        continue
    sub = text[m.end():]
    m2 = end_re.search(sub)
    if m2:
        sub = sub[:m2.start()]
    # normalize lines
    lines = [ln.strip() for ln in sub.splitlines()]
    for ln in lines:
        if not ln:
            continue
        low = ln.lower()
        if any(low.startswith(p) for p in skip_prefixes):
            continue
        if low.startswith('(') or low.startswith('cid'):
            continue
        # drop bullet artifacts
        ln_clean = re.sub(r'^[\W_]+', '', ln).strip()
        if not ln_clean:
            continue
        # likely headings are short-ish and not contain ':'
        if ':' in ln_clean:
            continue
        # exclude lines that are clearly sentences
        if len(ln_clean.split()) > 12:
            continue
        # must include at least one letter
        if not re.search(r'[A-Za-z]', ln_clean):
            continue
        # Exclude all-caps generic headers
        if ln_clean.lower() in ('capital improvement projects', 'capital improvement projects (design)'):
            continue
        candidate_projects.add(ln_clean)

# Filter to those with funding > 50k (by exact match)
design_with_funding = sorted([p for p in candidate_projects if p in fund_names])

result = {
    'count': len(design_with_funding),
    'projects': design_with_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_8YSPtlxKUqAdVgtYrYZYfHTz': [{'cnt': '276'}], 'var_call_dg5JVhfch06pxm1wQfiyAf8c': 'file_storage/call_dg5JVhfch06pxm1wQfiyAf8c.json', 'var_call_ogMj4TmRt3AwmHHdNOMCPFls': ['Funding'], 'var_call_6HF3oFNFRkfp4Hk7ogXyDhPA': 'file_storage/call_6HF3oFNFRkfp4Hk7ogXyDhPA.json'}

exec(code, env_args)
