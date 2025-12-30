code = """import json
import re
import pandas as pd

# Load papers
# The second call likely returned all papers (as the query probably fell back to find_all)
# But let's check the length.
with open(locals()['var_function-call-603899956623293996'], 'r') as f:
    papers_data = json.load(f)

print(f"Loaded {len(papers_data)} papers.")

# Load citations
with open(locals()['var_function-call-1625983961919980937'], 'r') as f:
    citations_data = json.load(f)

citations_df = pd.DataFrame(citations_data)
# Ensure citation_count is int
if 'total_citations' in citations_df.columns:
    # The previous query was SELECT title, SUM(citation_count) as total_citations ...
    # So we already have the totals per title.
    pass
else:
    # If the previous query failed or structure is different, handle it.
    # But the preview showed: [{"title": "...", "total_citations": "53"}, ...]
    pass

# Helper to extract year
def extract_year(text):
    # Look for year in the first 1000 chars
    header = text[:1000]
    matches = re.findall(r'\b(20\d{2})\b', header)
    if matches:
        # Return the most likely publication year. 
        # Usually headers have the year. We can take the first one or the most common.
        # Let's take the first one that is >= 2000.
        for y in matches:
            if 2000 <= int(y) <= 2025:
                return int(y)
    return None

# Helper to check empirical
def is_empirical(text):
    # Simple check for now
    return "empirical" in text.lower()

results = []
for p in papers_data:
    title = p.get('filename', '').replace('.txt', '')
    text = p.get('text', '')
    
    year = extract_year(text)
    empirical = is_empirical(text)
    
    # We need papers published > 2016
    if year and year > 2016 and empirical:
        # Find citation count
        cit_row = citations_df[citations_df['title'] == title]
        if not cit_row.empty:
            count = cit_row.iloc[0]['total_citations']
        else:
            count = 0
        results.append({"title": title, "total_citation_count": count})

# Output results
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-1625983961919980332': 'file_storage/function-call-1625983961919980332.json', 'var_function-call-1625983961919980937': 'file_storage/function-call-1625983961919980937.json', 'var_function-call-603899956623293996': 'file_storage/function-call-603899956623293996.json'}

exec(code, env_args)
