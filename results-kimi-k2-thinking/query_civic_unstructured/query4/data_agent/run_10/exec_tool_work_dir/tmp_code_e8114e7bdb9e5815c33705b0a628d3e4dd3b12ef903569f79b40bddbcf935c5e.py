code = """import json
import re

# Load civic documents
civic_file = locals()['var_functions.query_db:4']
with open(civic_file, 'r') as f:
    civic_docs = json.load(f)

# Let's examine document structure more carefully
sample_doc = civic_docs[0]
text = sample_doc['text']

print("Sample document text structure:")
print("=" * 80)
print(text[:1000])
print("=" * 80)

# Look for project patterns - they often appear with bullet points or specific formatting
project_indicators = [
    r'([A-Z][^.!?]*?(?:Project|Improvement|Repair|Renovation|Replacement)[^\n]*)',
    r'(?:cid:\d+)?\s*([A-Z][^.!?]*?(?:Project|Improvement|Repair)[^\n]*)',
    r'([A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,4}(?:\s+Project)?)'
]

all_potential_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    for pattern in project_indicators:
        matches = re.finditer(pattern, text)
        for match in matches:
            project_title = match.group(1).strip()
            if len(project_title) > 10 and len(project_title) < 200:
                all_potential_projects.append(project_title)

unique_potential = list(set(all_potential_projects))
print(f"\nFound {len(unique_potential)} potential project titles:")
for proj in unique_potential[:20]:
    print(f"  - {proj}")

# Now let's look for date patterns associated with projects
spring_2022_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    
    # Look for Spring 2022 or 2022-Spring patterns
    if re.search(r'Spring\s+2022|2022-Spring', text, re.IGNORECASE):
        # Extract sections around these dates
        sections = re.split(r'(?:\n\s*){2,}', text)
        for section in sections:
            if re.search(r'Spring\s+2022|2022-Spring', section, re.IGNORECASE):
                # Look for project names in these sections
                lines = section.split('\n')
                for line in lines:
                    line = line.strip()
                    if line and not line.startswith('(') and not line.startswith('cid:'):
                        if len(line) > 10 and len(line) < 150:
                            if any(keyword in line.lower() for keyword in ['project', 'improvement', 'repair', 'replacement']):
                                spring_2022_projects.append(line)

unique_spring = list(set(spring_2022_projects))
print(f"\nFound {len(unique_spring)} projects with Spring 2022 mentions:")
for proj in unique_spring:
    print(f"  - {proj}")

print("__RESULT__:")
print(json.dumps({
    "total_potential_projects": len(unique_potential),
    "spring_2022_mentions": len(unique_spring),
    "sample_spring_projects": unique_spring[:10]
}))"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': {'funding_records': 500, 'civic_docs': 5, 'unique_funded_projects': 500}, 'var_functions.execute_python:12': {'potential_projects': 1640, 'unique_projects': 94, 'sample_projects': ['2022\n\nTrancas Canyon Park Planting', 'The Cit', 'Complete Design', 'Malibu Bluffs Pa', 'Award Contract', 'Latigo Canyon Road', 'Westward Beach', 'Case Court', 'Complete Final Design', 'Westward Beach Road Shoulder Repairs']}}

exec(code, env_args)
