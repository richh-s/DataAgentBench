code = """import json
import re

# Load Citations
path_citations = locals()['var_function-call-6302261332534400928']
with open(path_citations, 'r') as f:
    citations_data = json.load(f)

# Group citations by title
title_citations = {}
for entry in citations_data:
    t = entry['title']
    c = int(entry['citation_count'])
    if t in title_citations:
        title_citations[t] += c
    else:
        title_citations[t] = c

# Load Papers
path_papers = locals()['var_function-call-6302261332534401433']
with open(path_papers, 'r') as f:
    papers = json.load(f)

results = []

for p in papers:
    filename = p['filename']
    title = filename.replace('.txt', '')
    text = p['text']
    
    # Extract Year
    # Strategy: Look for "Copyright 20xx" first.
    # Then look for "Conference 'yy" -> 20yy
    # Then look for any 20xx in first 1000 chars.
    
    year = None
    
    # 1. Copyright
    match = re.search(r'Copyright (20\d{2})', text[:5000])
    if match:
        year = int(match.group(1))
    else:
        # 2. Conference Year e.g. CHI '18, UbiComp '19
        match = re.search(r"[A-Za-z]+ '(\d{2})", text[:1000])
        if match:
            yy = int(match.group(1))
            year = 2000 + yy
        else:
            # 3. First 20xx in first 500 chars
            match = re.search(r"20[0-2][0-9]", text[:500])
            if match:
                year = int(match.group(0))
    
    # Extract Contribution
    is_empirical = 'empirical' in text.lower()
    
    # Filter
    if year and year > 2016 and is_empirical:
        # Check citations
        # The title from papers might need normalization? 
        # The SQLite title seems to match filename without .txt exactly as per hint.
        
        cit_count = title_citations.get(title, 0)
        results.append({
            "title": title,
            "total_citation_count": cit_count
        })

# Sort by citation count desc for better presentation? Or just return list.
results.sort(key=lambda x: x['total_citation_count'], reverse=True)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-10449789667232023992': ['paper_docs'], 'var_function-call-10449789667232022543': 'file_storage/function-call-10449789667232022543.json', 'var_function-call-10449789667232025190': 'file_storage/function-call-10449789667232025190.json', 'var_function-call-18099153275120727410': 'file_storage/function-call-18099153275120727410.json', 'var_function-call-18146542979440941861': ['====================', 'Title: A Lived Informatics Model of Personal Informatics.txt', 'COORD contribution: contributions  through  survey  design  and  participant  interviews.', 'Year (Copyright): 2015', 'Contains empirical: No', '====================', 'Title: A Stage-based Model of Personal Informatics Systems.txt', 'COORD contribution: We  provide  three  main  contributions  in  this  paper:  1)  we', 'Year (Copyright): 2010', 'Contains empirical: No', '====================', 'Title: A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'No contribution keyword found in lines.', 'Year not found via Copyright', 'Contains empirical: Yes', '====================', 'Title: A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'COORD contribution: their  contribution “I like drawing!” (UP4),  some  did not like', 'Year not found via Copyright', 'Contains empirical: Yes', '====================', 'Title: ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'COORD contribution: patient is important, the main contribution of this research is', 'COORD contribution: A  second  contribution  is  offered  through  the  design  of  a', 'Year not found via Copyright', 'Contains empirical: No'], 'var_function-call-6302261332534400928': 'file_storage/function-call-6302261332534400928.json', 'var_function-call-6302261332534401433': 'file_storage/function-call-6302261332534401433.json'}

exec(code, env_args)
