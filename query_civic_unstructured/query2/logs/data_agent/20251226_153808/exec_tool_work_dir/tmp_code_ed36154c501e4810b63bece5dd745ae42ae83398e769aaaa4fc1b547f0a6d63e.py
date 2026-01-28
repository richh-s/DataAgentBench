code = """import json

# Load civic docs
with open(var_call_ZGxPsl3QZckLx5Aftdn8Sa0X, 'r') as f:
    civic_docs = json.load(f)

# Function to find title above line index

def find_title(lines, idx):
    for j in range(idx - 1, max(-1, idx - 8), -1):
        cand = lines[j].strip()
        if not cand:
            continue
        cl = cand.lower()
        if (":" in cand) or cl.startswith('updates') or cl.startswith('project schedule') or cl.startswith('estimated schedule') or cl.startswith('project description') or ('agenda item' in cl) or ('page ' in cl) or ('capital improvement projects' in cl) or ('disaster recovery projects' in cl):
            continue
        if len(cand) > 120:
            continue
        return cand
    return None

matches = []
for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.split('\n')
    for i, line in enumerate(lines):
        low = line.lower()
        if ('completed' in low) and ('2022' in line):
            title = find_title(lines, i)
            matches.append({
                'filename': doc.get('filename'),
                'line': line.strip(),
                'title': title,
                'is_park_related': (title.lower().find('park') != -1) or (title.lower().find('playground') != -1) if title else False
            })

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_call_ZGxPsl3QZckLx5Aftdn8Sa0X': 'file_storage/call_ZGxPsl3QZckLx5Aftdn8Sa0X.json', 'var_call_vzEtHYEO2mxMyHPnsAC47tFQ': 'file_storage/call_vzEtHYEO2mxMyHPnsAC47tFQ.json', 'var_call_vPZiNK1ZwTOX2UZ4GF6PIA6T': {'num_docs': 5, 'num_funding': 500}, 'var_call_cZThiOLABlUz6DoiESoT9XnV': {'park_completed_2022_projects': ['Bluffs Park Shade Structure', 'Malibu Park Drainage Improvements'], 'total_funding': 38000}}

exec(code, env_args)
