code = """import json
import re

# Load the query results from storage variables
data_civic_path = var_call_LhusFwiiC92wk9UY7MUz509q
data_funding_path = var_call_oY9gDMHt3GJrCXCdBDuHEWyC

# Read the JSON files if paths provided
if isinstance(data_civic_path, str):
    with open(data_civic_path, 'r', encoding='utf-8') as f:
        civic_docs = json.load(f)
else:
    civic_docs = data_civic_path

if isinstance(data_funding_path, str):
    with open(data_funding_path, 'r', encoding='utf-8') as f:
        funding = json.load(f)
else:
    funding = data_funding_path

# Helper normalize
def normalize_name(s):
    s = s or ''
    s = s.strip()
    # remove parenthetical suffixes
    s = re.sub(r"\(.*?\)", "", s)
    s = s.lower()
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()

# Detect schedule-related lines that indicate Spring 2022
spring_terms = ['spring']
months = ['march', 'mar', 'april', 'apr', 'may']

def line_indicates_spring_2022(line):
    if not line:
        return False
    low = line.lower()
    if '2022' in low and 'spring' in low:
        return True
    # cases like 'spring 2022' with comma
    if re.search(r'spring[,\s]+2022', low):
        return True
    # '2022-spring'
    if '2022-spring' in low or '2022 spring' in low:
        return True
    # months with 2022
    for m in months:
        if m in low and '2022' in low:
            return True
    # phrases like 'begin construction: spring 2022' (covered) or 'advertise: spring 2022'
    # also handle 'spring, 2022'
    if re.search(r'spring\s*,\s*2022', low):
        return True
    return False

# Extract project names that have schedule lines indicating Spring 2022
projects_spring_2022 = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    # iterate through lines
    for i, line in enumerate(lines):
        if line_indicates_spring_2022(line):
            # find nearest project title above this line
            j = i-1
            # move up skipping empty or small lines or lines indicating updates/notes
            while j >= 0:
                candidate = lines[j].strip()
                if not candidate:
                    j -= 1
                    continue
                lowc = candidate.lower()
                # skip lines that are likely not titles
                if lowc.startswith('(cid:') or lowc.startswith('updates') or lowc.startswith('project schedule') or lowc.startswith('project description') or lowc.startswith('project updates') or lowc.startswith('agenda item') or lowc.startswith('page'):
                    j -= 1
                    continue
                # if candidate looks like a header (has at least 3 words and not all lowercase short words)
                if len(candidate.split()) >= 2:
                    projects_spring_2022.add(candidate.strip())
                    break
                j -= 1
        else:
            # also check lines that explicitly say 'Begin Construction:' etc and contain Spring 2022 nearby
            low = line.lower()
            if any(k in low for k in ['begin construction', 'advertise', 'complete design', 'complete construction', 'estimate', 'estimated schedule', 'project schedule', 'begin construction:']) and ('spring' in low and '2022' in low):
                j = i-1
                while j >= 0:
                    candidate = lines[j].strip()
                    if not candidate:
                        j -= 1
                        continue
                    lowc = candidate.lower()
                    if lowc.startswith('(cid:') or lowc.startswith('updates') or lowc.startswith('project schedule') or lowc.startswith('project description') or lowc.startswith('project updates') or lowc.startswith('agenda item') or lowc.startswith('page'):
                        j -= 1
                        continue
                    if len(candidate.split()) >= 2:
                        projects_spring_2022.add(candidate.strip())
                        break
                    j -= 1

# As a fallback, also search for project blocks like lines that look like project titles followed within next 6 lines by spring 2022
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        candidate = line.strip()
        if not candidate:
            continue
        lowc = candidate.lower()
        if lowc.startswith('(cid:'):
            continue
        if len(candidate.split()) < 2:
            continue
        # look ahead
        block = ' '.join(lines[i+1:i+8]).lower()
        if line_indicates_spring_2022(block):
            projects_spring_2022.add(candidate.strip())

# Normalize project names
projects_list = sorted(list(projects_spring_2022))
# Prepare funding records mapping
funding_records = funding
# Build normalized funding name to records mapping
from collections import defaultdict
fund_map = defaultdict(list)
for rec in funding_records:
    name = rec.get('Project_Name', '')
    norm = normalize_name(name)
    # store original amount as int
    try:
        amt = int(rec.get('Amount', 0))
    except:
        try:
            amt = int(float(rec.get('Amount', 0)))
        except:
            amt = 0
    fund_map[norm].append({'orig_name': name, 'amount': amt})

# For matching, prepare a list of funding normalized names
funding_norms = list(fund_map.keys())

matched_projects = []
matched_funding_records = []

for pname in projects_list:
    pnorm = normalize_name(pname)
    matched = False
    # exact match
    if pnorm in fund_map:
        matched = True
        matched_projects.append(pname)
        matched_funding_records.extend(fund_map[pnorm])
        continue
    # containment matches
    for fn in funding_norms:
        if pnorm and (pnorm in fn or fn in pnorm):
            matched = True
            matched_projects.append(pname)
            matched_funding_records.extend(fund_map[fn])
            break
    if matched:
        continue
    # token overlap heuristic: if majority of significant tokens in pname appear in funding name
    p_tokens = [t for t in pnorm.split() if len(t) > 3]
    for fn in funding_norms:
        if not p_tokens:
            continue
        count = sum(1 for t in p_tokens if t in fn)
        if count >= max(1, len(p_tokens)//2):
            matched = True
            matched_projects.append(pname)
            matched_funding_records.extend(fund_map[fn])
            break

# Deduplicate matched projects list
matched_projects = sorted(list(set(matched_projects)))

# Sum funding amounts, deduplicate funding records by orig_name to avoid double counting same funding entry if matched multiple ways
seen = set()
total = 0
for rec in matched_funding_records:
    key = (rec['orig_name'], rec['amount'])
    if key in seen:
        continue
    seen.add(key)
    total += rec['amount']

result = {'count': len(matched_projects), 'total_funding': total, 'projects': matched_projects}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_LhusFwiiC92wk9UY7MUz509q': 'file_storage/call_LhusFwiiC92wk9UY7MUz509q.json', 'var_call_oY9gDMHt3GJrCXCdBDuHEWyC': 'file_storage/call_oY9gDMHt3GJrCXCdBDuHEWyC.json'}

exec(code, env_args)
