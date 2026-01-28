code = """import json
import re

# Get citation data from file
citation_file_path = locals()['var_functions.query_db:16']
with open(citation_file_path, 'r') as f:
    citation_data = json.load(f)

# Get paper documents from file  
paper_file_path = locals()['var_functions.query_db:5']
with open(paper_file_path, 'r') as f:
    paper_docs = json.load(f)

# More robust year extraction
def extract_year_advanced(text):
    patterns = [
        r"20(1[7-9]|[2-9][0-9])",  # Full year 2017-2099
        r"'?(1[7-9]|[2-9][0-9])'?\s*(?:Proceedings|Conference|Paper|ACM|IEEE)",
        r"CHI\s+'?(1[7-9]|[2-9][0-9])",
        r"Ubicomp\s+'?(1[7-9]|[2-9][0-9])",
        r"UbiComp\s+'?(1[7-9]|[2-9][0-9])",
        r"CSCW\s+'?(1[7-9]|[2-9][0-9])",
        r"DIS\s+'?(1[7-9]|[2-9][0-9])",
        r"WWW\s+'?(1[7-9]|[2-9][0-9])",
        r"IUI\s+'?(1[7-9]|[2-9][0-9])",
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            year_str = match.group(1)
            if len(year_str) == 2:
                year = 2000 + int(year_str)
                if 2017 <= year <= 2030:
                    return year
            else:
                year = int(year_str)
                if 2017 <= year <= 2030:
                    return year
    return None

def is_empirical_paper(text, title):
    text_lower = text.lower()
    
    if 'empirical' in text_lower:
        return True
    
    study_keywords = [
        r'\b(study|studies|survey|experiment|evaluation|interview|interviews)\b',
        r'\b(field study|user study|case study|empirical study)\b',
        r'\b(qualitative|quantitative|mixed.method)\b',
        r'\b(participants|subjects|users|respondents)\b',
    ]
    
    for pattern in study_keywords:
        if re.search(pattern, text_lower):
            methodology_indicators = [
                'we conducted', 'we present', 'we report', 'we describe',
                'methodology', 'methods', 'participants', 'results',
                'findings', 'data collection', 'analysis'
            ]
            for indicator in methodology_indicators:
                if indicator in text_lower:
                    return True
    
    empirical_phrases_in_title = [
        'evaluating', 'evaluation', 'study', 'survey', 'experiment',
        'understanding', 'exploring', 'examining', 'investigating',
        'designing and evaluating', 'user study', 'field study'
    ]
    
    title_lower = title.lower()
    for phrase in empirical_phrases_in_title:
        if phrase in title_lower:
            return True
    
    return False

# Create a dictionary of papers with their info
papers_dict = {}
for doc in paper_docs:
    title = doc.get('filename', '').replace('.txt', '')
    text = doc.get('text', '')
    
    year = extract_year_advanced(text)
    is_empirical = is_empirical_paper(text, title)
    
    papers_dict[title] = {
        'year': year,
        'is_empirical': is_empirical,
        'title': title
    }

# Create citation dictionary
citation_dict = {}
for item in citation_data:
    citation_dict[item['title']] = int(item['total_citations'])

# Find empirical papers after 2016 and get their citations
results = []
for title, paper_info in papers_dict.items():
    if paper_info['year'] and paper_info['year'] > 2016 and paper_info['is_empirical']:
        total_citations = citation_dict.get(title, 0)
        results.append({
            'title': title,
            'year': paper_info['year'],
            'total_citations': total_citations
        })

# Sort by citations descending
results.sort(key=lambda x: x['total_citations'], reverse=True)

print('__RESULT__:')
print(json.dumps(results, indent=2))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.query_db:2': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:10': {'empirical_papers_count': 0, 'sample_papers': []}, 'var_functions.execute_python:12': [{'index': 0, 'title': 'A Lived Informatics Model of Personal Informatics', 'preview': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz"}, {'index': 1, 'title': 'A Stage-based Model of Personal Informatics Systems', 'preview': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that use'}, {'index': 2, 'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'preview': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-'}, {'index': 3, 'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'preview': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith'}, {'index': 4, 'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'preview': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The University of Melbourne, Australia \n2Queensland University of Technology, Brisbane, Australia \n3Department of Mechanical Engineering, The University of Melbourne, Australia \n4Augmented Human Lab, Singapor'}], 'var_functions.execute_python:14': {'total_papers': 5, 'empirical_papers_after_2016': 1, 'sample_empirical_papers': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'is_empirical': True}]}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:18': {'all_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2020, 'is_empirical': False, 'text_length': 68339}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 2020, 'is_empirical': False, 'text_length': 63309}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018, 'is_empirical': True, 'text_length': 54376}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019, 'is_empirical': True, 'text_length': 74850}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 2020, 'is_empirical': False, 'text_length': 73461}], 'empirical_papers_after_2016': [{'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 2018}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 2019}]}}

exec(code, env_args)
