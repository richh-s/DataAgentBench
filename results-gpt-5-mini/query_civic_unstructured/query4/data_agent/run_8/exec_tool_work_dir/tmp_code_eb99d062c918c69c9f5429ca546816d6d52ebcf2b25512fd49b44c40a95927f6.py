code = """import json, re

# Load civic_docs and funding data from storage file paths
with open(var_call_ImvtIxO2URjGsHAzMP1rhyj0, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_idfh9fUSKTs7w7lMx6A3CPFy, 'r') as f:
    funding = json.load(f)

# Helper to normalize text
def normalize(s):
    return re.sub(r"[^a-z0-9 ]", " ", s.lower()).strip()

# Patterns indicating Spring 2022
spring_patterns = [r"spring\s*2022", r"2022\s*spring", r"2022-?spring", r"march\s*2022", r"april\s*2022", r"may\s*2022", r"2022.*march", r"2022.*april", r"2022.*may"]
spring_regex = re.compile("|".join(spring_patterns), re.I)

# Heuristics for project title lines
title_indicators = re.compile(r"project|improvements|repairs|study|facility|park|road|traffic|master plan|water treatment|storm drain|playground|walkway|slope|retaining wall|resurfacing|median|ramp|curb|culvert|bridge", re.I)

found_projects = []
for doc in civic_docs:
    text = doc.get('text','')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if spring_regex.search(line):
            # look back up to 8 lines to find a title-like line
            for j in range(max(0, i-8), i):
                candidate = lines[j].strip()
                if not candidate:
                    continue
                # skip lines that look like generic headings
                if candidate.lower().startswith(('updates','project schedule','estimated schedule','agenda','discussion','recommend','page')):
                    continue
                # require it to contain a title indicator or end with common nouns
                if title_indicators.search(candidate) or len(candidate.split())<=6 and len(candidate)>5:
                    # Clean candidate
                    cand = re.sub(r"\s+"," ", candidate).strip()
                    # remove leading bullets or punctuation
                    cand = re.sub(r"^[^A-Za-z0-9]+", "", cand)
                    # Avoid very short
                    if len(cand) > 5:
                        found_projects.append({'project_name': cand, 'context_line': line.strip(), 'doc_file': doc.get('filename')})
                        break
            else:
                # If no title found, maybe previous non-empty line
                for j in range(max(0, i-3), i):
                    cand = lines[j].strip()
                    if cand and len(cand)>5:
                        found_projects.append({'project_name': cand, 'context_line': line.strip(), 'doc_file': doc.get('filename')})
                        break

# Deduplicate project names by normalized form
unique_projects = {}
for p in found_projects:
    name = p['project_name']
    n = normalize(name)
    if n not in unique_projects:
        unique_projects[n] = name

extracted_projects = list(unique_projects.values())

# Prepare funding lookup
for row in funding:
    # Ensure Amount int
    try:
        row['Amount'] = int(row['Amount'])
    except:
        try:
            row['Amount'] = int(float(row['Amount']))
        except:
            row['Amount'] = 0

# Normalize funding project names
funding_by_id = {int(r['Funding_ID']): r for r in funding}

# Matching: for each extracted project, find funding rows where tokens overlap or substring match
import math

def tokens(s):
    return set([t for t in normalize(s).split() if len(t)>2])

funding_matches = set()
project_to_matches = {}
for p in extracted_projects:
    ptoks = tokens(p)
    matches = []
    for r in funding:
        fname = r['Project_Name']
        ftoks = tokens(fname)
        # exact or substring
        if normalize(p) == normalize(fname) or normalize(p) in normalize(fname) or normalize(fname) in normalize(p):
            matches.append(int(r['Funding_ID']))
            continue
        # token overlap
        if len(ptoks & ftoks) >= 2:
            matches.append(int(r['Funding_ID']))
    if matches:
        project_to_matches[p] = matches
        for mid in matches:
            funding_matches.add(mid)

# Compute totals
total_funding = sum(funding_by_id[mid]['Amount'] for mid in funding_matches)
project_count = len(extracted_projects)

# Prepare output
result = {'project_count_extracted': project_count, 'projects_extracted': extracted_projects, 'matched_funding_ids': sorted(list(funding_matches)), 'total_funding': total_funding, 'matched_project_to_funding_count': {k: len(v) for k,v in project_to_matches.items()}}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_KqdWzV1kGtTrC5xzCZjIfOZa': ['civic_docs'], 'var_call_duz1lRog2NEIdDlQcwiMkwAU': ['Funding'], 'var_call_ImvtIxO2URjGsHAzMP1rhyj0': 'file_storage/call_ImvtIxO2URjGsHAzMP1rhyj0.json', 'var_call_idfh9fUSKTs7w7lMx6A3CPFy': 'file_storage/call_idfh9fUSKTs7w7lMx6A3CPFy.json'}

exec(code, env_args)
