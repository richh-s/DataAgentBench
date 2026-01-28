code = """import json

# Load the full paper documents to see what we have
papers_file_path = locals()['var_functions.query_db:5']
with open(papers_file_path, 'r') as f:
    paper_docs = json.load(f)

# Print detailed info about the papers we have
paper_info = []
for i, doc in enumerate(paper_docs):
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Show first part of text to help identify the paper
    text_preview = doc.get('text', '')[:200]
    
    paper_info.append({
        'index': i,
        'filename': filename,
        'title': title,
        'text_preview': text_preview
    })

print('__RESULT__:')
print(json.dumps(paper_info, indent=2))"""

env_args = {'var_functions.list_db:0': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.execute_python:12': {'citations_2018_count': 158, 'paper_docs_count': 5}, 'var_functions.execute_python:14': {'total_citations_2018': 158, 'matched_papers': 0, 'unmatched_papers': 156, 'acm_papers_2018': 0, 'acm_papers_sample': []}, 'var_functions.execute_python:16': {'citation_titles_2018': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Sundroid: Solar Radiation Awareness with Smartphones', 'Why We Use and Abandon Smart Devices', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'Reviewing Reflection: On the Use of Reflection in Interactive System Design', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'Beyond Self-Tracking and Reminders: Designing Smartphone Apps That Support Habit Formation', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection'], 'total_citations_2018': 158}}

exec(code, env_args)
