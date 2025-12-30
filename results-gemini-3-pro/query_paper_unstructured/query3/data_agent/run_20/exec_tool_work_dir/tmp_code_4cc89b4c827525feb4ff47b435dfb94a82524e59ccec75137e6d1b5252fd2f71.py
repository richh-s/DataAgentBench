code = """import json
import re

# Load citations
with open(locals()['var_function-call-389901141376174398'], 'r') as f:
    citations_data = json.load(f)

# Create a lookup for citations: title -> total_citations
# citations_data is a list of dicts: {"title": ..., "total_citations": ...}
citation_map = {item['title']: int(item['total_citations']) for item in citations_data}

# Load papers
with open(locals()['var_function-call-389901141376172653'], 'r') as f:
    papers_data = json.load(f)

results = []

for paper in papers_data:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Extract title
    if filename.endswith('.txt'):
        title = filename[:-4]
    else:
        title = filename
        
    # Extract year
    # Look for 20xx in first 1000 chars
    # We want published AFTER 2016, so >= 2017
    
    # Simple regex for year 2017-2029
    # This avoids picking up 2015, 2016.
    # But wait, if the paper is 2015, I should finding 2015 and REJECT it.
    # So I should find ANY year 20xx and check if it is > 2016.
    
    match = re.search(r'20\d{2}', text[:1000])
    year = 0
    if match:
        year = int(match.group(0))
    
    # Check if > 2016
    if year > 2016:
        # Check for 'empirical' contribution
        if 'empirical' in text.lower():
            # Get citation count
            count = citation_map.get(title, 0)
            results.append({
                "title": title,
                "total_citations": count
            })

# Sort results by title or something predictable
results.sort(key=lambda x: x['title'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-11261961701334828073': ['paper_docs'], 'var_function-call-11261961701334829364': 'file_storage/function-call-11261961701334829364.json', 'var_function-call-11261961701334830655': ['Citations', 'sqlite_sequence'], 'var_function-call-11261961701334827850': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-8802837961524065341': 'file_storage/function-call-8802837961524065341.json', 'var_function-call-389901141376174398': 'file_storage/function-call-389901141376174398.json', 'var_function-call-389901141376172653': 'file_storage/function-call-389901141376172653.json'}

exec(code, env_args)
