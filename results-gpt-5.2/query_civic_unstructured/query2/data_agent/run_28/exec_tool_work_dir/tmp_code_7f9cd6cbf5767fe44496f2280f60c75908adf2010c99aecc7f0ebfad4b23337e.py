code = """import json, re, pandas as pd

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

docs = load_records(var_call_zl52m9mn8D1cMBUR9ENZQ8n5)
fund = load_records(var_call_XVHE2S4YMwyqfgnXLhph61QL)

# Build a lookup of funding by project name
fund_df = pd.DataFrame(fund)
if not fund_df.empty:
    fund_df['Total_Amount'] = pd.to_numeric(fund_df['Total_Amount'])
fund_map = dict(zip(fund_df['Project_Name'], fund_df['Total_Amount']))

# Find park-related projects completed in 2022 from documents.
# Heuristic: locate lines like "<Project Name>" followed nearby by "Construction was completed ... 2022" or "completed ... 2022"
# Also include items that look like parks (contain 'Park', 'Playground', 'Bluffs', 'Skate') OR context has 'Park'.

park_keywords = re.compile(r"\b(park|playground|bluffs|skate)\b", re.I)
completed_2022 = re.compile(r"completed[^\n\r]*2022", re.I)

projects = set()

for d in docs:
    text = d.get('text','')
    # Normalize bullet markers and whitespace
    lines = [ln.strip() for ln in re.split(r"\r?\n", text)]
    for i, ln in enumerate(lines):
        if not ln:
            continue
        # Candidate project title lines are relatively short and not generic headers
        if len(ln) > 3 and len(ln) < 120 and not re.search(r"^(updates|project schedule|capital improvement|agenda|page |to:|prepared by:|subject:|recommended action|discussion)\b", ln, re.I):
            if park_keywords.search(ln):
                window = " ".join(lines[i:i+8])
                if completed_2022.search(window):
                    # Remove trailing punctuation
                    pname = re.sub(r"\s{2,}", " ", ln).strip().strip(':')
                    projects.add(pname)

# Sum funding for matched projects (exact name match)
matched = []
total = 0
for p in sorted(projects):
    amt = fund_map.get(p)
    if amt is not None:
        matched.append({'Project_Name': p, 'Funding': int(amt)})
        total += int(amt)
    else:
        matched.append({'Project_Name': p, 'Funding': None})

out = {
    'total_funding_completed_2022_park_related': total,
    'matched_projects': matched,
    'note': 'Funding summed only for projects whose names exactly matched Funding.Project_Name.'
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_VcSoEbEV11tJzvrjgzmhULMm': ['Funding'], 'var_call_B0V2TRekCl6vrNeq0NVAjjNk': ['civic_docs'], 'var_call_zl52m9mn8D1cMBUR9ENZQ8n5': 'file_storage/call_zl52m9mn8D1cMBUR9ENZQ8n5.json', 'var_call_XVHE2S4YMwyqfgnXLhph61QL': 'file_storage/call_XVHE2S4YMwyqfgnXLhph61QL.json'}

exec(code, env_args)
