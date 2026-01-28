code = """import json
import re

# Load paper documents
papers_path = locals()['var_functions.query_db:26']
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Process papers to extract title and year more accurately
processed_papers = []

for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    title = filename.replace('.txt', '').strip() if filename else ''
    
    # Try multiple patterns to extract year
    year = None
    
    # Pattern 1: Look for explicit years 2015-2030
    match1 = re.search(r'\b(201[5-9]|202[0-9]|2030)\b', text)
    if match1:
        year = int(match1.group(1))
    else:
        # Pattern 2: Look for conference notation like UBICOMP '15
        match2 = re.search(r"\b(?:UBICOMP|CHI|CSCW|DIS|UbiComp)\s*'?(\d{2})\b", text)
        if match2:
            year_str = match2.group(1)
            year = int('20' + year_str) if int(year_str) < 50 else int('19' + year_str)
        else:
            # Pattern 3: Look for any 4-digit number starting with 20
            match3 = re.search(r'\b(20\d{2})\b', text)
            if match3:
                year = int(match3.group(1))
    
    # Check if empirical contribution is mentioned
    is_empirical = 'empirical' in text.lower()
    
    # Check venue
    venue_match = re.search(r"\b(CHI|UbiComp|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UBICOMP)\b", text)
    venue = venue_match.group(1) if venue_match else None
    
    processed_papers.append({
        'title': title,
        'year': year,
        'venue': venue,
        'is_empirical': is_empirical,
        'text_length': len(text)
    })

# Load citations
citations_path = locals()['var_functions.query_db:27']
with open(citations_path, 'r') as f:
    citations = json.load(f)

# Sum citations by title
citation_totals = {}
for citation in citations:
    title = citation.get('title', '')
    count_str = str(citation.get('citation_count', '0'))
    count = int(''.join(filter(str.isdigit, count_str)))
    
    if title:
        citation_totals[title] = citation_totals.get(title, 0) + count

# Find empirical papers published after 2016
results = []
for paper in processed_papers:
    if paper['is_empirical'] and paper['year'] and paper['year'] > 2016:
        title = paper['title']
        if title in citation_totals:
            results.append({
                'title': title,
                'publication_year': paper['year'],
                'venue': paper['venue'],
                'total_citations': citation_totals[title]
            })

# Sort by total citations
results.sort(key=lambda x: x['total_citations'], reverse=True)

# Create output
output = {
    'empirical_papers_after_2016': results,
    'total_found': len(results)
}

print('__RESULT__:')
print(json.dumps(output, ensure_ascii=False, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'paper_count': 38, 'citation_count': 38}, 'var_functions.execute_python:22': {'paper_type': "<class 'str'>", 'paper_len': 38, 'citation_type': "<class 'str'>", 'citation_len': 38}, 'var_functions.execute_python:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json', 'var_functions.execute_python:30': [], 'var_functions.execute_python:34': [], 'var_functions.execute_python:36': {'empirical_papers_found': 2, 'empirical_papers': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 'Unknown', 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 'Unknown', 'has_empirical': True}], 'all_years_found': [], 'samples': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'years_found': [], 'preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz", 'has_empirical': False}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'years_found': [], 'preview': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that use', 'has_empirical': False}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_found': [], 'preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-', 'has_empirical': True}]}, 'var_functions.execute_python:38': {'all_empirical_or_dated_papers': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'has_empirical': True}], 'empirical_after_2016_count': 0, 'empirical_after_2016': []}}

exec(code, env_args)
