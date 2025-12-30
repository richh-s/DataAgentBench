code = """import json
import re

# Get file paths from storage variables
citations_file_path = locals()['var_function-call-6168559912964544783']
papers_file_path = locals()['var_function-call-7962722088325461616']

# Load citations
with open(citations_file_path, 'r') as f:
    citations_data = json.load(f)

# Create a dictionary for quick lookup
citations_map = {item['title']: item['total_citations'] for item in citations_data}

# Load papers
with open(papers_file_path, 'r') as f:
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
    # Look for years in the first 2000 characters
    header_text = text[:2000]
    
    is_target_year = False
    
    # Check for specific Copyright/Conference patterns first
    if re.search(r'(?:Copyright|©|Proceedings|Conference|Year|CHI|UbiComp|CSCW|DIS)\D{0,30}(20(?:1[7-9]|2[0-5]))', header_text, re.IGNORECASE):
        is_target_year = True
    else:
        # Fallback: check if any target year is in the first 500 chars
        early_text = text[:500]
        if any(y in early_text for y in target_years):
            is_target_year = True
            
    if is_target_year:
        # Check if year is strictly > 2016. The logic above looks for 2017-2025.
        # But we must ensure it's not picking up a year < 2017.
        # The regex (20(?:1[7-9]|2[0-5])) matches 2017-2029.
        # Wait, 2017, 2018, 2019. 2020-2025.
        # 1[7-9] matches 17, 18, 19.
        # 2[0-5] matches 20, 21, 22, 23, 24, 25.
        # So this regex strictly matches 2017-2025.
        
        citation_count = citations_map.get(title, 0)
        results.append({
            "title": title,
            "total_citations": citation_count
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-6384673105004028122': 'file_storage/function-call-6384673105004028122.json', 'var_function-call-11545422835381902119': 'file_storage/function-call-11545422835381902119.json', 'var_function-call-6168559912964544783': 'file_storage/function-call-6168559912964544783.json', 'var_function-call-7962722088325461616': 'file_storage/function-call-7962722088325461616.json'}

exec(code, env_args)
