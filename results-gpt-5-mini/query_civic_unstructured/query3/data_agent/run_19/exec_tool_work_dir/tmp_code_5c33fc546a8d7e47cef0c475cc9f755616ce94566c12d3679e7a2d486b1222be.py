code = """import json
import re

# Load civic docs results
civic_var = var_call_BAS2RGfY0bj1Wd8QeyPkbyl7
funding_var = var_call_KYYyJ3WPdtaRwmCRGz8qjTEz

def load_var(v):
    if isinstance(v, str):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

civic_docs = load_var(civic_var)
funding_records = load_var(funding_var)

# Normalize funding records
for fr in funding_records:
    # ensure fields
    fr['Project_Name'] = fr.get('Project_Name','')
    fr['Funding_Source'] = fr.get('Funding_Source','')
    fr['Amount'] = int(fr.get('Amount') or 0)

# Heuristics to extract project names and statuses near mentions of FEMA or emergency
matches = {}

trigger_pattern = re.compile(r"\b(fema|emergency)\b", re.IGNORECASE)
project_line_pattern = re.compile(r".*Project\b.*|.*project\b.*")

for doc in civic_docs:
    text = doc.get('text','')
    if not text:
        continue
    if not trigger_pattern.search(text):
        continue
    lines = text.splitlines()
    # collapse multiple spaces
    lines = [re.sub(r'\s+', ' ', ln).strip() for ln in lines]
    for i, line in enumerate(lines):
        if trigger_pattern.search(line):
            # search upward for a project title line within 15 lines
            proj_name = None
            proj_idx = None
            for j in range(i, max(i-16, -1), -1):
                l = lines[j]
                if not l:
                    continue
                # prefer lines that contain the word Project (case-insensitive)
                if re.search(r'\bProject\b', l, re.IGNORECASE):
                    proj_name = l
                    proj_idx = j
                    break
                # or lines that look like a title (Title Case and length reasonable)
                if 3 <= len(l.split()) <= 8 and re.match(r'^[A-Z0-9][A-Za-z0-9\s\-\&\/:,]{5,}$', l):
                    proj_name = l
                    proj_idx = j
                    break
            if proj_name is None:
                # fallback: take the preceding non-empty line
                for j in range(i-1, max(i-6,-1), -1):
                    if lines[j]:
                        proj_name = lines[j]
                        proj_idx = j
                        break
            # extract status snippet: look downward for status indicators
            status_snippet = None
            status_idx = None
            for k in range((proj_idx or 0), min(len(lines), (proj_idx or i)+20)):
                l = lines[k]
                if not l:
                    continue
                if re.search(r'updates?:|project schedule:|project is|begin construction|complete construction|complete design|advertise:|in the preliminary design|under construction|awaiting', l, re.IGNORECASE):
                    # gather a few lines around this
                    snippet_lines = [lines[k]]
                    # include next up to 3 lines
                    for kk in range(k+1, min(len(lines), k+4)):
                        if lines[kk]:
                            snippet_lines.append(lines[kk])
                    status_snippet = ' '.join(snippet_lines)
                    status_idx = k
                    break
            # if still none, take the line containing the trigger as status context
            if status_snippet is None:
                status_snippet = line
            if proj_name:
                key = proj_name.strip()
                if key not in matches:
                    matches[key] = {
                        'Project_Name': key,
                        'Status': status_snippet,
                        'Funding_Matches': []
                    }

# Now join with funding records by fuzzy containment
for pname, entry in matches.items():
    pname_low = re.sub(r"\s+"," ", pname.lower())
    found = []
    for fr in funding_records:
        fr_name_low = fr['Project_Name'].lower()
        if pname_low in fr_name_low or fr_name_low in pname_low:
            found.append({'Funding_Project_Name': fr['Project_Name'], 'Funding_Source': fr['Funding_Source'], 'Amount': fr['Amount']})
        else:
            # also match if fr name contains '(fema' or 'fema' and project name shares key tokens
            if 'fema' in fr_name_low and any(tok in fr_name_low for tok in pname_low.split()[:3]):
                found.append({'Funding_Project_Name': fr['Project_Name'], 'Funding_Source': fr['Funding_Source'], 'Amount': fr['Amount']})
    # deduplicate
    unique = { (f['Funding_Project_Name'], f['Funding_Source'], f['Amount']): f for f in found }
    entry['Funding_Matches'] = list(unique.values())

# Prepare final result list
result_list = list(matches.values())

# Sort by Project_Name
result_list = sorted(result_list, key=lambda x: x['Project_Name'])

# Convert non-serializable types
final = []
for r in result_list:
    final.append({
        'Project_Name': r['Project_Name'],
        'Status': r['Status'],
        'Funding_Matches': r['Funding_Matches']
    })

output = json.dumps(final, ensure_ascii=False)
print("__RESULT__:")
print(output)"""

env_args = {'var_call_BAS2RGfY0bj1Wd8QeyPkbyl7': 'file_storage/call_BAS2RGfY0bj1Wd8QeyPkbyl7.json', 'var_call_KYYyJ3WPdtaRwmCRGz8qjTEz': 'file_storage/call_KYYyJ3WPdtaRwmCRGz8qjTEz.json'}

exec(code, env_args)
