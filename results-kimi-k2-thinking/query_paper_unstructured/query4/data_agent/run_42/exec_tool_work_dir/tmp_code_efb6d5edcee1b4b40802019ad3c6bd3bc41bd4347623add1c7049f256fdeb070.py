code = """import json
import os

# Load the data files
paper_docs = json.load(open(locals()['var_functions.query_db:2'], 'r'))
citation_totals = json.load(open(locals()['var_functions.query_db:26'], 'r'))

print('Step 1: Data loaded')
print('  - Paper docs:', len(paper_docs))
print('  - Citation totals:', len(citation_totals))

# Process papers to identify 2016 papers in physical activity domain
papers_2016_pa = []
for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    
    # Check for 2016 publication
    is_2016 = '2016' in text[:3000]
    # Check for physical activity domain
    is_pa = 'physical activity' in text.lower()
    
    if is_2016 and is_pa and title:
        papers_2016_pa.append(title)

print('\nStep 2: Found', len(papers_2016_pa), '2016 papers in physical activity domain')
for title in papers_2016_pa:
    print('  -', title)

# Create citation lookup dictionary
citation_dict = {}
for item in citation_totals:
    title = item.get('title', '')
    total_cites = int(item.get('total_citations', 0))
    if title:
        citation_dict[title] = total_cites

print('\nStep 3: Created citation lookup with', len(citation_dict), 'entries')

# Match papers with citations
results = []
for paper_title in papers_2016_pa:
    if paper_title in citation_dict:
        results.append({
            'title': paper_title,
            'total_citation_count': citation_dict[paper_title]
        })
    else:
        # Check case-insensitive match
        lower_title = paper_title.lower()
        for cit_title, count in citation_dict.items():
            if cit_title.lower() == lower_title:
                results.append({
                    'title': paper_title,
                    'total_citation_count': count
                })
                break

print('\nStep 4: Matched', len(results), 'papers with citations')
for r in results:
    print('  ', r['title'][:50], ':', r['total_citation_count'])

# Output as JSON string
print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:20': [], 'var_functions.query_db:22': [{'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach'}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Understanding Physical Activity Through 3D Printed Material Artifacts'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
