code = """import json
import pandas as pd

# Load citations for 2018
citations_file = '/Users/Shared/wld12.json'
with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

# Load paper documents
papers_file = '/Users/Shared/wld14.json'
with open(papers_file, 'r') as f:
    papers = json.load(f)

print('Loaded {} citations for 2018'.format(len(citations_2018)))
print('Loaded {} paper documents'.format(len(papers)))

# Identify ACM papers from the paper documents
acm_papers = []
for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Check if ACM appears in the text (case-insensitive)
    if 'ACM' in text or 'acm' in text or 'Association for Computing Machinery' in text:
        title = filename.replace('.txt', '') if filename else ''
        acm_papers.append(title)

print('Found {} ACM papers'.format(len(acm_papers)))

# Create DataFrame for citations and filter for ACM papers
citations_df = pd.DataFrame(citations_2018)
acm_citations = citations_df[citations_df['title'].isin(acm_papers)]

print('Found {} citations in 2018 for ACM papers'.format(len(acm_citations)))

if len(acm_citations) > 0:
    # Convert citation_count to numeric
    acm_citations['citation_count'] = pd.to_numeric(acm_citations['citation_count'])
    
    # Calculate statistics
    avg_citations = acm_citations['citation_count'].mean()
    median_citations = acm_citations['citation_count'].median()
    min_citations = acm_citations['citation_count'].min()
    max_citations = acm_citations['citation_count'].max()
    
    print('Average citations for ACM papers in 2018: {:.2f}'.format(avg_citations))
    print('Total ACM papers cited in 2018: {}'.format(len(acm_citations)))
    
    result = {
        'average_citation_count': float(avg_citations),
        'total_papers': len(acm_citations),
        'median': float(median_citations),
        'minimum': int(min_citations),
        'maximum': int(max_citations)
    }
else:
    print('No ACM papers found in 2018 citations')
    result = {'average_citation_count': 0, 'total_papers': 0}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': ['paper_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
