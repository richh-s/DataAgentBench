code = """import json
import re
import pandas as pd

# Load the large query results from storage file paths
civic_path = var_call_w6K2sAAco6R6XmEszis8v8Tm
funding_path = var_call_89VOBanzqahik56AoT7e1fvl

with open(civic_path, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r', encoding='utf-8') as f:
    funding_rows = json.load(f)

# Convert funding to DataFrame and normalize amounts
fund_df = pd.DataFrame(funding_rows)
# Ensure Amount numeric
fund_df['Total_Amount'] = fund_df['Total_Amount'].astype(int)

# Helper normalization
import string

def normalize_text(s):
    if s is None:
        return ''
    s = s.lower()
    s = re.sub(r"\(.*?\)", "", s)  # remove parenthesis content
    s = re.sub(r"[^a-z0-9\s]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Find project names that have Spring 2022 in nearby schedule lines
spring_patterns = [re.compile(r"spring\s*,?\s*2022", re.I),
                   re.compile(r"2022\s*-\s*spring", re.I),
                   re.compile(r"2022\s+spring", re.I),
                   re.compile(r"spring\s+of\s+2022", re.I)]

candidate_projects = []

for doc in civic_docs:
    text = doc.get('text','')
    # split into lines
    lines = text.splitlines()
    # iterate lines to find spring 2022 occurrences
    for idx, line in enumerate(lines):
        if any(p.search(line) for p in spring_patterns):
            # search backwards up to 8 lines for a likely project title
            found = None
            for back in range(1,9):
                j = idx - back
                if j < 0:
                    break
                candidate = lines[j].strip()
                if not candidate:
                    continue
                # exclude lines that look like headers or metadata
                if re.search(r'page\s+\d+', candidate, re.I):
                    continue
                if len(candidate) < 5 or len(candidate) > 120:
                    continue
                # exclude lines that contain words like 'updates', 'project schedule', 'agenda', 'item', 'meeting', 'discussion', 'recommend', ':'
                low = candidate.lower()
                if any(k in low for k in ['updates', 'project schedule', 'agenda', 'item', 'meeting date', 'discussion', 'recommend', ':', 'prepared by', 'approved by']):
                    continue
                # likely a project name
                found = candidate
                break
            if found:
                candidate_projects.append(found)

# Deduplicate and clean
unique_projects = []
seen = set()
for p in candidate_projects:
    p_clean = re.sub(r"\s+", " ", p).strip()
    if p_clean.lower() not in seen:
        seen.add(p_clean.lower())
        unique_projects.append(p_clean)

# If none found by heuristic above, as fallback search for lines containing 'Advertise: Spring 2022' or 'Begin Construction: Spring 2022' and capture nearby heading
if not unique_projects:
    for doc in civic_docs:
        text = doc.get('text','')
        lines = text.splitlines()
        for idx, line in enumerate(lines):
            if 'spring' in line.lower() and '2022' in line:
                # same backward heuristic
                for back in range(1,12):
                    j = idx - back
                    if j < 0:
                        break
                    candidate = lines[j].strip()
                    if candidate and candidate.lower() not in seen:
                        unique_projects.append(candidate)
                        seen.add(candidate.lower())
                        break

# Now match unique_projects to funding
funding_list = []
for _, row in fund_df.iterrows():
    funding_list.append({'name': row['Project_Name'], 'amount': int(row['Total_Amount']), 'norm': normalize_text(row['Project_Name'])})

results = []
used_funding_indices = set()

for proj in unique_projects:
    norm_proj = normalize_text(proj)
    p_tokens = set(norm_proj.split())
    best = None
    best_score = 0.0
    best_idx = None
    for idx, f in enumerate(funding_list):
        f_tokens = set(f['norm'].split())
        if not p_tokens:
            continue
        inter = p_tokens.intersection(f_tokens)
        if len(inter) == 0:
            # also check substring
            if norm_proj and norm_proj in f['norm']:
                score = 1.0
            else:
                score = 0.0
        else:
            score = len(inter) / len(p_tokens)
        # boost if one contains the other
        if norm_proj and norm_proj == f['norm']:
            score = 1.0
        if norm_proj and norm_proj in f['norm']:
            score = max(score, 0.9)
        if f['norm'] in norm_proj:
            score = max(score, 0.9)
        if score > best_score:
            best_score = score
            best = f
            best_idx = idx
    # decide match threshold
    matched_name = None
    amount = 0
    matched_score = round(best_score, 3)
    if best and best_score >= 0.6:
        matched_name = best['name']
        amount = best['amount']
    # append result
    results.append({'project_name': proj, 'normalized_project': norm_proj, 'matched_funding_name': matched_name, 'amount': amount, 'match_score': matched_score})

# Sum totals
count = len(results)
total_funding = sum(r['amount'] for r in results)

output = {'count': count, 'total_funding': total_funding, 'projects': results}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_THHhbDp8KC4ZreG79yWtSrYZ': ['civic_docs'], 'var_call_XOiKFGOKFoKKfXvxRlDptxuO': ['Funding'], 'var_call_w6K2sAAco6R6XmEszis8v8Tm': 'file_storage/call_w6K2sAAco6R6XmEszis8v8Tm.json', 'var_call_89VOBanzqahik56AoT7e1fvl': 'file_storage/call_89VOBanzqahik56AoT7e1fvl.json'}

exec(code, env_args)
