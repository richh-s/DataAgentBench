code = """import json
import re

# Load all paper documents
papers_file = 'file_storage/functions.query_db:26.json'
with open(papers_file, 'r') as f:
    paper_docs = json.load(f)

# Find some ACM papers and show their text snippets around ACM
acm_papers = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = doc.get('text', '')
    
    # Check if ACM is mentioned
    if re.search(r'\bACM\b', text, re.IGNORECASE):
        # Find the ACM mention
        match = re.search(r'\bACM\b.{0,100}', text, re.IGNORECASE)
        snippet = match.group(0) if match else 'ACM found but no snippet'
        acm_papers.append({
            'title': title,
            'acm_snippet': snippet
        })

print('__RESULT__:')
print(json.dumps({
    'acm_papers_found': len(acm_papers),
    'sample_acm_papers': acm_papers[:10]
}))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:12': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:14': {'total_records': 158, 'sample_records': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95'}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '28'}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '58'}]}, 'var_functions.list_db:16': ['paper_docs'], 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.execute_python:20': {'total_papers': 5, 'sample_paper': 'A Lived Informatics Model of Personal Informatics.txt'}, 'var_functions.execute_python:22': {'citations_count': 158, 'papers_count': 5}, 'var_functions.execute_python:24': {'total_papers': 5, 'acm_papers': 5, 'acm_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation']}, 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.execute_python:28': {'total_citations_2018': 158, 'total_papers': 99, 'papers_with_info': 99}, 'var_functions.execute_python:30': {'total_papers_in_db': 99, 'acm_papers_total': 95, 'sample_titles': [['A Lived Informatics Model of Personal Informatics', True], ['A Stage-based Model of Personal Informatics Systems', True], ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', True], ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', True], ['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', True]]}, 'var_functions.execute_python:32': {'total_cited_papers_2018': 158, 'acm_papers_cited_in_2018': 0, 'non_acm_papers_cited_in_2018': 158, 'average_citation_count_acm': 0, 'acm_citation_counts': []}, 'var_functions.execute_python:34': {'citation_titles_sample': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Sundroid: Solar Radiation Awareness with Smartphones', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Reviewing Reflection: On the Use of Reflection in Interactive System Design', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Beyond Self-Tracking and Reminders: Designing Smartphone Apps That Support Habit Formation', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection'], 'paper_titles_sample': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone'], 'common_titles_found': 55, 'sample_common_titles': ['Making Sense of Sleep Sensors: How Sleep Sensing Technologies Support and Undermine Sleep Health', 'Goal-oriented Visualizations of Activity Tracking: A Case Study with Engineering Students', 'Sundroid: Solar Radiation Awareness with Smartphones', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"]}, 'var_functions.execute_python:36': {'total_citations_2018': 158, 'matched_citations': 55, 'acm_papers_cited': 0, 'non_acm_papers_cited': 55, 'average_citations_acm': 0, 'acm_citation_counts': []}}

exec(code, env_args)
