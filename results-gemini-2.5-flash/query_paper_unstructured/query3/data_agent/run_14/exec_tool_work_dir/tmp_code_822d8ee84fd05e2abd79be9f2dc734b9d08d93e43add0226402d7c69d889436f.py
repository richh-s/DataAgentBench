code = """import pandas as pd
import json
import re

# Load paper documents data
file_path_paper_docs = locals()['var_function-call-12891957927342614811']
with open(file_path_paper_docs, 'r') as f:
    paper_docs = json.load(f)

parsed_papers_data = []
for doc in paper_docs:
    filename = doc['filename']
    text = doc['text']
    title = filename.replace('.txt', '')

    year = None
    potential_years = []

    # Pattern 1: YYYY (4-digit year)
    for match in re.finditer(r'\b(19|20)\d{2}\b', text[:2000]):
        current_year = int(match.group(0))
        if 1950 <= current_year <= 2024:
            potential_years.append(current_year)

    # Pattern 2: 'YY (2-digit year, common in conference proceedings like '15)
    for match in re.finditer(r"'(\d{2})", text[:2000]):
        two_digit_year = int(match.group(1))
        if 0 <= two_digit_year <= 99:
            # Heuristic to convert 2-digit year to 4-digit
            if two_digit_year <= 24: # Assuming 2000-2024
                potential_years.append(2000 + two_digit_year)
            else: # Assuming 1950-1999 for older papers
                potential_years.append(1900 + two_digit_year)
    
    # Pattern 3: Copyright YYYY or similar
    for match in re.finditer(r'[Cc]opyright\s*(?:©)?\s*(19|20)\d{2}', text[:2000]):
        current_year = int(match.group(0)[-4:])
        if 1950 <= current_year <= 2024:
            potential_years.append(current_year)

    if potential_years:
        year = min(potential_years) # Take the earliest plausible year

    contribution = None
    # Check for 'empirical' or its derivatives (e.g., empirically) anywhere in the text
    if re.search(r'\bempiric(?:al|ally|ism|ist)s?\b', text, re.IGNORECASE):
        contribution = 'empirical'

    parsed_papers_data.append({'title': title, 'year': year, 'contribution': contribution})

df_papers = pd.DataFrame(parsed_papers_data)

# Filter for papers published after 2016 with 'empirical' contribution
filtered_papers = df_papers[
    (df_papers['year'].notna()) & 
    (df_papers['year'] > 2016) & 
    (df_papers['contribution'] == 'empirical')
]

# If filtered_papers is empty, print an empty JSON array and exit, otherwise proceed
if filtered_papers.empty:
    print('__RESULT__:')
    print(json.dumps([]))
else:
    empirical_titles_df = filtered_papers[['title']].copy()

    # Load citation data from the correct key
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

env_args = {'var_function-call-3207410245806214601': ['paper_docs'], 'var_function-call-89421489897449482': 'file_storage/function-call-89421489897449482.json', 'var_function-call-2589591416908310925': [], 'var_function-call-13239531528128313526': [], 'var_function-call-835119119760637705': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'has_empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'has_empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': False}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'has_empirical': False}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'has_empirical': False}], 'var_function-call-16986230209680427031': [], 'var_function-call-16617323784436067599': [], 'var_function-call-14351219517084226270': [], 'var_function-call-320867719890547711': [], 'var_function-call-17243782874587110711': [], 'var_function-call-10202973670430014698': [], 'var_function-call-15414146859521326470': 'file_storage/function-call-15414146859521326470.json', 'var_function-call-9425818148868776550': [], 'var_function-call-12608294071483797543': 'file_storage/function-call-12608294071483797543.json', 'var_function-call-6914328032805360955': [], 'var_function-call-8891258027671418511': [], 'var_function-call-7099604938380591321': [], 'var_function-call-12891957927342614811': 'file_storage/function-call-12891957927342614811.json', 'var_function-call-14820484231919104682': [], 'var_function-call-10820505087453654198': [{'title': 'A Lived Informatics Model of Personal Informatics', 'found_year': None, 'has_empirical_contribution': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'found_year': None, 'has_empirical_contribution': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'found_year': None, 'has_empirical_contribution': False}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'found_year': None, 'has_empirical_contribution': False}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'found_year': None, 'has_empirical_contribution': False}]}

exec(code, env_args)
