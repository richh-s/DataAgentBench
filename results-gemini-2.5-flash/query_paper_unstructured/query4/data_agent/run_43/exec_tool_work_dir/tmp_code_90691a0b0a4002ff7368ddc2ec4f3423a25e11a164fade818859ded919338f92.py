code = """import json
import re

def extract_info(text, filename):
    title = filename.replace(".txt", "")
    year = None
    domain = []

    # Extract year
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    if year_match:
        year = int(year_match.group(0))
    
    # Extract domain (looking for common domains in the text)
    common_domains = ["food", "physical activity", "sleep", "mental", "finances", "productivity", "screen time", "social interactions", "location", "chronic", "diabetes", "health_behavior"]
    for d in common_domains:
        # Construct the pattern string safely using raw string literals for word boundaries
        pattern = r'\b' + re.escape(d) + r'\b'
        if re.search(pattern, text, re.IGNORECASE):
            domain.append(d)

    return {"title": title, "year": year, "domain": list(set(domain))}

file_path = locals()['var_function-call-12752153450719007890']
with open(file_path, 'r') as f:
    mongo_data = json.load(f)

papers_info = []
for doc in mongo_data:
    papers_info.append(extract_info(doc['text'], doc['filename']))

# Filter papers for year 2016 and "physical activity" domain
filtered_papers = [
    p for p in papers_info 
    if p['year'] == 2016 and "physical activity" in [d.lower() for d in p['domain']]
]

# Prepare titles for SQL query
filtered_titles = [p['title'] for p in filtered_papers]

__RESULT__:
print(json.dumps(filtered_titles))"""

env_args = {'var_function-call-16161537513363771660': 'file_storage/function-call-16161537513363771660.json', 'var_function-call-12752153450719007890': 'file_storage/function-call-12752153450719007890.json'}

exec(code, env_args)
