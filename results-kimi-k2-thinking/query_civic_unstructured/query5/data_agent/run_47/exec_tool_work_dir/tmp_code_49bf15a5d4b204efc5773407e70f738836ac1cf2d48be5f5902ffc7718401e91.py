code = """import json
import re

# Load the disaster-related funding data
disaster_funding = var_functions.query_db:20

# Load the civic documents
file_path = var_functions.query_db:24
with open(file_path, 'r') as f:
    civic_docs = json.load(f)

print(f"Found {len(disaster_funding)} disaster-related funding records")
print(f"Found {len(civic_docs)} 2022-related documents to analyze")

# Create a list of project names from funding data
project_names = [record['Project_Name'] for record in disaster_funding]

print(f"\nAnalyzing {len(project_names)} disaster projects for 2022 start dates...")

# Function to check if a project started in 2022
def check_project_start_in_2022(project_name, documents):
    # Clean project name for matching (remove suffixes if needed)
    base_name = project_name.split(' (')[0].strip()
    
    for doc in documents:
        text = doc.get('text', '')
        
        # Check if project name appears in the document
        if base_name in text or project_name in text:
            # Look for date patterns around the project name
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if base_name in line or project_name in line:
                    # Check this line and surrounding lines for 2022 dates
                    context_lines = lines[max(0, i-3):min(len(lines), i+4)]
                    context = ' '.join(context_lines).lower()
                    
                    # Check for various 2022 date patterns
                    date_patterns = [
                        r'2022[-\s]',
                        r'start.*2022',
                        r'2022.*start',
                        r'begin.*2022',
                        r'2022.*begin',
                        r'advertise.*2022',
                        r'2022.*advertise',
                        r'design.*2022',
                        r'2022.*design'
                    ]
                    
                    for pattern in date_patterns:
                        if re.search(pattern, context, re.IGNORECASE):
                            return True, ' '.join(context_lines)
    
    return False, None

# Check which projects started in 2022
projects_in_2022 = []
print("\nChecking each project...")

for i, project_name in enumerate(project_names):
    started_in_2022, context = check_project_start_in_2022(project_name, civic_docs)
    if started_in_2022:
        print(f"✓ {project_name}")
        projects_in_2022.append({
            'Project_Name': project_name,
            'Context': context
        })
    else:
        print(f"✗ {project_name}")

print(f"\nFound {len(projects_in_2022)} disaster projects that started in 2022")

# Calculate total funding for these projects
total_funding = 0
projects_with_funding = []

for project in projects_in_2022:
    project_name = project['Project_Name']
    # Find the funding amount
    for funding_record in disaster_funding:
        if funding_record['Project_Name'] == project_name:
            amount = int(funding_record['Amount'])
            total_funding += amount
            projects_with_funding.append({
                'Project_Name': project_name,
                'Amount': amount,
                'Funding_Source': funding_record['Funding_Source']
            })
            break

print(f"\nTotal funding for disaster projects started in 2022: ${total_funding:,}")
print("\nProject breakdown:")
for proj in projects_with_funding:
    print(f"- {proj['Project_Name']}: ${proj['Amount']:,} ({proj['Funding_Source']})")

result = {
    'total_funding': total_funding,
    'projects': projects_with_funding,
    'count': len(projects_with_funding)
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:4': [], 'var_functions.query_db:6': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:20': [{'Funding_ID': '6', 'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '85000'}, {'Funding_ID': '7', 'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Research Institution Funding', 'Amount': '14000'}, {'Funding_ID': '11', 'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '81000'}, {'Funding_ID': '22', 'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_Source': 'Local NGO Fund', 'Amount': '21000'}, {'Funding_ID': '25', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '43000'}, {'Funding_ID': '26', 'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Taxpayer Contribution', 'Amount': '15000'}, {'Funding_ID': '28', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '25000'}, {'Funding_ID': '29', 'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': '58000'}, {'Funding_ID': '34', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Funding_Source': 'Educational Sponsorship', 'Amount': '18000'}, {'Funding_ID': '35', 'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Private Sponsor', 'Amount': '94000'}, {'Funding_ID': '38', 'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_Source': 'Impact Investment Fund', 'Amount': '22000'}, {'Funding_ID': '39', 'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_Source': 'Development Bank Loan', 'Amount': '45000'}, {'Funding_ID': '43', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_Source': 'Federal Assistance', 'Amount': '36000'}, {'Funding_ID': '44', 'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA/CalOES Project)', 'Funding_Source': 'National Foundation Fund', 'Amount': '44000'}, {'Funding_ID': '47', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Funding_Source': 'Municipal Fund', 'Amount': '91000'}, {'Funding_ID': '48', 'Project_Name': 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA/CalOES Project)', 'Funding_Source': 'Community Fund', 'Amount': '78000'}, {'Funding_ID': '59', 'Project_Name': 'Malibu Road Slope Repairs (CalOES Project)', 'Funding_Source': 'International Aid', 'Amount': '37000'}, {'Funding_ID': '66', 'Project_Name': 'Outdoor Warning Sirens (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '27000'}, {'Funding_ID': '67', 'Project_Name': 'Outdoor Warning Sirens (FEMA)', 'Funding_Source': 'State Development Grant', 'Amount': '81000'}, {'Funding_ID': '68', 'Project_Name': 'Outdoor Warning Sirens - Design (FEMA Project)', 'Funding_Source': 'Local Business Support', 'Amount': '43000'}, {'Funding_ID': '69', 'Project_Name': 'Outdoor Warningn Sirens - Design (FEMA Project)', 'Funding_Source': 'Technology Innovation Fund', 'Amount': '84000'}, {'Funding_ID': '82', 'Project_Name': 'Storm Drain Master Plan (FEMA Project)', 'Funding_Source': 'Environmental Grant', 'Amount': '80000'}, {'Funding_ID': '86', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '44000'}, {'Funding_ID': '87', 'Project_Name': 'Trancas Canyon Park Planting and Irrigation Repairs (FEMA/CalOES Project)', 'Funding_Source': 'Infrastructure Bond', 'Amount': '92000'}, {'Funding_ID': '91', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'Funding_Source': 'Government Grant', 'Amount': '43000'}, {'Funding_ID': '92', 'Project_Name': 'Trancas Canyon Park Slope Stabilization Project (CalOES Project)', 'Funding_Source': 'International Organization Grant', 'Amount': '32000'}, {'Funding_ID': '99', 'Project_Name': 'Westward Beach Road Shoulder Repairs (CalOES Project)', 'Funding_Source': 'Local Business Support', 'Amount': '77000'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json'}

exec(code, env_args)
