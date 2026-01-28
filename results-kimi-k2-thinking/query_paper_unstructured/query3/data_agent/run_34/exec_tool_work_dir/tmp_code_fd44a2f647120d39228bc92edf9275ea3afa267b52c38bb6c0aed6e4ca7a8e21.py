code = """import json
import pandas as pd
import re

# Read both datasets
mongo_key = 'var_functions.query_db:2'
citations_key = 'var_functions.query_db:20'

mongo_path = locals()[mongo_key]
citations_path = locals()[citations_key]

with open(mongo_path, 'r') as f:
    mongo_data = json.load(f)

with open(citations_path, 'r') as f:
    citations_data = json.load(f)

# Create a mapping of mongo titles to publication info
mongo_titles = {}
for doc in mongo_data:
    filename = doc.get('filename', '')
    if filename:
        title = filename.replace('.txt', '')
        text = doc.get('text', '')
        
        # Attempt to extract year
        year = None
        year_match = re.search(r'\b(20(1[7-9]|[2-9]\d))\b', text[:2000])
        if year_match:
            year = int(year_match.group(1))
        
        if not year:
            conf_match = re.search(r"(?:CHI|UbiComp|UBICOMP|CSCW|DIS|PervasiveHealth)\s*(?:'?(\d{2})\b|20(1[7-9]|[2-9]\d))", text[:2000], re.IGNORECASE)
            if conf_match:
                if conf_match.group(1):
                    year_num = int(conf_match.group(1))
                    if year_num >= 17:
                        year = 2000 + year_num
                elif conf_match.group(2):
                    year = int('20' + conf_match.group(2))
        
        # Check for empirical contribution
        if text:
            text_lower = text.lower()
            empirical_terms = ['study', 'empirical', 'experiment', 'evaluation', 'participants', 'user study', 'survey', 'interview', 'field study']
            methodology_terms = ['methodology', 'methods', 'data collection', 'analysis']
            
            term_count = sum(1 for term in empirical_terms if term in text_lower)
            has_methodology = any(term in text_lower for term in methodology_terms)
            
            is_empirical = term_count >= 2 or (term_count >= 1 and has_methodology)
            
            mongo_titles[title] = {
                'year': year,
                'is_empirical': is_empirical
            }

# Process citation data
citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Calculate total citations per paper
total_citations = citations_df.groupby('title')['citation_count'].sum().reset_index()

# Find empirical papers published after 2016
empirical_results = []

for title, mongo_info in mongo_titles.items():
    if mongo_info['year'] and mongo_info['year'] > 2016 and mongo_info['is_empirical']:
        # Find citation count
        citation_row = total_citations[total_citations['title'] == title]
        if not citation_row.empty:
            citation_count = int(citation_row.iloc[0]['citation_count'])
            empirical_results.append({
                'title': title,
                'year': mongo_info['year'],
                'total_citations': citation_count
            })

# Sort by citations for better output
empirical_results = sorted(empirical_results, key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps({
    'total_empirical_papers_after_2016': len(empirical_results),
    'papers': empirical_results
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:10': {'message': 'No empirical papers found after 2016', 'empirical_papers': []}, 'var_functions.execute_python:12': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'title': 'A Lived Informatics Model of Personal Informatics', 'year_matches': [], 'text_preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'title': 'A Stage-based Model of Personal Informatics Systems', 'year_matches': [], 'text_preview': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 152'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year_matches': [], 'text_preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosali'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year_matches': [], 'text_preview': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n E'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year_matches': [], 'text_preview': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent C'}], 'var_functions.execute_python:14': {'papers_after_2016': 0, 'empirical_papers_after_2016': 0, 'message': 'No papers found after 2016'}, 'var_functions.execute_python:16': {'total_papers': 5, 'sample_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_functions.list_db:18': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.execute_python:22': {'empirical_papers_after_2016': 0, 'papers': [], 'message': 'No empirical papers found after 2016 in this dataset'}, 'var_functions.execute_python:24': {'total_unique_papers': 259, 'candidate_empirical_papers': 28, 'empirical_papers_with_citations': 28, 'sample_empirical_papers': [{'title': 'An Empirical Exploration of Mindfulness Design Using Solo Travel Domain', 'citation_count': 352}, {'title': 'Closing the Feedback Loop: A 12-month Evaluation of ASTA, a Self-Tracking Application for ASHAs', 'citation_count': 197}, {'title': 'Data, Data Everywhere, and Still Too Hard to Link: Insights from User Interactions with Diabetes Apps', 'citation_count': 298}, {'title': 'Design Opportunities in Three Stages of Relationship Development Between Users and Self-Tracking Devices', 'citation_count': 343}, {'title': 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness', 'citation_count': 448}, {'title': 'Exploring Emotions Through Painting, Photography and Expressive Writing: An Early Experimental User Study', 'citation_count': 64}, {'title': 'Family Health Promotion in Low-SES Neighborhoods: A Two-Month Study of Wearable Activity Tracking', 'citation_count': 400}, {'title': 'Fostering User Engagement: Improving Sense of Identity Through Cosmetic Customization in Wearable Trackers', 'citation_count': 43}, {'title': 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students', 'citation_count': 339}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'citation_count': 133}]}}

exec(code, env_args)
