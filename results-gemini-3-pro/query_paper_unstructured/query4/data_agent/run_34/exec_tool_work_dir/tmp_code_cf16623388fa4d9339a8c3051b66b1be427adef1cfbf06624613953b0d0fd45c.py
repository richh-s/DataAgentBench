code = """import json
import pandas as pd
import re

# Load papers from the limit=1000 call
with open(locals()['var_function-call-1758232091178190065'], 'r') as f:
    papers = json.load(f)

# Load citations
with open(locals()['var_function-call-799378154932566157'], 'r') as f:
    citations = json.load(f)
df_citations = pd.DataFrame(citations)
df_citations['citation_count'] = df_citations['citation_count'].astype(int)

# Helper to check domain
def has_domain(text, domain="physical activity"):
    return domain in text.lower()

# Helper to extract year
def get_year(text):
    # Look at the first 1000 chars
    header = text[:1000]
    # Check for 2016
    if "2016" in header:
        return 2016
    # Check for '16 preceeded by conference name or quote
    # e.g. CHI '16, UbiComp '16
    if re.search(r"'\s?16", header):
        return 2016
    
    # Check for 2015 to be safe (if 2015 is there, it's not 2016 unless 2016 is also there and significant)
    # But let's assume if 2016 is present, it's 2016.
    return None

results = []
debug_titles = []

for paper in papers:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    if not has_domain(text):
        continue
        
    year = get_year(text)
    if year == 2016:
        # Sum citations
        paper_citations = df_citations[df_citations['title'] == title]
        total_citations = paper_citations['citation_count'].sum()
        results.append({
            "title": title,
            "total_citations": int(total_citations)
        })
        debug_titles.append(title)

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-18105369077024110272': 'file_storage/function-call-18105369077024110272.json', 'var_function-call-18105369077024110379': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}], 'var_function-call-799378154932565658': 'file_storage/function-call-799378154932565658.json', 'var_function-call-799378154932566157': 'file_storage/function-call-799378154932566157.json', 'var_function-call-16897121803853272035': [], 'var_function-call-14364000523960696617': {'total_papers': 5, 'pa_papers_count': 4, 'y2016_papers_count': 0, 'overlap_count': 0, 'sample_headers': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.wash", 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowled', 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard Unive'], 'paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation'], 'citation_titles': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'Sundroid: Solar Radiation Awareness with Smartphones', 'A Quantified-Self Framework for Exploring and Enhancing Personal Productivity', 'Why We Use and Abandon Smart Devices']}, 'var_function-call-1758232091178190065': 'file_storage/function-call-1758232091178190065.json', 'var_function-call-9913231817077185948': ['paper_docs'], 'var_function-call-14495842085911707909': 'file_storage/function-call-14495842085911707909.json'}

exec(code, env_args)
