code = """import json

# Load funding records from storage
path_funding = var_call_T8BHlZ9tQf77BgFKlNo1MHHl
with open(path_funding, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Ensure amounts are integers
for r in funding:
    try:
        r['Amount'] = int(r.get('Amount', 0))
    except:
        r['Amount'] = int(''.join(ch for ch in str(r.get('Amount', '0')) if ch.isdigit()) or 0)

# Manually extracted list of projects under 'Capital Improvement Projects (Design)'
design_projects = [
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
    'Malibu Canyon Road Traffic Study'
]

# Filter funding records > 50000
funding_filtered = [r for r in funding if r['Amount'] > 50000]

# Normalization helper
import string
allowed = set(string.ascii_lowercase + string.digits + ' ')
def normalize(s):
    s2 = s.lower()
    return ''.join(ch if ch in allowed else ' ' for ch in s2).split()

# Match design projects to funding by name similarity
matches = []
for dp in design_projects:
    dp_tokens = set(normalize(dp))
    for rec in funding_filtered:
        fn_tokens = set(normalize(rec['Project_Name']))
        # exact substring match on normalized joined tokens
        dp_join = ' '.join(normalize(dp))
        fn_join = ' '.join(normalize(rec['Project_Name']))
        if dp_join and (dp_join in fn_join or fn_join in dp_join):
            matches.append((dp, rec['Project_Name'], rec['Amount']))
            break
        # token overlap: at least half of smaller token set
        smaller = min(len(dp_tokens), len(fn_tokens))
        if smaller > 0 and len(dp_tokens & fn_tokens) >= max(1, smaller//2):
            matches.append((dp, rec['Project_Name'], rec['Amount']))
            break

unique_matched = sorted({m[0] for m in matches})
count = len(unique_matched)

output = {'count': count, 'matched_projects': unique_matched, 'matches_details': matches}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_rqBzkI0CJk86xb78roGc5I8P': ['civic_docs'], 'var_call_wqKExuccBtopMDlIMCAbedXd': ['Funding'], 'var_call_T8BHlZ9tQf77BgFKlNo1MHHl': 'file_storage/call_T8BHlZ9tQf77BgFKlNo1MHHl.json', 'var_call_N83ujLeP76Yi7NfYvJUwtHH5': 'file_storage/call_N83ujLeP76Yi7NfYvJUwtHH5.json'}

exec(code, env_args)
