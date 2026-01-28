code = """import json

# Read the funding database data
funding_data = [
  {"Funding_ID": "1", "Project_Name": "2021 Annual Street Maintenance", "Funding_Source": "Public-Private Partnership (PPP)", "Amount": "24000"},
  {"Funding_ID": "2", "Project_Name": "2022 Annual Street Maintenance", "Funding_Source": "Government Grant", "Amount": "45000"},
  {"Funding_ID": "3", "Project_Name": "2022 Morning View Resurfacing & Storm Drain Improvements", "Funding_Source": "State Development Grant", "Amount": "38000"},
  {"Funding_ID": "8", "Project_Name": "Bluffs Park Shade Structure", "Funding_Source": "Government Grant", "Amount": "21000"},
  {"Funding_ID": "12", "Project_Name": "Broad Beach Road Water Quality Repair", "Funding_Source": "University Research Fund", "Amount": "93000"},
  {"Funding_ID": "15", "Project_Name": "City Traffic Signals Backup Power", "Funding_Source": "Social Impact Investment", "Amount": "85000"},
  {"Funding_ID": "19", "Project_Name": "Civic Center Water Treatment Facility Phase 2", "Funding_Source": "Crowdfunding", "Amount": "45000"},
  {"Funding_ID": "21", "Project_Name": "Clover Heights Storm Drain", "Funding_Source": "Infrastructure Bond", "Amount": "53000"},
  {"Funding_ID": "23", "Project_Name": "Clover Heights Storm Drainage Improvements", "Funding_Source": "Development Bank Loan", "Amount": "22000"},
  {"Funding_ID": "36", "Project_Name": "Encinal Canyon Road Repairs", "Funding_Source": "State Development Grant", "Amount": "47000"},
  {"Funding_ID": "41", "Project_Name": "Kanan Dume Biofilter", "Funding_Source": "Venture Capital Fund", "Amount": "56000"},
  {"Funding_ID": "45", "Project_Name": "Latigo Canyon Road Retaining Wall Repair Project", "Funding_Source": "Educational Sponsorship", "Amount": "97000"},
  {"Funding_ID": "52", "Project_Name": "Malibu Bluffs Park South Walkway", "Funding_Source": "Cultural Heritage Grant", "Amount": "91000"},
  {"Funding_ID": "53", "Project_Name": "Malibu Bluffs Park South Walkway Repairs", "Funding_Source": "Educational Sponsorship", "Amount": "81000"},
  {"Funding_ID": "54", "Project_Name": "Malibu Canyon Road Traffic Study", "Funding_Source": "State Development Grant", "Amount": "97000"},
  {"Funding_ID": "58", "Project_Name": "Malibu Road Slope Repairs", "Funding_Source": "Development Bank Loan", "Amount": "44000"},
  {"Funding_ID": "61", "Project_Name": "Marie Canyon Green Streets", "Funding_Source": "Urban Renewal Fund", "Amount": "50000"},
  {"Funding_ID": "64", "Project_Name": "Outdoor Warning Signs", "Funding_Source": "Urban Renewal Fund", "Amount": "92000"},
  {"Funding_ID": "70", "Project_Name": "PCH Crosswalk Improvements at Big Rock Drive and 20326 PCH", "Funding_Source": "Research Institution Funding", "Amount": "10000"},
  {"Funding_ID": "72", "Project_Name": "PCH Median Improvements Project", "Funding_Source": "Public-Private Partnership (PPP)", "Amount": "35000"},
  {"Funding_ID": "73", "Project_Name": "PCH Signal Synchronization System Improvements Project", "Funding_Source": "Environmental Grant", "Amount": "96000"},
  {"Funding_ID": "83", "Project_Name": "Point Dume Walkway Repairs", "Funding_Source": "Municipal Fund", "Amount": "54000"},
  {"Funding_ID": "84", "Project_Name": "Permanent Skate Park", "Funding_Source": "Corporate Sponsorship", "Amount": "70000"},
  {"Funding_ID": "86", "Project_Name": "PCH at Trancas Canyon Road Right Turn Lane", "Funding_Source": "Social Impact Investment", "Amount": "46000"},
  {"Funding_ID": "90", "Project_Name": "Storm Drain Trash Screens Phase Two", "Funding_Source": "Social Impact Investment", "Amount": "34000"},
  {"Funding_ID": "93", "Project_Name": "Trancas Canyon Park Playground", "Funding_Source": "Community Fund", "Amount": "73000"},
  {"Funding_ID": "95", "Project_Name": "Trancas Canyon Park Upper and Lower Slopes Repair", "Funding_Source": "Non-profit Organization Grant", "Amount": "38000"},
  {"Funding_ID": "102", "Project_Name": "Westward Beach Road Drainage Improvements Project", "Funding_Source": "Development Bank Loan", "Amount": "81000"},
  {"Funding_ID": "103", "Project_Name": "Westward Beach Road Repair Project", "Funding_Source": "Educational Sponsorship", "Amount": "76000"}
]

# Read the civic documents data
with open('/tmp/tmpyq7d3x4g.json', 'r') as f:
    civic_docs = json.load(f)

# Simple approach: Look for projects mentioned with Spring 2022 in the text
spring_2022_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for Spring 2022 references and nearby project names
    spring_occurrences = [m.start() for m in __import__('re').finditer('Spring 2022', text, __import__('re').IGNORECASE)]
    
    for pos in spring_occurrences:
        # Look backwards for project name (up to 200 characters)
        start = max(0, pos - 200)
        preceding_text = text[start:pos]
        
        # Look for common project name patterns
        lines = preceding_text.split('\n')
        for i in range(len(lines)-1, -1, -1):
            line = lines[i].strip()
            if line and not line.startswith('(') and not line.startswith('Page') and len(line) > 10:
                # Check if this looks like a project name
                project_name = line[:150]
                spring_2022_projects.append(project_name)
                break

# Remove duplicates while preserving order
seen = set()
unique_projects = []
for proj in spring_2022_projects:
    if proj not in seen:
        seen.add(proj)
        unique_projects.append(proj)

print('Spring 2022 projects found:', len(unique_projects))
print('Projects:', unique_projects)

# Look for these projects in the funding data
project_names_from_docs = set(unique_projects)
funding_lookup = {f['Project_Name'].lower(): int(f['Amount']) for f in funding_data}

matching_projects = []
total_funding = 0

for project_name in unique_projects:
    # Try exact match
    for funding_proj in funding_data:
        if project_name.lower() in funding_proj['Project_Name'].lower():
            matching_projects.append({
                'project': project_name,
                'funding_project': funding_proj['Project_Name'],
                'amount': int(funding_proj['Amount'])
            })
            total_funding += int(funding_proj['Amount'])
            break

print('Matching funding records found:', len(matching_projects))
print('Total funding amount:', total_funding)

print('__RESULT__:')
print(json.dumps({
    'spring_2022_project_count': len(unique_projects),
    'projects_from_docs': unique_projects,
    'matched_funding_count': len(matching_projects),
    'total_funding': total_funding,
    'matched_projects': matching_projects
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:12': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}], 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
