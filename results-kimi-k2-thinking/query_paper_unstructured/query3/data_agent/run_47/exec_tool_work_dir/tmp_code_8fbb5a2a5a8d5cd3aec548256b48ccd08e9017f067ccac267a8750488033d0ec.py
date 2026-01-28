code = """import json
import re

# Load paper documents
papers_path = locals()['var_functions.query_db:26']
with open(papers_path, 'r') as f:
    papers = json.load(f)

# Debug: Check all papers more thoroughly
debug_results = []

for paper in papers:
    filename = paper.get('filename', '')
    text = paper.get('text', '')
    
    title = filename.replace('.txt', '').strip()
    text_lower = text.lower()
    
    # Check for empirical in various forms
    has_empirical = 'empirical' in text_lower
    
    # Try to extract year - multiple patterns
    year = None
    
    # Pattern 1: Full year like 2015, 2017, 2020 etc.
    match1 = re.search(r'\b(201[5-9]|202[0-9])\b', text)
    if match1:
        year = int(match1.group(1))
    else:
        # Pattern 2: Conference style with '15,' '16, etc near year
        match2 = re.search(r"\b(?:CHI|UbiComp|Ubicomp|CSCW|DIS|PervasiveHealth|WWW|IUI|OzCHI|TEI|AH|UBICOMP)\s*'?(\d{2})\b.*?\b(201[5-9]|202[0-9])\b", text)
        if match2:
            year = int(match2.group(2))
        else:
            # Pattern 3: Just look for any 4-digit year starting with 20
            match3 = re.search(r'\b(20\d{2})\b', text)
            if match3:
                year = int(match3.group(1))
    
    if has_empirical or year:
        debug_results.append({
            'title': title,
            'year': year,
            'has_empirical': has_empirical
        })

# Filter for empirical papers published after 2016
empirical_papers_after_2016 = [p for p in debug_results if p['has_empirical'] and p['year'] and p['year'] > 2016]

result = {
    'all_empirical_or_dated_papers': debug_results,
    'empirical_after_2016_count': len(empirical_papers_after_2016),
    'empirical_after_2016': empirical_papers_after_2016
}

print('__RESULT__:')
print(json.dumps(result, ensure_ascii=False, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:3': 'file_storage/functions.query_db:3.json', 'var_functions.execute_python:12': {'paper_count': 38, 'citation_count': 38}, 'var_functions.execute_python:22': {'paper_type': "<class 'str'>", 'paper_len': 38, 'citation_type': "<class 'str'>", 'citation_len': 38}, 'var_functions.execute_python:24': [], 'var_functions.query_db:26': 'file_storage/functions.query_db:26.json', 'var_functions.query_db:27': 'file_storage/functions.query_db:27.json', 'var_functions.execute_python:30': [], 'var_functions.execute_python:34': [], 'var_functions.execute_python:36': {'empirical_papers_found': 2, 'empirical_papers': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 'Unknown', 'has_empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 'Unknown', 'has_empirical': True}], 'all_years_found': [], 'samples': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'years_found': [], 'preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz", 'has_empirical': False}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'years_found': [], 'preview': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that use', 'has_empirical': False}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years_found': [], 'preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-', 'has_empirical': True}]}}

exec(code, env_args)
