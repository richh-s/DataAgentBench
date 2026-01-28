code = """import json
import re

# Load physical activity papers
pa_path = locals()['var_functions.query_db:34']
with open(pa_path, 'r') as f:
    pa_papers = json.load(f)

# Load citations
cite_path = locals()['var_functions.query_db:4']
with open(cite_path, 'r') as f:
    citations = json.load(f)

# Build title to citation count map
citation_map = {}
for rec in citations:
    title = rec['title']
    count = int(rec['total_citations'])
    citation_map[title] = count

# Find 2016 papers
papers_2016 = []

for paper in pa_papers:
    text = paper['text']
    title = paper['filename'].replace('.txt', '')
    
    # Skip if not in citation database
    if title not in citation_map:
        continue
    
    # Check for year 2016
    text_start = text[:5000]
    is_2016 = False
    
    if '2016' in text_start:
        is_2016 = True
    else:
        # Check conference patterns
        if "CHI '16" in text_start or "CHI 16" in text_start:
            is_2016 = True
        elif "UbiComp '16" in text_start or "UbiComp 16" in text_start:
            is_2016 = True
        elif "CSCW '16" in text_start or "CSCW 16" in text_start:
            is_2016 = True
        elif "DIS '16" in text_start or "DIS 16" in text_start:
            is_2016 = True
        elif "PervasiveHealth '16" in text_start or "PervasiveHealth 16" in text_start:
            is_2016 = True
        elif "WWW '16" in text_start or "WWW 16" in text_start:
            is_2016 = True
        elif "IUI '16" in text_start or "IUI 16" in text_start:
            is_2016 = True
        elif "OzCHI '16" in text_start or "OzCHI 16" in text_start:
            is_2016 = True
        elif "TEI '16" in text_start or "TEI 16" in text_start:
            is_2016 = True
        elif "AH '16" in text_start or "AH 16" in text_start:
            is_2016 = True
    
    if is_2016:
        total_citations = citation_map[title]
        papers_2016.append({
            'title': title,
            'year': 2016,
            'total_citations': total_citations
        })

# Sort by citation count descending
papers_2016.sort(key=lambda x: x['total_citations'], reverse=True)

print('Found ' + str(len(papers_2016)) + ' papers from 2016 in physical activity domain:')
for paper in papers_2016:
    print('Title: ' + paper['title'])
    print('Total Citations: ' + str(paper['total_citations']))
    print('')

result = json.dumps(papers_2016)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach'}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Understanding Physical Activity Through 3D Printed Material Artifacts'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}], 'var_functions.execute_python:24': [], 'var_functions.execute_python:30': [{'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'year': 2016, 'total_citations': 636}, {'title': 'Charting Design Preferences on Wellness Wearables', 'year': 2016, 'total_citations': 269}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:42': [], 'var_functions.execute_python:46': [], 'var_functions.execute_python:52': [], 'var_functions.execute_python:56': [], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
