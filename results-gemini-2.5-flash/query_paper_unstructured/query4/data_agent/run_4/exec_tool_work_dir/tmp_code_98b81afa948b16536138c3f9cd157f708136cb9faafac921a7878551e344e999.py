code = """import json
import re
import pandas as pd

# Load the full paper_docs data
with open(locals()['var_function-call-11852784549828080247'], 'r') as f:
    paper_docs = json.load(f)

all_extracted_papers = []
for doc in paper_docs:
    filename = doc['filename']
    title = filename.replace('.txt', '')
    text = doc['text']

    year = None
    # Attempt to find the year using a more robust regex that looks for typical publication year patterns
    # This regex tries to capture years in various common positions within academic papers
    year_match = re.search(r'\b(19|20)\d{2}\b', text)
    if year_match:
        year = int(year_match.group(0))
    else:
        # As a fallback, try to find the earliest 4-digit number that could be a year, assuming it's the publication year
        all_four_digit_numbers = re.findall(r'\b\d{4}\b', text)
        for num_str in all_four_digit_numbers:
            num = int(num_str)
            if 1900 <= num <= 2024:  # Reasonable range for publication years
                year = num
                break # Take the first plausible year found

    # Check if 'physical activity' is present in the text (case-insensitive) to determine the domain
    is_physical_activity_domain = 'physical activity' in text.lower()

    all_extracted_papers.append({'title': title, 'year': year, 'is_physical_activity': is_physical_activity_domain})


pd_all_extracted_papers = pd.DataFrame(all_extracted_papers)

# Filter for papers published in 2016 and in the 'physical activity' domain
filtered_papers_2016_pa = pd_all_extracted_papers[(pd_all_extracted_papers['year'] == 2016) & (pd_all_extracted_papers['is_physical_activity'] == True)]

# Load citations data
citations = pd.read_json(locals()['var_function-call-9934081816412356413'])
citations['citation_count'] = citations['citation_count'].astype(int)

final_result = []
# Only proceed with merging if there are filtered papers
if not filtered_papers_2016_pa.empty:
    merged_df = pd.merge(filtered_papers_2016_pa, citations, on='title', how='inner')
    
    # Only proceed with grouping if the merged DataFrame is not empty
    if not merged_df.empty:
        grouped_citations = merged_df.groupby('title')['citation_count'].sum().reset_index()
        final_result = grouped_citations.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(final_result))"""

env_args = {'var_function-call-8240804717267947776': ['paper_docs'], 'var_function-call-11852784549828080247': 'file_storage/function-call-11852784549828080247.json', 'var_function-call-3880476428057308976': [], 'var_function-call-375944317011682617': ['Citations', 'sqlite_sequence'], 'var_function-call-9934081816412356413': 'file_storage/function-call-9934081816412356413.json', 'var_function-call-15309218527712248463': []}

exec(code, env_args)
