code = """import json
import re

citations_path = locals()['var_function-call-10316639782376099170']
with open(citations_path, 'r') as f:
    citations_data = json.load(f)

citation_map = {item['title']: int(item['citation_count']) for item in citations_data}

papers_path = locals()['var_function-call-3655541512535358306']
with open(papers_path, 'r') as f:
    papers_data = json.load(f)

chi_papers = set()
total_citations = 0

# Patterns
# 1. "CHI 'YY" or "CHI 20YY"
# 2. "CHI Conference on Human Factors"
# 3. "Proceedings of the CHI"
# Using case insensitive just in case, though usually caps.
regex = re.compile(r"CHI\s*['\u2019]?\s*\d{2,4}\b|CHI\s+Conference\b|Conference\s+on\s+Human\s+Factors\s+in\s+Computing\s+Systems", re.IGNORECASE)

for p in papers_data:
    text = p.get('text', '')[:2000]
    filename = p.get('filename', '')
    title = filename.replace('.txt', '')
    
    if regex.search(text):
        chi_papers.add(title)

# Calculate citations
count = 0
for title in chi_papers:
    if title in citation_map:
        total_citations += citation_map[title]
        count += 1

print("__RESULT__:")
print(json.dumps({"chi_paper_count": len(chi_papers), "cited_chi_papers": count, "total_citations": total_citations}))"""

env_args = {'var_function-call-10316639782376097408': ['Citations', 'sqlite_sequence'], 'var_function-call-10316639782376098289': ['paper_docs'], 'var_function-call-10316639782376099170': 'file_storage/function-call-10316639782376099170.json', 'var_function-call-10316639782376095955': 'file_storage/function-call-10316639782376095955.json', 'var_function-call-3655541512535358306': 'file_storage/function-call-3655541512535358306.json', 'var_function-call-17554690775413640325': {'total_citations': 0, 'chi_paper_count': 0, 'papers_with_citations': 0, 'sample_titles': []}, 'var_function-call-17909243822308874303': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A Lived Informatics Model of Personal Informatics  ", 'A Stage-Based Model of Personal Informatics Systems  Ian Li1, Anind Dey1, and Jodi Forlizzi1,2  1Hum', 'Fengjiao Peng MIT Media Lab Cambridge, MA, USA fpeng@mit.edu  A Trip to the Moon: Personalized Anima', 'A Wee Bit More Interaction: Designing and Evaluating   an Overactive Bladder App  Ana-Maria Salai   ', 'ArmSleeve: a Patient Monitoring System to Support  Occupational Therapists in Stroke Rehabilitation '], 'var_function-call-16031832592638894853': [], 'var_function-call-4203575224647280671': ['eral Terms  Design, Human Factors   INTRODUCTION AND MOTIVATION  The  ', ' CHI  Conference on Human Factors in Computing Systems Proceedings (CH']}

exec(code, env_args)
