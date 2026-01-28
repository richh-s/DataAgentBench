code = """import json
import pandas as pd

# Load papers
with open(locals()['var_function-call-799378154932565658'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-799378154932566157'], 'r') as f:
    citations = json.load(f)

# Convert citations to DataFrame for easier summing
df_citations = pd.DataFrame(citations)
df_citations['citation_count'] = df_citations['citation_count'].astype(int)

# Process papers
results = []
for paper in papers:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Check domain
    if 'physical activity' not in text.lower():
        continue
        
    # Check year
    # Look for 2016 in the first 1000 characters
    header = text[:1000]
    if '2016' in header:
        # It's likely 2016
        pass
    else:
        # Maybe check for '16 in conference acronyms if needed, 
        # but 2016 is usually present in copyright or date lines.
        # Let's double check if we missed it.
        # If not 2016, skip.
        continue
        
    # Get total citations
    # Filter citations for this title
    paper_citations = df_citations[df_citations['title'] == title]
    total_citations = paper_citations['citation_count'].sum()
    
    results.append({
        "title": title,
        "citation_count": int(total_citations)
    })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-18105369077024110272': 'file_storage/function-call-18105369077024110272.json', 'var_function-call-18105369077024110379': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-799378154932565658': 'file_storage/function-call-799378154932565658.json', 'var_function-call-799378154932566157': 'file_storage/function-call-799378154932566157.json'}

exec(code, env_args)
