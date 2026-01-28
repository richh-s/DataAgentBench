code = """import json, re

# Load previous tool results from storage variables
with open(var_call_8NR8DFm3hMApQwlOhrQT5PLi, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)
with open(var_call_n650B47CT6lSGK36pdOukV2G, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Normalize funding records and filter amounts > 50000 just in case
funding = []
for r in funding_records:
    try:
        amt = int(r.get('Amount'))
    except:
        try:
            amt = int(float(r.get('Amount')))
        except:
            continue
    if amt > 50000:
        funding.append({'Project_Name': r.get('Project_Name','').strip(), 'Amount': amt})

# Prepare markers and search for project names within the Capital Improvement Projects (Design) section
design_marker = 'capital improvement projects (design)'
next_markers = [
    'capital improvement projects (construction)',
    'capital improvement projects (not started)',
    'capital improvement projects (completed)',
    'capital improvement projects (construction)',
    'capital improvement projects (design)'
]

matched_projects = set()

# Lowercase mapping of funding project names for matching
funding_names = [f['Project_Name'] for f in funding]
funding_names_lower = [n.lower() for n in funding_names]

for doc in civic_docs:
    text = doc.get('text','')
    if not text:
        continue
    text_lower = text.lower()
    start = text_lower.find(design_marker)
    if start == -1:
        continue
    # find earliest next marker after start
    end_positions = [text_lower.find(m, start+1) for m in next_markers]
    end_positions = [p for p in end_positions if p != -1]
    end = min(end_positions) if end_positions else len(text_lower)
    section = text_lower[start:end]
    # Check each funding project name for presence in the design section
    for orig_name, name_lower in zip(funding_names, funding_names_lower):
        # simple substring match
        if name_lower and name_lower in section:
            matched_projects.add(orig_name)

count = len(matched_projects)

# Prepare output
print("__RESULT__:")
print(json.dumps(count))"""

env_args = {'var_call_8NR8DFm3hMApQwlOhrQT5PLi': 'file_storage/call_8NR8DFm3hMApQwlOhrQT5PLi.json', 'var_call_ey0Eo7AEtMpklSN8fpkF1Ejn': ['civic_docs'], 'var_call_n650B47CT6lSGK36pdOukV2G': 'file_storage/call_n650B47CT6lSGK36pdOukV2G.json'}

exec(code, env_args)
