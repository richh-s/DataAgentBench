code = """import os
import json
import re

# Read the data from storage
with open('/tmp/tmpyq7d3x4g.json', 'r') as f:
    civic_docs = json.load(f)

# Initialize a list to store all projects
all_projects = []

for doc in civic_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Extract year from filename
    year_match = re.search(r'(?:20\d{2})', filename)
    doc_year = year_match.group() if year_match else None
    
    # Find different project sections
    sections = []
    
    # Design section
    design_start = text.find('Capital Improvement Projects (Design)')
    if design_start >= 0:
        end = text.find('Capital Improvement Projects (', design_start + 10)
        if end < 0: end = len(text)
        sections.append(('design', 'capital', text[design_start:end]))
    
    # Construction section
    construction_start = text.find('Capital Improvement Projects (Construction)')
    if construction_start >= 0:
        end = text.find('Capital Improvement Projects (', construction_start + 10)
        if end < 0: end = len(text)
        sections.append(('completed', 'capital', text[construction_start:end]))
    
    # Not Started section
    notstarted_start = text.find('Capital Improvement Projects (Not Started)')
    if notstarted_start >= 0:
        end = text.find('\n\n', notstarted_start + 20)
        if end < 0: end = len(text)
        sections.append(('not started', 'capital', text[notstarted_start:end]))
    
    # Disaster section (simpler pattern)
    disaster_keywords = ['FEMA', 'Disaster Recovery', 'Woolsey Fire', 'CalOES', 'CalJPIA']
    for keyword in disaster_keywords:
        if keyword in text:
            # Find sections mentioning disaster projects
            for match in re.finditer(keyword, text):
                start = max(0, match.start() - 200)
                end = min(len(text), match.end() + 500)
                snippet = text[start:end]
                sections.append(('design', 'disaster', snippet))
            break
    
    for status, proj_type, section in sections:
        # Split into potential projects at double newlines
        chunks = section.split('\n\n')
        for chunk in chunks:
            chunk = chunk.strip()
            if len(chunk) < 30 or 'Capital Improvement' in chunk:
                continue
            
            # Get first line as project name
            lines = chunk.split('\n')
            proj_name = lines[0].strip()[:200]
            if not proj_name or proj_name.startswith('(') or proj_name.startswith('Page'):
                continue
            
            # Determine topics
            lower = chunk.lower()
            topics = []
            if 'park' in lower: topics.append('park')
            if 'road' in lower: topics.append('road')
            if 'storm' in lower or 'drainage' in lower: topics.append('storm drain')
            if 'FEMA' in chunk.upper() or 'disaster' in lower or 'fire' in lower: 
                topics.extend(['FEMA', 'disaster'])
                proj_type = 'disaster'
            if 'emergency' in lower or 'warning' in lower: topics.append('emergency warning')
            
            # Check for Spring 2022
            st = None
            if '2022' in chunk:
                if 'Spring 2022' in chunk or 'spring 2022' in chunk:
                    st = '2022-Spring'
                elif any(word in lower for word in ['march', 'april', 'may']):
                    if '2022' in chunk:
                        st = '2022-Spring'
            elif doc_year == '2022' and any(word in lower for word in ['spring', 'march', 'april', 'may']):
                st = '2022-Spring'
            
            all_projects.append({
                'Project_Name': proj_name,
                'topic': ', '.join(topics),
                'type': proj_type,
                'status': status,
                'st': st,
                'et': None,
                'source_file': filename
            })

# Filter for Spring 2022 projects
spring_2022 = [p for p in all_projects if p['st'] and '2022-Spring' in p['st']]

print('Total extracted: ' + str(len(all_projects)))
print('Spring 2022: ' + str(len(spring_2022)))

# Save results
with open('/tmp/all_projects.json', 'w') as f:
    json.dump(all_projects, f, indent=2)

with open('/tmp/spring_2022_projects.json', 'w') as f:
    json.dump(spring_2022, f, indent=2)

print('__RESULT__:')
print(json.dumps({
    'total_extracted': len(all_projects),
    'spring_2022_count': len(spring_2022),
    'spring_2022': spring_2022
}))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json'}

exec(code, env_args)
