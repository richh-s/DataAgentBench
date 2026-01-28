code = """import json

# Read the citations data from the file
with open('/tmp/tmp2h3j9g2q.json', 'r') as f:
    all_citations = json.load(f)

print(f"Total citation records: {len(all_citations)}")

# Group by title and sum citation counts
citation_totals = {}
paper_years = {}

for record in all_citations:
    title = record['title']
    count = int(record['citation_count'])
    
    if title not in citation_totals:
        citation_totals[title] = 0
    citation_totals[title] += count

# Get unique paper titles
unique_titles = list(citation_totals.keys())
print(f"Unique papers: {len(unique_titles)}")
print("Sample titles:")
for i, title in enumerate(unique_titles[:10]):
    print(f"  {i+1}. {title}")

print('__RESULT__:')
print(json.dumps({'total_citations': len(all_citations), 'unique_papers': len(unique_titles), 'sample_titles': unique_titles[:5]}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:14': [{'id': '73', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '90', 'citation_year': '2017'}, {'id': '74', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '88', 'citation_year': '2018'}, {'id': '75', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '83', 'citation_year': '2019'}, {'id': '76', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '10', 'citation_year': '2020'}, {'id': '77', 'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': '78', 'citation_year': '2021'}, {'id': '194', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '57', 'citation_year': '2019'}, {'id': '195', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '67', 'citation_year': '2020'}, {'id': '196', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '58', 'citation_year': '2021'}, {'id': '197', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '16', 'citation_year': '2022'}, {'id': '198', 'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'citation_count': '32', 'citation_year': '2023'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
