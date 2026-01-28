code = """import json
import re

# Load the citations data for 2020
citations_file = var_functions.query_db:5
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

# Load the paper documents data
papers_file = var_functions.query_db:8
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

print('Loaded ' + str(len(citations_data)) + ' citations from 2020')
print('Loaded ' + str(len(papers_data)) + ' paper documents')

# Create a dictionary to map paper titles to venues
# Key: paper title (matching citation title), Value: venue
paper_venues = {}

# Common venues to look for
venues = ['CHI', 'Ubicomp', 'CSCW', 'DIS', 'PervasiveHealth', 'WWW', 'IUI', 'OzCHI', 'TEI', 'AH']

for paper in papers_data:
    filename = paper['filename']
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '')
    
    text = paper['text']
    venue_found = None
    
    # Look for venue information in the text
    # Usually appears at the beginning of the paper
    for venue in venues:
        # Check if venue appears in the text (case-insensitive)
        if re.search(r'\b' + venue + r'\b', text, re.IGNORECASE):
            venue_found = venue
            break
    
    paper_venues[title] = venue_found

# Count how many papers have CHI as venue
chi_papers = [title for title, venue in paper_venues.items() if venue == 'CHI']
print('Found ' + str(len(chi_papers)) + ' papers from CHI venue')

# Now join with citations data
total_citations = 0
matched_papers = 0
matched_chi_papers = []

for citation in citations_data:
    citation_title = citation['title']
    citation_count = int(citation['citation_count'])
    
    # Check if this paper is in our paper_venues dictionary
    if citation_title in paper_venues:
        venue = paper_venues[citation_title]
        if venue == 'CHI':
            total_citations += citation_count
            matched_papers += 1
            matched_chi_papers.append({
                'title': citation_title,
                'citations': citation_count
            })

print('Matched ' + str(matched_papers) + ' CHI papers with 2020 citations')
print('Total citations for CHI papers in 2020: ' + str(total_citations))

# Show top 5 CHI papers by citation count
matched_chi_papers_sorted = sorted(matched_chi_papers, key=lambda x: x['citations'], reverse=True)
print('\nTop 5 CHI papers by 2020 citations:')
for i, paper in enumerate(matched_chi_papers_sorted[:5]):
    print(str(i+1) + '. ' + paper['title'] + ': ' + str(paper['citations']) + ' citations')

result = {
    'total_citations_2020': total_citations,
    'num_chi_papers': matched_papers
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '16', 'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': '65', 'citation_year': '2020'}, {'id': '17', 'title': 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'citation_count': '4', 'citation_year': '2020'}, {'id': '27', 'title': 'Why We Use and Abandon Smart Devices', 'citation_count': '36', 'citation_year': '2020'}, {'id': '36', 'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': '98', 'citation_year': '2020'}, {'id': '42', 'title': "I'Ll Be Back: On the Multiple Lives of Users of a Mobile Activity Tracking Application", 'citation_count': '78', 'citation_year': '2020'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
