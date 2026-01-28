code = """import json
import re

# Load civic documents
civic_file = locals()['var_functions.query_db:4']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Now let's look for date patterns associated with projects
spring_2022_projects = []

# Patterns for Spring 2022
spring_patterns = [
    r'Spring\s+2022',
    r'2022-Spring',
    r'March\s+2022',
    r'April\s+2022', 
    r'May\s+2022',
    r'2022-March',
    r'2022-April',
    r'2022-May'
]

for doc in civic_docs:
    text = doc.get('text', '')
    
    # Check if this document contains any Spring 2022 references
    has_spring_2022 = any(re.search(pattern, text, re.IGNORECASE) for pattern in spring_patterns)
    
    if has_spring_2022:
        print(f'Found Spring 2022 reference in document: {doc.get("filename")}')
        
        # Extract sections that might contain project information
        # Look for capital improvement projects and disaster recovery projects sections
        sections = re.split(r'\n\s*\n', text)
        
        for section in sections:
            if re.search(r'(?:[Ss]pring\s+2022|2022-[Ss]pring|(?:March|April|May)\s+2022|2022-(?:March|April|May))', section, re.IGNORECASE):
                # This section contains Spring 2022, now extract project names
                lines = section.split('\n')
                for line in lines:
                    line = line.strip()
                    # Skip empty lines and common noise
                    if line and not line.startswith('(') and 'cid:' not in line:
                        # Look for potential project names (reasonable length, starts with capital)
                        if 15 < len(line) < 150 and line[0].isupper():
                            # Heuristic: project names often contain these words or are specific locations
                            project_keywords = ['Project', 'Improvements', 'Repair', 'Replacement', 'Renovation', 'Construction', 'Design']
                            location_keywords = ['Road', 'Street', 'Avenue', 'Drive', 'Canyon', 'Park', 'Beach', 'Highway', 'Bridge']
                            
                            if any(keyword in line for keyword in project_keywords) or \
                               (any(keyword in line for keyword in location_keywords) and len(line.split()) > 2):
                                spring_2022_projects.append(line)

# Remove duplicates
unique_spring = list(set(spring_2022_projects))
print(f'\nFound {len(unique_spring)} potential Spring 2022 projects')

for proj in unique_spring:
    print(f'  - {proj}')

# Also check for project schedules that might indicate start times
schedule_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    # Look for schedule indicators with Spring 2022
    schedule_matches = re.finditer(r'(?:Complete Design|Begin Construction|Advertise|Complete):\s*(Spring\s+2022|2022-Spring|March\s+2022|April\s+2022|May\s+2022)', text, re.IGNORECASE)
    
    for match in schedule_matches:
        # Look backwards to find the project name
        start_pos = max(0, match.start() - 500)
        context = text[start_pos:match.start()]
        
        # Try to extract project name from context
        lines = context.split('\n')
        for line in reversed(lines):
            line = line.strip()
            if line and line[0].isupper() and len(line) > 10:
                if any(keyword in line for keyword in ['Project', 'Improvements', 'Repair']):
                    schedule_projects.append(line + ' (Scheduled: ' + match.group(1) + ')')
                    break

unique_schedule = list(set(schedule_projects))
print(f'\nFound {len(unique_schedule)} projects with Spring 2022 schedules')
for proj in unique_schedule:
    print(f'  - {proj}')

print('\n__RESULT__:')
print(json.dumps({
    'potential_spring_projects': len(unique_spring),
    'scheduled_spring_projects': len(unique_schedule),
    'all_projects': unique_spring + unique_schedule
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}}

exec(code, env_args)
