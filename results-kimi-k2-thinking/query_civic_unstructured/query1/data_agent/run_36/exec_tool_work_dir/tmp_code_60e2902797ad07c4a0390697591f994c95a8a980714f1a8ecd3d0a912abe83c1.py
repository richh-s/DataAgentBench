code = """import json

# Load funding data
funding_file = "query_result.json"
with open("query_result.json") as f:
    funding_records = json.load(f)

# Filter for funding > $50,000
high_funding = []
for record in funding_records:
    try:
        amount = int(record['Amount'])
        if amount > 50000:
            high_funding.append(record)
    except:
        pass

# Capital design projects from civic docs (manually extracted)
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

# Match projects
matches = set()
for design in capital_design_projects:
    design_lower = design.lower()
    for fund in high_funding:
        fund_name = fund['Project_Name'].lower()
        if design_lower in fund_name or fund_name in design_lower:
            matches.add(design)
            break

# Return result
result = len(matches)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:26': [{'count': '276'}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.query_db:44': 'file_storage/functions.query_db:44.json', 'var_functions.query_db:50': 'file_storage/functions.query_db:50.json', 'var_functions.query_db:54': [{'Amount': '79000'}, {'Amount': '85000'}, {'Amount': '87000'}, {'Amount': '81000'}, {'Amount': '93000'}, {'Amount': '79000'}, {'Amount': '85000'}, {'Amount': '64000'}, {'Amount': '53000'}, {'Amount': '54000'}, {'Amount': '68000'}, {'Amount': '58000'}, {'Amount': '80000'}, {'Amount': '90000'}, {'Amount': '56000'}, {'Amount': '94000'}, {'Amount': '91000'}, {'Amount': '56000'}, {'Amount': '57000'}, {'Amount': '97000'}, {'Amount': '91000'}, {'Amount': '78000'}, {'Amount': '69000'}, {'Amount': '91000'}, {'Amount': '81000'}, {'Amount': '97000'}, {'Amount': '82000'}, {'Amount': '93000'}, {'Amount': '60000'}, {'Amount': '92000'}, {'Amount': '81000'}, {'Amount': '84000'}, {'Amount': '84000'}, {'Amount': '56000'}, {'Amount': '73000'}, {'Amount': '90000'}, {'Amount': '97000'}, {'Amount': '86000'}, {'Amount': '59000'}, {'Amount': '86000'}, {'Amount': '77000'}, {'Amount': '80000'}, {'Amount': '78000'}, {'Amount': '92000'}, {'Amount': '65000'}, {'Amount': '68000'}, {'Amount': '90000'}, {'Amount': '91000'}, {'Amount': '87000'}, {'Amount': '77000'}, {'Amount': '94000'}, {'Amount': '94000'}, {'Amount': '89000'}, {'Amount': '88000'}, {'Amount': '63000'}, {'Amount': '90000'}, {'Amount': '99000'}, {'Amount': '73000'}, {'Amount': '93000'}, {'Amount': '64000'}, {'Amount': '99000'}, {'Amount': '69000'}, {'Amount': '81000'}, {'Amount': '69000'}, {'Amount': '77000'}, {'Amount': '86000'}, {'Amount': '66000'}, {'Amount': '74000'}, {'Amount': '80000'}, {'Amount': '70000'}, {'Amount': '91000'}, {'Amount': '76000'}, {'Amount': '90000'}, {'Amount': '79000'}, {'Amount': '98000'}, {'Amount': '100000'}, {'Amount': '62000'}, {'Amount': '79000'}, {'Amount': '63000'}, {'Amount': '63000'}, {'Amount': '84000'}, {'Amount': '83000'}, {'Amount': '71000'}, {'Amount': '55000'}, {'Amount': '59000'}, {'Amount': '63000'}, {'Amount': '79000'}, {'Amount': '87000'}, {'Amount': '65000'}, {'Amount': '53000'}, {'Amount': '96000'}, {'Amount': '61000'}, {'Amount': '69000'}, {'Amount': '78000'}, {'Amount': '60000'}, {'Amount': '82000'}, {'Amount': '92000'}, {'Amount': '69000'}, {'Amount': '58000'}, {'Amount': '51000'}, {'Amount': '58000'}, {'Amount': '63000'}, {'Amount': '79000'}, {'Amount': '54000'}, {'Amount': '93000'}, {'Amount': '93000'}, {'Amount': '95000'}, {'Amount': '82000'}, {'Amount': '69000'}, {'Amount': '57000'}, {'Amount': '87000'}, {'Amount': '96000'}, {'Amount': '58000'}, {'Amount': '85000'}, {'Amount': '90000'}, {'Amount': '97000'}, {'Amount': '82000'}, {'Amount': '78000'}, {'Amount': '94000'}, {'Amount': '92000'}, {'Amount': '63000'}, {'Amount': '72000'}, {'Amount': '65000'}, {'Amount': '91000'}, {'Amount': '68000'}, {'Amount': '76000'}, {'Amount': '78000'}, {'Amount': '71000'}, {'Amount': '65000'}, {'Amount': '85000'}, {'Amount': '51000'}, {'Amount': '67000'}, {'Amount': '69000'}, {'Amount': '88000'}, {'Amount': '58000'}, {'Amount': '51000'}, {'Amount': '72000'}, {'Amount': '55000'}, {'Amount': '86000'}, {'Amount': '62000'}, {'Amount': '81000'}, {'Amount': '70000'}, {'Amount': '72000'}, {'Amount': '61000'}, {'Amount': '94000'}, {'Amount': '57000'}, {'Amount': '80000'}, {'Amount': '54000'}, {'Amount': '80000'}, {'Amount': '55000'}, {'Amount': '68000'}, {'Amount': '78000'}, {'Amount': '98000'}, {'Amount': '71000'}, {'Amount': '85000'}, {'Amount': '77000'}, {'Amount': '78000'}, {'Amount': '72000'}, {'Amount': '71000'}, {'Amount': '53000'}, {'Amount': '71000'}, {'Amount': '72000'}, {'Amount': '83000'}, {'Amount': '97000'}, {'Amount': '82000'}, {'Amount': '63000'}, {'Amount': '86000'}, {'Amount': '89000'}, {'Amount': '76000'}, {'Amount': '67000'}, {'Amount': '66000'}, {'Amount': '85000'}, {'Amount': '89000'}, {'Amount': '88000'}, {'Amount': '94000'}, {'Amount': '67000'}, {'Amount': '86000'}, {'Amount': '100000'}, {'Amount': '99000'}, {'Amount': '68000'}, {'Amount': '97000'}, {'Amount': '90000'}, {'Amount': '94000'}, {'Amount': '82000'}, {'Amount': '98000'}, {'Amount': '99000'}, {'Amount': '79000'}, {'Amount': '66000'}, {'Amount': '86000'}, {'Amount': '65000'}, {'Amount': '51000'}, {'Amount': '96000'}, {'Amount': '83000'}, {'Amount': '96000'}, {'Amount': '76000'}, {'Amount': '66000'}, {'Amount': '84000'}, {'Amount': '91000'}, {'Amount': '72000'}, {'Amount': '70000'}, {'Amount': '62000'}, {'Amount': '51000'}, {'Amount': '62000'}, {'Amount': '73000'}, {'Amount': '94000'}, {'Amount': '80000'}, {'Amount': '68000'}, {'Amount': '51000'}, {'Amount': '61000'}, {'Amount': '75000'}, {'Amount': '79000'}, {'Amount': '62000'}, {'Amount': '56000'}, {'Amount': '73000'}, {'Amount': '66000'}, {'Amount': '99000'}, {'Amount': '90000'}, {'Amount': '80000'}, {'Amount': '80000'}, {'Amount': '100000'}, {'Amount': '63000'}, {'Amount': '71000'}, {'Amount': '80000'}, {'Amount': '59000'}, {'Amount': '86000'}, {'Amount': '63000'}, {'Amount': '74000'}, {'Amount': '85000'}, {'Amount': '94000'}, {'Amount': '78000'}, {'Amount': '54000'}, {'Amount': '80000'}, {'Amount': '79000'}, {'Amount': '68000'}, {'Amount': '51000'}, {'Amount': '59000'}, {'Amount': '62000'}, {'Amount': '70000'}, {'Amount': '58000'}, {'Amount': '94000'}, {'Amount': '93000'}, {'Amount': '73000'}, {'Amount': '85000'}, {'Amount': '66000'}, {'Amount': '77000'}, {'Amount': '68000'}, {'Amount': '93000'}, {'Amount': '89000'}, {'Amount': '60000'}, {'Amount': '52000'}, {'Amount': '96000'}, {'Amount': '78000'}, {'Amount': '72000'}, {'Amount': '79000'}, {'Amount': '89000'}, {'Amount': '97000'}, {'Amount': '91000'}, {'Amount': '51000'}, {'Amount': '55000'}, {'Amount': '65000'}, {'Amount': '62000'}, {'Amount': '97000'}, {'Amount': '88000'}, {'Amount': '58000'}, {'Amount': '97000'}, {'Amount': '73000'}, {'Amount': '84000'}, {'Amount': '91000'}, {'Amount': '68000'}, {'Amount': '95000'}, {'Amount': '69000'}, {'Amount': '79000'}, {'Amount': '54000'}, {'Amount': '64000'}, {'Amount': '59000'}, {'Amount': '71000'}], 'var_functions.list_db:62': ['civic_docs']}

exec(code, env_args)
