code = """import json
import re

# Load the query results stored in the provided storage file paths
with open(var_call_XUBy8XmuJmOI8vXHIz3v37wT, 'r') as f:
    funding = json.load(f)
with open(var_call_KPdyHGx04fGghcaHvIyfkfCj, 'r') as f:
    civic_docs = json.load(f)

# Normalize civic texts combined
texts = [d.get('text','') for d in civic_docs]
combined_text = '\n'.join(texts)
combined_text_lower = combined_text.lower()

# Helper to get base name (remove parenthetical suffixes and trim)
def base_name(name):
    return name.split('(')[0].strip()

# Identify funding rows that are park-related by keywords in project name
park_keywords = ['park', 'playground', 'walkway', 'walkways', 'bluffs', 'trancas', 'point dume', 'malibu bluffs']

# Build list of unique base project names from funding that are park-related
park_funding_rows = []
for row in funding:
    pname = row.get('Project_Name','')
    pname_base = base_name(pname)
    low = pname_base.lower()
    if any(k in low for k in park_keywords):
        # keep original row but include base name and numeric amount
        try:
            amt = int(row.get('Amount'))
        except:
            try:
                amt = int(float(row.get('Amount')))
            except:
                amt = 0
        park_funding_rows.append({'orig_name': pname, 'base_name': pname_base, 'amount': amt})

# For each unique base_name, search in civic docs for evidence of completion in 2022
completed_2022_projects = set()
for row in park_funding_rows:
    bname = row['base_name']
    # search case-insensitive in combined_text; allow partial match of words
    pattern = re.escape(bname.lower())
    if pattern.strip() == '':
        continue
    if re.search(pattern, combined_text_lower):
        # find occurrences and check nearby context for 'completed' and '2022'
        for m in re.finditer(pattern, combined_text_lower):
            start = max(0, m.start()-200)
            end = min(len(combined_text_lower), m.end()+200)
            context = combined_text_lower[start:end]
            if 'completed' in context and '2022' in context:
                completed_2022_projects.add(bname)
                break
            # also check for phrases like 'construction was completed' with 2022 elsewhere in paragraph
            # check paragraph boundaries
            para_start = combined_text_lower.rfind('\n\n', 0, m.start())
            if para_start == -1:
                para_start = max(0, m.start()-500)
            para_end = combined_text_lower.find('\n\n', m.end())
            if para_end == -1:
                para_end = min(len(combined_text_lower), m.end()+500)
            paragraph = combined_text_lower[para_start:para_end]
            if 'completed' in paragraph and '2022' in paragraph:
                completed_2022_projects.add(bname)
                break

# Manually, some projects might be referred to slightly differently; also check some known park projects by explicit mentions
# Search for explicit project titles in civic docs that indicate completion in 2022 and are park-related
extra_matches = []
# find lines that contain 'park' and 'completed' and '2022'
for text in texts:
    lo = text.lower()
    if 'park' in lo and 'completed' in lo and '2022' in lo:
        # extract nearby title: look for line above containing non-empty and not too long
        lines = text.splitlines()
        for i,l in enumerate(lines):
            if 'completed' in l.lower() and '2022' in l.lower():
                # scan up for title
                title = None
                for j in range(i-1, max(-1, i-6), -1):
                    candidate = lines[j].strip()
                    if candidate and len(candidate) < 200:
                        title = candidate
                        break
                if title:
                    extra_matches.append(title.strip())

# Attempt to normalize extra_matches and add to completed set if they match base names
for t in extra_matches:
    tl = t.lower()
    for row in park_funding_rows:
        if row['base_name'].lower() in tl or tl in row['base_name'].lower():
            completed_2022_projects.add(row['base_name'])

# Now sum amounts for all funding rows whose base_name is in completed_2022_projects
total = 0
included_rows = []
for row in park_funding_rows:
    if row['base_name'] in completed_2022_projects:
        total += row['amount']
        included_rows.append(row)

# Prepare output
result = {
    'total_funding_completed_in_2022_for_park_projects': total,
    'completed_project_base_names': sorted(list(completed_2022_projects)),
    'included_funding_rows_count': len(included_rows)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_5hSTdGHQhXk0rZS3ZU1Xb9ji': ['civic_docs'], 'var_call_XUBy8XmuJmOI8vXHIz3v37wT': 'file_storage/call_XUBy8XmuJmOI8vXHIz3v37wT.json', 'var_call_KPdyHGx04fGghcaHvIyfkfCj': 'file_storage/call_KPdyHGx04fGghcaHvIyfkfCj.json'}

exec(code, env_args)
