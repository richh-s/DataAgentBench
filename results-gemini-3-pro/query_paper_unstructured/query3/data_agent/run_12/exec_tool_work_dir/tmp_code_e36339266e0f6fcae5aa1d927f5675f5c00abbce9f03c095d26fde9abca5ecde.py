code = """import json
import re

# Load data
with open(locals()['var_function-call-17632845538165496708'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-2108981104477433395'], 'r') as f:
    citations = json.load(f)

# Helper to extract year
def extract_year(text):
    # Look for year in first 2000 chars
    header = text[:3000]
    # Regex for year 2000-2029
    matches = re.findall(r'20[0-2][0-9]', header)
    if matches:
        # Return the first year found
        # Usually the first year mentioned is the conference year or copyright year
        return int(matches[0])
    # Try 'YY format? e.g. '15. Slightly risky.
    # Let's rely on 4-digit years first.
    return None

# Helper to check empirical
def is_empirical(text):
    return 'empirical' in text.lower()

results = []
processed_titles = set()

for p in papers:
    title = p['filename'].replace('.txt', '')
    if title in processed_titles:
        continue
    processed_titles.add(title)
    
    # Extract info
    year = extract_year(p['text'])
    is_emp = is_empirical(p['text'])
    
    # Filter
    # Published AFTER 2016 => year > 2016
    if year and year > 2016 and is_emp:
        # Find citations
        total_citations = 0
        found_citation_record = False
        for c in citations:
            if c['title'] == title:
                total_citations += int(c['citation_count'])
                found_citation_record = True
        
        # Only include if we have citation info?
        # The query asks for "title and total citation count". 
        # If no citations found, count is 0.
        results.append({
            "title": title,
            "citation_count": total_citations,
            "year": year # Debug info
        })

# Sort by title or something consistent
results.sort(key=lambda x: x['title'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-1840327009665407502': ['paper_docs'], 'var_function-call-12708107300142329': 'file_storage/function-call-12708107300142329.json', 'var_function-call-5269555748610322771': 'file_storage/function-call-5269555748610322771.json', 'var_function-call-17632845538165496708': 'file_storage/function-call-17632845538165496708.json', 'var_function-call-2108981104477433395': 'file_storage/function-call-2108981104477433395.json'}

exec(code, env_args)
