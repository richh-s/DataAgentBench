code = """import json
import re

# Load data from files
mongo_path = locals()['var_functions.query_db:2']
citations_path = locals()['var_functions.query_db:26']

with open(mongo_path) as f:
    papers = json.load(f)

with open(citations_path) as f:
    citations = json.load(f)

print('Data loaded:', len(papers), 'papers,', len(citations), 'citation records')

# Extract 2016 papers in physical activity domain
papers_2016_pa = []
for p in papers:
    filename = p.get('filename', '')
    text = p.get('text', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check for 2016 and physical activity
    if '2016' in text[:2000] and 'physical activity' in text.lower() and title:
        papers_2016_pa.append(title)

print('Found', len(papers_2016_pa), '2016 papers in physical activity domain')

# Create citation lookup
citation_lookup = {}
for c in citations:
    title = c.get('title', '')
    count = int(c.get('total_citations', 0))
    if title:
        citation_lookup[title] = count

print('Created citation lookup with', len(citation_lookup), 'entries')

# Match papers with citations
results = []
for paper_title in papers_2016_pa:
    # Try direct match
    if paper_title in citation_lookup:
        results.append({'title': paper_title, 'total_citation_count': citation_lookup[paper_title]})
    else:
        # Try case-insensitive match
        for cit_title, count in citation_lookup.items():
            if paper_title.lower() == cit_title.lower():
                results.append({'title': paper_title, 'total_citation_count': count})
                break

print('Matched', len(results), 'papers with citations')

# Output
print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:20': [], 'var_functions.query_db:22': [{'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach'}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Understanding Physical Activity Through 3D Printed Material Artifacts'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
