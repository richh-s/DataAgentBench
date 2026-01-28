code = """import pandas as pd
import json
import re

# Load the full result from the JSON file
with open(locals()['var_function-call-1472157430104590186'], 'r') as f:
    paper_docs = json.load(f)

df_papers = pd.DataFrame(paper_docs)

# Function to extract year and contribution
def extract_info(text):
    year = None
    contribution = None

    # Try to find a 4-digit year first (e.g., 2015)
    year_4_digit_match = re.search(r'\b(19|20)\d{2}\b', text)
    if year_4_digit_match:
        year = int(year_4_digit_match.group(0))
    else:
        # Try to find year in 'XX format (e.g., '15) preceded by a venue name
        venue_year_match = re.search(r'([A-Z]{3,}) ''(\d{2})', text)
        if venue_year_match:
            year = int("20" + venue_year_match.group(2))

    # Extract contribution types. Handle cases where it might be a list or single word.
    contribution_types = ["empirical", "artifact", "theoretical", "survey", "methodological"]
    extracted_contributions = []
    for contrib_type in contribution_types:
        if re.search(r'contribution[s]?.*\b{}\b'.format(re.escape(contrib_type)), text, re.IGNORECASE):
            extracted_contributions.append(contrib_type)
    
    if extracted_contributions:
        contribution = extracted_contributions

    return year, contribution

# Apply the extraction function
df_papers[['year', 'contribution']] = df_papers['text'].apply(lambda x: pd.Series(extract_info(x)))

# Filter for 'empirical' contribution and year after 2016
filtered_papers = df_papers[df_papers['contribution'].apply(lambda x: x is not None and 'empirical' in x if isinstance(x, list) else False) & (df_papers['year'] > 2016)]

# Extract title from filename
filtered_papers['title'] = filtered_papers['filename'].str.replace('.txt', '', regex=False)

# Select relevant columns
empirical_papers = filtered_papers[['title']].drop_duplicates()

result = empirical_papers.to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-18442985081393924164': ['paper_docs'], 'var_function-call-1472157430104590186': 'file_storage/function-call-1472157430104590186.json'}

exec(code, env_args)
