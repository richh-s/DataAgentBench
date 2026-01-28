code = """import json
import pandas as pd

# Load the citations data for 2018
citations_file = '/Users/Shared/var_functions.query_db:12.json'
with open(citations_file, 'r') as f:
    citations_2018 = json.load(f)

# Load the paper documents
papers_file = '/Users/Shared/var_functions.query_db:14.json'
with open(papers_file, 'r') as f:
    papers = json.load(f)

print('Loaded {0} citations for 2018'.format(len(citations_2018)))
print('Loaded {0} paper documents'.format(len(papers)))

# Identify ACM papers from the paper documents
acm_paper_titles = []
acm_papers_info = []

for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    # Check if ACM appears in the text (case-insensitive)
    if 'ACM' in text or 'acm' in text or 'Association for Computing Machinery' in text:
        title = filename.replace('.txt', '') if filename else ''
        acm_paper_titles.append(title)
        acm_papers_info.append({'title': title, 'source': 'ACM'})

print('Found {0} ACM papers'.format(len(acm_paper_titles)))

# Create DataFrame for citations
citations_df = pd.DataFrame(citations_2018)

# Filter citations for ACM papers only
acm_citations = citations_df[citations_df['title'].isin(acm_paper_titles)]

print('Found {0} citations in 2018 for ACM papers'.format(len(acm_citations)))

if len(acm_citations) > 0:
    # Convert citation_count to numeric
    acm_citations['citation_count'] = pd.to_numeric(acm_citations['citation_count'])
    
    # Calculate statistics
    avg_citations = acm_citations['citation_count'].mean()
    median_citations = acm_citations['citation_count'].median()
    min_citations = acm_citations['citation_count'].min()
    max_citations = acm_citations['citation_count'].max()
    
    print('Average citations for ACM papers in 2018: {0:.2f}'.format(avg_citations))
    print('Total ACM papers cited in 2018: {0}'.format(len(acm_citations)))
    print('Median citations: {0}'.format(median_citations))
    print('Min citations: {0}'.format(min_citations))
    print('Max citations: {0}'.format(max_citations))
    
    result = {
        'average_citation_count': float(avg_citations),
        'total_papers': len(acm_citations),
        'median': float(median_citations),
        'minimum': int(min_citations),
        'maximum': int(max_citations)
    }
else:
    print('No ACM papers found in 2018 citations')
    result = {'average_citation_count': 0, 'total_papers': 0, 'message': 'No ACM papers found'}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': ['paper_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:14': 'file_storage/functions.query_db:14.json'}

exec(code, env_args)
