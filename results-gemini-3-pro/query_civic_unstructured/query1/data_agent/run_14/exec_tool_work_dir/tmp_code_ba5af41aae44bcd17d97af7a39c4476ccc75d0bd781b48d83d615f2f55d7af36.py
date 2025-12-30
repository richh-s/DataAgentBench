code = """import json

# Load data
with open(locals()['var_function-call-14769478683806682002'], 'r') as f:
    funding_data = json.load(f)

# Previous matches
prev_result = json.loads('''{"matches": ["PCH Median Improvements Project", "Westward Beach Road Drainage Improvements Project", "Latigo Canyon Road Retaining Wall Repair Project", "Storm Drain Master Plan", "Permanent Skate Park", "PCH at Trancas Canyon Road Right Turn Lane", "Outdoor Warning Signs", "Malibu Bluffs Park South Walkway Repairs", "Malibu Canyon Road Traffic Study"], "extracted_names": ["2022 Morning View Resurfacing & Storm Drain Improvements", "PCH Median Improvements Project", "Westward Beach Road Repair Project", "Westward Beach Road Drainage Improvements Project", "Clover Heights Storm Drainage Improvements", "Latigo Canyon Road Retaining Wall Repair Project", "Storm Drain Master Plan", "Trancas Canyon Park Upper and Lower Slopes Repair", "Civic Center Water Treatment Facility Phase 2", "Permanent Skate Park", "PCH at Trancas Canyon Road Right Turn Lane", "Outdoor Warning Signs", "Malibu Bluffs Park South Walkway Repairs", "Trancas Canyon Park Playground", "Malibu Canyon Road Traffic Study", "feasible traffic safety improvements can be constructed at this location."], "count": 9}''')

matched_names = set(prev_result['matches'])
extracted_names = prev_result['extracted_names']
unmatched_names = [n for n in extracted_names if n not in matched_names]

funding_map = {}
for item in funding_data:
    funding_map[item['Project_Name']] = float(item['Amount'])

# Check for potential matches
potential_matches = []
for name in unmatched_names:
    # Logic: Check if the extracted name is a substring of a funding name, or vice versa
    # Or if they share significant words.
    
    # Simple substring check
    best_match = None
    for fname in funding_map:
        # Check if one is contained in the other
        if name.lower() in fname.lower() or fname.lower() in name.lower():
            # Found a candidate
            # We want to be careful. "Repair" vs "Repairs" etc.
            best_match = fname
            # If funding > 50000, keep it
            if funding_map[fname] > 50000:
                potential_matches.append({"extracted": name, "funding_name": fname, "amount": funding_map[fname]})
            break # Assume one match per name

print("__RESULT__:")
print(json.dumps(potential_matches))"""

env_args = {'var_function-call-14769478683806682002': 'file_storage/function-call-14769478683806682002.json', 'var_function-call-14769478683806682871': 'file_storage/function-call-14769478683806682871.json', 'var_function-call-602477253164993976': [{'_id': '694eef5c4ec675b6b5f5a285', 'filename': 'malibucity_agenda_03222023-2060.txt'}, {'_id': '694eef5c4ec675b6b5f5a286', 'filename': 'malibucity_agenda__01262022-1835.txt'}, {'_id': '694eef5c4ec675b6b5f5a287', 'filename': 'malibucity_agenda__01272021-1626.txt'}, {'_id': '694eef5c4ec675b6b5f5a288', 'filename': 'malibucity_agenda__03022021-1648.txt'}, {'_id': '694eef5c4ec675b6b5f5a289', 'filename': 'malibucity_agenda__03232022-1869.txt'}], 'var_function-call-11227068865765284835': {'matches': ['PCH Median Improvements Project', 'Westward Beach Road Drainage Improvements Project', 'Latigo Canyon Road Retaining Wall Repair Project', 'Storm Drain Master Plan', 'Permanent Skate Park', 'PCH at Trancas Canyon Road Right Turn Lane', 'Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway Repairs', 'Malibu Canyon Road Traffic Study'], 'extracted_names': ['2022 Morning View Resurfacing & Storm Drain Improvements', 'PCH Median Improvements Project', 'Westward Beach Road Repair Project', 'Westward Beach Road Drainage Improvements Project', 'Clover Heights Storm Drainage Improvements', 'Latigo Canyon Road Retaining Wall Repair Project', 'Storm Drain Master Plan', 'Trancas Canyon Park Upper and Lower Slopes Repair', 'Civic Center Water Treatment Facility Phase 2', 'Permanent Skate Park', 'PCH at Trancas Canyon Road Right Turn Lane', 'Outdoor Warning Signs', 'Malibu Bluffs Park South Walkway Repairs', 'Trancas Canyon Park Playground', 'Malibu Canyon Road Traffic Study', 'feasible traffic safety improvements can be constructed at this location.'], 'count': 9}}

exec(code, env_args)
