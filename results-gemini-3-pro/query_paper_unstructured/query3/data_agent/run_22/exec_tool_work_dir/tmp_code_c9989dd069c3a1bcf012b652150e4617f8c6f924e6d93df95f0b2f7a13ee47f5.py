code = """import json
import re

# Load data
citations_file = locals()['var_function-call-443104723977400605']
with open(citations_file, 'r') as f:
    citations_list = json.load(f)
citation_map = {c['title']: c['total_citation_count'] for c in citations_list}

papers_file = locals()['var_function-call-514374395063839489']
with open(papers_file, 'r') as f:
    papers_list = json.load(f)

def extract_year(text):
    head = text[:2000]
    
    # Full years 20xx
    matches_4d = re.findall(r'20\d\d', head)
    # Abbrev years 'xx (preceded by space or word boundary? "CHI '17")
    matches_2d = re.findall(r"(?:'|\u2019)(\d\d)\b", head) # Handle smart quote too?
    
    candidates = []
    for m in matches_4d:
        y = int(m)
        if 2000 <= y <= 2025:
            candidates.append(y)
            
    for m in matches_2d:
        y = int(m) + 2000
        if 2000 <= y <= 2025:
            candidates.append(y)
            
    if candidates:
        # Heuristic: The earliest year mentioned in header is often the pub year.
        # But sometimes "Copyright 2015 ACM".
        # Sometimes "References ... 2014".
        # Header usually comes first.
        # Let's take the first candidate found?
        # But re.findall returns in order.
        return candidates[0] 
    return None

def is_empirical(text):
    # Check for "empirical" keyword
    return "empirical" in text.lower()

results = []

for p in papers_list:
    title = p['filename'].replace('.txt', '')
    text = p['text']
    
    year = extract_year(text)
    empirical = is_empirical(text)
    
    if year and year > 2016 and empirical:
        count = citation_map.get(title, 0)
        results.append({"title": title, "total_citation_count": count})

# Output
print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-17048581051396880588': 'file_storage/function-call-17048581051396880588.json', 'var_function-call-1195878532623649544': ['paper_docs'], 'var_function-call-5496104119501985979': ['Citations', 'sqlite_sequence'], 'var_function-call-6413197713220877249': 'file_storage/function-call-6413197713220877249.json', 'var_function-call-16265840314316561750': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}], 'var_function-call-1389970747681226185': {'start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characterize  the  integration  of  self-tracking \ninto  everyday  life  by  people  with  varying  goals.  We  build \nupon  prior  work  by  embracing  the  perspective  of  lived \ninformatics to propose a new model of personal informatics. \nWe examine how lived informatics manifests in the habits of \nself-trackers across a variety of domains, first by surveying \n105, 99, and 83 past and present trackers of physical activity, \nfinances, and location and then by interviewing 22 trackers \nregarding their li", 'end': '83. \n\n37.  Smith, I., Consolvo, S., Lamarca, A., Hightower, J., \nScott, J., Sohn, T., Hughes, J., Iachello, G., and \nAbowd, G.D. Social Disclosure of Place: From \nLocation Technology to Communication Practices. \nPervasive 2005, 134-151. \n\n38.  Tang, K.P., Lin, J., Hong, J.I., Siewiorek, D.P., and \n\nSadeh, N. Rethinking Location Sharing: Exploring the \nImplications of Social-Driven vs. Purpose-Driven \nLocation Sharing. UbiComp 2010, 85-94. \n\n39.  Thomaz, E., Zhang, C., Essa, I., and Abowd, G.D. \n\nInferring Meal Eating Activities in Real World Settings \nfrom Ambient Sounds: A Feasibility Study. IUI 2015, \n427-431. \n\n40.  Toscos, T., Faber, A., Connelly, K., and Upoma, A.M. \n\nEncouraging Physical Activity in Teens: Can \nTechnology Help Reduce Barriers to Physical Activity \nin Adolescent Girls? PervasiveHealth 2008, 218-221. \n41.  Whooley, M., Gray, K., Ploderer, B., and Gray, K. On \n\nthe Integration of Self-tracking Data amongst \nQuantified Self Members. HCI 2014, 151-160.  \n\n742\n\n \n \n \n\x0c', 'len': 68339, 'has_empirical': False, 'has_contribution': True}, 'var_function-call-3264625079859679633': 'file_storage/function-call-3264625079859679633.json', 'var_function-call-443104723977400605': 'file_storage/function-call-443104723977400605.json', 'var_function-call-14778214612961354028': [], 'var_function-call-240669036982725001': {'cnt_year_gt_2016': 0, 'cnt_empirical': 48, 'cnt_both': 0, 'debug_list': [{'title': 'A Lived Informatics Model of Personal Informatics', 'year': None, 'empirical': False}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'year': None, 'empirical': False}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'year': None, 'empirical': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'year': None, 'empirical': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'year': None, 'empirical': False}, {'title': 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'year': None, 'empirical': True}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'year': None, 'empirical': False}, {'title': 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', 'year': None, 'empirical': False}, {'title': "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'year': None, 'empirical': False}, {'title': 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone', 'year': None, 'empirical': False}], 'total_papers': 99}, 'var_function-call-514374395063839489': 'file_storage/function-call-514374395063839489.json'}

exec(code, env_args)
