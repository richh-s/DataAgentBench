code = """import json
import re
import pandas as pd

# Load full papers data
papers_file = locals()['var_functions.query_db:120']
with open(papers_file, 'r') as f:
    papers = json.load(f)

print('Total papers:', len(papers))

# Find empirical papers and extract year
empirical_papers = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    # Check for empirical
    if 'empirical' in text.lower():
        # Extract year
        year = None
        year_matches = re.findall(r"\b(20[0-9]{2})\b", text)
        if year_matches:
            valid_years = [int(y) for y in year_matches if 2000 <= int(y) <= 2030]
            if valid_years:
                year = max(valid_years)
        
        empirical_papers.append({'title': title, 'year': year})

print('Empirical papers found:', len(empirical_papers))

# Filter after 2016
empirical_df = pd.DataFrame(empirical_papers)
empirical_after_2016 = empirical_df[empirical_df['year'] > 2016]

print('After 2016:', len(empirical_after_2016))

if len(empirical_after_2016) > 0:
    titles = empirical_after_2016['title'].tolist()
    years = empirical_after_2016['year'].tolist()
    result = [{'title': t, 'year': y} for t, y in zip(titles, years)]
else:
    result = []

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.list_db:6': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.execute_python:16': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}], 'var_functions.execute_python:22': [], 'var_functions.execute_python:32': [], 'var_functions.execute_python:42': [], 'var_functions.execute_python:44': {'total_papers': 5, 'sample_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'sample_text_start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Hu"}, 'var_functions.query_db:46': 'file_storage/functions.query_db:46.json', 'var_functions.execute_python:50': [], 'var_functions.execute_python:52': {'total_records': 259, 'unique_titles': 259, 'sample_titles': ['"This Girl is on Fire": Sensemaking in an Online Health Community for Vulvodynia', 'A Family Health App: Engaging Children to Manage Wellness of Adults', 'A Lived Informatics Model of Personal Informatics', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'A Situated Exploration of Designing for Personal Health Ecosystems Through Data-enabled Design', 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'Activity Tracking in Vivo']}, 'var_functions.execute_python:56': [], 'var_functions.execute_python:64': {'count': 0, 'titles': []}, 'var_functions.execute_python:72': {'papers': []}, 'var_functions.execute_python:80': [], 'var_functions.query_db:84': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_functions.query_db:92': [{'citation_year': '2011'}, {'citation_year': '2012'}, {'citation_year': '2013'}, {'citation_year': '2014'}, {'citation_year': '2015'}, {'citation_year': '2016'}, {'citation_year': '2017'}, {'citation_year': '2018'}, {'citation_year': '2019'}, {'citation_year': '2020'}, {'citation_year': '2021'}, {'citation_year': '2022'}, {'citation_year': '2023'}, {'citation_year': '2024'}, {'citation_year': '2025'}], 'var_functions.execute_python:112': {'papers': 5, 'citations': 1}, 'var_functions.query_db:114': [{'name': 'Citations'}, {'name': 'sqlite_sequence'}], 'var_functions.query_db:116': [{'total_records': '1405'}], 'var_functions.query_db:118': [{'total_citations': '847'}], 'var_functions.query_db:120': 'file_storage/functions.query_db:120.json', 'var_functions.list_db:122': ['paper_docs'], 'var_functions.execute_python:124': {'count': 0, 'titles': []}, 'var_functions.query_db:126': [{'title': "Everybody Knows What You'Re Doing: A Critical Design Approach to Personal Informatics", 'total_citations': '694', 'first_citation_year': '2014', 'last_citation_year': '2023'}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'total_citations': '636', 'first_citation_year': '2017', 'last_citation_year': '2025'}, {'title': 'Contextual Influences on the Use and Non-Use of Digital Technology While Exercising at the Gym', 'total_citations': '595', 'first_citation_year': '2016', 'last_citation_year': '2024'}, {'title': 'See Friendship, Sort of: How Conversation and Digital Traces Might Support Reflection on Friendships', 'total_citations': '593', 'first_citation_year': '2013', 'last_citation_year': '2022'}, {'title': 'Shifting Dynamics or Breaking Sacred Traditions?: The Role of Technology in Twelve-step Fellowships', 'total_citations': '587', 'first_citation_year': '2014', 'last_citation_year': '2023'}, {'title': 'ClimbSense: Automatic Climbing Route Recognition Using Wrist-worn Inertia Measurement Units', 'total_citations': '557', 'first_citation_year': '2016', 'last_citation_year': '2024'}, {'title': "It Feels Like I'm Managing Myself: HIV+ People Tracking Their Personal Health Information", 'total_citations': '556', 'first_citation_year': '2017', 'last_citation_year': '2025'}, {'title': "But, I Don'T Take Steps: Examining the Inaccessibility of Fitness Trackers for Wheelchair Athletes", 'total_citations': '554', 'first_citation_year': '2016', 'last_citation_year': '2024'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure", 'total_citations': '542', 'first_citation_year': '2017', 'last_citation_year': '2025'}, {'title': 'Anxiety and Autism: Towards Personalized Digital Health', 'total_citations': '520', 'first_citation_year': '2017', 'last_citation_year': '2025'}], 'var_functions.query_db:128': 'file_storage/functions.query_db:128.json', 'var_functions.execute_python:132': [], 'var_functions.query_db:134': [{'title': 'An Empirical Exploration of Mindfulness Design Using Solo Travel Domain', 'total_citations': '352'}, {'title': 'Understanding the Adoption of Quantified Self-tracking Wearable Devices in the Organization Environment: An Empirical Case Study', 'total_citations': '231'}], 'var_functions.query_db:136': []}

exec(code, env_args)
