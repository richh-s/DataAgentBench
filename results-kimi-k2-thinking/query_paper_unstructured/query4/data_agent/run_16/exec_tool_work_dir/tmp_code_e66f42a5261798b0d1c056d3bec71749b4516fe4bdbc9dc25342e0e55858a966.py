code = """import json
import re

# Load paper documents
with open(locals()['var_functions.query_db:2'], 'r') as f:
    paper_docs = json.load(f)

# Load citations data
with open(locals()['var_functions.query_db:15'], 'r') as f:
    citations_data = json.load(f)

print('Papers loaded:', len(paper_docs))
print('Citation records loaded:', len(citations_data))

# Create citations index by title
citations_index = {}
for cite in citations_data:
    title = cite['title']
    year = int(cite['citation_year'])
    count = int(cite['citation_count'])
    
    if title not in citations_index:
        citations_index[title] = {}
    citations_index[title][year] = count

# Extract 2016 papers and identify those in physical activity domain
papers_2016_physical_activity = []

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check for 2016 publication year
    has_2016 = '2016' in text
    
    # Broader domain detection for physical activity
    text_lower = text.lower()
    domain_keywords = [
        'physical activity', 'fitness', 'exercise', 'walking', 'running', 
        'steps', 'step count', 'active', 'workout', 'wearable', 'wearables',
        'activity tracking', 'activity tracker', 'sedentary', 'calories burned',
        'heart rate', 'physiological', 'health monitoring', 'health tracking'
    ]
    
    domain_score = sum(1 for keyword in domain_keywords if keyword in text_lower)
    is_physical_activity = 'physical activity' in text_lower or 'fitness' in text_lower or domain_score >= 2
    
    if has_2016 and is_physical_activity:
        # Check if this paper has citations
        if title in citations_index:
            papers_2016_physical_activity.append({
                'title': title,
                'citations_index': citations_index[title]
            })
        else:
            # Check for partial title match in citations
            for cite_title in citations_index.keys():
                if title.lower() in cite_title.lower() or cite_title.lower() in title.lower():
                    papers_2016_physical_activity.append({
                        'title': title,
                        'citation_title': cite_title,
                        'citations_index': citations_index[cite_title]
                    })
                    break

print('\nFound', len(papers_2016_physical_activity), '2016 physical activity papers with citations')

# Calculate total citations for each paper
results = []
for paper in papers_2016_physical_activity:
    total_citations = sum(paper['citations_index'].values())
    results.append({
        'title': paper['title'],
        'total_citation_count': total_citations,
        'yearly_breakdown': paper['citations_index']
    })
    print(f"\n{paper['title']}")
    print(f"  Total citations: {total_citations}")
    print(f"  Yearly breakdown: {paper['citations_index']}")

print('\n__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.execute_python:8': [], 'var_functions.list_db:10': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:12': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}, {'id': '6', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '95', 'citation_year': '2015'}, {'id': '7', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '14', 'citation_year': '2016'}, {'id': '8', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '12', 'citation_year': '2012'}, {'id': '9', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '76', 'citation_year': '2013'}, {'id': '10', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '55', 'citation_year': '2014'}], 'var_functions.query_db:15': 'file_storage/functions.query_db:15.json', 'var_functions.execute_python:18': [], 'var_functions.execute_python:24': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App']}

exec(code, env_args)
