code = """import json
import re
import pandas as pd

def extract_paper_info_final_attempt(doc):
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')
    
    year = None
    # Search for all 4-digit numbers in the first 1000 characters
    search_text_for_year = text[:1000]
    # Regex to find 4-digit numbers that could be years (19xx or 20xx)
    potential_years = re.findall(r'\b(19\d{2}|20\d{2})\b', search_text_for_year)
    
    if potential_years:
        # Convert to integers and sort, then take the first one (most likely publication year)
        sorted_years = sorted([int(y) for y in potential_years])
        year = sorted_years[0]

    # Check if 'physical activity' is present in the entire text (case-insensitive) for domain identification
    is_physical_activity_domain = 'physical activity' in text.lower()
    
    return {'title': title, 'year': year, 'is_physical_activity': is_physical_activity_domain}

with open(locals()['var_function-call-1819138674056248880'], 'r') as f:
    paper_docs_full = json.load(f)

extracted_papers_final_attempt = []
for doc in paper_docs_full:
    extracted_papers_final_attempt.append(extract_paper_info_final_attempt(doc))

# Filter for papers published in 2016 and in 'physical activity' domain
filtered_papers_for_query = [
    p for p in extracted_papers_final_attempt 
    if p['year'] == 2016 and p['is_physical_activity']
]

# Get the titles of these papers
paper_titles_2016_physical_activity = [p['title'] for p in filtered_papers_for_query]

# Load all citations from the file
with open(locals()['var_function-call-880522876073640375'], 'r') as f:
    all_citations = json.load(f)

df_all_citations = pd.DataFrame(all_citations)

# Ensure 'citation_count' is numeric, coercing errors to NaN
df_all_citations['citation_count'] = pd.to_numeric(df_all_citations['citation_count'], errors='coerce')

# Filter citations for the relevant paper titles
df_filtered_citations = df_all_citations[
    df_all_citations['title'].isin(paper_titles_2016_physical_activity)
]

# Group by title and sum citation counts
total_citations_for_filtered_papers = df_filtered_citations.groupby('title')['citation_count'].sum().reset_index()

# Convert to a list of dictionaries
result_list = total_citations_for_filtered_papers.to_dict(orient='records')

print('__RESULT__:')
print(json.dumps(result_list))"""

env_args = {'var_function-call-14428271549656226849': ['paper_docs'], 'var_function-call-1819138674056248880': 'file_storage/function-call-1819138674056248880.json', 'var_function-call-15955492775391050376': [], 'var_function-call-8361182827540506550': ['Citations', 'sqlite_sequence'], 'var_function-call-1642100287304137362': [{'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'citation_count': '12'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity', 'citation_count': '65'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'citation_count': '36'}, {'title': 'SweatAtoms: Materializing Physical Activity', 'citation_count': '61'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity', 'citation_count': '39'}, {'title': 'Low Sampling Rate for Physical Activity Recognition', 'citation_count': '88'}], 'var_function-call-880522876073640375': 'file_storage/function-call-880522876073640375.json', 'var_function-call-5881033254162741036': [{'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'citation_count': 36}, {'title': 'Low Sampling Rate for Physical Activity Recognition', 'citation_count': 88}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'citation_count': 12}, {'title': 'SweatAtoms: Materializing Physical Activity', 'citation_count': 61}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity', 'citation_count': 65}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity', 'citation_count': 39}], 'var_function-call-13717564857377406101': [], 'var_function-call-14109133086239619179': [], 'var_function-call-8443211732484623878': [], 'var_function-call-9079714996325125576': [], 'var_function-call-11313103349534325145': []}

exec(code, env_args)
