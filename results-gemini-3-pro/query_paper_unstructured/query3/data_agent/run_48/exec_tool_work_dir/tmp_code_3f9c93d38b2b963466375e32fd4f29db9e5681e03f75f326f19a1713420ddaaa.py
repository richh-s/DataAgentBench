code = """import json
import re

# Load data
with open(locals()['var_function-call-1645148403302341982'], 'r') as f:
    papers = json.load(f)

with open(locals()['var_function-call-2108608692273987200'], 'r') as f:
    citations = json.load(f)

# Build citation info
citation_info = {}
for c in citations:
    t = c['title']
    try:
        yr = int(c['citation_year'])
        cnt = int(c['citation_count'])
    except:
        continue
        
    if t not in citation_info:
        citation_info[t] = {"total": 0, "min_year": 9999, "years": []}
    
    citation_info[t]["total"] += cnt
    if yr < citation_info[t]["min_year"]:
        citation_info[t]["min_year"] = yr
    citation_info[t]["years"].append(yr)

results = []
debug_skipped = []

for p in papers:
    title = p['filename'].replace('.txt', '')
    text = p.get('text', '')
    
    if title not in citation_info:
        continue
        
    info = citation_info[title]
    min_cite_year = info["min_year"]
    
    # Year Determination
    # Search for year candidates in first 2000 chars
    candidates = re.findall(r'\b(20\d{2})\b', text[:2000])
    # Convert to ints
    candidates = [int(y) for y in candidates]
    
    # Pick the best candidate
    # It should be <= min_cite_year
    # And preferably close to it (0-2 years diff)
    pub_year = 0
    
    valid_candidates = [y for y in candidates if y <= min_cite_year]
    if valid_candidates:
        # Pick the max of valid candidates (closest to citation start)
        pub_year = max(valid_candidates)
    else:
        # Fallback: assume pub_year = min_cite_year - 1
        pub_year = min_cite_year - 1
        
    # Check empirical
    is_empirical = "empirical" in text.lower()
    
    if pub_year > 2016 and is_empirical:
        results.append({
            "title": title,
            "total_citation_count": info["total"]
        })
    else:
        debug_skipped.append({
            "title": title,
            "pub_year": pub_year,
            "is_empirical": is_empirical
        })

# Sort by title
results.sort(key=lambda x: x['title'])

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-3660777886062697260': ['paper_docs'], 'var_function-call-3660777886062696049': [{'id': '1', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '4', 'citation_year': '2017'}, {'id': '2', 'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': '95', 'citation_year': '2018'}, {'id': '3', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '32', 'citation_year': '2012'}, {'id': '4', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '29', 'citation_year': '2013'}, {'id': '5', 'title': 'Understanding My Data, Myself: Supporting Self-reflection with Ubicomp Technologies', 'citation_count': '18', 'citation_year': '2014'}], 'var_function-call-6381855521960426930': 'file_storage/function-call-6381855521960426930.json', 'var_function-call-8113430388473756974': 'file_storage/function-call-8113430388473756974.json', 'var_function-call-2108608692273987200': 'file_storage/function-call-2108608692273987200.json', 'var_function-call-1673231077875897011': {'count': 5, 'first_paper_len': 68339, 'last_1000': '83. \n\n37.  Smith, I., Consolvo, S., Lamarca, A., Hightower, J., \nScott, J., Sohn, T., Hughes, J., Iachello, G., and \nAbowd, G.D. Social Disclosure of Place: From \nLocation Technology to Communication Practices. \nPervasive 2005, 134-151. \n\n38.  Tang, K.P., Lin, J., Hong, J.I., Siewiorek, D.P., and \n\nSadeh, N. Rethinking Location Sharing: Exploring the \nImplications of Social-Driven vs. Purpose-Driven \nLocation Sharing. UbiComp 2010, 85-94. \n\n39.  Thomaz, E., Zhang, C., Essa, I., and Abowd, G.D. \n\nInferring Meal Eating Activities in Real World Settings \nfrom Ambient Sounds: A Feasibility Study. IUI 2015, \n427-431. \n\n40.  Toscos, T., Faber, A., Connelly, K., and Upoma, A.M. \n\nEncouraging Physical Activity in Teens: Can \nTechnology Help Reduce Barriers to Physical Activity \nin Adolescent Girls? PervasiveHealth 2008, 218-221. \n41.  Whooley, M., Gray, K., Ploderer, B., and Gray, K. On \n\nthe Integration of Self-tracking Data amongst \nQuantified Self Members. HCI 2014, 151-160.  \n\n742\n\n \n \n \n\x0c', 'first_500': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz", 'contribution_match': 'Not found', 'year_match': 'Not found'}, 'var_function-call-1645148403302341982': 'file_storage/function-call-1645148403302341982.json', 'var_function-call-16548406697322182489': [], 'var_function-call-4593885512663760110': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': 2015, 'has_empirical': False, 'in_citations': True}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': 0, 'has_empirical': False, 'in_citations': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': 0, 'has_empirical': True, 'in_citations': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': 0, 'has_empirical': True, 'in_citations': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': 0, 'has_empirical': False, 'in_citations': True}], 'var_function-call-18177026415948588008': {'A Stage-based Model of Personal Informatics Systems': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that users experience \nusing  these  systems,  and  no  guidance  for  making  these \nsystems  more  effective.  To  address  this,  we  conducted \nsurveys and interviews with people who collect and reflect \non  personal  information.  We  derived  a  stage-based  model \nof  personal  informatics  systems  composed  of  five  stages  \n(preparation, collection, integration, reflection, and action) \nand  identified  barriers  in  each  of  the  stages.  These  stages \nhave  four  essential  properties:  b', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith  30  stakeholders  (9  medical  professionals  and  21  end-\nusers)  an  OAB  mobile  health  application  that  aims  to \nincrease  adherence  to  self-managed  treatment.  Our  results \nsupport previous research that visualizing progress, setting \ngoals, receiving reminders and feedback  increases  use.  We \ndiscovered  that  games  could  be  used  successfully  as  a \ndistraction technique for urge suppression. Contrary to the \ncurrent research direction, automatically calculated features \n'}}

exec(code, env_args)
