code = """import json
import re

# Load civic docs
civic_docs = locals()['var_functions.query_db:5']
if isinstance(civic_docs, str):
    with open(civic_docs, 'r') as f:
        civic_docs = json.load(f)

# Parse all civic documents to extract project information
all_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project patterns
    # Common patterns in the text documents
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names - typically on their own line or with status indicators
        # Skip empty lines, agenda items, and section headers
        if (line and not line.startswith('Item') and not line.startswith('To:') and 
            not line.startswith('Prepared by') and not line.startswith('Approved by') and
            not line.startswith('Date prepared') and not line.startswith('Meeting date') and
            not line.startswith('Subject') and not line.startswith('RECOMMENDED ACTION') and
            not line.startswith('DISCUSSION') and not line.startswith('Capital Improvement') and
            not line.startswith('Page') and not line.startswith('Agenda Item') and
            not line.startswith('Project Description') and not line.startswith('Project Updates') and
            not line.startswith('Project Schedule')):
            
            # Check if this might be a project name (typically title case or with specific keywords)
            if (len(line) > 10 and not line.endswith(':') and 
                not all(word.isupper() for word in line.split()[:3]) and  # Not all uppercase heading
                any(keyword in line.lower() for keyword in ['project', 'repair', 'improvement', 'maintenance', 'replacement']) or
                any(keyword in line for keyword in ['Road', 'Street', 'Park', 'Drain', 'Bridge', 'Culvert', 'Drive', 'Avenue'])):
                
                project_name = line
                
                # Look for date information near this project (within next few lines)
                start_date = None
                for j in range(i+1, min(i+5, len(lines))):
                    next_line = lines[j].strip()
                    
                    # Look for date patterns like 2022, 2022-Spring, etc.
                    if '2022' in next_line or '2021' in next_line or '2023' in next_line:
                        # Look for start/completion dates
                        if any(phrase in next_line for phrase in ['Complete ', 'Complete:', 'Schedule:', 'Advertise:', 'Begin Construction:', 'Complete Construction:', 'Estimated Schedule:', 'Complete Design:']):
                            # Extract year
                            year_match = re.search(r'(202\d)', next_line)
                            if year_match:
                                start_date = year_match.group(1)
                                break
                
                # Classify project type based on keywords
                project_type = None
                if any(keyword in project_name.upper() for keyword in ['FEMA', 'CALOES', 'CALJPIA']):
                    project_type = 'disaster'
                elif any(keyword in project_name.lower() for keyword in ['drain', 'storm', 'road', 'street', 'bridge', 'culvert', 'park', 'facility']):
                    project_type = 'capital'
                
                # Extract status if mentioned
                status = None
                if any(keyword in line for keyword in ['(Design)', '(Construction)', '(Not Started)', '(Completed)']):
                    status = line.split('(')[-1].replace(')', '')
                
                all_projects.append({
                    'Project_Name': project_name,
                    'start_date': start_date,
                    'type': project_type,
                    'status': status,
                    'filename': filename
                })

# Filter projects with 2022 start dates
disaster_2022_projects = []

for project in all_projects:
    if project['type'] == 'disaster' and project['start_date'] and '2022' in project['start_date']:
        disaster_2022_projects.append(project['Project_Name'])

print('__RESULT__:')
print(json.dumps({
    'total_projects_extracted': len(all_projects),
    'disaster_2022_projects': disaster_2022_projects[:20],  # Show first 20
    'sample_projects': all_projects[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': {'total_disaster_projects_in_funding': 20, 'sample_disaster_projects': [{'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Funding_ID': '7', 'Funding_Source': 'Research Institution Funding', 'Amount': 14000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Funding_ID': '22', 'Funding_Source': 'Local NGO Fund', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Funding_ID': '25', 'Funding_Source': 'Municipal Fund', 'Amount': 43000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA/CalOES Project)', 'Funding_ID': '26', 'Funding_Source': 'Taxpayer Contribution', 'Amount': 15000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA Project)', 'Funding_ID': '28', 'Funding_Source': 'Local Business Support', 'Amount': 25000}, {'Project_Name': 'Corral Canyon Road Bridge Repairs (FEMA/CalOES Project)', 'Funding_ID': '29', 'Funding_Source': 'Cultural Heritage Grant', 'Amount': 58000}, {'Project_Name': 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Funding_ID': '35', 'Funding_Source': 'Private Sponsor', 'Amount': 94000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA Project)', 'Funding_ID': '38', 'Funding_Source': 'Impact Investment Fund', 'Amount': 22000}, {'Project_Name': 'Guardrail Replacement Citywide (FEMA/CalOES Project)', 'Funding_ID': '39', 'Funding_Source': 'Development Bank Loan', 'Amount': 45000}, {'Project_Name': 'Latigo Canyon Road Culvert Repairs (FEMA Project)', 'Funding_ID': '43', 'Funding_Source': 'Federal Assistance', 'Amount': 36000}]}}

exec(code, env_args)
