code = """import json
import re
import pandas as pd

# Load funding data
funding_file = locals()['var_functions.query_db:8']
with open(funding_file, 'r') as f:
    funding_data = json.load(f)

# Load civic documents
civic_file = locals()['var_functions.query_db:9']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Create funding dataframe
funding_df = pd.DataFrame(funding_data)
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'])

# Function to extract projects with Spring 2022 dates
def extract_spring_2022_projects(text):
    projects = []
    
    # Look for project sections - split by common headers
    # Pattern: Project name line followed by info
    lines = text.split('\n')
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Skip empty lines, bullet points, and headers
        if (not line or 
            line.startswith('(') or 
            line.startswith('•') or 
            line.startswith('cid:') or
            line.isupper() or
            line.startswith('To:') or
            'Prepared by:' in line or
            'Subject:' in line or
            'Agenda' in line):
            continue
            
        # Look for potential project names (contain key terms but not typical headers)
        project_keywords = ['Project', 'Improvement', 'Repair', 'Drainage', 'Resurfacing', 'Replacement', 'Bridge', 'Culvert', 'Road', 'Street', 'Park']
        has_keyword = any(keyword in line for keyword in project_keywords)
        
        # Check if line looks like a project name (not too short, not all numbers)
        if has_keyword and len(line) > 8 and not line.startswith('Page'):
            # Look ahead for date information
            context = ''
            if i + 1 < len(lines):
                context = ' '.join(lines[i:i+4])
            
            # Check for Spring 2022 dates
            spring_2022_patterns = [
                r'2022[-\s]Spring',
                r'Spring[-\s]2022',
                r'2022[-\s]March',
                r'March[-\s]2022',
                r'2022[-\s]April',
                r'April[-\s]2022',
                r'2022[-\s]May',
                r'May[-\s]2022'
            ]
            
            has_spring_2022 = any(re.search(pattern, context, re.IGNORECASE) for pattern in spring_2022_patterns)
            
            # Also check for Complete Design/Advertise/Begin Construction dates in 2022
            if re.search(r'(Complete Design|Advertise|Begin Construction):[^\n]*2022', context):
                if 'Spring' in context or 'March' in context or 'April' in context or 'May' in context:
                    has_spring_2022 = True
            
            if has_spring_2022:
                projects.append(line.strip())
    
    return projects

# Extract all Spring 2022 projects
all_spring_projects = []
for doc in civic_docs:
    projects = extract_spring_2022_projects(doc['text'])
    all_spring_projects.extend(projects)

# Remove duplicates
all_spring_projects = list(set(all_spring_projects))

print('__RESULT__:') 
print(json.dumps({
    'spring_2022_projects': all_spring_projects,
    'count': len(all_spring_projects)
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:6': {'total_docs': 5, 'sample_doc_preview': 'Public Works Commission\nAgenda Report\n\nPublic Works\nCommission Meeting\n03-22-23\nItem\n4.B.\n\nTo:\n\nChair Dittrich and Members of the Public Works Commission\n\nPrepared by:\n\nJorge Rubalcava, Senior Civil Engineer\n\nApproved by:\n\nRob DuBoux, Public Works Director/City Engineer\n\nDate prepared: March 15, 2023\n\nMeeting date: March 22, 2023\n\nSubject:\n\nCapital Improvement Projects and Disaster Recovery Projects Status\nReport\n\nRECOMMENDED ACTION: Receive and file report on the status of the City’s current and\nupcoming Capital Improvement Projects and Disaster Recovery Projects.\n\nDISCUSSION: Staff will provide a status update on the following active projects in the\nFiscal Year 2022-2023 Capital Improvement Program:\n\nCapital Improvement Projects (Design)\n\n2022 Morning View Resurfacing & Storm Drain Improvements\n\n(cid:190) Updates:\n\n(cid:131) Staff is working with the consultant to finalize the design plans for this\n\nproject and will submit to the County for review.\n\n(cid:190) Project Schedule:\n\n(cid:'}, 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'funding_records': 500, 'civic_docs': 5, 'sample_funding': [{'Funding_ID': '1', 'Project_Name': '2021 Annual Street Maintenance', 'Funding_Source': 'Public-Private Partnership (PPP)', 'Amount': '24000'}, {'Funding_ID': '2', 'Project_Name': '2022 Annual Street Maintenance', 'Funding_Source': 'Government Grant', 'Amount': '45000'}], 'sample_civic': 9796}}

exec(code, env_args)
