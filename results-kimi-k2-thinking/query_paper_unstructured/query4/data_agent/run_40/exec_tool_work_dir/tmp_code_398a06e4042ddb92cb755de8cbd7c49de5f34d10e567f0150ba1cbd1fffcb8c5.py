code = """import json
import re

# Load papers about physical activity
pa_file = locals()['var_functions.query_db:34']
with open(pa_file, 'r') as f:
    pa_papers = json.load(f)

# Load all citations
cite_file = locals()['var_functions.query_db:4']
with open(cite_file, 'r') as f:
    citations = json.load(f)

print(f"Loaded {len(pa_papers)} papers mentioning physical activity")
print(f"Loaded {len(citations)} citation records")

# Build citation map from title to total citations across all years
citation_map = {}
for rec in citations:
    title = rec['title']
    count = int(rec['total_citations'])
    if title in citation_map:
        citation_map[title] += count
    else:
        citation_map[title] = count

print(f"Total unique papers in citations: {len(citation_map)}")

# Function to extract publication year from text
def extract_publication_year(text):
    # Check first 3000 characters (usually contains header with year)
    text_start = text[:3000]
    
    # Look for explicit year in 20xx format
    year_matches = re.findall(r'\b(20\d{2})\b', text_start)
    for year_str in year_matches:
        year = int(year_str)
        if 2010 <= year <= 2020:
            return year
    
    # Look for conference patterns like CHI '16, UbiComp '16, CSCW '16, etc.
    conferences = ['CHI', 'UbiComp', 'CSCW', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH']
    for conf in conferences:
        # Pattern: CHI '16 or CHI 16 or CHI'16
        pattern = conf + r"\s*['"]\s*16\b|\b" + conf + r"\s+16\b"
        match = re.search(pattern, text_start, re.IGNORECASE)
        if match:
            return 2016
    
    return None

# Find papers from 2016 in physical activity domain
papers_2016 = []

for paper in pa_papers:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    # Skip if not in citation database
    if title not in citation_map:
        continue
    
    # Extract year
    year = extract_publication_year(text)
    
    if year == 2016:
        papers_2016.append({
            'title': title,
            'year': year,
            'total_citations': citation_map[title]
        })

# Sort by citation count descending
papers_2016.sort(key=lambda x: x['total_citations'], reverse=True)

print(f"\nFound {len(papers_2016)} papers from 2016 in physical activity domain:")
for paper in papers_2016:
    print(f"- {paper['title']}")
    print(f"  Total Citations: {paper['total_citations']}")
    print()

# Output as JSON
result = json.dumps(papers_2016, indent=2)
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:4': 'file_storage/functions.query_db:4.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': [{'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach'}, {'title': 'Fine-grained Sharing of Sensed Physical Activity: A Value Sensitive Approach'}, {'title': 'Personalization Revisited: A Reflective Approach Helps People Better Personalize Health Services and Motivates Them to Increase Physical Activity'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'Scaffolding for an OLM for Long-Term Physical Activity Goals'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'TastyBeats: Designing Palatable Representations of Physical Activity'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices'}, {'title': 'Understanding Physical Activity Through 3D Printed Material Artifacts'}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': "Monitoring Children's Physical Activity and Sleep: A Study of Surveillance and Information Disclosure"}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'A Spark of Activity: Exploring Informative Art As Visualization for Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'SweatAtoms: Materializing Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Using Context to Reveal Factors That Affect Physical Activity'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions'}, {'title': 'Move into Another World of Happy: Insights for Designing Affect-based Physical Activity Interventions'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}, {'title': 'Low Sampling Rate for Physical Activity Recognition'}], 'var_functions.execute_python:24': [], 'var_functions.execute_python:30': [{'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'year': 2016, 'total_citations': 636}, {'title': 'Charting Design Preferences on Wellness Wearables', 'year': 2016, 'total_citations': 269}], 'var_functions.query_db:32': 'file_storage/functions.query_db:32.json', 'var_functions.query_db:34': 'file_storage/functions.query_db:34.json', 'var_functions.execute_python:42': [], 'var_functions.execute_python:46': [], 'var_functions.execute_python:52': [], 'var_functions.execute_python:56': [], 'var_functions.query_db:58': 'file_storage/functions.query_db:58.json'}

exec(code, env_args)
