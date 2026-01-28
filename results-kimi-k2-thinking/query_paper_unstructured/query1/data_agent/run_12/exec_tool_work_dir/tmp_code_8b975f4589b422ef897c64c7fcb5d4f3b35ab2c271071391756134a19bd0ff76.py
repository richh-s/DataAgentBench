code = """import json

# Load paper documents data
paper_docs_data = locals()['var_functions.query_db:18']
if isinstance(paper_docs_data, str):
    with open(paper_docs_data, 'r') as f:
        paper_docs = json.load(f)
else:
    paper_docs = paper_docs_data

# Load citations data
citations_data = locals()['var_functions.query_db:8']
if isinstance(citations_data, str):
    with open(citations_data, 'r') as f:
        citations = json.load(f)
else:
    citations = citations_data

# Process paper documents to identify food papers
print("Processing paper documents...")
domain_keywords = ['food', 'nutrition', 'diet', 'eating', 'meal', 'calorie']

food_papers = []
paper_lookup = {}

for doc in paper_docs:
    filename = doc.get('filename', '')
    text = doc.get('text', '')
    
    # Extract title from filename
    title = filename.replace('.txt', '') if filename else ''
    
    # Check if paper is in food domain
    text_lower = text.lower()
    is_food_paper = any(keyword in text_lower for keyword in domain_keywords)
    
    if is_food_paper:
        food_papers.append(title)
        
    paper_lookup[title] = {
        'filename': filename,
        'is_food': is_food_paper
    }

print(f"Found {len(food_papers)} food domain papers:")
for fp in food_papers:
    print(f"  - {fp}")

# Find citations for food papers
food_citations = []

citations_processed = []
for cit in citations:
    cit_title = cit.get('title', '')
    cit_count = int(cit.get('citation_count', 0))
    cit_year = int(cit.get('citation_year', 0))
    
    citations_processed.append({
        'title': cit_title,
        'count': cit_count,
        'year': cit_year
    })
    
    # Check if this citation belongs to a food paper
    for food_title in food_papers:
        if food_title.lower() == cit_title.lower():
            food_citations.append({
                'title': food_title,
                'count': cit_count,
                'year': cit_year
            })
            print(f"  Found citation: {food_title} ({cit_year}): {cit_count}")

# Calculate total citations for food papers
total_citations = sum(c['count'] for c in food_citations)

print('__RESULT__:')
print(json.dumps({
    'food_papers': food_papers,
    'food_citations': food_citations,
    'total_food_citations': total_citations,
    'total_citation_records': len(citations_processed)
}))"""

env_args = {'var_functions.list_db:0': ['paper_docs'], 'var_functions.list_db:2': ['Citations', 'sqlite_sequence'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.execute_python:10': 'file_storage/functions.execute_python:10.json', 'var_functions.execute_python:12': {'papers_processed': 5, 'citations_processed': 1405, 'sample_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'domains': ['food', 'eating', 'meal', 'calorie', 'physical activity', 'exercise', 'fitness', 'mental', 'finances', 'location', 'chronic'], 'text': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characterize  the  integration  of  self-tracking \ninto  everyday  life  by  people  with  varying  goals.  We  build \nupon  prior  work  by  embracing  the  perspective  of  lived \ninformatics to propose a new model of personal informatics. \nWe examine how lived informatics manifests in the habits of \nself-trackers across a variety of domains, first by surveying \n105, 99, and 83 past and present trackers of physical activity, \nfinances, and location and then by interviewing 22 trackers \nregarding their li"}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'domains': ['food', 'eating', 'meal', 'calorie', 'physical activity', 'exercise', 'sleep', 'finances', 'productivity', 'location', 'diabetes'], 'text': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that users experience \nusing  these  systems,  and  no  guidance  for  making  these \nsystems  more  effective.  To  address  this,  we  conducted \nsurveys and interviews with people who collect and reflect \non  personal  information.  We  derived  a  stage-based  model \nof  personal  informatics  systems  composed  of  five  stages  \n(preparation, collection, integration, reflection, and action) \nand  identified  barriers  in  each  of  the  stages.  These  stages \nhave  four  essential  properties:  b'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'domains': ['eating', 'physical activity', 'exercise', 'sleep', 'mental', 'social interactions'], 'text': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-tracking data can motivate the user towards\nconstructive self-reﬂection. One powerful form of narrative\nthat engages audience across various culture and age groups\nis animated movies. We collected a week of self-reported\nmood and behavior data from each user and created in Unity a\npersonalized animation based on their data. We evaluated the\nimpact of their video in a randomized control trial with a non-\npersonalized animated video as control. We found that person-\nalized videos tend to be more e'}], 'sample_citations': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': 4, 'citation_year': 2017}, {'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': 95, 'citation_year': 2018}, {'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': 32, 'citation_year': 2012}]}, 'var_functions.execute_python:16': {'total_papers': 5, 'food_papers': 3, 'food_paper_titles': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App'], 'total_citations_records': 1405, 'sample_food_papers': [{'title': 'A Lived Informatics Model of Personal Informatics', 'domains': ['food', 'eating', 'meal', 'calorie', 'physical activity', 'exercise', 'fitness', 'mental', 'finances', 'location', 'chronic'], 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'domains': ['food', 'eating', 'meal', 'calorie', 'physical activity', 'exercise', 'sleep', 'finances', 'productivity', 'location', 'diabetes'], 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'domains': ['food', 'diet', 'meal', 'physical activity', 'exercise', 'fitness', 'mental', 'productivity', 'location', 'chronic'], 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}]}, 'var_functions.query_db:18': 'file_storage/functions.query_db:18.json'}

exec(code, env_args)
