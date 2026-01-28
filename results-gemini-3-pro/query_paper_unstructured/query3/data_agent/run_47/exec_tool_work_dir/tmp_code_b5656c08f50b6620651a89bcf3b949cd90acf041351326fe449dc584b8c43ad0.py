code = """import json
import re

path_citations = locals()['var_function-call-6302261332534400928']
with open(path_citations, 'r') as f:
    citations_data = json.load(f)

title_citations = {}
for entry in citations_data:
    t = entry['title']
    title_citations[t] = 1 # just existence check for now

path_papers = locals()['var_function-call-6302261332534401433']
with open(path_papers, 'r') as f:
    papers = json.load(f)

debug_info = []

for p in papers[:20]:
    filename = p['filename']
    title = filename.replace('.txt', '')
    text = p['text']
    
    year = None
    # Loose regex for copyright
    match = re.search(r'Copyright.*?20(\d{2})', text[:3000])
    if match:
        year = 2000 + int(match.group(1))
    else:
        # Check specific format seen in sample: UBICOMP '15
        match = re.search(r"'\d{2}", text[:500])
        if match:
            # This is risky, '15 could be anything.
            pass
        
        # Check 4 digit
        match = re.search(r"20[0-2][0-9]", text[:1000])
        if match:
            year = int(match.group(0))

    is_empirical = 'empirical' in text.lower()
    in_citations = title in title_citations
    
    debug_info.append({
        "title": title,
        "year": year,
        "is_empirical": is_empirical,
        "in_citations": in_citations
    })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-10449789667232023992': ['paper_docs'], 'var_function-call-10449789667232022543': 'file_storage/function-call-10449789667232022543.json', 'var_function-call-10449789667232025190': 'file_storage/function-call-10449789667232025190.json', 'var_function-call-18099153275120727410': 'file_storage/function-call-18099153275120727410.json', 'var_function-call-18146542979440941861': ['====================', 'Title: A Lived Informatics Model of Personal Informatics.txt', 'COORD contribution: contributions  through  survey  design  and  participant  interviews.', 'Year (Copyright): 2015', 'Contains empirical: No', '====================', 'Title: A Stage-based Model of Personal Informatics Systems.txt', 'COORD contribution: We  provide  three  main  contributions  in  this  paper:  1)  we', 'Year (Copyright): 2010', 'Contains empirical: No', '====================', 'Title: A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'No contribution keyword found in lines.', 'Year not found via Copyright', 'Contains empirical: Yes', '====================', 'Title: A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'COORD contribution: their  contribution “I like drawing!” (UP4),  some  did not like', 'Year not found via Copyright', 'Contains empirical: Yes', '====================', 'Title: ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'COORD contribution: patient is important, the main contribution of this research is', 'COORD contribution: A  second  contribution  is  offered  through  the  design  of  a', 'Year not found via Copyright', 'Contains empirical: No'], 'var_function-call-6302261332534400928': 'file_storage/function-call-6302261332534400928.json', 'var_function-call-6302261332534401433': 'file_storage/function-call-6302261332534401433.json', 'var_function-call-10306656514989444309': []}

exec(code, env_args)
