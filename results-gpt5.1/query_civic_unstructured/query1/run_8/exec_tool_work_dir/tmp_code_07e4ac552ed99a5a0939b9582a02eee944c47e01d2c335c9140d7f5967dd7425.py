code = """import re, json

funding_records = var_call_fZwVzoqbNV63YP7IMGxsaKtN
civic_preview = var_call_fhcrm31wd4b0nbzY2Tue6YFW

texts = [d['text'] for d in civic_preview]
full_text = '\n'.join(texts)

sections = re.split(r'Capital Improvement Projects \(Design\)', full_text, flags=re.IGNORECASE)
if len(sections) < 2:
    design_block = full_text
else:
    design_block = sections[1]

end_match = re.search(r'Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\)', design_block, flags=re.IGNORECASE)
if end_match:
    design_block = design_block[:end_match.start()]

capital_design_projects = [
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

funding_names = set()
for rec in funding_records:
    name = rec['Project_Name']
    amt = int(rec['Amount']) if isinstance(rec['Amount'], str) else rec['Amount']
    if amt > 50000:
        funding_names.add(name)

count = 0
for p in capital_design_projects:
    if p in funding_names:
        count += 1

print('__RESULT__:')
print(json.dumps(count))"""

env_args = {'var_call_fZwVzoqbNV63YP7IMGxsaKtN': 'file_storage/call_fZwVzoqbNV63YP7IMGxsaKtN.json', 'var_call_fhcrm31wd4b0nbzY2Tue6YFW': 'file_storage/call_fhcrm31wd4b0nbzY2Tue6YFW.json'}

exec(code, env_args)
