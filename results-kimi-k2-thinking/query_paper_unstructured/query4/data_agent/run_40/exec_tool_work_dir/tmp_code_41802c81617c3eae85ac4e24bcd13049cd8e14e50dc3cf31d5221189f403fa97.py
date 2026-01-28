code = """import json
import re

# Load papers with physical activity
pa_file = locals()['var_functions.query_db:2']
with open(pa_file, 'r') as f:
    pa_papers = json.load(f)

print("Loaded", len(pa_papers), "papers about physical activity")

# Load all citations
citations_file = locals()['var_functions.query_db:4']
with open(citations_file, 'r') as f:
    citations = json.load(f)

print("Loaded", len(citations), "citation records")

# Create dict of title -> total citations
citations_dict = {}
for record in citations:
    title = record['title']
    count = int(record['total_citations'])
    citations_dict[title] = count

print("Unique papers in citations:", len(citations_dict))

# Look for 2016 patterns more carefully
def find_year(text, title):
    # Check common locations for year
    text_start = text[:5000]
    
    # Look for explicit 2016
    if "2016" in text_start:
        return 2016
    
    # Look for conference patterns (CHI '16, etc.)
    conferences = ["CHI", "UbiComp", "CSCW", "DIS", "PervasiveHealth", "WWW", "IUI", "OzCHI", "TEI", "AH"]
    for conf in conferences:
        pattern = conf + r"\s*[\'\"]?\s*16"
        if re.search(pattern, text_start, re.IGNORECASE):
            return 2016
    
    # Check if title exists in citations and has 2016 data
    return None

# Check each paper
papers_2016 = []
for paper in pa_papers:
    year = find_year(paper['text'], paper['filename'])
    if year == 2016:
        title = paper['filename'].replace('.txt', '')
        if title in citations_dict:
            papers_2016.append({
                'title': title,
                'year': 2016,
                'citations': citations_dict[title]
            })
        else:
            papers_2016.append({
                'title': title,
                'year': 2016,
                'citations': 0
            })

print("\nPapers from 2016 in physical activity domain:")
for p in papers_2016:
    print(f"- {p['title']} ({p['citations']} citations)")

# Output result
result = json.dumps(papers_2016)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach'}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Understanding Physical Activity Through 3D Printed Material Artifacts'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}], 'var_functions.execute_python:24': []}

exec(code, env_args)
