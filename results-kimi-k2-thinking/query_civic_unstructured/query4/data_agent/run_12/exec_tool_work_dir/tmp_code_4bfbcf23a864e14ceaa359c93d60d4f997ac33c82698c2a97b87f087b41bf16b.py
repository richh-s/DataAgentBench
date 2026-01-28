code = """import json
import re

# Load the civic documents
result_file = var_functions.query_db:2
with open(result_file, 'r') as f:
    all_docs = json.load(f)

print('Loaded %d civic documents' % len(all_docs))

# Load the funding data
funding_file = var_functions.query_db:12
with open(funding_file, 'r') as f:
    funding_records = json.load(f)

print('Loaded %d funding records' % len(funding_records))

# Create a funding lookup by project name
funding_lookup = {}
for record in funding_records:
    project_name = record['Project_Name']
    amount = int(record['Amount'])
    if project_name in funding_lookup:
        funding_lookup[project_name] += amount
    else:
        funding_lookup[project_name] = amount

print('Created funding lookup with %d unique projects' % len(funding_lookup))

# Extract projects from civic documents
projects = []

for doc in all_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for project patterns in text
    # Projects often have names followed by schedule or status sections
    
    # Split by common section headers to find project blocks
    sections = re.split(r'\n(?=\w.*?\n\(cid:\d+\))', text)
    
    for section in sections:
        # Look for project name patterns
        # Project names are typically followed by bullet points with updates
        lines = section.strip().split('\n')
        if len(lines) < 2:
            continue
            
        # First line is likely the project name (not a bullet)
        first_line = lines[0].strip()
        if first_line and len(first_line) > 5 and not first_line.startswith('('):
            # This might be a project name
            project_name = first_line
            
            # Look for start date in section
            st_match = None
            for line in lines:
                line_lower = line.lower()
                # Look for start dates
                if 'begin' in line_lower or 'start' in line_lower or 'schedule' in line_lower:
                    # Look for Spring 2022 patterns
                    if 'spring 2022' in line_lower or '2022-spring' in line_lower:
                        st_match = '2022-Spring'
                        break
                    elif '2022-03' in line_lower or '2022-march' in line_lower:
                        st_match = '2022-03'
                        break
                    elif '2022-04' in line_lower or '2022-april' in line_lower:
                        st_match = '2022-04'
                        break
                    elif '2022-05' in line_lower or '2022-may' in line_lower:
                        st_match = '2022-05'
                        break
            
            if st_match:
                # Normalize project name
                clean_name = project_name.strip()
                
                # Check if this project has funding
                funding_amount = funding_lookup.get(clean_name, 0)
                
                projects.append({
                    'project_name': clean_name,
                    'start_time': st_match,
                    'filename': filename,
                    'funding_amount': funding_amount
                })

# Filter for Spring 2022 projects
spring_2022_projects = []
for project in projects:
    st = project['start_time']
    if st.startswith('2022') and ('spring' in st or '-03' in st or '-04' in st or '-05' in st):
        spring_2022_projects.append(project)

print('\nFound %d projects with Spring 2022 start times' % len(spring_2022_projects))

# Also check by examining text more directly for Spring 2022 mentions
# This more targeted approach
spring_projects_direct = []
for doc in all_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for sections mentioning Spring 2022 with project names
    for line in text.split('\n'):
        line = line.strip()
        if '2022' in line and ('spring' in line.lower() or '-03' in line or '-04' in line or '-05' in line):
            # Look at surrounding context
            context_start = max(0, text.find(line) - 200)
            context_end = min(len(text), text.find(line) + 300)
            context = text[context_start:context_end]
            
            # Extract potential project name from context
            sentences = context.split('\n')
            for sentence in sentences:
                if sentence.strip() and not sentence.startswith('(') and len(sentence.strip()) > 10:
                    # This might be a project name with Spring 2022 schedule
                    clean_sentence = sentence.strip()
                    
                    # Check if it has funding
                    funding_amount = 0
                    for funded_project in funding_lookup:
                        if funded_project in clean_sentence or clean_sentence in funded_project:
                            funding_amount = funding_lookup[funded_project]
                            break
                    
                    if funding_amount > 0:
                        spring_projects_direct.append({
                            'project_name': clean_sentence,
                            'start_time': '2022-Spring',
                            'funding_amount': funding_amount
                        })

print('Direct method found %d funded projects potentially starting Spring 2022' % len(spring_projects_direct))

# Look at specific projects that mention "2022 Morning View Resurfacing" which we know has funding
for doc in all_docs:
    text = doc.get('text', '')
    if 'Morning View' in text and '2022' in text:
        print('Found Morning View project in document')
        # Extract the project name more carefully
        lines = text.split('\n')
        for i, line in enumerate(lines):
            if 'Morning View' in line and '2022' in line:
                print('Line %d: %s' % (i, line))
                # Look backward for the project name
                for j in range(max(0, i-5), i):
                    prev_line = lines[j].strip()
                    if prev_line and not prev_line.startswith('(') and len(prev_line) > 5:
                        print('Potential project name: %s' % prev_line)
                        
                        # Check funding
                        if prev_line in funding_lookup:
                            print('Found funding: $%d' % funding_lookup[prev_line])
                        break

print('\n__RESULT__')
print('Initial analysis completed')"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
