code = """import pandas as pd
import json
import re

# Load the full result from the JSON file
with open(locals()['var_function-call-1472157430104590186'], 'r') as f:
    paper_docs = json.load(f)

df_papers = pd.DataFrame(paper_docs)

# Function to extract year and contribution
def extract_info(text):
    year_match = re.search(r'([A-Z]{3,}\s'\d{2}|\d{4})', text)
    year = None
    if year_match:
        year_str = year_match.group(1)
        if len(year_str) == 4 and year_str.isdigit():
            year = int(year_str)
        elif len(year_str) == 7 and year_str.endswith("'\d{2}"): #e.g., CHI '15
            year = int("20" + year_str[-2:])

    contribution_match = re.search(r'contribution: (\w+)', text, re.IGNORECASE)
    contribution = contribution_match.group(1) if contribution_match else None

    # Refine contribution extraction
    contribution_types = ["empirical", "artifact", "theoretical", "survey", "methodological"]
    extracted_contributions = []
    for contrib_type in contribution_types:
        if re.search(r'contribution.*\b{}\b'.format(re.escape(contrib_type)), text, re.IGNORECASE):
            extracted_contributions.append(contrib_type)
    
    # If no specific contribution is found, try to find a year from copyright or venue
    if year is None:
        copyright_year_match = re.search(r'Copyright (\d{4})', text)
        if copyright_year_match:
            year = int(copyright_year_match.group(1))
        else:
            venue_year_match = re.search(r'[A-Z]{3,}\s'(\d{2})', text)
            if venue_year_match:
                year = int("20" + venue_year_match.group(1))

    return year, extracted_contributions if extracted_contributions else None

# Apply the extraction function
df_papers[['year', 'contribution']] = df_papers['text'].apply(lambda x: pd.Series(extract_info(x)))

# Filter for 'empirical' contribution and year after 2016
filtered_papers = df_papers[df_papers['contribution'].apply(lambda x: x is not None and 'empirical' in x if isinstance(x, list) else False) & (df_papers['year'] > 2016)]

# Extract title from filename
filtered_papers['title'] = filtered_papers['filename'].str.replace('.txt', '', regex=False)

# Select relevant columns
result = filtered_papers[['title', 'year', 'contribution']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-18442985081393924164': ['paper_docs'], 'var_function-call-1472157430104590186': 'file_storage/function-call-1472157430104590186.json'}

exec(code, env_args)
