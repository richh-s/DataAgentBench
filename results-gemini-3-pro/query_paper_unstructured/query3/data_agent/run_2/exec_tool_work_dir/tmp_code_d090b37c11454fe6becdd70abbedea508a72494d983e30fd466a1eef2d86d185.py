code = """import json
import re
import pandas as pd

# Access the file paths from the local variables
papers_path = locals()['var_function-call-13085037572156381968']
citations_path = locals()['var_function-call-13580482470423784099']

# Load papers
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Load citations
with open(citations_path, 'r') as f:
    citations = json.load(f)

citations_df = pd.DataFrame(citations)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

results = []

for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p['text']
    
    # Extract Year from first 1000 chars
    header = text[:1000]
    years = re.findall(r'\b(20[1-2][0-9])\b', header)
    
    pub_year = None
    if years:
        # Take the first year found as the publication year
        pub_year = int(years[0])
    
    # Check empirical
    is_empirical = "empirical" in text.lower()
    
    # Filter: published after 2016 (year > 2016)
    if pub_year and pub_year > 2016 and is_empirical:
        # Sum citations
        total_citations = citations_df[citations_df['title'] == title]['citation_count'].sum()
        results.append({
            "title": title,
            "total_citation_count": int(total_citations)
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-7886853940146991682': 'file_storage/function-call-7886853940146991682.json', 'var_function-call-14846085348849016055': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-13085037572156381968': 'file_storage/function-call-13085037572156381968.json', 'var_function-call-1254515193280365466': [{'COUNT(*)': '1405'}], 'var_function-call-13580482470423784099': 'file_storage/function-call-13580482470423784099.json'}

exec(code, env_args)
