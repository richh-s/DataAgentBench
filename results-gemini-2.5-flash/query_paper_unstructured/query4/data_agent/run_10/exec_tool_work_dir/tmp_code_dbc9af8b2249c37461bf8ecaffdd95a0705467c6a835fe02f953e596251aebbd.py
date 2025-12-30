code = """import pandas as pd
import re
import json

papers_data = json.loads(open(locals()['var_function-call-14890926156089513429'], 'r').read())

extracted_papers = []
for paper in papers_data:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')

    # More robust year extraction
    year = None
    year_match_strict = re.search(r'year:\s*(\d{4})', text, re.IGNORECASE)
    if year_match_strict:
        year = int(year_match_strict.group(1))
    else:
        # Try to find a four-digit number that could be a year, often in the first 500 characters
        # This is a heuristic and might pick up false positives, but aims for better coverage
        potential_years = re.findall(r'\b(19|20)\d{2}\b', text[:1000], re.IGNORECASE)
        for p_year in potential_years:
            if int(p_year) >= 1900 and int(p_year) <= 2025: # Reasonable range for publication years
                year = int(p_year)
                break

    # More robust domain extraction
    domain = None
    domain_match_strict = re.search(r'domain:\s*(.*)', text, re.IGNORECASE)
    if domain_match_strict:
        domain = domain_match_strict.group(1).strip()
    else:
        # Look for 'domain' or 'topics' keywords followed by potential list of domains
        domain_keywords = re.search(r'(domain|topics):\s*([a-zA-Z0-9, ]+)', text, re.IGNORECASE)
        if domain_keywords:
            domain = domain_keywords.group(2).strip()
        elif 'physical activity' in text.lower(): # Check for direct mention if no structured field
            domain = 'physical activity'

    extracted_papers.append({
        'title': title,
        'year': year,
        'domain': domain
    })

df_papers = pd.DataFrame(extracted_papers)

df_filtered_papers = df_papers[
    (df_papers['year'] == 2016) &
    (df_papers['domain'].str.contains('physical activity', case=False, na=False))
]

citations_data = json.loads(open(locals()['var_function-call-16257161724348090214'], 'r').read())
df_citations = pd.DataFrame(citations_data)

# Ensure 'citation_count' is numeric
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'], errors='coerce')

# Group by title and sum citation counts
df_total_citations = df_citations.groupby('title')['citation_count'].sum().reset_index()
df_total_citations.rename(columns={'citation_count': 'total_citation_count'}, inplace=True)

# Merge filtered papers with total citation counts
result = pd.merge(df_filtered_papers, df_total_citations, on='title', how='inner')

# Select and reorder columns for the final output
final_result = result[['title', 'total_citation_count']]

print('__RESULT__:')
print(final_result.to_json(orient='records'))"""

env_args = {'var_function-call-12243833719420803506': ['paper_docs'], 'var_function-call-12656719124189789220': [], 'var_function-call-14890926156089513429': 'file_storage/function-call-14890926156089513429.json', 'var_function-call-18429680994506560701': [], 'var_function-call-6495032645474842279': ['Citations', 'sqlite_sequence'], 'var_function-call-16257161724348090214': 'file_storage/function-call-16257161724348090214.json'}

exec(code, env_args)
