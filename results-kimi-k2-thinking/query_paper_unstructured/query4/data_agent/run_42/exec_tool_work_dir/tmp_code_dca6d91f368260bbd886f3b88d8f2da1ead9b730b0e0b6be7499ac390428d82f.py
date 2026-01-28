code = """import json
import re

# Load the three datasets
pa_papers_path = locals()['var_functions.query_db:2']
papers_2016_path = locals()['var_functions.query_db:24']
citation_totals_path = locals()['var_functions.query_db:26']

with open(pa_papers_path, 'r') as f:
    pa_papers = json.load(f)

with open(papers_2016_path, 'r') as f:
    papers_2016 = json.load(f)

with open(citation_totals_path, 'r') as f:
    citation_totals = json.load(f)

print(f'Loaded {len(pa_papers)} physical activity papers')
print(f'Loaded {len(papers_2016)} papers from 2016')
print(f'Loaded {len(citation_totals)} citation totals')

# Look at one example from each to understand structure
print('\nSample PA paper:', pa_papers[0].get('filename', 'no filename'))
print('Sample 2016 paper:', papers_2016[0].get('filename', 'no filename'))
print('Sample citation:', citation_totals[0])

# Extract titles from each dataset
pa_titles = []
for p in pa_papers:
    filename = p.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    if title:
        pa_titles.append(title)

papers_2016_titles = []
for p in papers_2016:
    filename = p.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    if title:
        papers_2016_titles.append(title)

print(f'\nExtracted {len(pa_titles)} PA titles and {len(papers_2016_titles)} 2016 titles')

# Find intersection
pa_set = set(pa_titles)
papers_2016_set = set(papers_2016_titles)

common_titles = pa_set.intersection(papers_2016_set)
print(f'Found {len(common_titles)} common titles')

if len(common_titles) > 0:
    print('\nCommon titles:')
    for t in list(common_titles)[:10]:
        print(f'  - {t}')

# Create citation lookup
citation_lookup = {}
for item in citation_totals:
    title = item.get('title', '')
    total_citations = int(item.get('total_citations', 0))
    if title:
        citation_lookup[title] = total_citations

print(f'\nCreated citation lookup with {len(citation_lookup)} entries')

# Match common titles with citations
final_results = []
for title in common_titles:
    if title in citation_lookup:
        final_results.append({
            'title': title,
            'total_citation_count': citation_lookup[title]
        })
    else:
        # Try case-insensitive match
        for cit_title, count in citation_lookup.items():
            if title.lower() == cit_title.lower():
                final_results.append({
                    'title': title,
                    'total_citation_count': count
                })
                break

print(f'\nFinal results: {len(final_results)} papers matched with citations')
for r in final_results:
    print(f"  {r['title']}: {r['total_citation_count']} citations")

output = json.dumps(final_results, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': [], 'var_functions.execute_python:20': [], 'var_functions.query_db:22': [{'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach'}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Understanding Physical Activity Through 3D Printed Material Artifacts'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}], 'var_functions.query_db:24': 'file_storage/functions.query_db:24.json', 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json'}

exec(code, env_args)
