code = """import json
import re
import pandas as pd

def extract_info(text, filename):
    title = filename.replace(".txt", "")
    year = None
    domain = []

    # Extract year - looking for a 4-digit number that starts with 19 or 20
    # It's better to look for common year patterns or specific venue/source info for publication year.
    # For now, let's keep the broad year search.
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

# Load MongoDB data
mongo_file_path = locals()['var_function-call-12752153450719007890']
with open(mongo_file_path, 'r') as f:
    mongo_data = json.load(f)

papers_info = []
for doc in mongo_data:
    papers_info.append(extract_info(doc['text'], doc['filename']))

# Filter papers for year 2016 and "physical activity" domain
filtered_papers = [
    p for p in papers_info 
    if p['year'] == 2016 and "physical activity" in [d.lower() for d in p['domain']]
]

# Print filtered papers to debug
print("__RESULT__:")
print(json.dumps(filtered_papers))"""

env_args = {'var_function-call-16161537513363771660': 'file_storage/function-call-16161537513363771660.json', 'var_function-call-12752153450719007890': 'file_storage/function-call-12752153450719007890.json', 'var_function-call-866722953621056295': []}

exec(code, env_args)
