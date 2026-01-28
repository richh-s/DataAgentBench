code = """import json
import re

# Step 1: Filter papers from the physical activity query that are from 2016
paper_file = locals()['var_functions.query_db:40']
citation_file = locals()['var_functions.query_db:42']

with open(paper_file, 'r') as f:
    physical_activity_papers = json.load(f)

with open(citation_file, 'r') as f:
    all_citations = json.load(f)

print('Total physical activity papers:', len(physical_activity_papers))
print('Total citation records:', len(all_citations))

papers_2016 = []
for paper in physical_activity_papers:
    text = paper.get('text', '')
    if '2016' in text:
        filename = paper.get('filename', '')
        title = filename.replace('.txt', '') if filename else 'Unknown'
        papers_2016.append(title)

print('Papers from 2016:', papers_2016)

# Create citation map
citation_map = {}
for item in all_citations:
    title = item.get('title', '').strip().lower()
    citations = int(item.get('total_citations', 0))
    citation_map[title] = citations

# Match and get results
results = []
for title in papers_2016:
    normalized = title.strip().lower()
    total_cites = citation_map.get(normalized, 0)
    results.append({'title': title, 'total_citations': total_cites})

# Sort by citations
results_sorted = sorted(results, key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(results_sorted, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:6': [], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.list_db:14': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json', 'var_functions.query_db:22': 'file_storage/functions.query_db:22.json', 'var_functions.query_db:30': 'file_storage/functions.query_db:30.json', 'var_functions.query_db:40': 'file_storage/functions.query_db:40.json', 'var_functions.query_db:42': 'file_storage/functions.query_db:42.json', 'var_functions.query_db:52': [{'id': '41', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '45', 'citation_year': '2019'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}, {'id': '43', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '34', 'citation_year': '2021'}, {'id': '44', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '6', 'citation_year': '2022'}, {'id': '45', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '94', 'citation_year': '2023'}, {'id': '46', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '59', 'citation_year': '2024'}, {'id': '73', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '90', 'citation_year': '2017'}, {'id': '74', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '88', 'citation_year': '2018'}, {'id': '75', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '83', 'citation_year': '2019'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '77', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '78', 'citation_year': '2021'}, {'id': '107', 'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'citation_count': '69', 'citation_year': '2020'}, {'id': '108', 'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'citation_count': '34', 'citation_year': '2021'}, {'id': '109', 'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'citation_count': '96', 'citation_year': '2022'}, {'id': '110', 'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'citation_count': '75', 'citation_year': '2023'}, {'id': '111', 'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'citation_count': '55', 'citation_year': '2024'}, {'id': '112', 'title': 'Social Activity Measurement by Counting Faces Captured in First-Person View Lifelogging Video', 'citation_count': '75', 'citation_year': '2025'}, {'id': '121', 'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'citation_count': '81', 'citation_year': '2018'}, {'id': '122', 'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'citation_count': '21', 'citation_year': '2019'}, {'id': '123', 'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'citation_count': '88', 'citation_year': '2020'}, {'id': '172', 'title': 'Sensor Requirements for Activity Recognition on Smart Watches', 'citation_count': '11', 'citation_year': '2014'}, {'id': '173', 'title': 'Sensor Requirements for Activity Recognition on Smart Watches', 'citation_count': '11', 'citation_year': '2015'}, {'id': '174', 'title': 'Sensor Requirements for Activity Recognition on Smart Watches', 'citation_count': '94', 'citation_year': '2016'}, {'id': '175', 'title': 'Sensor Requirements for Activity Recognition on Smart Watches', 'citation_count': '63', 'citation_year': '2017'}, {'id': '176', 'title': 'Sensor Requirements for Activity Recognition on Smart Watches', 'citation_count': '9', 'citation_year': '2018'}, {'id': '177', 'title': 'Sensor Requirements for Activity Recognition on Smart Watches', 'citation_count': '98', 'citation_year': '2019'}, {'id': '178', 'title': 'Sensor Requirements for Activity Recognition on Smart Watches', 'citation_count': '69', 'citation_year': '2020'}, {'id': '179', 'title': 'Sensor Requirements for Activity Recognition on Smart Watches', 'citation_count': '99', 'citation_year': '2021'}, {'id': '180', 'title': 'Sensor Requirements for Activity Recognition on Smart Watches', 'citation_count': '17', 'citation_year': '2022'}, {'id': '181', 'title': 'Sensor Requirements for Activity Recognition on Smart Watches', 'citation_count': '17', 'citation_year': '2023'}, {'id': '194', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '57', 'citation_year': '2019'}, {'id': '195', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '67', 'citation_year': '2020'}, {'id': '196', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '58', 'citation_year': '2021'}, {'id': '197', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '16', 'citation_year': '2022'}, {'id': '198', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '32', 'citation_year': '2023'}, {'id': '199', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '29', 'citation_year': '2024'}, {'id': '227', 'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', 'citation_count': '13', 'citation_year': '2014'}, {'id': '228', 'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach', 'citation_count': '85', 'citation_year': '2015'}, {'id': '247', 'title': 'Pass the Ball: Enforced Turn-Taking in Activity Tracking', 'citation_count': '32', 'citation_year': '2016'}, {'id': '248', 'title': 'Pass the Ball: Enforced Turn-Taking in Activity Tracking', 'citation_count': '10', 'citation_year': '2017'}, {'id': '249', 'title': 'Pass the Ball: Enforced Turn-Taking in Activity Tracking', 'citation_count': '57', 'citation_year': '2018'}, {'id': '250', 'title': 'Pass the Ball: Enforced Turn-Taking in Activity Tracking', 'citation_count': '71', 'citation_year': '2019'}, {'id': '251', 'title': 'Pass the Ball: Enforced Turn-Taking in Activity Tracking', 'citation_count': '13', 'citation_year': '2020'}, {'id': '252', 'title': 'Pass the Ball: Enforced Turn-Taking in Activity Tracking', 'citation_count': '7', 'citation_year': '2021'}, {'id': '253', 'title': 'Pass the Ball: Enforced Turn-Taking in Activity Tracking', 'citation_count': '84', 'citation_year': '2022'}, {'id': '254', 'title': 'Pass the Ball: Enforced Turn-Taking in Activity Tracking', 'citation_count': '70', 'citation_year': '2023'}, {'id': '255', 'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'citation_count': '12', 'citation_year': '2016'}, {'id': '265', 'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'citation_count': '59', 'citation_year': '2019'}, {'id': '266', 'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'citation_count': '37', 'citation_year': '2020'}, {'id': '267', 'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals', 'citation_count': '55', 'citation_year': '2021'}], 'var_functions.query_db:54': 'file_storage/functions.query_db:54.json'}

exec(code, env_args)
