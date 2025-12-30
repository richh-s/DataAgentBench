code = """import pandas as pd
import json
import re

file_path_papers = locals()['var_function-call-16910803448492452394']
file_path_citations = locals()['var_function-call-6290455492128806949']

with open(file_path_papers, 'r') as f:
    papers_data = json.load(f)

with open(file_path_citations, 'r') as f:
    citations_data = json.load(f)

extracted_papers_info = []

for paper in papers_data:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')

    year = None
    # Search for a 4-digit year that could be a publication year anywhere in the text
    # Prioritize years appearing early in the document
    year_matches = re.findall(r'\\b(19\\d{2}|20\\d{2})\\b', text)
    for ym in year_matches:
        y = int(ym)
        if 1990 <= y <= 2024: # A broad but reasonable range for publication years
            year = y
            break # Take the first reasonable year found

    is_empirical = False
    # Check for explicit 'contribution' field mentioning 'empirical' anywhere in the text
    contribution_match = re.search(r'contribution: (.*?)(?:\\n|\\.|,)', text, re.IGNORECASE)
    if contribution_match and 'empirical' in contribution_match.group(1).lower():
        is_empirical = True
    
    # If not explicitly in 'contribution', check for empirical keywords throughout the entire text
    if not is_empirical:
        # Expanded list of keywords to identify empirical contributions
        empirical_keywords_in_text = [
            'empirical study', 'we conducted an experiment', 'our study involved', 'data collected from',
            'surveyed participants', 'interviews with', 'user study', 'field study', 'observational study',
            'quantitative analysis', 'qualitative analysis', 'experimental design', 'results indicate',
            'participants reported', 'evaluation of', 'investigated through', 'findings suggest',
            'examined the impact', 'tested the hypothesis', 'demonstrated through', 'measured the effect',
            'empirical evidence', 'empirical findings', 'empirical evaluation', 'an empirical exploration',
            'pilot study', 'case study', 'research methods', 'methodology section', 'data analysis', 
            'statistical analysis', 'the participants', 'study design', 'data-driven', 'evidence-based', 
            'experimental results', 'user feedback', 'observing users', 'gathered data', 'research questions',
            'participant recruitment', 'collected data', 'performed an analysis', 'conducted a series of experiments',
            'quantitative data', 'qualitative data', 'statistical methods', 'human subjects', 'experiment group',
            'control group', 'hypothesis testing', 'observed behaviors', 'measured variables', 'effect of',
            'evaluating the', 'investigating the', 'explored the', 'analyzed the', 'collected and analyzed'
        ]
        if any(keyword in text.lower() for keyword in empirical_keywords_in_text):
            is_empirical = True

    # Only add to the list if it's empirical and published after 2016
    if year and year > 2016 and is_empirical:
        extracted_papers_info.append({
            'title': title,
            'year': year
        })

df_filtered_papers = pd.DataFrame(extracted_papers_info)

# Check if df_filtered_papers is empty
if df_filtered_papers.empty:
    print('__RESULT__:')
    print(json.dumps([])) # Return an empty list if no matching papers are found
else:
    df_citations = pd.DataFrame(citations_data)

    # Convert 'total_citation_count' to numeric, handling potential errors and coercing to NaN
    df_citations['total_citation_count'] = pd.to_numeric(df_citations['total_citation_count'], errors='coerce')

    # Filter out any rows where 'total_citation_count' became NaN after conversion
    df_citations = df_citations.dropna(subset=['total_citation_count'])

    # Ensure title columns are of string type for merging
    df_filtered_papers['title'] = df_filtered_papers['title'].astype(str)
    df_citations['title'] = df_citations['title'].astype(str)

    # Merge the dataframes
    merged_df = pd.merge(df_filtered_papers, df_citations, on='title', how='inner')

    # Select and rename columns as requested
    result = merged_df[['title', 'total_citation_count']]

    # Convert the result to JSON string
    print('__RESULT__:')
    print(result.to_json(orient='records'))"""

env_args = {'var_function-call-2783535409203713964': ['paper_docs'], 'var_function-call-11985281394751560404': 'file_storage/function-call-11985281394751560404.json', 'var_function-call-1858781425464915204': [], 'var_function-call-16910803448492452394': 'file_storage/function-call-16910803448492452394.json', 'var_function-call-1569923686048684083': [], 'var_function-call-6290455492128806949': 'file_storage/function-call-6290455492128806949.json', 'var_function-call-15391798736132793423': [], 'var_function-call-6132096007992688768': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_function-call-4315299038744484136': [], 'var_function-call-7402946793141852739': [], 'var_function-call-17784596592726517006': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_function-call-7089471432629544821': [], 'var_function-call-14965344820861257744': [], 'var_function-call-12874905180232078639': [], 'var_function-call-719211006829589809': [{'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'}]}

exec(code, env_args)
