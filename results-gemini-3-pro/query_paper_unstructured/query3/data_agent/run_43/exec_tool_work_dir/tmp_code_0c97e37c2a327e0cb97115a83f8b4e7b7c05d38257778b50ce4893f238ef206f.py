code = """import json
import re

# Load citations
with open('var_function-call-6168559912964544783.json', 'r') as f:
    citations_data = json.load(f)

# Create a dictionary for quick lookup
citations_map = {item['title']: item['total_citations'] for item in citations_data}

# Load papers
with open('var_function-call-7962722088325461616.json', 'r') as f:
    papers_data = json.load(f)

results = []

target_years = [str(y) for y in range(2017, 2026)]

for paper in papers_data:
    title = paper.get('filename', '').replace('.txt', '')
    text = paper.get('text', '')
    
    # Check for empirical contribution
    if 'empirical' not in text.lower():
        continue

    # Check for year > 2016
    # Look for years in the first 2000 characters to avoid references
    header_text = text[:2000]
    
    # Find all 4-digit years starting with 20
    years_found = re.findall(r'\b(20\d{2})\b', header_text)
    
    # Filter years to reasonable range (e.g. 2000-2025) to avoid noise
    valid_years = [y for y in years_found if 2000 <= int(y) <= 2025]
    
    if not valid_years:
        continue
    
    # Heuristic: The publication year is likely the one that appears in copyright or conference line
    # Often it is the *max* year found in the header (since previous work citations are older), 
    # OR it is the one associated with "Copyright" or "Proceedings"
    # But sometimes the header has "2017 12th International Conference..."
    
    # Let's take the set of years found. If any year > 2016 is present, we need to be careful not to pick up a reference.
    # But references usually appear later or as (Author, 2015).
    # In the header, the publication year is usually prominent.
    
    # Let's check if the document contains any of the target years in the header.
    # If it contains 2015 and 2017, which one is it?
    # Usually the publication year is the latest year in the header.
    # Example: "Ubicomp '15 ... 2015".
    # If a paper is published in 2017, it might cite 2015 work in the abstract.
    # But "Copyright 2017" is strong.
    
    is_target_year = False
    
    # Check for specific Copyright/Conference patterns first
    if re.search(r'(?:Copyright|©|Proceedings|Conference|Year)\D{0,20}(20(?:1[7-9]|2[0-5]))', header_text, re.IGNORECASE):
        is_target_year = True
    else:
        # Fallback: check if the most frequent year in header is > 2016? 
        # Or just if the set of years found intersects with target years?
        # Let's assume if a target year is found in the first 500 chars, it's the year.
        # This covers "CHI 2017", "2017", etc. at the top.
        early_text = text[:500]
        if any(y in early_text for y in target_years):
            is_target_year = True
            
    if is_target_year:
        citation_count = citations_map.get(title, 0)
        results.append({
            "title": title,
            "total_citations": citation_count
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-6384673105004028122': 'file_storage/function-call-6384673105004028122.json', 'var_function-call-11545422835381902119': 'file_storage/function-call-11545422835381902119.json', 'var_function-call-6168559912964544783': 'file_storage/function-call-6168559912964544783.json', 'var_function-call-7962722088325461616': 'file_storage/function-call-7962722088325461616.json'}

exec(code, env_args)
