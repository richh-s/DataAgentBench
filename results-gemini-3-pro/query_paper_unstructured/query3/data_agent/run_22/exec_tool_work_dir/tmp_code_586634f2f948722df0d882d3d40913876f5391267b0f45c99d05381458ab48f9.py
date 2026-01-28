code = """import json
import re

citations_file = locals()['var_function-call-443104723977400605']
with open(citations_file, 'r') as f:
    citations_list = json.load(f)
citation_map = {c['title']: c['total_citation_count'] for c in citations_list}

papers_file = locals()['var_function-call-3264625079859679633']
with open(papers_file, 'r') as f:
    papers_list = json.load(f)

def extract_year(text):
    head = text[:2000] # Increased range
    matches_4d = re.findall(r'\b(20[12]\d)\b', head)
    matches_2d = re.findall(r"'\s*(1[7-9]|2[0-9])\b", head)
    
    candidates = []
    for m in matches_4d:
        y = int(m)
        if 2000 <= y <= 2025:
            candidates.append(y)
    for m in matches_2d:
        y = int(m) + 2000
        candidates.append(y)
        
    if candidates:
        return min(candidates)
    return None

def is_empirical(text):
    return "empirical" in text.lower()

cnt_year_gt_2016 = 0
cnt_empirical = 0
cnt_both = 0
debug_list = []

for p in papers_list:
    title = p['filename'].replace('.txt', '')
    text = p['text']
    year = extract_year(text)
    empirical = is_empirical(text)
    
    if year and year > 2016:
        cnt_year_gt_2016 += 1
    if empirical:
        cnt_empirical += 1
    if year and year > 2016 and empirical:
        cnt_both += 1
        
    if len(debug_list) < 10:
        debug_list.append({"title": title, "year": year, "empirical": empirical})

print("__RESULT__:")
print(json.dumps({
    "cnt_year_gt_2016": cnt_year_gt_2016,
    "cnt_empirical": cnt_empirical,
    "cnt_both": cnt_both,
    "debug_list": debug_list,
    "total_papers": len(papers_list)
}))"""

env_args = {'var_function-call-17048581051396880588': 'file_storage/function-call-17048581051396880588.json', 'var_function-call-1195878532623649544': ['paper_docs'], 'var_function-call-5496104119501985979': ['Citations', 'sqlite_sequence'], 'var_function-call-6413197713220877249': 'file_storage/function-call-6413197713220877249.json', 'var_function-call-16265840314316561750': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}], 'var_function-call-1389970747681226185': {'start': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characterize  the  integration  of  self-tracking \ninto  everyday  life  by  people  with  varying  goals.  We  build \nupon  prior  work  by  embracing  the  perspective  of  lived \ninformatics to propose a new model of personal informatics. \nWe examine how lived informatics manifests in the habits of \nself-trackers across a variety of domains, first by surveying \n105, 99, and 83 past and present trackers of physical activity, \nfinances, and location and then by interviewing 22 trackers \nregarding their li", 'end': '83. \n\n37.  Smith, I., Consolvo, S., Lamarca, A., Hightower, J., \nScott, J., Sohn, T., Hughes, J., Iachello, G., and \nAbowd, G.D. Social Disclosure of Place: From \nLocation Technology to Communication Practices. \nPervasive 2005, 134-151. \n\n38.  Tang, K.P., Lin, J., Hong, J.I., Siewiorek, D.P., and \n\nSadeh, N. Rethinking Location Sharing: Exploring the \nImplications of Social-Driven vs. Purpose-Driven \nLocation Sharing. UbiComp 2010, 85-94. \n\n39.  Thomaz, E., Zhang, C., Essa, I., and Abowd, G.D. \n\nInferring Meal Eating Activities in Real World Settings \nfrom Ambient Sounds: A Feasibility Study. IUI 2015, \n427-431. \n\n40.  Toscos, T., Faber, A., Connelly, K., and Upoma, A.M. \n\nEncouraging Physical Activity in Teens: Can \nTechnology Help Reduce Barriers to Physical Activity \nin Adolescent Girls? PervasiveHealth 2008, 218-221. \n41.  Whooley, M., Gray, K., Ploderer, B., and Gray, K. On \n\nthe Integration of Self-tracking Data amongst \nQuantified Self Members. HCI 2014, 151-160.  \n\n742\n\n \n \n \n\x0c', 'len': 68339, 'has_empirical': False, 'has_contribution': True}, 'var_function-call-3264625079859679633': 'file_storage/function-call-3264625079859679633.json', 'var_function-call-443104723977400605': 'file_storage/function-call-443104723977400605.json', 'var_function-call-14778214612961354028': []}

exec(code, env_args)
