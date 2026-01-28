code = """import json
import re

# Load MongoDB results
mongo_file_path = var_functions.query_db:2
with open(mongo_file_path, 'r') as f:
    paper_docs = json.load(f)

# Load citations data
citations_file_path = var_functions.query_db:5
with open(citations_file_path, 'r') as f:
    citations = json.load(f)

print(f"Total papers mentioning 'physical activity': {len(paper_docs)}")
print(f"Total citation records: {len(citations)}")

# Process paper documents to extract info
papers = []

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename (remove .txt extension)
    title = filename.replace('.txt', '') if filename else ''
    
    # Extract year from text
    # Look for patterns like: 2016, '16, conferences with years
    year = None
    
    # Pattern 1: Direct year mention 2016
    year_match = re.search(r'\b2016\b', text)
    if year_match:
        year = 2016
    
    # Pattern 2: Conference year format like CHI '16, Ubicomp '16, etc.
    if not year:
        conf_year_match = re.search(r"[A-Z]+\s+'(16)\b", text)
        if conf_year_match:
            year = 2016
    
    # Pattern 3: Look for common HCI conference patterns
    if not year:
        # Look for 2016 in venue mentions
        if '2016' in text[:1000]:  # Check first 1000 characters
            year = 2016
    
    # Extract domain - check if 'physical activity' is mentioned (case-insensitive)
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

print(f"Papers from 2016 in physical activity domain: {len(papers_2016_pa)}")

if papers_2016_pa:
    print("\nPapers found:")
    for p in papers_2016_pa:
        print(f"- {p['title']}")

# Convert citations to DataFrame for easier processing
import pandas as pd

citations_df = pd.DataFrame(citations)
citations_df['citation_count'] = citations_df['citation_count'].astype(int)
citations_df['citation_year'] = citations_df['citation_year'].astype(int)

print(f"\nCitation records for 2016 papers:")
print(citations_df.head())

# Initialize result list
result_list = []

# For each 2016 physical activity paper, find its citations
for paper in papers_2016_pa:
    paper_title = paper['title']
    
    # Find matching citations (exact title match)
    paper_citations = citations_df[citations_df['title'] == paper_title]
    
    if not paper_citations.empty:
        total_citations = paper_citations['citation_count'].sum()
        result_list.append({
            'title': paper_title,
            'total_citation_count': int(total_citations),
            'citation_years': paper_citations['citation_year'].tolist()
        })
        print(f"Found {total_citations} total citations for '{paper_title}'")
    else:
        # Try to find citations with similar titles (case-insensitive)
        paper_citations = citations_df[
            citations_df['title'].str.lower() == paper_title.lower()
        ]
        if not paper_citations.empty:
            total_citations = paper_citations['citation_count'].sum()
            result_list.append({
                'title': paper_title,
                'total_citation_count': int(total_citations),
                'citation_years': paper_citations['citation_year'].tolist()
            })
            print(f"Found {total_citations} total citations (case-insensitive) for '{paper_title}'")

# If no results found, let's investigate why
if not result_list:
    print("\nNo citations found for 2016 physical activity papers.")
    print("\nInvestigating...")
    
    # Check some sample titles from our papers
    sample_titles = [p['title'] for p in papers_2016_pa[:5]]
    print(f"Sample paper titles: {sample_titles}")
    
    # Check some citation titles
    sample_citation_titles = citations_df['title'].head(10).tolist()
    print(f"Sample citation titles: {sample_citation_titles}")
    
    # Let's try to find any matching titles
    matching_titles = []
    for paper in papers_2016_pa:
        paper_title = paper['title']
        matches = citations_df[citations_df['title'].str.contains(re.escape(paper_title[:20]), case=False, na=False)]
        if not matches.empty:
            matching_titles.append((paper_title, matches['title'].iloc[0]))
    
    print(f"Potential matches found: {len(matching_titles)}")
    for p_title, c_title in matching_titles[:5]:
        print(f"  '{p_title}' -> '{c_title}'")

# Print the final result
print("\n" + "="*50)
print("FINAL RESULTS:")
for item in result_list:
    print(f"Title: {item['title']}")
    print(f"Total Citation Count: {item['total_citation_count']}")
    print("-" * 30)

# Format for JSON output
if result_list:
    output = json.dumps(result_list, indent=2)
else:
    output = json.dumps([], indent=2)

print("__RESULT__:")
print(output)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
