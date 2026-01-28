code = """import json
import re

# Load data from storage-provided file paths
funding_path = var_call_Ncx1OMYqOJMCIzxbwcw2SGP4
civic_path = var_call_bPrtG60ziMydChYoQ8enDdFc

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(civic_path, 'r', encoding='utf-8') as f:
    civic = json.load(f)

# Helper to normalize strings
def norm(s):
    return re.sub(r"\s+"," ", (s or '').strip()).lower()

# Helper to strip parentheses suffix
def base_name(s):
    m = re.match(r'^(.*?)\s*\(', s)
    if m:
        return m.group(1).strip()
    return s

# Status mapping keywords
completed_kw = ['construction was completed', 'notice of completion', 'complete construction', 'completed', 'completion filed', 'complete:']
design_kw = ['complete design', 'design', 'designs', 'design phase', 'preliminary design', 'finalize the design', 'final design', 'plans and specifications', 'planning', 'design phase']
not_started_kw = ['not started', 'identified', 'will be identified', 'not begun', 'pending', 'awaiting', 'waiting']
under_construction_kw = ['under construction', 'begin construction', 'begin construction:', 'began construction', 'start construction', 'construction:']

results = []

# Precompute civic document lower texts
civic_texts = [doc.get('text','') for doc in civic]
civic_texts_lower = [t.lower() for t in civic_texts]

for rec in funding:
    proj = rec.get('Project_Name','')
    proj_norm = norm(proj)
    candidate = False
    status_found = None

    # If funding project name contains fema or emergency
    if 'fema' in proj_norm or 'emergency' in proj_norm:
        candidate = True

    # Prepare search names: original and base without parenthesis
    names_to_search = [proj, base_name(proj)]

    # Search civic docs for occurrences where doc contains fema/emergency and project name
    for doc_text, doc_text_lower in zip(civic_texts, civic_texts_lower):
        for name in names_to_search:
            if not name:
                continue
            if norm(name) in doc_text_lower:
                # If doc also mentions fema or emergency, mark candidate
                if 'fema' in doc_text_lower or 'emergency' in doc_text_lower:
                    candidate = True
                # Try to extract status from nearby lines
                lines = doc_text.splitlines()
                # find line indices containing the project name
                for i, line in enumerate(lines):
                    if norm(name) in norm(line):
                        # examine window of lines
                        window = ' '.join(lines[max(0,i-3):min(len(lines),i+4)]).lower()
                        # check completed
                        if any(k in window for k in completed_kw):
                            status_found = 'completed'
                            break
                        if any(k in window for k in design_kw):
                            status_found = 'design'
                            break
                        if any(k in window for k in not_started_kw):
                            status_found = 'not started'
                            break
                        if any(k in window for k in under_construction_kw):
                            # map under construction / begin construction as design (in-progress)
                            status_found = 'design'
                            break
                if status_found:
                    break
        if status_found:
            break

    # Also if not found in doc but project name contains 'fema' we still include with unknown status
    if candidate:
        amt = rec.get('Amount')
        try:
            amt_val = int(amt)
        except:
            try:
                amt_val = int(float(amt))
            except:
                amt_val = None
        results.append({
            'Project_Name': rec.get('Project_Name'),
            'Funding_Source': rec.get('Funding_Source'),
            'Amount': amt_val,
            'Status': status_found
        })

# Remove duplicates by Project_Name (keep first)
seen = set()
unique_results = []
for r in results:
    if r['Project_Name'] not in seen:
        unique_results.append(r)
        seen.add(r['Project_Name'])

import json
print("__RESULT__:")
print(json.dumps(unique_results))"""

env_args = {'var_call_Ncx1OMYqOJMCIzxbwcw2SGP4': 'file_storage/call_Ncx1OMYqOJMCIzxbwcw2SGP4.json', 'var_call_bPrtG60ziMydChYoQ8enDdFc': 'file_storage/call_bPrtG60ziMydChYoQ8enDdFc.json'}

exec(code, env_args)
