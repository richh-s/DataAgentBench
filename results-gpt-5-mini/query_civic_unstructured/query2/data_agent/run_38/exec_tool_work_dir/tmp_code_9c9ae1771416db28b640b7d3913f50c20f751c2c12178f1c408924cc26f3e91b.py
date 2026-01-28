code = """import json, re

# Load the large results from storage file paths
with open(var_call_UnYOruakbLEubMPEjdnbIbFN, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)
with open(var_call_0VlHSAjA8oAeNXBPOEXNwXzf, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Normalize funding entries and find park-related projects in funding table
park_funding = []
for entry in funding:
    name = entry.get('Project_Name', '')
    if 'park' in name.lower():
        try:
            amt = int(entry.get('Amount') or 0)
        except:
            try:
                amt = int(float(entry.get('Amount')))
            except:
                amt = 0
        park_funding.append({'Funding_ID': entry.get('Funding_ID'), 'Project_Name': name, 'Amount': amt})

# Build lowercase project name set for substring matching
park_names = [p['Project_Name'].lower() for p in park_funding]

matched = []
matched_names = set()

# Search civic documents for lines indicating completion in 2022 that mention parks or park project names
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for line in lines:
        low = line.lower()
        if 'completed' in low and '2022' in line:
            # If the line mentions park or any known park project name, try to match
            if 'park' in low or any(pn in low for pn in park_names):
                for p in park_funding:
                    if p['Project_Name'].lower() in low:
                        matched.append(p)
                        matched_names.add(p['Project_Name'])
                # Also if generic 'bluffs park shade structure' might appear as 'Bluffs Park Shade Structure'
                # try token-based fuzzy match: check if all words of project name appear
                for p in park_funding:
                    name_low = p['Project_Name'].lower()
                    # skip if already matched
                    if p['Project_Name'] in matched_names:
                        continue
                    words = [w for w in re.split(r'[^a-z0-9]+', name_low) if w]
                    if words and all(w in low for w in words[:3]):
                        matched.append(p)
                        matched_names.add(p['Project_Name'])

# Additionally, some projects might be mentioned with 'Construction was completed, November 2022' but project name earlier
# Search for lines that contain both 'completed' and '2022' and then look nearby (previous 3 lines) for a park project name
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for idx, line in enumerate(lines):
        low = line.lower()
        if 'completed' in low and '2022' in line:
            # examine this line and previous 3 lines for park project names
            context = ' '.join(lines[max(0, idx-3): idx+1]).lower()
            for p in park_funding:
                if p['Project_Name'].lower() in context and p['Project_Name'] not in matched_names:
                    matched.append(p)
                    matched_names.add(p['Project_Name'])
            # also check for 'malibu bluffs park' mapping to 'Malibu Bluffs Park South Walkway Repairs' etc.
            for p in park_funding:
                name_low = p['Project_Name'].lower()
                if any(phrase in context for phrase in [name_low, 'bluffs park', 'malibu park', 'legacy park']):
                    if p['Project_Name'] not in matched_names and any(w in context for w in name_low.split()[:2]):
                        matched.append(p)
                        matched_names.add(p['Project_Name'])

# Deduplicate matched by Project_Name
unique_matched = {}
for p in matched:
    unique_matched[p['Project_Name']] = p

matched_list = list(unique_matched.values())

# Compute total
total = sum(p['Amount'] for p in matched_list)

# Prepare result
result = {'matched_projects': matched_list, 'total_funding': total}

import json
print("----BEGIN PRINT FORMAT----")
print("print(\"__RESULT__:\")")
print("print('" + json.dumps(result).replace("'", "\\'") + "')")
print("----END PRINT FORMAT----")"""

env_args = {'var_call_TenNsadP4ijMxU8ivUzpD1p8': [], 'var_call_E02bb2NNu0gqPdDQNnqjE30V': ['civic_docs'], 'var_call_UnYOruakbLEubMPEjdnbIbFN': 'file_storage/call_UnYOruakbLEubMPEjdnbIbFN.json', 'var_call_59Lp1s5RndrufOMad3wuudAj': ['Funding'], 'var_call_0VlHSAjA8oAeNXBPOEXNwXzf': 'file_storage/call_0VlHSAjA8oAeNXBPOEXNwXzf.json'}

exec(code, env_args)
