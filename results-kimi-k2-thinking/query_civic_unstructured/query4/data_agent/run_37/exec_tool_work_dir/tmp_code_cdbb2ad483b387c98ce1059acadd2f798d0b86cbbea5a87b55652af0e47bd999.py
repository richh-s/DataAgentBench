code = """import json, re

# Access the civic documents data
civic_docs = locals().get('var_functions.query_db:2', [])

if not civic_docs:
    print('No civic documents data available')
    result = {'error': 'no_data'}
else:
    print('Processing', len(civic_docs), 'documents')
    
    # Extract projects from documents
    all_projects = []
    
    for doc in civic_docs:
        text = doc.get('text', '')
        filename = doc.get('filename', '')
        
        # Split into lines for easier parsing
        lines = text.split('\n')
        
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            
            # Look for project name patterns
            # Projects often appear as standalone lines with title format
            if (len(line) > 10 and 
                not line.startswith('(') and 
                not line.startswith('cid:') and
                not line.startswith('Page') and
                not any(keyword in line for keyword in [
                    'RECOMMENDED ACTION', 'DISCUSSION', 'Prepared by', 
                    'Approved by', 'Subject:', 'To:', 'Meeting date', 
                    'Capital Improvement Projects', 'Disaster Recovery Projects',
                    'Project Schedule', 'Updates', 'Project Description'
                ]) and
                (line.istitle() or ('2022' in line) or ('Project' in line))):
                
                # This might be a project name
                project_name = line
                
                # Look ahead for schedule/project details
                project_details = {'Project_Name': project_name, 'filename': filename}
                
                # Check next few lines for dates
                for j in range(i+1, min(i+10, len(lines))):
                    next_line = lines[j].strip()
                    
                    # Look for date patterns
                    if 'Complete Design:' in next_line or 'Begin Construction:' in next_line or 'Advertise:' in next_line:
                        if '2022' in next_line:
                            project_details['has_2022_date'] = True
                            # Extract the season if mentioned
                            if 'Spring' in next_line:
                                project_details['season'] = 'Spring'
                            elif 'Summer' in next_line:
                                project_details['season'] = 'Summer'
                            elif 'Fall' in next_line:
                                project_details['season'] = 'Fall'
                            elif 'Winter' in next_line:
                                project_details['season'] = 'Winter'
                    
                    # Break if we hit another project or major section
                    if next_line == '' and j > i+2:
                        break
                
                # Also check if project name itself contains year info
                if '2022' in project_name:
                    project_details['has_2022_date'] = True
                    
                    # Check for season in name
                    if 'Spring' in project_name:
                        project_details['season'] = 'Spring'
                
                if 'has_2022_date' in project_details:
                    all_projects.append(project_details)
                    i += 5  # Skip ahead to avoid duplicate detection
                    continue
            
            i += 1
    
    print('Extracted', len(all_projects), 'projects with 2022 dates')
    
    # Filter for Spring 2022 projects
    spring_2022_projects = []
    for proj in all_projects:
        # Check if it's Spring 2022
        is_spring_2022 = False
        
        project_name = proj.get('Project_Name', '')
        
        # Direct mention of Spring 2022
        if 'Spring 2022' in project_name or '2022-Spring' in project_name:
            is_spring_2022 = True
        elif '2022' in project_name:
            # Check if it's in the filename or context suggesting Spring
            # Spring = March, April, May (months 3-5)
            filename = proj.get('filename', '')
            if 'Spring' in str(proj):
                is_spring_2022 = True
        elif '2022' in str(proj.get('filename', '')):
            # Check file date
            filename = proj.get('filename', '')
            if '01262022' in filename or '022022' in filename or '032022' in filename:
                # January, February, March = could be Spring (March is Spring)
                if '032022' in filename:
                    is_spring_2022 = True
        
        if is_spring_2022:
            spring_2022_projects.append(proj)
    
    print('Found', len(spring_2022_projects), 'Spring 2022 projects')
    
    # Show some examples
    for p in spring_2022_projects[:5]:
        print('Project:', p['Project_Name'])
    
    result = {
        'total_projects_with_2022': len(all_projects),
        'spring_2022_projects_count': len(spring_2022_projects),
        'spring_2022_projects': spring_2022_projects
    }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:12': {'status': 'error', 'message': "[Errno 2] No such file or directory: '/tmp/tmpub7z9f6a.json'"}, 'var_functions.execute_python:14': {'available_vars': ['var_functions.query_db:2', 'var_functions.query_db:5']}, 'var_functions.execute_python:18': {'step': 'inspection'}, 'var_functions.execute_python:20': {'check': 'complete'}, 'var_functions.query_db:22': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}, {'Funding_ID': '3', 'Project_Name': '2022 Morning View Resurfacing & Storm Drain Improvements', 'Funding_Source': 'State Development Grant', 'Amount': '38000'}, {'Funding_ID': '4', 'Project_Name': 'Annual Street Maintenance', 'Funding_Source': 'Corporate Sponsorship', 'Amount': '23000'}, {'Funding_ID': '5', 'Project_Name': 'Birdview Avenue Improvements', 'Funding_Source': 'National Foundation Fund', 'Amount': '79000'}]}

exec(code, env_args)
