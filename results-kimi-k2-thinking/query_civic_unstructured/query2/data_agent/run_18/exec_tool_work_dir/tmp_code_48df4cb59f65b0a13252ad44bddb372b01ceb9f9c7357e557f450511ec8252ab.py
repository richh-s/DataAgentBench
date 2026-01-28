code = """import json
import pandas as pd
import re

# Load funding data
with open('/tmp/tmp8opjs8_m.json', 'r') as f:
    funding_data = json.load(f)

# Load civic documents data
with open('/tmp/tmpg5k2n9mq.json', 'r') as f:
    civic_docs_data = json.load(f)

# Convert funding data to DataFrame
funding_df = pd.DataFrame(funding_data)
print('Total funding records: ' + str(len(funding_df)))

# Sample of funding data first few records
print('\nSample funding data:')
print(funding_df.head().to_string())

print('\nTotal civic documents: ' + str(len(civic_docs_data)))

# Process all civic documents to extract project information
print('\nProcessing civic documents to extract project information...')

# Function to extract project info from text
def extract_projects_from_text(text):
    projects = []
    lines = text.split('\n')
    
    current_project = None
    
    for i, line in enumerate(lines):
        line = line.strip()
        
        # Look for project names (typically bold or standalone lines)
        if line and len(line) > 5 and not line.startswith('(') and not line.startswith('•'):
            # Skip headers
            skip_patterns = ['Agenda', 'Public Works', 'Commission', 'Capital Improvement', 
                           'Disaster Recovery', 'Page', 'Item', 'To:', 'From:', 'Subject:', 
                           'Date prepared:', 'Meeting date:', 'RECOMMENDED ACTION:', 'DISCUSSION:']
            
            should_skip = any(pattern in line for pattern in skip_patterns)
            
            if not should_skip and not line.isupper() and len(line.split()) < 15:
                # Check if this looks like a project name
                project_indicators = ['Project', 'Improvements', 'Repairs', 'Replacement', 
                                    'Construction', 'Installation', 'System', 'Study']
                
                # Look at surrounding lines for context
                context_start = max(0, i-2)
                context_end = min(len(lines), i+10)
                context = ' '.join(lines[context_start:context_end])
                
                # Check for topics and status in context
                topics = []
                if 'park' in context.lower():
                    topics.append('park')
                if 'road' in context.lower():
                    topics.append('road')
                if 'drain' in context.lower() or 'storm' in context.lower():
                    topics.append('drainage')
                if 'FEMA' in context:
                    topics.append('FEMA')
                if 'fire' in context.lower():
                    topics.append('fire')
                
                # Determine status and year
                status = None
                year = None
                
                # Look for completion indicators with 2022
                completion_patterns = [
                    (r'(?:completed|construction was completed|notice of completion).*?2022', 'completed', '2022'),
                    (r'(?:completed|construction was completed|notice of completion).*?November 2022', 'completed', '2022'),
                    (r'(?:completed|construction was completed|notice of completion).*?January 2023', 'completed', '2022'),
                    (r'Complete Construction.*?2022', 'completed', '2022'),
                    (r'Complete Construction.*?Summer 2022', 'completed', '2022'),
                    (r'Complete Construction.*?Fall 2022', 'completed', '2022'),
                ]
                
                for pattern, stat, yr in completion_patterns:
                    if re.search(pattern, context, re.IGNORECASE):
                        status = stat
                        year = yr
                        break
                
                # If not completed, check for other statuses
                if not status:
                    if 'design' in context.lower() and 'complete design' in context.lower():
                        status = 'design'
                    elif 'not started' in context.lower():
                        status = 'not started'
                
                if topics and status == 'completed' and year == '2022':
                    projects.append({
                        'Project_Name': line,
                        'topic': ','.join(topics),
                        'status': status,
                        'year': year,
                        'full_context': context
                    })
    
    return projects

# Extract projects from all documents
all_projects = []
for doc in civic_docs_data:
    projects = extract_projects_from_text(doc['text'])
    all_projects.extend(projects)

print('\nExtracted park-related projects completed in 2022:')
park_projects_2022 = [p for p in all_projects if 'park' in p['topic']]
for proj in park_projects_2022:
    print('Name: ' + proj['Project_Name'])
    print('Topic: ' + proj['topic'] + ', Status: ' + proj['status'] + ', Year: ' + proj['year'])
    print('---')

print('\nTotal park projects completed in 2022 found: ' + str(len(park_projects_2022)))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:1': 'file_storage/functions.query_db:1.json'}

exec(code, env_args)
