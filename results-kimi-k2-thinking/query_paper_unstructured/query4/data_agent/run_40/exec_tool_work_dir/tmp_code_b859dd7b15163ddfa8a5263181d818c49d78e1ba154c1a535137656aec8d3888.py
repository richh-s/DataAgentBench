code = """import json
import re

# Load all paper documents
all_papers_file = locals()['var_functions.query_db:66']
with open(all_papers_file, 'r') as f:
    all_papers = json.load(f)

# Load citations for physical activity papers
pa_citations_file = locals()['var_functions.query_db:58']
with open(pa_citations_file, 'r') as f:
    pa_citations = json.load(f)

# Load all citations
all_citations_file = locals()['var_functions.query_db:4']
with open(all_citations_file, 'r') as f:
    all_citations = json.load(f)

# Build citation total map
citation_totals = {}
for rec in all_citations:
    citation_totals[rec['title']] = int(rec['total_citations'])

print(f"Total paper documents: {len(all_papers)}")
print(f"Physical activity citation records: {len(pa_citations)}")
print(f"Unique papers in citation database: {len(citation_totals)}")

# Get set of physical activity paper titles from citations
physical_activity_titles = set()
for rec in pa_citations:
    physical_activity_titles.add(rec['title'])

print(f"Physical activity papers in citation database: {len(physical_activity_titles)}")

# Function to extract year from paper text
def extract_year(text):
    # Check first 8000 characters
    text_start = text[:8000]
    
    # Look for explicit year (2016)
    if '2016' in text_start:
        return 2016
    
    # Look for conference patterns
    conferences = ['CHI', 'UbiComp', 'CSCW', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH']
    for conf in conferences:
        # Pattern: CHI '16 or CHI'16
        pattern = conf + r"\s*'\s*16\b"
        if re.search(pattern, text_start, re.IGNORECASE):
            return 2016
        # Pattern: CHI 16
        pattern2 = conf + r"\s+16\b"
        if re.search(pattern2, text_start, re.IGNORECASE):
            return 2016
    
    return None

# Find all papers from 2016 that are in the physical activity domain
papers_2016_physical_activity = []
processed_titles = set()

for paper in all_papers:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Skip if already processed or not in physical activity domain
    if title in processed_titles or title not in physical_activity_titles:
        continue
    
    text = paper['text']
    
    # Extract year
    year = extract_year(text)
    
    if year == 2016:
        if title in citation_totals:
            papers_2016_physical_activity.append({
                'title': title,
                'year': year,
                'total_citations': citation_totals[title]
            })
        processed_titles.add(title)

# Sort by total citations descending
papers_2016_physical_activity.sort(key=lambda x: x['total_citations'], reverse=True)

print(f"\nFound {len(papers_2016_physical_activity)} papers from 2016 in physical activity domain:")
for paper in papers_2016_physical_activity:
    print(f"- {paper['title']}")
    print(f"  Total Citations: {paper['total_citations']}")
    print()

# Output as JSON
result = json.dumps(papers_2016_physical_activity, indent=2)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach'}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Understanding Physical Activity Through 3D Printed Material Artifacts'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}], 'var_functions.execute_python:24': [], 'var_functions.execute_python:30': [{'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'year': 2016, 'total_citations': 636}, {'title': 'Charting Design Preferences on Wellness Wearables', 'year': 2016, 'total_citations': 269}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:42': [], 'var_functions.execute_python:46': [], 'var_functions.execute_python:52': [], 'var_functions.execute_python:56': [], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json', 'var_functions.execute_python:62': [], 'var_functions.execute_python:64': [{'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity', 'total_citations': 12}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity', 'total_citations': 180}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity', 'total_citations': 221}, {'title': 'SweatAtoms: Materializing Physical Activity', 'total_citations': 428}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity', 'total_citations': 358}, {'title': 'Low Sampling Rate for Physical Activity Recognition', 'total_citations': 348}], 'var_functions.query_db:66': 'file_storage/functions.query_db:66.json'}

exec(code, env_args)
