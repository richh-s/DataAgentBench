code = """import json
import re

# Load data from storage-provided file paths
with open(var_call_3V3LBuTrnTf5FD8CAnAfAlHL, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

with open(var_call_NT3Q3dsTFn3mJHGGbLBIEHZH, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Prepare funding records
for r in funding:
    # ensure Amount is int
    try:
        r['Amount'] = int(r['Amount'])
    except:
        # fallback if non-numeric
        r['Amount'] = 0

# Combine all civic texts into one large string for searching
all_text = "\n".join([doc.get('text','') for doc in civic_docs])

# lower-case version for case-insensitive search
all_text_lower = all_text.lower()

# disaster keywords
disaster_keywords = ['fema', 'caloes', 'caloja', 'caljpia', 'disaster', 'recovery', 'fire', 'woolsey', 'emergency']

def is_disaster_related(proj_name, context):
    name_low = proj_name.lower()
    # check project name for keywords
    for kw in disaster_keywords:
        if kw in name_low:
            return True
    # check context
    for kw in disaster_keywords:
        if kw in context.lower():
            return True
    return False

# function to check if 'start' date in context contains 2022
def context_has_2022_start(context):
    # look for phrases like Begin, Start, Advertise, Planned, Construction was started, Complete
    patterns = [r'(begin\s+construction\s*:\s*[^\\n]{0,80}2022)',
                r'(begin\s+construction\s*:\s*[^\\n]{0,80}2022)',
                r'(begin\s+construction\s*:\s*[^\\n]{0,80}2022)',
                r'(advertise\s*:\s*[^\\n]{0,80}2022)',
                r'(complete\s+construction\s*:\s*[^\\n]{0,80}2022)',
                r'(begin\s+construction\s*:\s*[^\\n]{0,80}2022)',
                r'\b2022\b']
    ctx_low = context.lower()
    # If any of these patterns match within the small context, consider it started in 2022
    for pat in patterns:
        if re.search(pat, ctx_low):
            return True
    return False

# For each funding project, search for occurrences in civic text and check conditions
matched_projects = []

for rec in funding:
    proj = rec['Project_Name']
    proj_low = proj.lower()
    # find occurrences of project name in civic text
    occurrences = [m.start() for m in re.finditer(re.escape(proj_low), all_text_lower)]
    found = False
    for pos in occurrences:
        # get context window after occurrence
        start = max(0, pos)
        end = min(len(all_text_lower), pos + 400)
        context = all_text[start:end]
        # check if context has 2022 indicating start or schedule
        if context_has_2022_start(context):
            # check disaster relation either by name or context
            if is_disaster_related(proj, context):
                matched_projects.append(rec)
                found = True
                break
            else:
                # even if name doesn't include keywords, check further nearby for disaster keywords
                # expand context
                start2 = max(0, pos-200)
                end2 = min(len(all_text_lower), pos+800)
                context2 = all_text[start2:end2]
                if is_disaster_related(proj, context2):
                    matched_projects.append(rec)
                    found = True
                    break
    # If no direct occurrence, also check if project name without parentheses version appears
    if not found:
        # strip parenthetical parts from project name
        base = re.sub(r"\s*\(.*?\)", "", proj).strip().lower()
        if base != proj_low:
            occurrences = [m.start() for m in re.finditer(re.escape(base), all_text_lower)]
            for pos in occurrences:
                start = max(0, pos)
                end = min(len(all_text_lower), pos + 400)
                context = all_text[start:end]
                if context_has_2022_start(context):
                    if is_disaster_related(proj, context):
                        matched_projects.append(rec)
                        found = True
                        break
                    else:
                        start2 = max(0, pos-200)
                        end2 = min(len(all_text_lower), pos+800)
                        context2 = all_text[start2:end2]
                        if is_disaster_related(proj, context2):
                            matched_projects.append(rec)
                            found = True
                            break

# As a fallback, also include any funding rows whose project name itself contains disaster keywords and whose funding record project name contains '2022' (rare) or check civic docs for any mention of project plus '2022' anywhere
for rec in funding:
    if rec in matched_projects:
        continue
    proj = rec['Project_Name']
    if any(kw in proj.lower() for kw in ['fema', 'caloes', 'caljpia']):
        # check if proj (or base) appears anywhere near '2022' in the civic docs
        if re.search(re.escape(proj.lower()) + r'.{0,200}2022', all_text_lower):
            matched_projects.append(rec)
        else:
            base = re.sub(r"\s*\(.*?\)", "", proj).strip().lower()
            if re.search(re.escape(base) + r'.{0,200}2022', all_text_lower):
                matched_projects.append(rec)

# Remove duplicates
unique = {}
for r in matched_projects:
    unique[r['Project_Name']] = r
matched = list(unique.values())

# Sum amounts
total = sum(r['Amount'] for r in matched)

# Prepare output details (list of matched project names and amounts) for transparency
output = {
    'total_funding': total,
    'matched_projects': [{ 'Project_Name': r['Project_Name'], 'Amount': r['Amount']} for r in matched]
}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_ewZx9GEvkYHuhFSdepF0EpJu': ['civic_docs'], 'var_call_P0nG1k5Ak7Vdxl9PloiZ7Cjc': ['Funding'], 'var_call_3V3LBuTrnTf5FD8CAnAfAlHL': 'file_storage/call_3V3LBuTrnTf5FD8CAnAfAlHL.json', 'var_call_NT3Q3dsTFn3mJHGGbLBIEHZH': 'file_storage/call_NT3Q3dsTFn3mJHGGbLBIEHZH.json'}

exec(code, env_args)
