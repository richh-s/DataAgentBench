code = """import json
import os

# Access the file path from the query result
table_result = locals()['var_functions.query_db:2']
print('File path:', table_result)

# Load the civic documents
with open(table_result, 'r') as f:
    civic_docs = json.load(f)

print('Successfully loaded', len(civic_docs), 'documents')

# Initialize project tracking
spring_2022_projects = []

# Process each document to find Spring 2022 projects
for doc_idx, doc in enumerate(civic_docs):
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    
    # Look for Spring 2022 references in the text
    spring_patterns = ['2022-Spring', '2022-March', '2022-April', '2022-May', '2022-03', '2022-04', '2022-05']
    has_spring_2022 = any(pattern in text for pattern in spring_patterns)
    
    if has_spring_2022:
        # Extract lines containing project names and Spring 2022
        lines = text.split('\n')
        for line in lines:
            line = line.strip()
            # Look for project name patterns
            if line and any(keyword in line for keyword in ['Project', 'Improvements', 'Repairs', 'Repair', 'Improvement']):
                # Check if this line contains uppercase letters (indicating project name)
                upper_count = sum(1 for c in line if c.isupper())
                if upper_count > 3:  # Has some uppercase letters
                    # Check if there's a Spring 2022 reference near this line
                    context_start = max(0, lines.index(line) - 5)
                    context_end = min(len(lines), lines.index(line) + 5)
                    context = '\n'.join(lines[context_start:context_end])
                    
                    if any(pattern in context for pattern in spring_patterns):
                        spring_2022_projects.append({
                            'project_name': line[:200],  # Limit length
                            'filename': filename,
                            'doc_index': doc_idx
                        })

print('\nProjects starting in Spring 2022:')
for proj in spring_2022_projects[:20]:
    print(f"- {proj['project_name'][:100]}...")

result = {
    'spring_2022_count': len(spring_2022_projects),
    'projects': spring_2022_projects[:50]  # Return first 50
}

print('\n__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
