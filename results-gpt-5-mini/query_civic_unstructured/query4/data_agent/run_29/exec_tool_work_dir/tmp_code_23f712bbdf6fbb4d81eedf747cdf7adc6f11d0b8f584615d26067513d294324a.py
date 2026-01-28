code = """import json, re
# Load the civic docs and funding data from storage file paths
with open(var_call_eY6MrH3yMduMhdp7Od4wxifW, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_mfhhNhnlDRowwEHz4PEUqpDB, 'r') as f:
    funding = json.load(f)

# Normalize funding amounts and build list of project names
for rec in funding:
    # convert Amount to int
    try:
        rec['Amount'] = int(rec.get('Amount') if rec.get('Amount') is not None else 0)
    except:
        # remove non-digits
        s = re.sub(r"[^0-9]", "", str(rec.get('Amount', '0')))
        rec['Amount'] = int(s) if s!='' else 0

funding_by_name = {}
for rec in funding:
    name = rec.get('Project_Name', '').strip()
    if name:
        funding_by_name.setdefault(name, 0)
        funding_by_name[name] += rec.get('Amount', 0)

project_names = list(funding_by_name.keys())

# Regex to detect Spring 2022 or March/April/May 2022
spring_pattern = re.compile(r"(Spring\s*2022|2022\s*Spring|2022-?03|2022-?04|2022-?05|March\s*2022|April\s*2022|May\s*2022|2022-March|2022-April|2022-May)", re.I)

matched_projects = set()

# For each project name in funding, search the civic docs texts for occurrences
for pname in project_names:
    pname_re = re.compile(re.escape(pname), re.I)
    found = False
    for doc in civic_docs:
        text = doc.get('text','')
        # quick check
        if not re.search(pname_re, text):
            continue
        # split into lines and search for lines near the match
        lines = text.splitlines()
        # find line indices containing the project name
        indices = [i for i,l in enumerate(lines) if re.search(pname_re, l)]
        # if none, attempt to find in the whole text and approximate by character index
        if not indices:
            for m in re.finditer(pname_re, text):
                # find line index by counting newlines before match
                idx = text.count('\n', 0, m.start())
                indices.append(idx)
        # For each index, check a window of nearby lines for spring pattern
        for idx in indices:
            window = '\n'.join(lines[max(0, idx-6): idx+7])
            if re.search(spring_pattern, window):
                # Ensure it's about a start/begin schedule nearby
                # Look for words that indicate start/time (Begin, Advertise, Start, Complete Design, Estimated Schedule)
                if re.search(r"\b(Begin|Begin Construction|Advertise|Start(?:ed|ing)?|Estimated Schedule|Project Schedule|Complete Design)\b", window, re.I):
                    matched_projects.add(pname)
                    found = True
                    break
                else:
                    # even if no explicit start word, if spring term is in close proximity, include
                    matched_projects.add(pname)
                    found = True
                    break
        if found:
            break

# Compute count and total funding
matched_list = sorted(list(matched_projects))
count = len(matched_list)
total = sum(funding_by_name[n] for n in matched_list)

result = {
    'count': count,
    'total_funding': total,
    'projects': matched_list
}

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NxzWWT5KvvxnzaNw09EloWJH': ['civic_docs'], 'var_call_zdTWCxg3xHrmDB2Vw93UB0ER': ['Funding'], 'var_call_kiS82EWlxpy6moSmreVncFDG': [], 'var_call_eY6MrH3yMduMhdp7Od4wxifW': 'file_storage/call_eY6MrH3yMduMhdp7Od4wxifW.json', 'var_call_mfhhNhnlDRowwEHz4PEUqpDB': 'file_storage/call_mfhhNhnlDRowwEHz4PEUqpDB.json'}

exec(code, env_args)
