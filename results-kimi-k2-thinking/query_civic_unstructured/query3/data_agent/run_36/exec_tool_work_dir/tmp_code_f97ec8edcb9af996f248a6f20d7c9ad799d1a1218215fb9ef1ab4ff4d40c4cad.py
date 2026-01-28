code = """# Load civic documents to extract statuses
civic_docs_file = locals()['var_functions.query_db:6']
import json
with open(civic_docs_file, 'r') as f:
    civic_docs_data = json.load(f)

# The relevant funding records from previous step
relevant_funding_records = locals()['var_functions.execute_python:20']

print('Searching for project statuses in civic documents...')

# Function to find project status in documents
def find_project_status(project_name, docs_data):
    project_lower = project_name.lower()
    for doc in docs_data:
        text = doc.get('text', '')
        if project_lower in text.lower():
            # Look for status indicators near the project name
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if project_lower in line.lower():
                    # Look at surrounding lines for status information
                    context_start = max(0, i-5)
                    context_end = min(len(lines), i+6)
                    context = '\n'.join(lines[context_start:context_end])
                    
                    # Check for common status patterns
                    if 'will provide' in context.lower() or 'presentation' in context.lower():
                        return 'informational', doc.get('filename', ''), context[:200]
                    elif 'construction' in context.lower() and ('begin' in context.lower() or 'under' in context.lower()):
                        return 'construction', doc.get('filename', ''), context[:200]
                    elif 'design' in context.lower() or 'planning' in context.lower():
                        return 'design', doc.get('filename', ''), context[:200]
                    elif 'completed' in context.lower() or 'completion' in context.lower():
                        return 'completed', doc.get('filename', ''), context[:200]
                    elif 'not started' in context.lower() or 'upcoming' in context.lower() or 'future' in context.lower():
                        return 'not_started', doc.get('filename', ''), context[:200]
                    else:
                        return 'mentioned', doc.get('filename', ''), context[:200]
    return 'not_found', '', ''

# Find statuses for all relevant projects
projects_with_status = []
for record in relevant_funding_records:
    project_name = record['project_name']
    status, filename, context = find_project_status(project_name, civic_docs_data)
    
    projects_with_status.append({
        'project_name': project_name,
        'funding_source': record['funding_source'],
        'amount': record['amount'],
        'status': status,
        'found_in_document': filename
    })

# Also search for projects with 'emergency' or 'fema' in the document text
# but without explicit FEMA/CalOES suffixes
additional_emergency_projects = []

# Keywords to search for in documents
disaster_keywords = ['fema', 'emergency', 'disaster', 'woolsey fire', 'caloes', 'caljpia']

for doc in civic_docs_data:
    text = doc.get('text', '').lower()
    if any(keyword in text for keyword in disaster_keywords):
        # Look for project names in this document
        lines = doc.get('text', '').split('\n')
        for line in lines:
            line = line.strip()
            # Skip non-project lines
            if not line or len(line) < 15:
                continue
            if line.startswith('(') or line.startswith('•') or line.startswith('●'):
                continue
            if any(keyword in line.lower() for keyword in ['updates', 'project schedule', 'page', 'staff', 'city']):
                continue
            
            # Check if this project is already in our list
            already_listed = False
            for existing in projects_with_status:
                if line.lower() == existing['project_name'].lower():
                    already_listed = True
                    break
            
            if not already_listed and any(indicator in line.lower() for indicator in ['drain', 'culvert', 'bridge', 'road', 'guardrail', 'repair']):
                # Check if there's funding for this project
                for funding_record in locals()['var_functions.query_db:5']:
                    if line.lower() in funding_record.get('Project_Name', '').lower():
                        additional_emergency_projects.append({
                            'project_name': funding_record.get('Project_Name', ''),
                            'funding_source': funding_record.get('Funding_Source', ''),
                            'amount': int(funding_record.get('Amount', 0)),
                            'status': 'disaster_related',
                            'found_in_document': doc.get('filename', '')
                        })
                        break

# Combine and deduplicate
all_projects = {}
for proj in projects_with_status + additional_emergency_projects:
    name = proj['project_name']
    if name not in all_projects:
        all_projects[name] = proj

final_projects = list(all_projects.values())
print('\nFound ' + str(len(final_projects)) + ' emergency/FEMA related projects with funding and status information')

# Format the output for display
output = []
output.append('Emergency/FEMA Related Projects - Funding and Status')
output.append('=' * 70)

# Sort by amount descending
final_projects.sort(key=lambda x: x['amount'], reverse=True)

for proj in final_projects:
    output.append('Project Name: ' + proj['project_name'])
    output.append('  Funding Source: ' + proj['funding_source'])
    output.append('  Amount: $' + str(proj['amount']))
    output.append('  Status: ' + proj['status'])
    if proj['found_in_document']:
        output.append('  Document: ' + proj['found_in_document'])
    output.append('')

for line in output:
    print(line)

# Return structured data
print('__RESULT__:')
structured_data = [{
    'project_name': p['project_name'],
    'funding_source': p['funding_source'],
    'amount': p['amount'],
    'status': p['status'],
    'document': p['found_in_document']
} for p in final_projects]
print(json.dumps(structured_data))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:2': ['Funding'], 'var_functions.query_db:5': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}, {'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '8', 'Project_Name': 'Bluffs Park Shade Structure', 'Funding_Source': 'Government Grant', 'Amount': '21000'}, {'Funding_ID': '9', 'Project_Name': 'Bluffs Park Workout Station', 'Funding_Source': 'University Research Fund', 'Amount': '39000'}, {'Funding_ID': '10', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs', 'Funding_Source': 'International Organization Grant', 'Amount': '87000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '12', 'Project_Name': 'Broad Beach Road Water Quality Repair', 'Funding_Source': 'University Research Fund', 'Amount': '93000'}, {'Funding_ID': '13', 'Project_Name': 'City Hall Roof Replacement', 'Funding_Source': 'Educational Sponsorship', 'Amount': '79000'}, {'Funding_ID': '14', 'Project_Name': 'City Hall Solar Project', 'Funding_Source': 'Research Institution Funding', 'Amount': '38000'}, {'Funding_ID': '15', 'Project_Name': 'City Traffic Signals Backup Power', 'Funding_Source': 'Social Impact Investment', 'Amount': '85000'}, {'Funding_ID': '16', 'Project_Name': 'Citywide Asphalt Concrete Berms Repairs', 'Funding_Source': 'Environmental Grant', 'Amount': '10000'}, {'Funding_ID': '17', 'Project_Name': 'Citywide Guardrail Replacement', 'Funding_Source': 'Infrastructure Bond', 'Amount': '30000'}, {'Funding_ID': '18', 'Project_Name': 'Civic Center Stormwater Diversion Structure', 'Funding_Source': 'Educational Sponsorship', 'Amount': '64000'}, {'Funding_ID': '19', 'Project_Name': 'Civic Center Water Treatment Facility Phase 2', 'Funding_Source': 'Crowdfunding', 'Amount': '45000'}, {'Funding_ID': '20', 'Project_Name': 'Civic Center Way Improvements', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '37000'}, {'Funding_ID': '21', 'Project_Name': 'Clover Heights Storm Drain', 'Funding_Source': 'Infrastructure Bond', 'Amount': '53000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '23', 'Project_Name': 'Clover Heights Storm Drainage Improvements', 'Funding_Source': 'Development Bank Loan', 'Amount': '22000'}, {'Funding_ID': '24', 'Project_Name': 'Corral Canyon Culvert Repairs', 'Funding_Source': 'Federal Assistance', 'Amount': '54000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '27', 'Project_Name': 'Corral Canyon Road Bridge Repairs', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '68000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '30', 'Project_Name': 'Discussion', 'Funding_Source': 'International Aid', 'Amount': '80000'}, {'Funding_ID': '31', 'Project_Name': 'Dume Drive and Fernhill Drive Speed Humps Project', 'Funding_Source': 'Philanthropic Donation', 'Amount': '90000'}, {'Funding_ID': '32', 'Project_Name': 'Encinal Canyon 60-inch Storm Drain Repairs', 'Funding_Source': 'Municipal Fund', 'Amount': '56000'}, {'Funding_ID': '33', 'Project_Name': 'Encinal Canyon Road Drainage Improvements', 'Funding_Source': 'Non-profit Organization Grant', 'Amount': '34000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '36', 'Project_Name': 'Encinal Canyon Road Repairs', 'Funding_Source': 'State Development Grant', 'Amount': '47000'}, {'Funding_ID': '37', 'Project_Name': 'Guardrail Replacement Citywide', 'Funding_Source': 'International Aid', 'Amount': '39000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '40', 'Project_Name': 'Harbor Vista Curb Return', 'Funding_Source': 'Social Impact Investment', 'Amount': '91000'}, {'Funding_ID': '41', 'Project_Name': 'Kanan Dume Biofilter', 'Funding_Source': 'Venture Capital Fund', 'Amount': '56000'}, {'Funding_ID': '42', 'Project_Name': 'Latigo Canyon Road Culvert Repairs', 'Funding_Source': 'Community Fund', 'Amount': '57000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '45', 'Project_Name': 'Latigo Canyon Road Retaining Wall Repair Project', 'Funding_Source': 'Educational Sponsorship', 'Amount': '97000'}, {'Funding_ID': '46', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '19000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '49', 'Project_Name': 'Legacy Park Benches and Arbors Renovation', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '41000'}, {'Funding_ID': '50', 'Project_Name': 'Legacy Park Paver Repair Project', 'Funding_Source': 'Community Fund', 'Amount': '69000'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:12': {'funding_records': 50, 'civic_docs': 19, 'fema_docs': 19, 'emergency_docs': 5}, 'var_functions.execute_python:20': [{'project_name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'funding_source': 'Research Institution Funding', 'amount': 14000, 'funding_id': '7'}, {'project_name': 'Clover Heights Storm Drain (FEMA Project)', 'funding_source': 'Local NGO Fund', 'amount': 21000, 'funding_id': '22'}, {'project_name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'funding_source': 'Municipal Fund', 'amount': 43000, 'funding_id': '25'}, {'project_name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'funding_source': 'Taxpayer Contribution', 'amount': 15000, 'funding_id': '26'}, {'project_name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'funding_source': 'Local Business Support', 'amount': 25000, 'funding_id': '28'}, {'project_name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'funding_source': 'Cultural Heritage Grant', 'amount': 58000, 'funding_id': '29'}, {'project_name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'funding_source': 'Private Sponsor', 'amount': 94000, 'funding_id': '35'}, {'project_name': 'Guardrail Replacement Citywide (FEMA Project)', 'funding_source': 'Impact Investment Fund', 'amount': 22000, 'funding_id': '38'}, {'project_name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'funding_source': 'Development Bank Loan', 'amount': 45000, 'funding_id': '39'}, {'project_name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'funding_source': 'Federal Assistance', 'amount': 36000, 'funding_id': '43'}, {'project_name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'funding_source': 'National Foundation Fund', 'amount': 44000, 'funding_id': '44'}, {'project_name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'funding_source': 'Municipal Fund', 'amount': 91000, 'funding_id': '47'}, {'project_name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'funding_source': 'Community Fund', 'amount': 78000, 'funding_id': '48'}, {'project_name': 'Birdview Avenue Improvements (CalOES Project)', 'funding_source': 'International Aid', 'amount': 85000, 'funding_id': '6'}, {'project_name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'funding_source': 'Government Grant', 'amount': 81000, 'funding_id': '11'}, {'project_name': 'Corral Canyon Culvert Repairs', 'funding_source': 'Federal Assistance', 'amount': 54000, 'funding_id': '24'}, {'project_name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'funding_source': 'Educational Sponsorship', 'amount': 18000, 'funding_id': '34'}]}

exec(code, env_args)
