code = """import json
import pandas as pd
import re

# Load data
f_file = locals()['var_functions.query_db:9']
with open(f_file, 'r') as f:
    funding_data = json.load(f)

c_file = locals()['var_functions.query_db:5']
with open(c_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding DataFrame
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Extract project information from civic documents
projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project names and schedules
    # Patterns to match:
    # 1. Project names at the start of lines or after bullet points
    # 2. Schedule lines with dates
    
    lines = text.split('\n')
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names (typically title case, not followed by "Updates:" or "Project Schedule:")
        if (line and 
            not line.startswith('(') and 
            not line.startswith('Page') and 
            not line.startswith('Agenda') and
            not any(keyword in line for keyword in ['Updates:', 'Project Schedule:', 'RECOMMENDED ACTION', 'DISCUSSION:', 'To:', 'Prepared by:', 'Approved by:', 'Date prepared:', 'Meeting date:', 'Subject:']) and
            len(line) > 10 and
            len(line.split()) <= 15 and
            (i == 0 or not lines[i-1].strip().startswith('('))):
            
            # Check if next line looks like project details or if this is a section header
            next_line = lines[i+1].strip() if i+1 < len(lines) else ''
            if 'Updates:' in next_line or 'Project Schedule:' in next_line:
                current_project = line
                
                # Look for schedule info after this project
                for j in range(i+1, min(i+10, len(lines))):
                    schedule_line = lines[j].strip()
                    if 'Updates:' in schedule_line or 'Project Schedule:' in schedule_line:
                        # Look for date patterns in the next few lines
                        for k in range(j+1, min(j+5, len(lines))):
                            date_line = lines[k].strip()
                            # Look for 2022 dates
                            if '2022' in date_line:
                                projects.append({
                                    'Project_Name': current_project,
                                    'Start_Date_Info': date_line,
                                    'Source_File': filename
                                })
                                break
                        break

# Look more specifically for disaster projects with 2022 start dates
disaster_indicators = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster', 'recovery']

# More comprehensive extraction
comprehensive_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Find all potential project names and their contexts
    # Projects often appear before "Updates:" or "Project Schedule:"
    pattern = r'([A-Z][^\n]{10,100})\n\s*\(cid:\d+\)\s*Updates:'
    
    matches = re.finditer(pattern, text, re.IGNORECASE)
    
    for match in matches:
        project_name = match.group(1).strip()
        
        # Get the context after the match (up to 500 chars)
        start_pos = match.end()
        context = text[start_pos:start_pos+500]
        
        # Check for 2022 dates in context
        if '2022' in context:
            # Look for disaster indicators in project name or nearby
            project_lower = project_name.lower()
            context_lower = context.lower()
            
            is_disaster = any(indicator.lower() in project_lower or 
                             indicator.lower() in context_lower 
                             for indicator in disaster_indicators)
            
            if is_disaster:
                # Extract date info
                date_lines = []
                for line in context.split('\n'):
                    if '2022' in line:
                        date_lines.append(line.strip())
                        break
                
                comprehensive_projects.append({
                    'Project_Name': project_name,
                    'Is_Disaster': is_disaster,
                    'Date_Info': date_lines[0] if date_lines else context[:200],
                    'Disaster_Type_Detected': is_disaster
                })

print('Total projects extracted:', len(projects))
print('Comprehensive extraction count:', len(comprehensive_projects))

if comprehensive_projects:
    print('\nSample disaster projects from 2022:')
    for proj in comprehensive_projects[:5]:
        print('  Name:', proj['Project_Name'])
        print('  Date:', proj['Date_Info'])
        print()

# Check if any project names match funding data
if comprehensive_projects:
    project_names = [p['Project_Name'] for p in comprehensive_projects]
    matching_funding = funding_df[funding_df['Project_Name'].isin(project_names)]
    print('Matching funding records:', len(matching_funding))
    if len(matching_funding) > 0:
        print('Total from matching:', matching_funding['Amount'].sum())

# Alternative: Find all disaster funding and manually check for 2022 indicators
all_disaster_keywords = ['FEMA', 'CalOES', 'CalJPIA', 'fire', 'disaster']
all_disaster_funding = funding_df[
    funding_df['Project_Name'].str.contains('|'.join(all_disaster_keywords), case=False, na=False)
]

print('\nTotal disaster funding (all years):', all_disaster_funding['Amount'].sum())
print('Disaster project count (all years):', len(all_disaster_funding))

# Check which disaster projects have 2022 in their name
funding_2022_in_name = all_disaster_funding[all_disaster_funding['Project_Name'].str.contains('2022', case=False, na=False)]
print('\nDisaster projects with 2022 in name:')
print(funding_2022_in_name[['Project_Name', 'Amount']].to_string())

result = {
    'comprehensive_projects_count': len(comprehensive_projects),
    'total_disaster_funding_all_years': int(all_disaster_funding['Amount'].sum()),
    'disaster_funding_2022_in_name': int(funding_2022_in_name['Amount'].sum()) if len(funding_2022_in_name) > 0 else 0
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:18': {'total_disaster_funding': 1410000, 'disaster_project_count': 27, 'sample_projects': [{'Project_Name': 'Birdview Avenue Improvements (CalOES Project)', 'Amount': 85000}, {'Project_Name': 'Birdview Avenue Improvements (FEMA/CalOES Project)', 'Amount': 14000}, {'Project_Name': 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Amount': 81000}, {'Project_Name': 'Clover Heights Storm Drain (FEMA Project)', 'Amount': 21000}, {'Project_Name': 'Corral Canyon Culvert Repairs (FEMA Project)', 'Amount': 43000}]}}

exec(code, env_args)
