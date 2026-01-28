code = """import pandas as pd
import re
import json

# Load citation data
with open(locals()['var_function-call-1105675117886834803'], 'r') as f:
    citations_data = json.load(f)
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Load paper documents
with open(locals()['var_function-call-12491728221895612274'], 'r') as f:
    paper_docs = json.load(f)

# Process paper documents to extract title, year, and domain
papers_info = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year = None
    # Try to extract year from various patterns, searching the whole text
    # Pattern 1: explicit 'publication year: YYYY'
    year_match = re.search(r"publication year: (\d{4})", text)
    if year_match:
        year = int(year_match.group(1))
    else:
        # Pattern 2: venue shorthand like 'UbiComp '16' or 'CHI '16'
        venue_year_match = re.search(r"(?:CHI|UbiComp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH) \'(\d{2})", text)
        if venue_year_match:
            short_year = int(venue_year_match.group(1))
            year = 2000 + short_year if short_year < 50 else 1900 + short_year # Assume 21st century for 00-49, 20th for 50-99
        else:
            # Pattern 3: general 4-digit year, searching the entire text
            general_year_match = re.search(r"\b(19|20)\d{2}\b", text)
            if general_year_match:
                year = int(general_year_match.group(0))

    # Check for 'physical activity' (case-insensitive) in the entire text for domain
    is_physical_activity_domain = 'physical activity' in text.lower()

    papers_info.append({'title': title, 'year': year, 'is_physical_activity': is_physical_activity_domain})

papers_df = pd.DataFrame(papers_info)

# Filter papers for 2016 and 'physical activity' domain
filtered_papers_df = papers_df[
    (papers_df['year'] == 2016) & 
    (papers_df['is_physical_activity'])
]

# Merge with citations data
merged_df = pd.merge(filtered_papers_df, citations_df, on='title', how='inner')

# Calculate total citation count for each paper
result = merged_df.groupby('title')['citation_count'].sum().reset_index()
result.rename(columns={'citation_count': 'total_citation_count'}, inplace=True)

print('__RESULT__:')
print(result.to_json(orient='records'))"""

env_args = {'var_function-call-1105675117886834803': 'file_storage/function-call-1105675117886834803.json', 'var_function-call-12491728221895612274': 'file_storage/function-call-12491728221895612274.json', 'var_function-call-14844828871360626708': [], 'var_function-call-11656898717481283878': [], 'var_function-call-278694898533866311': []}

exec(code, env_args)
