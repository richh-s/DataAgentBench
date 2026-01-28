code = """import json

# Load funding data
funding_file = locals()['var_functions.query_db:32']
with open(funding_file) as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:24']
with open(civic_file) as f:
    civic_docs = json.load(f)

# Build map of projects with funding > 50000
funding_map = {}
for item in funding_data:
    funding_map[item['Project_Name']] = int(item['Amount'])

# Extract design project names from documents
design_projects = set()
for doc in civic_docs:
    text = doc['text']
    if 'Capital Improvement Projects (Design)' in text:
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            section = parts[1].split('Capital Improvement Projects (Construction)')[0]
            for line in section.split('\n'):
                line = line.strip()
                if line and len(line) > 10 and 'Page' not in line and line[0].isalnum():
                    design_projects.add(line)

# Count capital design projects with funding > 50000
capital_count = 0
capital_project_names = []
for proj in design_projects:
    is_disaster = any(x in proj for x in ['(FEMA', '(CalOES', '(CalJPIA'])
    if not is_disaster and proj in funding_map:
        capital_count += 1
        capital_project_names.append(proj)

print('__RESULT__:')
print(json.dumps({'count': capital_count, 'projects': capital_project_names}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:22': ['Funding'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs', 'Corral Canyon Road Bridge Repairs', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Discussion', 'Dume Drive and Fernhill Drive Speed Humps Project', 'Encinal Canyon 60-inch Storm Drain Repairs', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Harbor Vista Curb Return', 'Kanan Dume Biofilter', 'Latigo Canyon Road Culvert Repairs', 'Latigo Canyon Road Retaining Wall Repair Project', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Legacy Park Paver Repair Project', 'Malibu Bluffs Park South Walkway', 'Malibu Bluffs Park South Walkway Repairs', 'Malibu Canyon Road Traffic Study', 'Malibu Seafood Undercrossing', 'Michael Landon Center HVAC Replacement Project', 'Michael Landon Center Roof Replacement Project', 'Outdoor Warning Signs', 'Outdoor Warning Sirens (FEMA)', 'Outdoor Warningn Sirens - Design (FEMA Project)', 'PCH Crosswalk Improvements at Big Rock Drive and 20326 PCH', 'PCH Median Improvements Project', 'PCH Overhead Warning Signs', 'PCH at Trancas Canyon Road Right Turn Lane', 'Permanent Skate Park', 'Point Dume Decomposed Granite Walkway Repair Project', 'Point Dume Walkway Repairs', 'Recommended Action', 'Storm Drain Master Plan', 'Storm Drain Master Plan (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Trancas Canyon Park Playground Resurfacing', 'Trancas Canyon Park Slope Stabilization Project', 'Trancas Playground Resurfacing', 'Vehicle Protection Devices', 'Westward Beach Road Drainage Improvements Project', 'Westward Beach Road Shoulder Repairs (CalOES Project)'], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json'}

exec(code, env_args)
