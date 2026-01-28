code = """import json
import re

# Load the paper documents from storage
papers_file = locals()['var_functions.query_db:5']
print('Loading papers from file: ' + str(papers_file))

with open(papers_file, 'r') as f:
    papers = json.load(f)

print('Loaded ' + str(len(papers)) + ' papers')

# Extract structured information from papers - with improved year extraction
paper_info = []

for i, paper in enumerate(papers[:20]):  # Look at first 20 to debug
    # Extract title from filename
    title = paper['filename'].replace('.txt', '')
    
    # Extract year from the text - look for publication year patterns
    text = paper['text']
    
    # Look for year patterns (year numbers around 2010-2029)
    year_match = re.search(r'(?<!\d)(20(1[0-9]|[2-9]\d))(?!\d)', text)
    if year_match:
        year = int(year_match.group())
    else:
        year = None
    
    print(f'Paper {i+1}: {title[:50]}...')
    print(f'  Year found: {year}')
    
    # Determine contribution type
    contribution = []
    
    # Check for empirical keywords
    has_empirical = re.search(r'(?i)\b(survey|questionnaire|interview|field study|field research|user study|empirical|observation|data collection|experiment|case study|participants)\b', text)
    
    # Check for study keywords  
    has_study = re.search(r'(?i)\b(study|studies|investigation|evaluation|assessment|analysis of|examining|exploring)\b', text)
    
    if has_empirical or has_study:
        contribution.append('empirical')
        print(f'  Contribution: EMPERICAL')
    else:
        print(f'  Contribution: other')
    
    paper_info.append({
        'title': title,
        'year': year,
        'contribution': contribution,
    })

# Check all papers without year filter
all_empirical = [p for p in paper_info if 'empirical' in p['contribution']]
print('\nAll empirical papers (first 20 only):')
for p in all_empirical:
    print(f"- {p['title']} ({p['year']})")

# Now check the full dataset
paper_info_full = []
for paper in papers:
    title = paper['filename'].replace('.txt', '')
    text = paper['text']
    
    year_match = re.search(r'(?<!\d)(20(1[0-9]|[2-9]\d))(?!\d)', text)
    year = int(year_match.group()) if year_match else None
    
    contribution = []
    if re.search(r'(?i)\b(survey|questionnaire|interview|field study|field research|user study|empirical|observation|data collection|experiment|case study|participants|study|investigation|evaluation|assessment)\b', text):
        contribution.append('empirical')
    
    paper_info_full.append({
        'title': title,
        'year': year,
        'contribution': contribution,
    })

all_empirical_full = [p for p in paper_info_full if 'empirical' in p['contribution']]
empirical_after_2016 = [p for p in all_empirical_full if p['year'] and p['year'] > 2016]

print('\nFull dataset:')
print('Total papers: ' + str(len(paper_info_full)))
print('All empirical papers: ' + str(len(all_empirical_full)))
print('Empirical papers after 2016: ' + str(len(empirical_after_2016)))

# Show some examples of empirical papers
print('\nSample empirical papers:')
for p in all_empirical_full[:10]:
    print(f"- {p['title']} ({p['year']})")

# Load citation data and check if any titles match
citations_file = locals()['var_functions.query_db:12']
with open(citations_file, 'r') as f:
    citations = json.load(f)

# Get titles from citations
citation_titles = set(c['title'] for c in citations)
paper_titles = set(p['title'] for p in paper_info_full)

print('\nMatching titles between papers and citations:')
matching_titles = citation_titles.intersection(paper_titles)
print(f'Found {len(matching_titles)} matching titles')

if matching_titles:
    print('Sample matching titles:')
    for title in list(matching_titles)[:5]:
        print(f'  - {title}')

out_result = json.dumps({
    'paper_titles': list(paper_titles)[:20],
    'citation_titles': list(citation_titles)[:20],
    'matching_titles': list(matching_titles)[:20],
    'total_papers': len(paper_info_full),
    'total_empirical': len(all_empirical_full),
    'total_empirical_after_2016': len(empirical_after_2016)
})

print('---PRINT FORMAT---')
print('__RESULT__:')
print(out_result)"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.execute_python:20': []}

exec(code, env_args)
