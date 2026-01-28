code = """import json
import re
import pandas as pd

def extract_paper_info(paper_text, filename):
    title = filename.replace(".txt", "")
    year = None
    is_empirical = False

    # Extract year: look for 4-digit numbers starting with 19 or 20 in the first 500 characters
    year_match = re.search(r'\b(19|20)\d{2}\b', paper_text[:500])
    if year_match:
        year = int(year_match.group(0))

    # Check if 'empirical' is in the text (case-insensitive)
    if 'empirical' in paper_text.lower():
        is_empirical = True

    return {'title': title, 'year': year, 'is_empirical': is_empirical}

file_path = locals()['var_function-call-17384357217489800854']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

all_papers_extracted_info = []
for doc in paper_docs:
    info = extract_paper_info(doc['text'], doc['filename'])
    all_papers_extracted_info.append(info)

# Filter papers based on year and empirical contribution
filtered_papers = []
for paper in all_papers_extracted_info:
    if paper['year'] is not None and paper['year'] > 2016 and paper['is_empirical']:
        filtered_papers.append(paper)

# Convert to DataFrame for easier merging
filtered_papers_df = pd.DataFrame(filtered_papers)

# Load citation data
citation_file_path = locals()['var_function-call-505378774442661286']
with open(citation_file_path, 'r') as f:
    citation_data = json.load(f)

citations_df = pd.DataFrame(citation_data)
citations_df['total_citation_count'] = citations_df['total_citation_count'].astype(int)

# Merge the two dataframes if filtered_papers_df is not empty
if not filtered_papers_df.empty:
    merged_df = pd.merge(filtered_papers_df, citations_df, on='title', how='inner')
    result = merged_df[['title', 'total_citation_count']].to_json(orient='records')
else:
    result = json.dumps([]) # Return empty list if no papers match criteria

print("__RESULT__:")
print(result)"""

env_args = {'var_function-call-8876707072609632946': ['Citations', 'sqlite_sequence'], 'var_function-call-9424252978014940020': ['paper_docs'], 'var_function-call-17384357217489800854': 'file_storage/function-call-17384357217489800854.json', 'var_function-call-13031117097295312790': [], 'var_function-call-505378774442661286': 'file_storage/function-call-505378774442661286.json', 'var_function-call-1634136829314383703': {'filtered_papers_df_columns': [], 'citations_df_columns': ['title', 'total_citation_count']}, 'var_function-call-2768330533041466436': {'extracted_info_sample': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'is_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'is_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'is_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'is_empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'is_empirical': False}], 'unique_years': [], 'empirical_papers_count': 2, 'papers_after_2016_count': 0, 'filtered_papers_count': 0, 'final_result': []}}

exec(code, env_args)
