code = """import json
import re

citations_file = locals()['var_function-call-1796445934379117253']
papers_file = locals()['var_function-call-4873793932197398139']

with open(citations_file, 'r') as f:
    citations = json.load(f)
with open(papers_file, 'r') as f:
    papers = json.load(f)

extracted_info = []

food_titles = []
seen_titles = set()

for paper in papers:
    text = paper['text']
    filename = paper['filename']
    title = filename.replace('.txt', '')
    
    if title in seen_titles:
        continue
    seen_titles.add(title)
    
    found_keyword_section = False
    keywords_snippet = ""
    is_food = False
    
    # Check title first
    if 'food' in title.lower():
        is_food = True
    
    # Check keywords
    pattern = "(Author\\s+Keywords|Index\\s+Terms|Keywords|General\\s+Terms)"
    matches = list(re.finditer(pattern, text[:10000], re.IGNORECASE))
    
    if matches:
        found_keyword_section = True
        for m in matches:
            start = m.end()
            snippet = text[start:start+1000]
            keywords_snippet = snippet
            
            block = snippet.split(chr(10)+chr(10))[0]
            if 'food' in block.lower():
                is_food = True
                break
    
    if is_food:
        food_titles.append(title)
    
    if len(extracted_info) < 5:
        preview = keywords_snippet[:50].replace(chr(10), ' ')
        extracted_info.append({
            "title": title,
            "found_keywords": found_keyword_section,
            "snippet_preview": preview,
            "is_food": is_food
        })

total_citations = 0
found_citations = 0

for cit in citations:
    if cit['title'] in food_titles:
        try:
            count = int(cit['citation_count'])
            total_citations += count
            found_citations += 1
        except:
            pass

print("__RESULT__:")
print(json.dumps({
    "total_citations": total_citations, 
    "food_paper_count": len(food_titles), 
    "matched_citations": found_citations,
    "debug_info": extracted_info
}))"""

env_args = {'var_function-call-2863254843670531231': 'file_storage/function-call-2863254843670531231.json', 'var_function-call-14615599340757939529': ['Citations', 'sqlite_sequence'], 'var_function-call-1796445934379117253': 'file_storage/function-call-1796445934379117253.json', 'var_function-call-4873793932197398139': 'file_storage/function-call-4873793932197398139.json', 'var_function-call-3523739802275053802': {'total_citations': 0, 'food_paper_count': 0, 'matched_citations': 0, 'sample_titles': []}, 'var_function-call-15750728853753372280': ["UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characterize  the  integration  of  self-tracking \ninto  everyday  life  by  people  with  varying  goals.  We  build \nupon  prior  work  by  embracing  the  perspective  of  lived \ninformatics to propose a new model of personal informatics. \nWe examine how lived informatics manifests in the habits of \nself-trackers across a variety of domains, first by surveying \n105, 99, and 83 past and present trackers of physical activity, \nfinances, and location and then by interviewing 22 trackers \nregarding their li", 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that users experience \nusing  these  systems,  and  no  guidance  for  making  these \nsystems  more  effective.  To  address  this,  we  conducted \nsurveys and interviews with people who collect and reflect \non  personal  information.  We  derived  a  stage-based  model \nof  personal  informatics  systems  composed  of  five  stages  \n(preparation, collection, integration, reflection, and action) \nand  identified  barriers  in  each  of  the  stages.  These  stages \nhave  four  essential  properties:  b', 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-tracking data can motivate the user towards\nconstructive self-reﬂection. One powerful form of narrative\nthat engages audience across various culture and age groups\nis animated movies. We collected a week of self-reported\nmood and behavior data from each user and created in Unity a\npersonalized animation based on their data. We evaluated the\nimpact of their video in a randomized control trial with a non-\npersonalized animated video as control. We found that person-\nalized videos tend to be more e']}

exec(code, env_args)
