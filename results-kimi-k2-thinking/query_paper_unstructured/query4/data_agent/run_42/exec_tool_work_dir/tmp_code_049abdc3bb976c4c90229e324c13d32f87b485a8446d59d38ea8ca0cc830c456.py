code = """import json
import re

# Load MongoDB results
mongo_file_path = locals()['var_functions.query_db:2']
with open(mongo_file_path, 'r') as f:
    paper_docs = json.load(f)

# Load citations data
citations_file_path = locals()['var_functions.query_db:5']
with open(citations_file_path, 'r') as f:
    citations = json.load(f)

print('Step 1: Data loaded successfully')
print('  - ' + str(len(paper_docs)) + ' papers mentioning physical activity')
print('  - ' + str(len(citations)) + ' citation records')

# Process paper documents to extract title, year, and domain
papers_with_year = []

for idx, doc in enumerate(paper_docs):
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Try multiple patterns to extract year
    year = None
    
    # Pattern 1: Look for year 2016 in first 2000 characters
    if re.search(r'\b2016\b', text[:2000]):
        year = 2016
    
    # Pattern 2: Look for conference format with '16
    if not year and re.search(r"[A-Z][A-Za-z]*\s+'16", text[:2000]):
        year = 2016
    
    # Pattern 3: Look for venue headers with 2016
    if not year and re.search(r'2016\s+Proceedings|Proceedings\s+2016', text[:2000]):
        year = 2016
    
    # Count physical activity mentions to confirm domain
    pa_mentions = len(re.findall(r'physical activity', text, re.IGNORECASE))
    
    papers_with_year.append({
        'index': idx,
        'title': title,
        'year': year,
        'filename': filename,
        'pa_mentions': pa_mentions
    })

# Show all papers and their extracted years
print('\nStep 2: All papers mentioning physical activity:')
for p in papers_with_year:
    year_str = str(p['year']) if p['year'] else 'Unknown'
    print('  ' + str(p['index']+1) + '. Year: ' + year_str + ', Title: ' + p['title'][:60])
    print('     PA mentions: ' + str(p['pa_mentions']))

# Filter for 2016 papers
papers_2016 = [p for p in papers_with_year if p['year'] == 2016]
print('\nStep 3: Found ' + str(len(papers_2016)) + ' papers from 2016')

for p in papers_2016:
    print('  - ' + p['title'])

# Load citations into DataFrame
import pandas as pd

citations_df = pd.DataFrame(citations)
citations_df['citation_count'] = citations_df['citation_count'].astype(int)
citations_df['citation_year'] = citations_df['citation_year'].astype(int)

print('\nStep 4: Processing ' + str(len(citations_df)) + ' citation records')

# Match papers with citations
results = []

# Create a lookup for citations by simplified title
citation_lookup = {}
for _, row in citations_df.iterrows():
    simplified_title = re.sub(r'[^a-zA-Z0-9]', '', str(row['title']).lower().strip())
    if simplified_title:
        if simplified_title not in citation_lookup:
            citation_lookup[simplified_title] = []
        citation_lookup[simplified_title].append({
            'title': row['title'],
            'citation_count': row['citation_count'],
            'citation_year': row['citation_year']
        })

print('  - Created lookup with ' + str(len(citation_lookup)) + ' unique citation titles')

# Try to match each 2016 paper
for paper in papers_2016:
    paper_title = paper['title']
    paper_simplified = re.sub(r'[^a-zA-Z0-9]', '', paper_title.lower().strip())
    
    print('\n  Matching: ' + paper_title[:60])
    print('  Simplified: ' + paper_simplified[:40])
    
    # Try exact simplified match
    if paper_simplified in citation_lookup:
        matching_citations = citation_lookup[paper_simplified]
        total_citations = sum(c['citation_count'] for c in matching_citations)
        results.append({
            'title': paper_title,
            'total_citation_count': total_citations
        })
        print('  FOUND ' + str(total_citations) + ' citations')
    else:
        # Try partial matching
        found = False
        for cit_simplified, cit_list in citation_lookup.items():
            if paper_simplified in cit_simplified or cit_simplified in paper_simplified:
                if len(paper_simplified) > 10:
                    total_citations = sum(c['citation_count'] for c in cit_list)
                    results.append({
                        'title': paper_title,
                        'total_citation_count': total_citations
                    })
                    print('  FOUND ' + str(total_citations) + ' citations (partial match)')
                    found = True
                    break
        
        if not found:
            print('  NO MATCH')

print('\nStep 5: Final results - ' + str(len(results)) + ' papers matched')
for r in results:
    print('  - ' + r['title'] + ': ' + str(r['total_citation_count']) + ' citations')

# Output as JSON
output = json.dumps(results, indent=2)
print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.execute_python:8': []}

exec(code, env_args)
