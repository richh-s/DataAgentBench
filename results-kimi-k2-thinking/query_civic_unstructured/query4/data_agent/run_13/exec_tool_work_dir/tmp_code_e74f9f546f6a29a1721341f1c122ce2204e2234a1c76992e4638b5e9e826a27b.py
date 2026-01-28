code = """import json
import re

# Load both datasets
civic_docs_path = locals()['var_functions.query_db:4']
funding_path = locals()['var_functions.query_db:5']

with open(civic_docs_path, 'r') as f:
    civic_docs = json.load(f)

with open(funding_path, 'r') as f:
    funding = json.load(f)

# Step 1: Extract projects with Spring 2022 start dates from civic documents
spring_2022_projects = set()
project_start_dates = {}

for doc in civic_docs:
    text = doc['text']
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue
        
        # Look for project name patterns
        # Project names are typically uppercase or title case, not page headers
        if (len(line) > 10 and 
            line[0].isupper() and 
            not line.startswith('Page') and 
            not line.startswith('Item') and
            'PUBLIC WORKS' not in line and
            'COMMISSION' not in line and
            'AGENDA' not in line and
            'REPORT' not in line and
            'MINUTES' not in line):
            
            # Check if next few lines contain project indicators (updates, schedule)
            next_lines = ' '.join(lines[i+1:min(i+5, len(lines))])
            if 'Updates:' in next_lines or 'Schedule:' in next_lines:
                current_project = line
        
        # Look for Spring 2022 start/end dates
        if current_project:
            lower_line = line.lower()
            
            # Check for Spring 2022 patterns
            spring_patterns = [
                r'spring\s*2022',
                r'2022\s*-?\s*spring',
                r'mar(ch)?\s*2022',
                r'apr(il)?\s*2022',
                r'may\s*2022',
                r'2022[-\s](0?[3-5]|03|04|05)'
            ]
            
            # Check if line mentions a date with begin/start/advertise/complete
            if ('begin' in lower_line or 'start' in lower_line or 'advertise' in lower_line or 
                'complete' in lower_line or 'construction' in lower_line or 'design' in lower_line):
                
                for pattern in spring_patterns:
                    if re.search(pattern, lower_line):
                        spring_2022_projects.add(current_project)
                        project_start_dates[current_project] = line
                        break

# Step 2: Get the list of project names
project_list = sorted(list(spring_2022_projects))

# Step 3: Match with funding data
total_funding = 0
matched_projects = []

# Create a mapping for easier lookup
funding_by_name = {f['Project_Name'].lower(): f for f in funding}

for project in project_list:
    project_lower = project.lower()
    
    # Try exact match first
    if project_lower in funding_by_name:
        amount = int(funding_by_name[project_lower]['Amount'])
        total_funding += amount
        matched_projects.append({
            'project': project,
            'funding_record': funding_by_name[project_lower]['Project_Name'],
            'amount': amount
        })
        continue
    
    # Try partial matching
    for fund_lower, fund in funding_by_name.items():
        if (project_lower in fund_lower or fund_lower in project_lower or
            any(word in fund_lower for word in project_lower.split() if len(word) > 6)):
            amount = int(fund['Amount'])
            total_funding += amount
            matched_projects.append({
                'project': project,
                'funding_record': fund['Project_Name'],
                'amount': amount
            })
            break

# Step 4: Create final result
result = {
    'number_of_spring_2022_projects': len(project_list),
    'total_funding': total_funding,
    'project_names': project_list,
    'detailed_matches': matched_projects
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.list_db:1': ['Funding'], 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:28': {'spring_2022_docs': 4}, 'var_functions.execute_python:34': {'spring_2022_projects': 4, 'funding_matches': 31, 'total_funding': 1614000}, 'var_functions.execute_python:44': {'spring_2022_projects': 4, 'total_funding': 0}, 'var_functions.execute_python:50': {'spring_2022_projects': 4, 'total_funding': 83000}, 'var_functions.execute_python:54': {'spring_2022_projects': 4, 'total_funding': 0}, 'var_functions.query_db:58': [{'total_funding': 'None', 'project_count': '0'}], 'var_functions.execute_python:64': {'spring_2022_projects': 4, 'total_funding': 83000}, 'var_functions.query_db:70': [{'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}]}

exec(code, env_args)
