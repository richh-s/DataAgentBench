code = """import json
import re
import pandas as pd

# Get file path for paper documents
paper_docs_file = locals()['var_functions.query_db:8']

# Load paper documents
with open(paper_docs_file, 'r') as f:
    paper_docs = json.load(f)

print("Total papers in collection:", len(paper_docs))

# Extract year information systematically
papers_data = []
for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    if not filename or not text:
        continue
    
    title = filename.replace('.txt', '')
    
    # Try multiple methods to extract year
    year = None
    
    # Method 1: Look for explicit year patterns
    year_patterns = [
        r'\b(20(?:11|12|13|14|15|16|17|18|19|20|21|22|23|24|25))\b',
        r'(?:CHI|UbiComp|CSCW|Ubicomp|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH)\s*[\'"](\d{2})[\'"]',
        r'(?:September|October|November|December|January|February|March|April|May|June|July|August)\s+\d{1,2}[^\d]*\b(20\d{2})\b'
    ]
    
    for pattern in year_patterns:
        matches = re.findall(pattern, text[:3000])
        if matches:
            if len(matches[0]) == 2:  # Handle conference year notation
                year_int = 2000 + int(matches[0])
                if 2010 <= year_int <= 2025:
                    year = year_int
                    break
            else:
                year_int = int(matches[0])
                if 2010 <= year_int <= 2025:
                    year = year_int
                    break
    
    # Method 2: Look in filename for year hints
    if not year:
        file_year = re.findall(r'(20\d{2})', filename)
        if file_year and 2010 <= int(file_year[0]) <= 2025:
            year = int(file_year[0])
    
    papers_data.append({'title': title, 'year': year, 'text': text})

df_papers = pd.DataFrame(papers_data)
print("\nPapers by year (excluding None):")
by_year = df_papers['year'].value_counts().sort_index()
print(by_year)

# Search for physical activity papers
pa_papers = []
for paper in papers_data:
    text_lower = paper['text'].lower()
    
    # Very broad physical activity keywords
    pa_keywords = [
        'physical activity', 'fitness', 'exercise', 'walking', 'running', 
        'activity tracker', 'activity tracking', 'step count', 'workout',
        'sedentary', 'movement', 'calorie', 'weight loss', 'sport'
    ]
    
    if any(keyword in text_lower for keyword in pa_keywords):
        pa_papers.append({
            'title': paper['title'],
            'year': paper['year'],
            'has_physical_activity': True
        })

df_pa = pd.DataFrame(pa_papers)
print(f"\nFound {len(df_pa)} papers with physical activity keywords")
print("Year distribution for physical activity papers:")
print(df_pa['year'].value_counts().sort_index())

# Check 2016 specifically
pa_2016 = df_pa[df_pa['year'] == 2016]
print(f"\nPhysical activity papers from 2016: {len(pa_2016)}")

if not pa_2016.empty:
    print("\n2016 physical activity papers:")
    for _, paper in pa_2016.iterrows():
        print(f"  - {paper['title']}")
    
    # Get citation data
    citations_file = locals()['var_functions.query_db:5']
    with open(citations_file, 'r') as f:
        citations = json.load(f)
    
    df_citations = pd.DataFrame(citations)
    df_citations['citation_count'] = df_citations['citation_count'].astype(int)
    df_citation_sums = df_citations.groupby('title')['citation_count'].sum().reset_index()
    df_citation_sums.columns = ['title', 'total_citations']
    
    # Merge with 2016 PA papers
    result = pd.merge(pa_2016, df_citation_sums, on='title', how='left')
    result = result.fillna({'total_citations': 0})
    result['total_citations'] = result['total_citations'].astype(int)
    output = result[['title', 'total_citations']].to_dict('records')
else:
    output = []

# Format and print result
result_json = json.dumps(output, indent=2)
print('__RESULT__:')
print(result_json)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:18': [], 'var_functions.execute_python:24': [], 'var_functions.execute_python:30': []}

exec(code, env_args)
