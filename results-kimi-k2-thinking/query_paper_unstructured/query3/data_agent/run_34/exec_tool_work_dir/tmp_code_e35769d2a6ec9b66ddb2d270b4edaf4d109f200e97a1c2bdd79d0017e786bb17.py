code = """import json
import pandas as pd

# Read the citations data from the file
storage_key = 'var_functions.query_db:20'
file_path = locals()[storage_key]

with open(file_path, 'r') as f:
    citations_data = json.load(f)

# Create DataFrame
citations_df = pd.DataFrame(citations_data)

# Convert numeric fields
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])
citations_df['citation_year'] = pd.to_numeric(citations_df['citation_year'])

# Group by title to get total citation count per paper
total_citations = citations_df.groupby('title')['citation_count'].sum().reset_index()

# Find papers with citations in 2017+ (which means they were likely published before or around then)
# This is a proxy for post-2016 papers
modern_papers = citations_df[citations_df['citation_year'] >= 2017]['title'].unique()

# Get paper titles that appear to be empirical based on title keywords
empirical_indicators = ['study', 'evaluation', 'empirical', 'experiment', 'survey', 'user', 'field', 'analysis', 'assessment']

candidate_empirical = []
for title in modern_papers:
    title_lower = title.lower()
    if any(indicator in title_lower for indicator in empirical_indicators):
        candidate_empirical.append(title)

# Get total citations for these candidate empirical papers
empirical_citations = total_citations[total_citations['title'].isin(candidate_empirical)].copy()

print('__RESULT__:')
print(json.dumps({
    'total_unique_papers': len(total_citations),
    'candidate_empirical_papers': len(candidate_empirical),
    'empirical_papers_with_citations': len(empirical_citations),
    'sample_empirical_papers': empirical_citations.head(10).to_dict('records')
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'message': 'No empirical papers found after 2016', 'empirical_papers': []}, 'var_functions.execute_python:12': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'title': 'A Lived Informatics Model of Personal Informatics', 'year_matches': [], 'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'title': 'A Stage-based Model of Personal Informatics Systems', 'year_matches': [], 'text_preview': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year_matches': [], 'text_preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year_matches': [], 'text_preview': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year_matches': [], 'text_preview': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}], 'var_functions.execute_python:14': {'papers_after_2016': 0, 'empirical_papers_after_2016': 0, 'message': 'No papers found after 2016'}, 'var_functions.execute_python:16': {'total_papers': 5, 'sample_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_functions.list_db:18': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'empirical_papers_after_2016': 0, 'papers': [], 'message': 'No empirical papers found after 2016 in this dataset'}}

exec(code, env_args)
