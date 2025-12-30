code = """import json
import re

# Load citations
citations_path = locals()['var_function-call-4507795440507618758']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

citation_map = {}
for row in citations_data:
    t = row['title']
    c = row['total_citations']
    if c is not None:
        citation_map[t] = int(float(c))
    else:
        citation_map[t] = 0

# Load papers
papers_path = locals()['var_function-call-10894468654798374866']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

results = []

for paper in papers_data:
    filename = paper.get('filename', '')
    if not filename.endswith('.txt'):
        continue
    title = filename[:-4]
    text = paper.get('text', '')
    
    # Extract Year
    # We look for 2010-2029 in the first 2000 characters
    header_text = text[:2000]
    years = re.findall(r"20[12]\d", header_text)
    
    pub_year = None
    if years:
        # Convert to ints
        year_ints = [int(y) for y in years]
        # Filter reasonable years for this dataset (e.g. 2000-2025)
        valid_years = [y for y in year_ints if 2000 <= y <= 2025]
        if valid_years:
            # First valid year found is likely the publication year in header
            pub_year = valid_years[0]
            
            # Sanity check: if multiple years, picking the first is usually correct for header
            # But sometimes Copyright 2018 is after CHI 2018. same year.
            
    # Extract Contribution
    # Check for "empirical"
    # To be safer, check first 5000 chars (body) to avoid references
    # But usually "empirical" is mentioned in Abstract or Intro.
    is_empirical = "empirical" in text[:10000].lower()
    
    if pub_year and pub_year > 2016 and is_empirical:
        count = citation_map.get(title, 0)
        results.append({"title": title, "citation_count": count})

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5623558947517056704': 'file_storage/function-call-5623558947517056704.json', 'var_function-call-4507795440507618758': 'file_storage/function-call-4507795440507618758.json', 'var_function-call-10894468654798374866': 'file_storage/function-call-10894468654798374866.json'}

exec(code, env_args)
