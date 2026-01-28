code = """import json
import re

# Load the previous tool results from the storage file paths
with open(var_call_GkmSDQTPWl4imroM1mEpmbPM, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_hmbQbJAU5DGjdddo8bqvJ75p, 'r') as f:
    funding = json.load(f)

# Helper functions
def normalize_name(name):
    if name is None:
        return ''
    name = name.lower()
    # remove parenthetical suffixes like (fema project)
    name = re.sub(r"\(.*?\)", "", name)
    # remove punctuation
    name = re.sub(r"[^a-z0-9\s]", " ", name)
    name = re.sub(r"\s+", " ", name).strip()
    return name

# Build funding records mapping
funding_records = []
for rec in funding:
    pname = rec.get('Project_Name')
    amt = rec.get('Amount')
    try:
        amt_val = int(str(amt))
    except:
        try:
            amt_val = int(float(str(amt)))
        except:
            amt_val = 0
    funding_records.append({'orig_name': pname, 'norm_name': normalize_name(pname), 'amount': amt_val})

# Build a set of candidate project normalized names from funding (to search in docs)
funding_names = set(r['norm_name'] for r in funding_records if r['norm_name'])

# Prepare civic docs texts normalized
docs = []
for d in civic_docs:
    txt = d.get('text','')
    txt_norm = txt.lower()
    docs.append({'filename': d.get('filename'), 'text': txt, 'text_norm': txt_norm})

# Patterns indicating spring 2022
spring_months = ['march', 'mar', 'april', 'apr', 'may']

def has_spring_2022_context(window_text):
    t = window_text.lower()
    if '2022' in t and 'spring' in t:
        return True
    if '2022' in t and any(mon in t for mon in spring_months):
        return True
    # also check formats like 2022-03 or 2022-04 or 2022-05
    if re.search(r'2022[-/]0?3', t) or re.search(r'2022[-/]0?4', t) or re.search(r'2022[-/]0?5', t):
        return True
    if re.search(r'0?3[-/]2022', t) or re.search(r'0?4[-/]2022', t) or re.search(r'0?5[-/]2022', t):
        return True
    return False

# Search for funding project names appearing in docs with spring 2022 context
projects_started_spring_2022 = set()
for fn in funding_names:
    if not fn:
        continue
    for doc in docs:
        idx = doc['text_norm'].find(fn)
        if idx != -1:
            # examine a window around the match
            start = max(0, idx-500)
            end = min(len(doc['text_norm']), idx+500)
            window = doc['text_norm'][start:end]
            if has_spring_2022_context(window):
                projects_started_spring_2022.add(fn)
                break
        else:
            # maybe project name words are split; try fuzzy: all words present in doc
            words = fn.split()
            if words and all(w in doc['text_norm'] for w in words[:3]):
                # get first occurrence of first word
                idx2 = doc['text_norm'].find(words[0])
                if idx2!=-1:
                    start = max(0, idx2-500)
                    end = min(len(doc['text_norm']), idx2+500)
                    window = doc['text_norm'][start:end]
                    if has_spring_2022_context(window):
                        projects_started_spring_2022.add(fn)
                        break

# Now match funding records whose normalized name is in projects_started_spring_2022
matched_funding = [r for r in funding_records if r['norm_name'] in projects_started_spring_2022]

# For safety, also try to match doc-extracted names that may not be exact: search docs for patterns like "Begin Construction: Spring 2022" and extract preceding project name lines
# Extract simple project titles from docs by finding lines followed by "Project" and then check nearby spring 2022
additional_projects = set()
for doc in docs:
    lines = doc['text'].splitlines()
    for i, line in enumerate(lines):
        low = line.lower()
        if any(k in low for k in ['begin construction', 'advertise', 'complete design', 'project schedule', 'project schedule:']):
            # look backward up to 3 lines for a project title
            snippet = '\n'.join(lines[max(0,i-3):i+1])
            if '2022' in snippet and any(mon in snippet.lower() for mon in spring_months) or ('spring' in snippet.lower() and '2022' in snippet.lower()):
                # try to find a project name in previous lines
                for j in range(max(0,i-3), i):
                    candidate = lines[j].strip()
                    if len(candidate)>3 and len(candidate)<200:
                        cand_norm = normalize_name(candidate)
                        if cand_norm:
                            additional_projects.add(cand_norm)

# Add any additional projects that appear in funding names
for ap in additional_projects:
    if ap in funding_names:
        projects_started_spring_2022.add(ap)

# Compute unique project count and total funding
unique_projects = sorted(list(projects_started_spring_2022))
count = len(unique_projects)
# Sum funding amounts for all funding records whose normalized name matches any project in set
total = sum(r['amount'] for r in funding_records if r['norm_name'] in projects_started_spring_2022)

# Prepare readable mapping of project original names discovered (list original names corresponding to normalized)
orig_names = {}
for r in funding_records:
    if r['norm_name'] in projects_started_spring_2022:
        orig_names.setdefault(r['norm_name'], []).append({'orig_name': r['orig_name'], 'amount': r['amount']})

result = {
    'count': count,
    'total_funding': total,
    'projects_normalized': unique_projects,
    'projects_details': orig_names
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_9HODkiC8wjfGKJrxlQ5AIKcj': ['civic_docs'], 'var_call_ECY4K9fE4JT46s2M7ZcBZ68U': ['Funding'], 'var_call_GkmSDQTPWl4imroM1mEpmbPM': 'file_storage/call_GkmSDQTPWl4imroM1mEpmbPM.json', 'var_call_hmbQbJAU5DGjdddo8bqvJ75p': 'file_storage/call_hmbQbJAU5DGjdddo8bqvJ75p.json'}

exec(code, env_args)
