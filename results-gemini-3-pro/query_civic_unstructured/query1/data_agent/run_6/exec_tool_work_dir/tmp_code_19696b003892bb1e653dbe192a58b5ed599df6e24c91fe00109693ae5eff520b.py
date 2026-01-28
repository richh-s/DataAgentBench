code = """# Re-run matching with substring logic to see if we missed any obvious ones
import json

with open(locals()['var_function-call-10013282059874824067'], 'r') as f:
    funding_data = json.load(f)

extracted_names = locals()['var_function-call-13744913590369230901']['design_projects_found']
matches = locals()['var_function-call-13744913590369230901']['matches']
matches_set = set(matches)

potential_matches = []
funding_map = {item['Project_Name']: item['Amount'] for item in funding_data if float(item['Amount']) > 50000}

for name in extracted_names:
    if name in matches_set:
        continue
    # Check against funding names
    for fname in funding_map:
        if fname in name or name in fname:
            potential_matches.append((name, fname, funding_map[fname]))

print("__RESULT__:")
print(json.dumps(potential_matches))"""

env_args = {'var_function-call-10013282059874824067': 'file_storage/function-call-10013282059874824067.json', 'var_function-call-10013282059874822964': 'file_storage/function-call-10013282059874822964.json', 'var_function-call-14944349868689513364': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}], 'var_function-call-13744913590369230901': {'design_projects_found': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'PCH Median Improvements Project', 'Westward Beach Road Repair Project', 'Westward Beach Road Drainage Improvements Project', 'Clover Heights Storm Drainage Improvements', 'Latigo Canyon Road Retaining Wall Repair Project', 'Storm Drain Master Plan', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Civic Center Water Treatment Facility Phase 2', 'Permanent Skate Park', 'PCH at Trancas Canyon Road Right Turn Lane', 'Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway Repairs', 'Trancas Canyon Park Playground', 'Malibu Canyon Road Traffic Study', 'feasible traffic safety improvements can be constructed at this location.'], 'matches': ['PCH Median Improvements Project', 'Westward Beach Road Drainage Improvements Project', 'Latigo Canyon Road Retaining Wall Repair Project', 'Storm Drain Master Plan', 'Permanent Skate Park', 'PCH at Trancas Canyon Road Right Turn Lane', 'Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway Repairs', 'Malibu Canyon Road Traffic Study'], 'count': 9}}

exec(code, env_args)
