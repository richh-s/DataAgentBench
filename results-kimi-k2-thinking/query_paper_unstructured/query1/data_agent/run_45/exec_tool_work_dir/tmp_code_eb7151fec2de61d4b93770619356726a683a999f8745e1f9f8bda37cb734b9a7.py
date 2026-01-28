code = """import json
import pandas as pd

# Read paper docs data from file
with open('var_functions.query_db:2', 'r') as f:
    paper_docs_data = json.load(f)

# Extract title from filename and check for food domain
paper_titles = []
for doc in paper_docs_data:
    filename = doc.get('filename', '')
    # Extract title by removing .txt extension
    title = filename.replace('.txt', '')
    text = doc.get('text', '')
    
    # Check if paper is in food domain (case insensitive)
    is_food_domain = 'food' in text.lower()
    
    paper_titles.append({
        'title': title,
        'is_food_domain': is_food_domain,
        'text_preview': text[:500] if text else ''  # First 500 chars for debugging
    })

# Convert to DataFrame
paper_df = pd.DataFrame(paper_titles)

# Read citations data from file
with open('var_functions.query_db:5', 'r') as f:
    citations_data = json.load(f)

citations_df = pd.DataFrame(citations_data)
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'])

# Join paper data with citations data
citations_df['title'] = citations_df['title']
merged_df = pd.merge(citations_df, paper_df[['title', 'is_food_domain']], on='title')

# Filter for food domain papers and sum citation counts
food_citations = merged_df[merged_df['is_food_domain'] == True]
total_citations = food_citations['citation_count'].sum()

# Also get number of unique food papers
total_food_papers = food_citations['title'].nunique()

# Results summary
result = {
    'total_food_papers': total_food_papers,
    'total_citation_count': int(total_citations),
    'total_food_domain_papers': len(paper_df[paper_df['is_food_domain'] == True])
}

# Let's also preview some food domain papers to ensure we caught the right ones
food_papers_preview = []
for paper in paper_df[paper_df['is_food_domain'] == True].head(3).itertuples():
    food_papers_preview.append({
        'title': paper.title,
        'preview': paper.text_preview[:200]
    })

result['food_papers_preview'] = food_papers_preview

total_citations_str = str(total_citations)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
