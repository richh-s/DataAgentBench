code = """import json
import re

# Load the paper documents from storage
papers_file = locals()['var_functions.query_db:5']
print(f'Loading papers from file: {papers_file}')

with open(papers_file, 'r') as f:
    papers = json.load(f)

print(f'Loaded {len(papers)} papers')

# Extract structured information from papers
paper_info = []

for paper in papers:
    # Extract title from filename
    title = paper['filename'].replace('.txt', '')
    
    # Extract year from the text - look for publication year patterns
    text = paper['text']
    
    # Look for year patterns (20XX, 199X, etc.)
    year_match = re.search(r'(?<!\d)(20(1[7-9]|[2-9]\d)|2016)(?!\d)', text)
    if year_match:
        year = int(year_match.group())
    else:
        year = None
    
    # Determine contribution type
    contribution = []
    
    # Check for empirical indicators
    if re.search(r'(?i)\b(survey|questionnaire|interview|field study|field research|user study|empirical|observation|data collection|experiment|case study)\b', text):
        if 'empirical' not in contribution:
            contribution.append('empirical')
    
    # Check for artifact/design indicators
    if re.search(r'(?i)\b(design|prototype|system|tool|artifact|framework|method|methodology|approach|implementation|developed|created|built)\b', text):
        if 'artifact' not in contribution:
            contribution.append('artifact')
    
    # Check for theoretical indicators
    if re.search(r'(?i)\b(theory|theoretical|model|framework|conceptual|analysis|literature review|taxonomy|synthesis)\b', text):
        if 'theoretical' not in contribution:
            contribution.append('theoretical')
    
    # Check for survey indicators (explicit survey type)
    if re.search(r'(?i)\b(survey|literature review|meta.analysis|systematic review|scoping review)\b', text):
        if 'survey' not in contribution:
            contribution.append('survey')
    
    # Default to 'other' if no clear type
    if not contribution:
        contribution = ['other']
    
    # Determine venue and domain (basic extraction)
    venue = []
    if re.search(r'(?i)\b(CHI|Ubicomp|UbiComp|PervasiveHealth|CSCW|DIS|WWW|IUI|OzCHI|TEI|AH)\b', text):
        venue_match = re.search(r'(?i)\b(CHI|Ubicomp|UbiComp|PervasiveHealth|CSCW|DIS|WWW|IUI|OzCHI|TEI|AH)\b', text)
        venue = [venue_match.group().upper()]
    
    domain = []
    if re.search(r'(?i)\b(finances?|money|expense|budget)\b', text):
        domain.append('finances')
    if re.search(r'(?i)\b(activity|fitness|exercise|walking|running|physical|workout|steps)\b', text):
        domain.append('physical activity')
    if re.search(r'(?i)\b(mental|psychology|depression|anxiety|mood|stress|wellbeing|well.being)\b', text):
        domain.append('mental')
    if re.search(r'(?i)\b(food|diet|eating|nutrition|meal)\b', text):
        domain.append('food')
    if re.search(r'(?i)\b(sleep|sleeping|bedtime|rest)\b', text):
        domain.append('sleep')
    if re.search(r'(?i)\b(location|place|geo|spatial|gps|mobility)\b', text):
        domain.append('location')
    
    paper_info.append({
        'title': title,
        'year': year,
        'contribution': contribution,
        'venue': venue,
        'domain': domain
    })

# Filter papers for empirical contribution after 2016
empirical_after_2016 = [p for p in paper_info if 'empirical' in p['contribution'] and p['year'] and p['year'] > 2016]

print(f'Papers extracted: {len(paper_info)}')
print(f'Papers with empirical contribution after 2016: {len(empirical_after_2016)}')

# Load citation data
citations_file = locals()['var_functions.query_db:12']
print(f'Loading citations from file: {citations_file}')

with open(citations_file, 'r') as f:
    citations = json.load(f)

print(f'Loaded {len(citations)} citation records')

# Join paper info with citation data
result = []
for paper in empirical_after_2016:
    title = paper['title']
    # Find all citations for this title
    paper_citations = [c for c in citations if c['title'] == title]
    total_citations = sum(int(c['citation_count']) for c in paper_citations)
    
    if total_citations > 0:
        result.append({
            'title': title,
            'year': paper['year'],
            'total_citation_count': total_citations
        })

# Sort by citation count descending
result.sort(key=lambda x: x['total_citation_count'], reverse=True)

print(f'Found {len(result)} empirical papers after 2016 with citations')

if result:
    print('\nTop papers by citation count:')
    for p in result[:10]:
        print(f"{p['title']} - {p['year']} - {p['total_citation_count']} citations")
else:
    print('\nNo results found')

print('\n---FINAL RESULT---')
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:9': 'file_storage/functions.query_db:9.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json'}

exec(code, env_args)
