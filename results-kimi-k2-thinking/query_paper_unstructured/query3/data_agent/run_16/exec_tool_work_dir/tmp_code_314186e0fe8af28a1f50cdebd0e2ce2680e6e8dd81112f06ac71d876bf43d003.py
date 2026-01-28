code = """import json
import re

# Read the full paper documents data
file_path = locals()['var_functions.query_db:5']
with open(file_path, 'r') as f:
    paper_docs = json.load(f)

# Better year extraction
def extract_year_from_text(text):
    # Look for patterns like: CHI '17, Ubicomp '16, 2017, 2018 etc.
    patterns = [
        r"CHI\s+'(\d{2})",  # CHI '17
        r"Ubicomp\s+'(\d{2})",  # Ubicomp '16
        r"CSCW\s+'(\d{2})",  # CSCW '17
        r"UbiComp\s+'(\d{2})",  # UbiComp '15
        r"DIS\s+'(\d{2})",  # DIS '17
        r"WWW\s+'(\d{2})",  # WWW '17
        r"IUI\s+'(\d{2})",  # IUI '17
        r"20(1[7-9]|[2-9][0-9])"  # Full year 2017-2099
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            year_str = match.group(1)
            if len(year_str) == 2:
                # Convert 2-digit year to 4-digit
                year = 2000 + int(year_str)
            else:
                year = int(year_str)
            return year
    return None

# Check for empirical contributions more carefully
def has_empirical_contribution(text):
    # Look for keywords indicating empirical work
    empirical_keywords = [
        'empirical', 'study', 'survey', 'experiment', 'evaluation',
        'interview', 'field study', 'user study', 'case study',
        'qualitative', 'quantitative', 'mixed-methods'
    ]
    
    text_lower = text.lower()
    
    # If explicitly mentions empirical, return True
    if 'empirical' in text_lower:
        return True
    
    # Check for other indicators
    for keyword in empirical_keywords:
        # Look for phrases like "we conducted a study" or "user study"
        if re.search(r'\b' + keyword + r'\b', text_lower):
            # Additional check to avoid false positives
            if 'we conducted' in text_lower or 'we present' in text_lower or 'we report' in text_lower:
                return True
    
    return False

# Process all papers
papers_info = []
for doc in paper_docs:
    title = doc.get('filename', '').replace('.txt', '')
    text = doc.get('text', '')
    
    year = extract_year_from_text(text)
    is_empirical = has_empirical_contribution(text)
    
    if year and year > 2016 and is_empirical:
        papers_info.append({
            'title': title,
            'year': year,
            'is_empirical': True
        })

print('__RESULT__:')
print(json.dumps({
    "total_papers": len(paper_docs),
    "empirical_papers_after_2016": len(papers_info),
    "sample_empirical_papers": papers_info[:10]
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'empirical_papers_count': 0, 'sample_papers': []}, 'var_functions.execute_python:12': [{'index': 0, 'title': 'A Lived Informatics Model of Personal Informatics', 'preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz"}, {'index': 1, 'title': 'A Stage-based Model of Personal Informatics Systems', 'preview': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that use'}, {'index': 2, 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-'}, {'index': 3, 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'preview': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith'}, {'index': 4, 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'preview': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The University of Melbourne, Australia \n2Queensland University of Technology, Brisbane, Australia \n3Department of Mechanical Engineering, The University of Melbourne, Australia \n4Augmented Human Lab, Singapor'}]}

exec(code, env_args)
