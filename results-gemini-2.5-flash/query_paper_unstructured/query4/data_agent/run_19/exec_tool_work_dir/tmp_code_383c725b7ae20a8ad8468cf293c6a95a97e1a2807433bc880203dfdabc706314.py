code = """import json
import re
import pandas as pd

def extract_paper_info_all_years_improved(doc):
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')
    
    # Find all 4-digit numbers (potential years)
    all_four_digit_numbers = [int(y) for y in re.findall(r'\b\d{4}\b', text)]
    
    # Filter for plausible publication years (e.g., between 1900 and 2024)
    plausible_years = [y for y in all_four_digit_numbers if 1900 <= y <= 2024]
            
    is_physical_activity_domain = 'physical activity' in text.lower()
    
    return {'title': title, 'plausible_years': plausible_years, 'is_physical_activity': is_physical_activity_domain}

with open(locals()['var_function-call-1819138674056248880'], 'r') as f:
    paper_docs_full = json.load(f)

extracted_papers_with_all_years_improved = []
for doc in paper_docs_full:
    extracted_papers_with_all_years_improved.append(extract_paper_info_all_years_improved(doc))

# Filter for papers where 2016 is among the plausible years AND in 'physical activity' domain
filtered_papers_for_query = [
    p for p in extracted_papers_with_all_years_improved 
    if 2016 in p['plausible_years'] and p['is_physical_activity']
]

paper_titles_2016_physical_activity = [p['title'] for p in filtered_papers_for_query]

# If no papers found with the above criteria, return an empty list or appropriate message
if not paper_titles_2016_physical_activity:
    print('__RESULT__:')
    print(json.dumps([]))
else:
    with open(locals()['var_function-call-880522876073640375'], 'r') as f:
        all_citations = json.load(f)

    df_all_citations = pd.DataFrame(all_citations)

    df_all_citations['citation_count'] = pd.to_numeric(df_all_citations['citation_count'], errors='coerce')

    df_filtered_citations = df_all_citations[
        (df_all_citations['title'].isin(paper_titles_2016_physical_activity))
    ]

    total_citations_for_filtered_papers = df_filtered_citations.groupby('title')['citation_count'].sum().reset_index()

    result_list = total_citations_for_filtered_papers.to_dict(orient='records')

    print('__RESULT__:')
    print(json.dumps(result_list))"""

env_args = {'var_function-call-14428271549656226849': ['paper_docs'], 'var_function-call-1819138674056248880': 'file_storage/function-call-1819138674056248880.json', 'var_function-call-15955492775391050376': [], 'var_function-call-8361182827540506550': ['Citations', 'sqlite_sequence'], 'var_function-call-1642100287304137362': [{'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'citation_count': '12'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity', 'citation_count': '65'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'citation_count': '36'}, {'title': 'SweatAtoms: Materializing Physical Activity', 'citation_count': '61'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity', 'citation_count': '39'}, {'title': 'Low Sampling Rate for Physical Activity Recognition', 'citation_count': '88'}], 'var_function-call-880522876073640375': 'file_storage/function-call-880522876073640375.json', 'var_function-call-5881033254162741036': [{'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'citation_count': 36}, {'title': 'Low Sampling Rate for Physical Activity Recognition', 'citation_count': 88}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'citation_count': 12}, {'title': 'SweatAtoms: Materializing Physical Activity', 'citation_count': 61}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity', 'citation_count': 65}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity', 'citation_count': 39}], 'var_function-call-13717564857377406101': [], 'var_function-call-14109133086239619179': []}

exec(code, env_args)
