code = """import json
import re
import pandas as pd

def extract_info(text, filename):
    title = filename.replace(".txt", "")
    year = None
    domain = []

    # Try to extract year from copyright statement first
    copyright_year_match = re.search(r'Copyright\s+(?:\(c\)|\u00a9)?\s*(\d{4})', text, re.IGNORECASE)
    if copyright_year_match:
        year = int(copyright_year_match.group(1))
    else:
        # Fallback to general year extraction if copyright year not found
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

# Get titles of filtered papers
filtered_titles = [p['title'] for p in filtered_papers]

# Load citation data
citations_file_path = locals()['var_function-call-16161537513363771660']
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

# Filter citations by the titles of the 2016 "physical activity" papers
df_filtered_citations = df_citations[df_citations['title'].isin(filtered_titles)]

# Calculate total citation count for each paper
total_citations_per_paper = df_filtered_citations.groupby('title')['citation_count'].sum().reset_index()

# Convert to desired output format
result = total_citations_per_paper.to_json(orient='records')

print("__RESULT__:")
print(result)"""

env_args = {'var_function-call-16161537513363771660': 'file_storage/function-call-16161537513363771660.json', 'var_function-call-12752153450719007890': 'file_storage/function-call-12752153450719007890.json', 'var_function-call-866722953621056295': [], 'var_function-call-8171478659109438870': []}

exec(code, env_args)
