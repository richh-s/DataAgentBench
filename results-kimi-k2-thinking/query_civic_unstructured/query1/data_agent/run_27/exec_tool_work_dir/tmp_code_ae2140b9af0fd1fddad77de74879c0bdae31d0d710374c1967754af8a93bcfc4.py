code = """import json

# Load the data
var_civic_docs = locals()['var_functions.query_db:24']
if isinstance(var_civic_docs, str):
    with open(var_civic_docs) as f:
        civic_docs = json.load(f)
else:
    civic_docs = var_civic_docs

var_funding = locals()['var_functions.query_db:6']
if isinstance(var_funding, str):
    with open(var_funding) as f:
        funding_data = json.load(f)
else:
    funding_data = var_funding

# Get projects with funding > 50000
high_funding = {}
for f in funding_data:
    amount = int(f['Amount'])
    if amount > 50000:
        high_funding[f['Project_Name']] = amount

# Extract design projects from the text
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    if 'Capital Improvement Projects (Design)' in text:
        # Find the design section
        parts = text.split('Capital Improvement Projects (Design)')
        if len(parts) > 1:
            design_section = parts[1]
            # Split by known boundaries
            before_construction = design_section.split('Capital Improvement Projects (Construction)')[0]
            
            # Extract project names - they appear as standalone lines
            lines = before_construction.split('\n')
            for line in lines:
                clean_line = line.strip()
                # Project names are capitalized, contain spaces, not control lines
                if (clean_line and len(clean_line) > 10 and 
                    not clean_line.startswith('Page') and 
                    not clean_line.startswith('(') and
                    ':' not in clean_line and
                    'Updates' not in clean_line and
                    'Schedule' not in clean_line and
                    'RECOMMENDED' not in clean_line and
                    not clean_line.startswith('To:') and
                    not clean_line.startswith('From:') and
                    not clean_line.startswith('Date') and
                    len(clean_line) < 150):
                    
                    design_projects.append(clean_line)

# Remove obvious duplicates and clean up
unique_design_projects = []
seen = set()
for proj in design_projects:
    if proj not in seen:
        unique_design_projects.append(proj)
        seen.add(proj)

# Check which design projects have high funding and are capital (not disaster)
capital_design_high_funding = []
for proj in unique_design_projects:
    if proj in high_funding:
        # Check if it's a capital project (not disaster)
        is_disaster = any(marker in proj for marker in ['(FEMA', '(CalOES', '(CalJPIA'])
        if not is_disaster:
            capital_design_high_funding.append({
                'project': proj,
                'amount': high_funding[proj]
            })

result = {
    'count': len(capital_design_high_funding),
    'projects': capital_design_high_funding
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.list_db:5': ['Funding'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.list_db:22': ['Funding'], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.execute_python:26': ['Birdview Avenue Improvements', 'Birdview Avenue Improvements (CalOES Project)', 'Broad Beach Road Water Quality Infrastructure Repairs', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Broad Beach Road Water Quality Repair', 'City Hall Roof Replacement', 'City Traffic Signals Backup Power', 'Civic Center Stormwater Diversion Structure', 'Clover Heights Storm Drain', 'Corral Canyon Culvert Repairs', 'Corral Canyon Road Bridge Repairs', 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Discussion', 'Dume Drive and Fernhill Drive Speed Humps Project', 'Encinal Canyon 60-inch Storm Drain Repairs', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Harbor Vista Curb Return', 'Kanan Dume Biofilter', 'Latigo Canyon Road Culvert Repairs', 'Latigo Canyon Road Retaining Wall Repair Project', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Legacy Park Paver Repair Project', 'Malibu Bluffs Park South Walkway', 'Malibu Bluffs Park South Walkway Repairs', 'Malibu Canyon Road Traffic Study', 'Malibu Seafood Undercrossing', 'Michael Landon Center HVAC Replacement Project', 'Michael Landon Center Roof Replacement Project', 'Outdoor Warning Signs', 'Outdoor Warning Sirens (FEMA)', 'Outdoor Warningn Sirens - Design (FEMA Project)', 'PCH Crosswalk Improvements at Big Rock Drive and 20326 PCH', 'PCH Median Improvements Project', 'PCH Overhead Warning Signs', 'PCH at Trancas Canyon Road Right Turn Lane', 'Permanent Skate Park', 'Point Dume Decomposed Granite Walkway Repair Project', 'Point Dume Walkway Repairs', 'Recommended Action', 'Storm Drain Master Plan', 'Storm Drain Master Plan (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs', 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Trancas Canyon Park Playground Resurfacing', 'Trancas Canyon Park Slope Stabilization Project', 'Trancas Playground Resurfacing', 'Vehicle Protection Devices', 'Westward Beach Road Drainage Improvements Project', 'Westward Beach Road Shoulder Repairs (CalOES Project)']}

exec(code, env_args)
