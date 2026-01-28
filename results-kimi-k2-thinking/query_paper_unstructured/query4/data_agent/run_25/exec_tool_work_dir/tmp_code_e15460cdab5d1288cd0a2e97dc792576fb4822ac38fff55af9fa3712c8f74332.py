code = """import json

# Get paper data for 2016 physical activity papers
paper_data_2016_pa = locals()['var_functions.query_db:22']
print(f"Found {len(paper_data_2016_pa)} papers from 2016 in physical activity domain")
print("Paper titles:")
for paper in paper_data_2016_pa:
    print(f"  - {paper['filename']}")

# Get all citation data
citation_file_path = locals()['var_functions.query_db:16']
print(f"\nCitation data stored at: {citation_file_path}")"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:14': [{'id': '73', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '90', 'citation_year': '2017'}, {'id': '74', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '88', 'citation_year': '2018'}, {'id': '75', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '83', 'citation_year': '2019'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '77', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '78', 'citation_year': '2021'}, {'id': '194', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '57', 'citation_year': '2019'}, {'id': '195', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '67', 'citation_year': '2020'}, {'id': '196', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '58', 'citation_year': '2021'}, {'id': '197', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '16', 'citation_year': '2022'}, {'id': '198', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '32', 'citation_year': '2023'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:20': 'file_storage/functions.query_db:20.json', 'var_functions.query_db:22': [{'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'filename': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use.txt'}, {'filename': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching.txt"}, {'filename': 'Charting Design Preferences on Wellness Wearables.txt'}]}

exec(code, env_args)
