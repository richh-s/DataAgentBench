code = """import json
import re

# Load citation data
citations_var = locals()['var_functions.query_db:28']
if isinstance(citations_var, str):
    with open(citations_var, 'r') as f:
        citations = json.load(f)
else:
    citations = citations_var

# Create citation lookup
citation_lookup = {cit['title']: int(cit['total_citations']) for cit in citations}

# Based on the data preview and analysis, identify 2016 physical activity papers
# These are papers with explicit physical activity keywords in title or clear domain relevance
papers_2016_activity = [
    {
        'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity',
        'citations': citation_lookup.get('A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 0)
    },
    {
        'title': 'Activity Tracking: Barriers, Workarounds and Customisation', 
        'citations': citation_lookup.get('Activity Tracking: Barriers, Workarounds and Customisation', 0)
    },
    {
        'title': 'Affordances for Self-tracking Wearable Devices',
        'citations': citation_lookup.get('Affordances for Self-tracking Wearable Devices', 0)
    },
    {
        'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers',
        'citations': citation_lookup.get('Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 0)
    },
    {
        'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data',
        'citations': citation_lookup.get('Defining Adherence: Making Sense of Physical Activity Tracker Data', 0)
    },
    {
        'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation',
        'citations': citation_lookup.get('ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 0)
    },
    {
        'title': 'HealthyTogether: Exploring Social Incentives for Mobile Fitness Applications',
        'citations': citation_lookup.get('HealthyTogether: Exploring Social Incentives for Mobile Fitness Applications', 0)
    },
    {
        'title': 'How Do We Engage with Activity Trackers?: A Longitudinal Study of Habito',
        'citations': citation_lookup.get('How Do We Engage with Activity Trackers?: A Longitudinal Study of Habito', 0)
    }
]

# Filter out papers with 0 citations and sort by citation count
results = [p for p in papers_2016_activity if p['citations'] > 0]
results = sorted(results, key=lambda x: x['citations'], reverse=True)

print('Found', len(results), 'papers from 2016 in physical activity domain')
for p in results:
    print(f"{p['title'][:60]}...: {p['citations']} citations")

print('__RESULT__:')
print(json.dumps(results))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:7': 'file_storage/functions.query_db:7.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json', 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.execute_python:26': [{'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citation_count': 96}], 'var_functions.query_db:28': 'file_storage/functions.query_db:28.json', 'var_functions.execute_python:34': [{'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'total_citation_count': 452}]}

exec(code, env_args)
