code = """import json
funding = [
 "Birdview Avenue Improvements", "Birdview Avenue Improvements (CalOES Project)",
 "Broad Beach Road Water Quality Infrastructure Repairs", "Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)", "Broad Beach Road Water Quality Repair",
 "City Hall Roof Replacement", "City Traffic Signals Backup Power", "Civic Center Stormwater Diversion Structure", "Clover Heights Storm Drain", "Corral Canyon Culvert Repairs",
 "Corral Canyon Road Bridge Repairs", "Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)", "Discussion", "Dume Drive and Fernhill Drive Speed Humps Project",
 "Encinal Canyon 60-inch Storm Drain Repairs", "Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)", "Harbor Vista Curb Return", "Kanan Dume Biofilter",
 "Latigo Canyon Road Culvert Repairs", "Latigo Canyon Road Retaining Wall Repair Project", "Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)",
 "Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)", "Legacy Park Paver Repair Project", "Malibu Bluffs Park South Walkway", "Malibu Bluffs Park South Walkway Repairs",
 "Malibu Canyon Road Traffic Study", "Malibu Seafood Undercrossing", "Michael Landon Center HVAC Replacement Project", "Michael Landon Center Roof Replacement Project", "Outdoor Warning Signs"
]
design_projs = [
 "2022 Morning View Resurfacing & Storm Drain Improvements", "PCH Median Improvements Project", "Westward Beach Road Repair Project", "Westward Beach Road Drainage Improvements Project",
 "Clover Heights Storm Drainage Improvements", "Latigo Canyon Road Retaining Wall Repair Project", "Storm Drain Master Plan", "Trancas Canyon Park Upper and Lower Slopes Repair",
 "Civic Center Water Treatment Facility Phase 2", "Permanent Skate Park", "PCH at Trancas Canyon Road Right Turn Lane", "Outdoor Warning Signs", "Malibu Bluffs Park South Walkway Repairs",
 "Trancas Canyon Park Playground", "Malibu Canyon Road Traffic Study", "PCH Median Improvements Project", "PCH Crosswalk Improvements at Big Rock Drive and 20326 PCH", "Kanan Dume Biofilter",
 "City Traffic Signals Backup Power"
]
matched = 0
for p in design_projs:
    for f in funding:
        if p.lower() in f.lower() or f.lower() in p.lower():
            if abs(len(p)-len(f)) < 30:
                matched += 1
                break
print('__RESULT__:')
print(json.dumps({'count': matched}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:60': 'file_storage/functions.query_db:60.json', 'var_functions.list_db:82': ['civic_docs'], 'var_functions.query_db:84': 'file_storage/functions.query_db:84.json', 'var_functions.execute_python:86': [], 'var_functions.query_db:90': 'file_storage/functions.query_db:90.json'}

exec(code, env_args)
