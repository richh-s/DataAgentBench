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

print('Total papers mentioning physical activity: ' + str(len(paper_docs)))
print('Total citation records: ' + str(len(citations)))

# Process paper documents to extract info
papers = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text - look for 2016
    year = None
    
    # Check if 2016 appears in text
    if re.search(r'\b2016\b', text):
        year = 2016
    
    # Check for conference year format like CHI '16
    if not year and re.search(r"[A-Z]+\s+'16\b", text):
        year = 2016
    
    # Check for 2016 specifically in the first part of text
    if not year and '2016' in text[:2000]:
        year = 2016
    
    # Extract domain - check if physical activity is mentioned (case-insensitive)
    domain_match = re.search(r'physical activity', text, re.IGNORECASE)
    in_physical_activity_domain = domain_match is not None
    
    papers.append({
        'title': title,
        'year': year,
        'in_physical_activity_domain': in_physical_activity_domain,
        'filename': filename
    })

# Filter papers published in 2016 and in physical activity domain
papers_2016_pa = [p for p in papers if p['year'] == 2016 and p['in_physical_activity_domain']]

print('Papers from 2016 in physical activity domain: ' + str(len(papers_2016_pa)))

# For debugging, show some of the papers found
if papers_2016_pa:
    print('Sample papers found:')
    for i, p in enumerate(papers_2016_pa[:5]):
        print(str(i+1) + '. ' + p['title'])

# Convert citations to DataFrame for easier processing
import pandas as pd

citations_df = pd.DataFrame(citations)
citations_df['citation_count'] = citations_df['citation_count'].astype(int)
citations_df['citation_year'] = citations_df['citation_year'].astype(int)

print('Total citation records in database: ' + str(len(citations_df)))

# For debugging, show sample citation titles
print('Sample citation titles:')
for i, title in enumerate(citations_df['title'].head(5)):
    print(str(i+1) + '. ' + str(title))

# Process each 2016 physical activity paper
result_list = []

for paper in papers_2016_pa:
    paper_title = paper['title']
    
    # Find matching citations (exact title match)
    paper_citations = citations_df[citations_df['title'] == paper_title]
    
    if not paper_citations.empty:
        total_citations = paper_citations['citation_count'].sum()
        result_list.append({
            'title': paper_title,
            'total_citation_count': int(total_citations)
        })
        print('EXACT MATCH - Found ' + str(total_citations) + ' citations for: ' + paper_title)
    else:
        # Try case-insensitive match
        paper_citations = citations_df[citations_df['title'].str.lower() == paper_title.lower()]
        if not paper_citations.empty:
            total_citations = paper_citations['citation_count'].sum()
            result_list.append({
                'title': paper_title,
                'total_citation_count': int(total_citations)
            })
            print('CASE-INSENSITIVE MATCH - Found ' + str(total_citations) + ' citations for: ' + paper_title)

# If still no results, try more flexible matching
if not result_list:
    print('NO MATCHES FOUND - Trying flexible matching...')
    
    # Create a mapping of simplified titles
    citation_titles_simplified = {}
    for _, row in citations_df.iterrows():
        simplified = re.sub(r'[^a-zA-Z0-9]', '', str(row['title']).lower())
        citation_titles_simplified[simplified] = row['title']
    
    for paper in papers_2016_pa:
        paper_title = paper['title']
        paper_simplified = re.sub(r'[^a-zA-Z0-9]', '', paper_title.lower())
        
        if paper_simplified in citation_titles_simplified:
            matching_citation_title = citation_titles_simplified[paper_simplified]
            paper_citations = citations_df[citations_df['title'] == matching_citation_title]
            if not paper_citations.empty:
                total_citations = paper_citations['citation_count'].sum()
                result_list.append({
                    'title': paper_title,
                    'total_citation_count': int(total_citations)
                })
                print('FLEXIBLE MATCH - Found ' + str(total_citations) + ' citations for: ' + paper_title)

# Create the final result
if result_list:
    output = json.dumps(result_list, indent=2)
else:
    # If no results found, return empty list with message
    output = json.dumps([], indent=2)

print('__RESULT__:')
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
