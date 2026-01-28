code = """import json

# Load funding data
f_file = var_functions.query_db:50
with open(f_file) as f:
    funding_data = json.load(f)

# List of capital projects with design status (from civic documents)
capital_design_projects = [
    "2022 Morning View Resurfacing & Storm Drain Improvements",
    "PCH Median Improvements Project",
    "Westward Beach Road Repair Project",
    "Westward Beach Road Drainage Improvements Project",
    "Clover Heights Storm Drainage Improvements",
    "Latigo Canyon Road Retaining Wall Repair Project",
    "Storm Drain Master Plan",
    "Trancas Canyon Park Upper and Lower Slopes Repair",
    "Civic Center Water Treatment Facility Phase 2",
    "Permanent Skate Park",
    "PCH at Trancas Canyon Road Right Turn Lane",
    "Outdoor Warning Signs",
    "Malibu Bluffs Park South Walkway Repairs",
    "Trancas Canyon Park Playground",
    "Malibu Canyon Road Traffic Study"
]

# Filter funding records for amounts > $50,000
high_funding_projects = []
for record in funding_data:
    try:
        if int(record['Amount']) > 50000:
            high_funding_projects.append(record)
    except:
        pass

# Match design projects with high funding
matching_projects = set()
for design in capital_design_projects:
    design_lower = design.lower()
    
    for fund in high_funding_projects:
        fund_name = fund['Project_Name'].lower()
        
        # Check for exact or substring match
        if (design_lower == fund_name or 
            design_lower in fund_name or 
            fund_name in design_lower):
            matching_projects.add(design)
            break
        
        # Check for key term matches (at least 3 matching words)
        design_words = design_lower.split()
        fund_words = fund_name.split()
        match_count = sum(1 for word in design_words if word in fund_words and len(word) > 3)
        if match_count >= 3:
            matching_projects.add(design)
            break

# Additional matches based on partial names
additional_checks = [
    ("Malibu Bluffs Park South Walkway", "Malibu Bluffs Park South Walkway"),
    ("Storm Drain Master Plan", "Storm Drain Master Plan"),
    ("Outdoor Warning Signs", "Outdoor Warning Signs"),
    ("Malibu Canyon Road Traffic Study", "Malibu Canyon Road Traffic Study"),
    ("PCH Median Improvements", "PCH Median Improvements Project"),
    ("Westward Beach Road Drainage", "Westward Beach Road Drainage Improvements Project"),
    ("Latigo Canyon Road Retaining Wall", "Latigo Canyon Road Retaining Wall Repair Project"),
    ("Clover Heights Storm Drain", "Clover Heights Storm Drainage Improvements"),
    ("Trancas Canyon Park", "Trancas Canyon Park Playground"),
    ("Permanent Skate Park", "Permanent Skate Park"),
    ("PCH at Trancas", "PCH at Trancas Canyon Road Right Turn Lane"),
    ("Civic Center Water Treatment", "Civic Center Water Treatment Facility Phase 2")
]

for design, search_term in additional_checks:
    if design not in matching_projects:
        for fund in high_funding_projects:
            if search_term.lower() in fund['Project_Name'].lower():
                matching_projects.add(design)
                break

# Count final matches
result = len(matching_projects)

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'count': '276'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': [{'Amount': '79000'}, {'Amount': '85000'}, {'Amount': '87000'}, {'Amount': '81000'}, {'Amount': '93000'}, {'Amount': '79000'}, {'Amount': '85000'}, {'Amount': '64000'}, {'Amount': '53000'}, {'Amount': '54000'}, {'Amount': '68000'}, {'Amount': '58000'}, {'Amount': '80000'}, {'Amount': '90000'}, {'Amount': '56000'}, {'Amount': '94000'}, {'Amount': '91000'}, {'Amount': '56000'}, {'Amount': '57000'}, {'Amount': '97000'}, {'Amount': '91000'}, {'Amount': '78000'}, {'Amount': '69000'}, {'Amount': '91000'}, {'Amount': '81000'}, {'Amount': '97000'}, {'Amount': '82000'}, {'Amount': '93000'}, {'Amount': '60000'}, {'Amount': '92000'}, {'Amount': '81000'}, {'Amount': '84000'}, {'Amount': '84000'}, {'Amount': '56000'}, {'Amount': '73000'}, {'Amount': '90000'}, {'Amount': '97000'}, {'Amount': '86000'}, {'Amount': '59000'}, {'Amount': '86000'}, {'Amount': '77000'}, {'Amount': '80000'}, {'Amount': '78000'}, {'Amount': '92000'}, {'Amount': '65000'}, {'Amount': '68000'}, {'Amount': '90000'}, {'Amount': '91000'}, {'Amount': '87000'}, {'Amount': '77000'}, {'Amount': '94000'}, {'Amount': '94000'}, {'Amount': '89000'}, {'Amount': '88000'}, {'Amount': '63000'}, {'Amount': '90000'}, {'Amount': '99000'}, {'Amount': '73000'}, {'Amount': '93000'}, {'Amount': '64000'}, {'Amount': '99000'}, {'Amount': '69000'}, {'Amount': '81000'}, {'Amount': '69000'}, {'Amount': '77000'}, {'Amount': '86000'}, {'Amount': '66000'}, {'Amount': '74000'}, {'Amount': '80000'}, {'Amount': '70000'}, {'Amount': '91000'}, {'Amount': '76000'}, {'Amount': '90000'}, {'Amount': '79000'}, {'Amount': '98000'}, {'Amount': '100000'}, {'Amount': '62000'}, {'Amount': '79000'}, {'Amount': '63000'}, {'Amount': '63000'}, {'Amount': '84000'}, {'Amount': '83000'}, {'Amount': '71000'}, {'Amount': '55000'}, {'Amount': '59000'}, {'Amount': '63000'}, {'Amount': '79000'}, {'Amount': '87000'}, {'Amount': '65000'}, {'Amount': '53000'}, {'Amount': '96000'}, {'Amount': '61000'}, {'Amount': '69000'}, {'Amount': '78000'}, {'Amount': '60000'}, {'Amount': '82000'}, {'Amount': '92000'}, {'Amount': '69000'}, {'Amount': '58000'}, {'Amount': '51000'}, {'Amount': '58000'}, {'Amount': '63000'}, {'Amount': '79000'}, {'Amount': '54000'}, {'Amount': '93000'}, {'Amount': '93000'}, {'Amount': '95000'}, {'Amount': '82000'}, {'Amount': '69000'}, {'Amount': '57000'}, {'Amount': '87000'}, {'Amount': '96000'}, {'Amount': '58000'}, {'Amount': '85000'}, {'Amount': '90000'}, {'Amount': '97000'}, {'Amount': '82000'}, {'Amount': '78000'}, {'Amount': '94000'}, {'Amount': '92000'}, {'Amount': '63000'}, {'Amount': '72000'}, {'Amount': '65000'}, {'Amount': '91000'}, {'Amount': '68000'}, {'Amount': '76000'}, {'Amount': '78000'}, {'Amount': '71000'}, {'Amount': '65000'}, {'Amount': '85000'}, {'Amount': '51000'}, {'Amount': '67000'}, {'Amount': '69000'}, {'Amount': '88000'}, {'Amount': '58000'}, {'Amount': '51000'}, {'Amount': '72000'}, {'Amount': '55000'}, {'Amount': '86000'}, {'Amount': '62000'}, {'Amount': '81000'}, {'Amount': '70000'}, {'Amount': '72000'}, {'Amount': '61000'}, {'Amount': '94000'}, {'Amount': '57000'}, {'Amount': '80000'}, {'Amount': '54000'}, {'Amount': '80000'}, {'Amount': '55000'}, {'Amount': '68000'}, {'Amount': '78000'}, {'Amount': '98000'}, {'Amount': '71000'}, {'Amount': '85000'}, {'Amount': '77000'}, {'Amount': '78000'}, {'Amount': '72000'}, {'Amount': '71000'}, {'Amount': '53000'}, {'Amount': '71000'}, {'Amount': '72000'}, {'Amount': '83000'}, {'Amount': '97000'}, {'Amount': '82000'}, {'Amount': '63000'}, {'Amount': '86000'}, {'Amount': '89000'}, {'Amount': '76000'}, {'Amount': '67000'}, {'Amount': '66000'}, {'Amount': '85000'}, {'Amount': '89000'}, {'Amount': '88000'}, {'Amount': '94000'}, {'Amount': '67000'}, {'Amount': '86000'}, {'Amount': '100000'}, {'Amount': '99000'}, {'Amount': '68000'}, {'Amount': '97000'}, {'Amount': '90000'}, {'Amount': '94000'}, {'Amount': '82000'}, {'Amount': '98000'}, {'Amount': '99000'}, {'Amount': '79000'}, {'Amount': '66000'}, {'Amount': '86000'}, {'Amount': '65000'}, {'Amount': '51000'}, {'Amount': '96000'}, {'Amount': '83000'}, {'Amount': '96000'}, {'Amount': '76000'}, {'Amount': '66000'}, {'Amount': '84000'}, {'Amount': '91000'}, {'Amount': '72000'}, {'Amount': '70000'}, {'Amount': '62000'}, {'Amount': '51000'}, {'Amount': '62000'}, {'Amount': '73000'}, {'Amount': '94000'}, {'Amount': '80000'}, {'Amount': '68000'}, {'Amount': '51000'}, {'Amount': '61000'}, {'Amount': '75000'}, {'Amount': '79000'}, {'Amount': '62000'}, {'Amount': '56000'}, {'Amount': '73000'}, {'Amount': '66000'}, {'Amount': '99000'}, {'Amount': '90000'}, {'Amount': '80000'}, {'Amount': '80000'}, {'Amount': '100000'}, {'Amount': '63000'}, {'Amount': '71000'}, {'Amount': '80000'}, {'Amount': '59000'}, {'Amount': '86000'}, {'Amount': '63000'}, {'Amount': '74000'}, {'Amount': '85000'}, {'Amount': '94000'}, {'Amount': '78000'}, {'Amount': '54000'}, {'Amount': '80000'}, {'Amount': '79000'}, {'Amount': '68000'}, {'Amount': '51000'}, {'Amount': '59000'}, {'Amount': '62000'}, {'Amount': '70000'}, {'Amount': '58000'}, {'Amount': '94000'}, {'Amount': '93000'}, {'Amount': '73000'}, {'Amount': '85000'}, {'Amount': '66000'}, {'Amount': '77000'}, {'Amount': '68000'}, {'Amount': '93000'}, {'Amount': '89000'}, {'Amount': '60000'}, {'Amount': '52000'}, {'Amount': '96000'}, {'Amount': '78000'}, {'Amount': '72000'}, {'Amount': '79000'}, {'Amount': '89000'}, {'Amount': '97000'}, {'Amount': '91000'}, {'Amount': '51000'}, {'Amount': '55000'}, {'Amount': '65000'}, {'Amount': '62000'}, {'Amount': '97000'}, {'Amount': '88000'}, {'Amount': '58000'}, {'Amount': '97000'}, {'Amount': '73000'}, {'Amount': '84000'}, {'Amount': '91000'}, {'Amount': '68000'}, {'Amount': '95000'}, {'Amount': '69000'}, {'Amount': '79000'}, {'Amount': '54000'}, {'Amount': '64000'}, {'Amount': '59000'}, {'Amount': '71000'}]}

exec(code, env_args)
