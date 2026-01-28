code = """import json
import re
import pandas as pd

# Load citations
with open(locals()['var_function-call-15161005825129355678'], 'r') as f:
    citations_data = json.load(f)

# Create DataFrame for citations
df_citations = pd.DataFrame(citations_data)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])
# Group by title and sum citation_count
citation_sums = df_citations.groupby('title')['citation_count'].sum().reset_index()

# Load papers
with open(locals()['var_function-call-14023155913287027792'], 'r') as f:
    papers_data = json.load(f)

extracted_papers = []

for doc in papers_data:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']
    
    # Extract Year
    year = None
    # Strategy 1: Look for "Copyright 20xx" or "© 20xx"
    copy_match = re.search(r'Copyright\s.*?(\d{4})', text[:5000], re.IGNORECASE)
    if copy_match:
        year = int(copy_match.group(1))
    
    # Strategy 2: Look for conference year in header (e.g. CHI '18, UbiComp '19)
    if not year:
        header_match = re.search(r"[A-Z]+\s+'(\d{2})", text[:500])
        if header_match:
            y_short = int(header_match.group(1))
            year = 2000 + y_short # Assume 20xx
            
    # Strategy 3: Look for any 20xx in the first 500 chars
    if not year:
        year_match = re.search(r'\b(20\d\d)\b', text[:500])
        if year_match:
            year = int(year_match.group(1))
            
    # Extract Contribution
    # Check for "empirical" keyword
    contribution_empirical = False
    if "empirical" in text.lower():
        contribution_empirical = True
    
    # Also check if there is a "Contribution" section or keyword list?
    # Based on the sample, there isn't a clear metadata block.
    # But let's stick to the "empirical" keyword presence or maybe "user study", "participants"?
    # The prompt specifically lists "empirical" as a type.
    # I'll rely on the word "empirical" being present.
    # To be safer, I'll also look for "study" AND "participants" as a proxy for empirical work if "empirical" is missing?
    # But usually, academic papers claiming an empirical contribution use the word "empirical".
    
    extracted_papers.append({
        "title": title,
        "year": year,
        "is_empirical": contribution_empirical
    })

# Filter papers
# Published after 2016 -> year > 2016
filtered_papers = [
    p for p in extracted_papers 
    if p['year'] and p['year'] > 2016 and p['is_empirical']
]

# Create DataFrame for filtered papers
df_papers = pd.DataFrame(filtered_papers)

# Merge with citations
if not df_papers.empty:
    result_df = pd.merge(df_papers, citation_sums, on='title', how='inner')
    final_result = result_df[['title', 'citation_count']].to_dict(orient='records')
else:
    final_result = []

print("__RESULT__:")
print(json.dumps(final_result))"""

env_args = {'var_function-call-15870197178321181346': 'file_storage/function-call-15870197178321181346.json', 'var_function-call-15870197178321180761': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-5877010014911458978': 'file_storage/function-call-5877010014911458978.json', 'var_function-call-15161005825129355678': 'file_storage/function-call-15161005825129355678.json', 'var_function-call-14023155913287027792': 'file_storage/function-call-14023155913287027792.json'}

exec(code, env_args)
