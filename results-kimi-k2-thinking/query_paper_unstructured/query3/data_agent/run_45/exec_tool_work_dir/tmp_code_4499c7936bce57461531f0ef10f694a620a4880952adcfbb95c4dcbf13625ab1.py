code = """import json
import re

# Get the variables using the proper syntax
papers = locals().get('var_functions.query_db:12')
citations_path = locals().get('var_functions.query_db:13')

print('Papers type:', type(papers))
print('Citations path type:', type(citations_path))

# Load citations from file
with open(citations_path) as f:
    citations = json.load(f)

print('Total papers:', len(papers))
print('Total citations:', len(citations))

# Process papers to extract metadata
paper_metadata = []
for paper in papers:
    filename = paper['filename']
    title = filename.replace('.txt', '')
    text = paper['text']
    
    # Extract year (common patterns: 2015 in header, or 2015 in references)
    year = None
    
    # Look for year patterns in the text
    year_matches = re.findall(r'\b(20[0-2][0-9])\b', text)
    if year_matches:
        # Use the earliest year as publication year
        year = min(map(int, year_matches))
    
    # Check if contribution type is empirical (case-insensitive)
    is_empirical = 'empirical' in text.lower()
    
    # Extract venue (common HCI venues)
    venue = None
    venue_patterns = r'(?:CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UIST)\s*[\'"]?\d{2,4}'
    venue_match = re.search(venue_patterns, text, re.IGNORECASE)
    if venue_match:
        venue_name = re.search(r'(CHI|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UIST)', venue_match.group(), re.IGNORECASE)
        venue = venue_name.group().upper() if venue_name else None
    
    paper_metadata.append({
        'title': title,
        'year': year,
        'venue': venue,
        'is_empirical': is_empirical
    })

# Filter empirical papers published after 2016
empirical_papers = [p for p in paper_metadata if p['is_empirical'] and p['year'] and p['year'] > 2016]
print('Empirical papers after 2016:', len(empirical_papers))

# Create title mapping for citations
empirical_titles = {p['title']: p for p in empirical_papers}

# Sum citations for each empirical paper
citation_counts = {}
for citation in citations:
    title = citation['title']
    if title in empirical_titles:
        citation_counts[title] = citation_counts.get(title, 0) + int(citation['citation_count'])

# Add total citations to paper metadata
results = []
for paper in empirical_papers:
    title = paper['title']
    total_citations = citation_counts.get(title, 0)
    results.append({
        'title': title,
        'year': paper['year'],
        'venue': paper['venue'],
        'total_citations': total_citations
    })

# Sort by citation count
df = results
results_sorted = sorted(df, key=lambda x: x['total_citations'], reverse=True)

# Print top 10 for verification
print('Top empirical papers by citations:')
for i, paper in enumerate(results_sorted[:10]):
    print(f"{i+1}. {paper['title']} ({paper['year']}) - {paper['total_citations']} citations")

# Output results
output = {'papers': results_sorted}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:10': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:13': 'file_storage/functions.query_db:13.json'}

exec(code, env_args)
