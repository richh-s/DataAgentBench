code = """import re, json, pandas as pd

# Load full civic docs
path_docs = var_call_eQAIe9y9YkspmXUSaoAjAcQT
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

texts = ' '.join(doc['text'] for doc in civic_docs)

# Heuristic: list of known project names to search around dates
project_patterns = [
    '2022 Morning View Resurfacing & Storm Drain Improvements',
    'PCH Median Improvements Project',
    'Westward Beach Road Repair Project',
    'Westward Beach Road Drainage Improvements Project',
    'Clover Heights Storm Drainage Improvements',
    'Latigo Canyon Road Retaining Wall Repair Project',
    'Storm Drain Master Plan',
    'Trancas Canyon Park Upper and Lower Slopes Repair',
    'Civic Center Water Treatment Facility Phase 2',
    'Permanent Skate Park',
    'PCH at Trancas Canyon Road Right Turn Lane',
    'Outdoor Warning Signs',
    'Malibu Bluffs Park South Walkway Repairs',
    'Trancas Canyon Park Playground',
    'Malibu Canyon Road Traffic Study',
    'Malibu Road Slope Repairs',
    'Encinal Canyon Road Repairs',
    'PCH Signal Synchronization System Improvements Project',
    'Storm Drain Trash Screens Phase Two',
    'Bluffs Park Shade Structure',
    'Marie Canyon Green Streets',
    'Broad Beach Road Water Quality Repair',
    'Point Dume Walkway Repairs',
]

# We will search for patterns like 'Begin Construction: Spring 2022' or 'Start: Spring 2022'
results = []
for name in project_patterns:
    # Find a window of text around the project name
    for m in re.finditer(re.escape(name), texts):
        start = max(0, m.start()-400)
        end = m.end()+400
        window = texts[start:end]
        # Look for "Begin Construction" or "Advertise" or similar with Spring 2022
        for label in ['Begin Construction', 'Begin construction', 'Start', 'Advertise', 'Complete Design', 'Final Design', 'Estimated Schedule']:
            pattern = label + r'.{0,40}?Spring 2022'
            if re.search(pattern, window):
                results.append({'Project_Name': name, 'context': window})
                break

# Load funding table
path_fund = var_call_HRJLhpzZTIp2SgwcD3VGF8vx
with open(path_fund, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

spring_projects = sorted({r['Project_Name'] for r in results})

matched = fund_df[fund_df['Project_Name'].isin(spring_projects)]

answer = {
    'spring_2022_projects': spring_projects,
    'count': int(len(spring_projects)),
    'total_funding': int(matched['Amount'].sum())
}

out = json.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_eQAIe9y9YkspmXUSaoAjAcQT': 'file_storage/call_eQAIe9y9YkspmXUSaoAjAcQT.json', 'var_call_HRJLhpzZTIp2SgwcD3VGF8vx': 'file_storage/call_HRJLhpzZTIp2SgwcD3VGF8vx.json'}

exec(code, env_args)
