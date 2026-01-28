code = """import json
import pandas as pd

# Load citations data for 2018
citations_file = '/Users/Shared/wld9.json'
with open(citations_file, 'r') as f:
    citations_data = json.load(f)

print('Number of 2018 citations loaded:', len(citations_data))

# Load paper documents
papers_file = '/Users/Shared/wld10.json'
with open(papers_file, 'r') as f:
    papers_data = json.load(f)

print('Number of paper documents loaded:', len(papers_data))

# Identify ACM papers
acm_paper_titles = []
for paper in papers_data:
    filename = paper.get('filename', '')
    title = filename.replace('.txt', '') if filename else ''
    text = paper.get('text', '')
    
    # Check if ACM appears in the text (case-insensitive)
    if 'ACM' in text or 'acm' in text:
        acm_paper_titles.append(title)

print('Number of ACM papers identified:', len(acm_paper_titles))
print('Sample ACM papers:', acm_paper_titles[:5])

# Create DataFrame for citations
citations_df = pd.DataFrame(citations_data)

# Filter for ACM papers only
acm_citations = citations_df[citations_df['title'].isin(acm_paper_titles)]
print('Number of 2018 citations for ACM papers:', len(acm_citations))

if len(acm_citations) > 0:
    # Convert citation count to numeric
    acm_citations['citation_count'] = pd.to_numeric(acm_citations['citation_count'])
    
    # Calculate statistics
    avg_citations = acm_citations['citation_count'].mean()
    median_citations = acm_citations['citation_count'].median()
    min_citations = acm_citations['citation_count'].min()
    max_citations = acm_citations['citation_count'].max()
    
    print('Average citations:', avg_citations)
    print('Median citations:', median_citations)
    print('Min citations:', min_citations)
    print('Max citations:', max_citations)
    print('Total ACM papers cited in 2018:', len(acm_citations))
    
    result_dict = {
        'average_citation_count': float(avg_citations),
        'total_papers': len(acm_citations),
        'median': float(median_citations),
        'minimum': int(min_citations),
        'maximum': int(max_citations)
    }
else:
    print('No ACM papers found in 2018 citations')
    result_dict = {'average_citation_count': 0, 'total_papers': 0}

print('__RESULT__:')
print(json.dumps(result_dict))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.list_db:5': ['paper_docs'], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json'}

exec(code, env_args)
