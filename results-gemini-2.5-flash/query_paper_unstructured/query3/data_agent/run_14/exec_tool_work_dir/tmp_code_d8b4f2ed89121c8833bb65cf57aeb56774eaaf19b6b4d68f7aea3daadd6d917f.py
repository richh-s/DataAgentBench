code = """import pandas as pd
import json
import re

# Load paper documents data
file_path_paper_docs = locals()['var_function-call-12608294071483797543']
with open(file_path_paper_docs, 'r') as f:
    paper_docs = json.load(f)

parsed_papers_data = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')

    year = None
    # Try to find a year in the first 2000 characters (where publication info often appears)
    year_match = re.search(r'\b(19|20)\d{2}\b', text[:2000])
    if year_match:
        year = int(year_match.group(0))

    contribution = None
    # Check for 'empirical' (case-insensitive) anywhere in the text
    if re.search(r'\bempirical\b', text, re.IGNORECASE):
        contribution = 'empirical'

    parsed_papers_data.append({'title': title, 'year': year, 'contribution': contribution})

df_papers = pd.DataFrame(parsed_papers_data)

# Filter for papers published after 2016 with 'empirical' contribution
filtered_papers = df_papers[
    (df_papers['year'].notna()) & 
    (df_papers['year'] > 2016) & 
    (df_papers['contribution'] == 'empirical')
]

empirical_titles_df = filtered_papers[['title']].copy()

# Load citation data
file_path_citations = locals()['var_function-call-15414146859521326470']
with open(file_path_citations, 'r') as f:
    citation_data = json.load(f)

df_citations = pd.DataFrame(citation_data)

# Ensure 'total_citation_count' is numeric
df_citations['total_citation_count'] = pd.to_numeric(df_citations['total_citation_count'])

# Merge the two dataframes on 'title'
merged_df = pd.merge(empirical_titles_df, df_citations, on='title', how='inner')

# Select the required columns and format the output
result = merged_df[['title', 'total_citation_count']].to_json(orient='records')

print('__RESULT__:')
print(result)"""

env_args = {'var_function-call-3207410245806214601': ['paper_docs'], 'var_function-call-89421489897449482': 'file_storage/function-call-89421489897449482.json', 'var_function-call-2589591416908310925': [], 'var_function-call-13239531528128313526': [], 'var_function-call-835119119760637705': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': False}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'has_empirical': False}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'has_empirical': False}], 'var_function-call-16986230209680427031': [], 'var_function-call-16617323784436067599': [], 'var_function-call-14351219517084226270': [], 'var_function-call-320867719890547711': [], 'var_function-call-17243782874587110711': [], 'var_function-call-10202973670430014698': [], 'var_function-call-15414146859521326470': 'file_storage/function-call-15414146859521326470.json', 'var_function-call-9425818148868776550': [], 'var_function-call-12608294071483797543': 'file_storage/function-call-12608294071483797543.json'}

exec(code, env_args)
