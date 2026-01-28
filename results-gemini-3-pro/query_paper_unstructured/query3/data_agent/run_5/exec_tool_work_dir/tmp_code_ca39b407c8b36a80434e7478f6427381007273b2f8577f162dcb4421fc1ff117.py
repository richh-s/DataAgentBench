code = """import json
import re
import pandas as pd

# Load data
with open(locals()['var_function-call-12792815428648479832'], 'r') as f:
    paper_docs = json.load(f)

with open(locals()['var_function-call-15343514597715386657'], 'r') as f:
    citations_data = json.load(f)

# Convert citations to DataFrame
df_citations = pd.DataFrame(citations_data)
# Ensure citation_count is int
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

# Process papers
target_papers = []

for doc in paper_docs:
    text = doc['text']
    filename = doc['filename']
    title = filename.replace('.txt', '')
    
    # Extract Year
    # Look for 2017, 2018, 2019, 2020, 2021, 2022...
    # Typically in header or copyright
    # Search in first 2000 chars
    header_text = text[:2000]
    years = re.findall(r'\b(20\d{2})\b', header_text)
    
    pub_year = None
    if years:
        # Filter valid years, e.g., 2000-2030
        valid_years = [int(y) for y in years if 2000 <= int(y) <= 2030]
        if valid_years:
            pub_year = valid_years[0] # Take the first found year
    
    # Extract Contribution
    # Check for 'empirical' in text (case insensitive)
    # Also check if there is a specific "Contribution" field if "empirical" is not just a random word
    # Given the hint "values may be part of a list", I'll look for "Contribution" near "empirical" or just "empirical" in keywords?
    # Let's try simple contains "empirical" first.
    is_empirical = "empirical" in text.lower()
    
    # Refined check: maybe "Contribution: ... empirical ..."
    # But if "empirical" is just in the text, does it count?
    # The prompt says "contribution: Type of contribution".
    # Many HCI papers list contributions in the intro: "Our empirical contribution..."
    # If I just check "empirical" in text, I might get false positives.
    # But without structure, it's the best proxy.
    
    if pub_year and pub_year > 2016 and is_empirical:
        target_papers.append({
            'title': title,
            'year': pub_year,
            'contribution': 'empirical'
        })

# Get citations for target papers
target_titles = [p['title'] for p in target_papers]

# Filter citations
matched_citations = df_citations[df_citations['title'].isin(target_titles)]

# Group by title and sum
result_df = matched_citations.groupby('title')['citation_count'].sum().reset_index()

# Convert to list of dicts
final_result = result_df.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(final_result))"""

env_args = {'var_function-call-9689432006532158130': 'file_storage/function-call-9689432006532158130.json', 'var_function-call-7106794807816664619': 'file_storage/function-call-7106794807816664619.json', 'var_function-call-12792815428648479832': 'file_storage/function-call-12792815428648479832.json', 'var_function-call-15343514597715386657': 'file_storage/function-call-15343514597715386657.json'}

exec(code, env_args)
