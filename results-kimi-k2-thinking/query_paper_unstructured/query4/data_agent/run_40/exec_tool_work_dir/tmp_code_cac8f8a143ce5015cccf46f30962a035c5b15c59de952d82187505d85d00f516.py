code = """import json

# Load physical activity citations with 2016 data
pa_cites_file = locals()['var_functions.query_db:58']
with open(pa_cites_file, 'r') as f:
    pa_citations = json.load(f)

# Load all citations to get total counts
all_cites_file = locals()['var_functions.query_db:4']
with open(all_cites_file, 'r') as f:
    all_citations = json.load(f)

print('Physical activity citation records:', len(pa_citations))
print('Total citation records:', len(all_citations))

# Build total citation map
total_citation_map = {}
for rec in all_citations:
    total_citation_map[rec['title']] = int(rec['total_citations'])

print('Unique papers in citation database:', len(total_citation_map))

# Identify papers that have citations in 2016 (indicating they were published in 2016)
papers_in_2016 = {}

# Check each record - if citation_year is 2016, the paper was published that year
for rec in pa_citations:
    citation_year = int(rec['citation_year'])
    title = rec['title']
    
    if citation_year == 2016:
        papers_in_2016[title] = total_citation_map.get(title, 0)

# Convert to list and sort
results = []
for title, total_citations in papers_in_2016.items():
    results.append({
        'title': title,
        'total_citations': total_citations
    })

# Sort by total citations
def get_citations(p):
    return p['total_citations']

results.sort(key=get_citations, reverse=True)

print('\nPapers published in 2016 in physical activity domain:')
print('Format: Title - Total Citations\n')

for p in results:
    print(p['title'])
    print('Total Citations:', p['total_citations'])
    print()

print('Total papers found:', len(results))

# Output as JSON string
output = json.dumps(results)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach'}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Understanding Physical Activity Through 3D Printed Material Artifacts'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}], 'var_functions.execute_python:24': [], 'var_functions.execute_python:30': [{'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'year': 2016, 'total_citations': 636}, {'title': 'Charting Design Preferences on Wellness Wearables', 'year': 2016, 'total_citations': 269}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:42': [], 'var_functions.execute_python:46': [], 'var_functions.execute_python:52': [], 'var_functions.execute_python:56': [], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:62': [], 'var_functions.execute_python:64': [{'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'total_citations': 12}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity', 'total_citations': 180}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'total_citations': 221}, {'title': 'SweatAtoms: Materializing Physical Activity', 'total_citations': 428}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity', 'total_citations': 358}, {'title': 'Low Sampling Rate for Physical Activity Recognition', 'total_citations': 348}], 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json'}

exec(code, env_args)
