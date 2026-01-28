code = """import json

with open(locals()['var_function-call-12905975960640330469'], 'r') as f:
    paper_docs = json.load(f)

# Load citations
with open(locals()['var_function-call-1669477486731597489'], 'r') as f:
    citations_data = json.load(f)

citation_map = {}
for entry in citations_data:
    t = entry['title']
    c = int(entry['total_citations']) if entry['total_citations'] else 0
    citation_map[t] = c

results = []
debug_years = []

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check Year
    # Look for 2016 in first 3000 chars
    header = text[:3000]
    is_2016 = '2016' in header
    
    # Check Domain
    has_pa = 'physical activity' in text.lower()
    
    if is_2016 and has_pa:
        count = citation_map.get(title, 0)
        results.append({
            "title": title,
            "citation_count": count
        })
    
    if is_2016:
        debug_years.append({"title": title, "has_pa": has_pa})

# If no results found, checking if any 2016 papers exist
if not results:
    print("__RESULT__:")
    # Print debug info to help understand
    print(json.dumps({"info": "No matches found", "2016_papers": debug_years, "total_docs": len(paper_docs)}))
else:
    print("__RESULT__:")
    print(json.dumps(results))"""

env_args = {'var_function-call-15838279633175563818': 'file_storage/function-call-15838279633175563818.json', 'var_function-call-1669477486731597489': 'file_storage/function-call-1669477486731597489.json', 'var_function-call-1669477486731597534': 'file_storage/function-call-1669477486731597534.json', 'var_function-call-2579067088761269272': [], 'var_function-call-13126364427078448234': 'Debug Complete', 'var_function-call-13483012681038943566': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'has_pa': True, 'has_2016_top': False, 'has_2016_any': False, 'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'has_pa': True, 'has_2016_top': False, 'has_2016_any': False, 'snippet': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Hum'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'has_pa': True, 'has_2016_top': False, 'has_2016_any': True, 'snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Anima'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'has_pa': True, 'has_2016_top': False, 'has_2016_any': True, 'snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n '}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'has_pa': False, 'has_2016_top': False, 'has_2016_any': True, 'snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation '}], 'var_function-call-16857236882397559169': [], 'var_function-call-8662658670787056330': {'count': 1, 'examples': [{'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'context': 'missions from Permissions@acm.org.  DIS 2016, June 04 - 08, 2016, Brisbane, QLD,'}]}, 'var_function-call-13667809118932674388': {'total': 5, 'pa_count': 4, '2016_anywhere_count': 3, 'intersection_count': 2, 'intersection_titles': ['A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt']}, 'var_function-call-4258120896771591873': 'file_storage/function-call-4258120896771591873.json', 'var_function-call-8557991181196192520': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A Lived Informatics Model of Personal Informatics   Daniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2  1Computer Science & Engineering, 2Human Centered Design & Engineering  DUB Group, University of Washington  {depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu   ABSTRACT  Current  models  of  how  people  use  personal  informatics  systems are largely based in behavior change goals. They do  not  adequately  characteriz", 'has_physical_activity': True}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems  Ian Li1, Anind Dey1, and Jodi Forlizzi1,2  1Human Computer Interaction Institute, 2School of Design  Carnegie Mellon University, Pittsburgh, PA 15213  ianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu   ABSTRACT  People  strive  to  obtain  self-knowledge.  A  class  of  systems  called  personal  informatics  is  appearing  that  help  people  collect and reflect on personal information. However, there  is no comprehensive list of problems that use', 'has_physical_activity': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'header_snippet': 'Fengjiao Peng MIT Media Lab Cambridge, MA, USA fpeng@mit.edu  A Trip to the Moon: Personalized Animated Movies for Self-reﬂection Veronica Crista LaBelle MIT Cambridge, MA, USA vlabelle@mit.edu Rosalind W. Picard MIT Media Lab Cambridge, MA, USA picard@media.mit.edu  Emily Christen Yue Harvard University Cambridge, MA, USA eyue@college.harvard.edu  ABSTRACT Self-tracking physiological and psychological data poses the challenge of presentation and interpretation. Insightful nar- ratives for self-', 'has_physical_activity': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating   an Overactive Bladder App  Ana-Maria Salai   Heriot-Watt University   Edinburgh, UK   as152@hw.ac.uk   Lynne Baillie   Heriot-Watt University   Edinburgh, UK   l.baillie@hw.ac.uk  ABSTRACT   Overactive  Bladder  (OAB)  is  a  widespread  condition,  affecting  20%  of  the  population.  Even  though  it  is  a  treatable  condition,  people  often  do  not  seek  treatment.  In  this paper, we  describe how we co-designed and evaluated  with', 'has_physical_activity': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support  Occupational Therapists in Stroke Rehabilitation  Bernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1,  Vincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4  1Microsoft Research Centre for SocialNUI, The University of Melbourne, Australia  2Queensland University of Technology, Brisbane, Australia  3Department of Mechanical Engineering, The University of Melbourne, Australia  4Augmented Human Lab, Singapor', 'has_physical_activity': False}], 'var_function-call-14495050114153052380': 'Done', 'var_function-call-10444946535842023923': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'years': [2015], 'has_pa': True}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'years': [2010], 'has_pa': True}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'years': [2018], 'has_pa': True}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'years': [2018, 2019], 'has_pa': True}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'years': [2016], 'has_pa': False}], 'var_function-call-12905975960640330469': 'file_storage/function-call-12905975960640330469.json'}

exec(code, env_args)
