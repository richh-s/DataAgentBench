code = """import json
import re

# Load Papers
with open(locals()['var_function-call-10956757805883297717'], 'r') as f:
    papers = json.load(f)

# Load Citations
with open(locals()['var_function-call-5688695509175081780'], 'r') as f:
    citations_list = json.load(f)

# Create Citation Map
citation_map = {}
for c in citations_list:
    t = c['title']
    count = c['total_citations']
    # counts might be strings or ints in the JSON
    if count is not None:
        citation_map[t] = int(count)
    else:
        citation_map[t] = 0

results = []

for p in papers:
    # 1. Title
    fname = p['filename']
    if fname.endswith('.txt'):
        title = fname[:-4]
    else:
        title = fname
    
    text = p['text']
    
    # 2. Year extraction
    # Look for year in first 2000 chars to cover header
    header = text[:2000]
    # Find all 4-digit years starting with 20
    # We want publication year. Usually the venue year.
    # Common venues: CHI, Ubicomp, CSCW, DIS...
    # Strategy: Find "Venue 'YY" or "Venue 20YY"
    # Or just find the first year.
    # Let's try to be smart. If "2015" is found, it's 2015.
    
    years = re.findall(r'\b(20\d\d)\b', header)
    if not years:
        # Try 'YY format? Too risky (e.g. '15).
        # Fallback: Search whole text? No, refs have dates.
        # If no year found in header, assume not in range?
        pub_year = 0
    else:
        # Pick the first one. Usually correct for top-level metadata.
        # But sometimes copyright is 2015 for a 2015 paper.
        pub_year = int(years[0])
        
    # Check if > 2016
    if pub_year <= 2016:
        continue

    # 3. Contribution extraction
    # Check if "empirical" is in the text
    if 'empirical' not in text.lower():
        continue
        
    # 4. Join with citations
    if title in citation_map:
        count = citation_map[title]
        results.append({
            "title": title,
            "total_citations": count
        })

# Sort by citations descending for better presentation, though not required
results.sort(key=lambda x: x['total_citations'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-5688695509175081780': 'file_storage/function-call-5688695509175081780.json', 'var_function-call-5688695509175080773': 'file_storage/function-call-5688695509175080773.json', 'var_function-call-10956757805883297717': 'file_storage/function-call-10956757805883297717.json'}

exec(code, env_args)
