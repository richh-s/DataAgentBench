code = """import json
import re

with open(locals()['var_function-call-4534989108856043984'], 'r') as f:
    paper_docs = json.load(f)

candidates = [
    "A Stage-based Model of Personal Informatics Systems.txt",
    "A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt",
    "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt"
]

results = []

for doc in paper_docs:
    if doc['filename'] in candidates:
        text = doc['text']
        # Search for year patterns
        # Look for "Copyright 20xx" or "20xx" near conference names
        patterns = [
            r"Copyright\s+(20\d{2})",
            r"\u00a9\s*(20\d{2})", # Copyright symbol
            r"CHI\s*'?(\d{2,4})",
            r"UbiComp\s*'?(\d{2,4})",
            r"CSCW\s*'?(\d{2,4})",
            r"DIS\s*'?(\d{2,4})",
            r"Permission.*(20\d{2})"
        ]
        
        found_years = []
        for pat in patterns:
            matches = re.findall(pat, text, re.IGNORECASE)
            found_years.extend(matches)
            
        results.append({
            "filename": doc['filename'],
            "found_years": list(set(found_years)),
            "snippet": text[-1000:].replace(chr(10), " ") # Check end of file too
        })

print("__RESULT__:")
print(json.dumps(results))"""

env_args = {'var_function-call-8115990490355926110': 'file_storage/function-call-8115990490355926110.json', 'var_function-call-15132226113380290757': 'file_storage/function-call-15132226113380290757.json', 'var_function-call-4534989108856043984': 'file_storage/function-call-4534989108856043984.json', 'var_function-call-280795814972665149': 'file_storage/function-call-280795814972665149.json', 'var_function-call-6662066494306016302': [], 'var_function-call-3983899214788075315': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A Lived Informatics Model of Personal Informatics   Daniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2  1Computer Science & Engineering, 2Human Centered Design & Engineering  DUB Group, University of Washington  {depstein, jfogarty}@cs.wash"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'snippet': 'A Stage-Based Model of Personal Informatics Systems  Ian Li1, Anind Dey1, and Jodi Forlizzi1,2  1Human Computer Interaction Institute, 2School of Design  Carnegie Mellon University, Pittsburgh, PA 15213  ianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu   ABSTRACT  People  strive  to  obtain  self-knowled'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'snippet': 'Fengjiao Peng MIT Media Lab Cambridge, MA, USA fpeng@mit.edu  A Trip to the Moon: Personalized Animated Movies for Self-reﬂection Veronica Crista LaBelle MIT Cambridge, MA, USA vlabelle@mit.edu Rosalind W. Picard MIT Media Lab Cambridge, MA, USA picard@media.mit.edu  Emily Christen Yue Harvard Unive'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'snippet': 'A Wee Bit More Interaction: Designing and Evaluating   an Overactive Bladder App  Ana-Maria Salai   Heriot-Watt University   Edinburgh, UK   as152@hw.ac.uk   Lynne Baillie   Heriot-Watt University   Edinburgh, UK   l.baillie@hw.ac.uk  ABSTRACT   Overactive  Bladder  (OAB)  is  a  widespread  conditi'}], 'var_function-call-2007031801828517213': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'year_check': 'Found 2015'}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'year_check': 'Unknown'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'year_check': 'Found 2016: ...ng, François  Guimbetiere, and Tanzeem Choudhury. 2016. EmotionCheck: leveraging bodily signals and ...'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'year_check': 'Found 2016: ...Paul  Dendale,  Kris  Luyten  and  Karin  Coninx. 2016. Back on bike: the BoB mobile cycling app for...'}], 'var_function-call-2350562070890207248': ['A Lived Informatics Model of Personal Informatics.txt', 'A Stage-based Model of Personal Informatics Systems.txt', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'], 'var_function-call-8334145075669477640': 5, 'var_function-call-16121886756264192141': [{'filename': 'A Lived Informatics Model of Personal Informatics.txt', 'has_physical_activity': True, 'header_snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN  A Lived Informatics Model of Personal Informatics   Daniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2  1Computer Science & Engineering, 2Human Centered Design & Engineering  DUB Group, University of Washington  {depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu   ABSTRACT  Current  models  of  how  people  use  personal  informatics  systems are largely based in behavior change goals. They do  not  adequately  characteriz"}, {'filename': 'A Stage-based Model of Personal Informatics Systems.txt', 'has_physical_activity': True, 'header_snippet': 'A Stage-Based Model of Personal Informatics Systems  Ian Li1, Anind Dey1, and Jodi Forlizzi1,2  1Human Computer Interaction Institute, 2School of Design  Carnegie Mellon University, Pittsburgh, PA 15213  ianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu   ABSTRACT  People  strive  to  obtain  self-knowledge.  A  class  of  systems  called  personal  informatics  is  appearing  that  help  people  collect and reflect on personal information. However, there  is no comprehensive list of problems that use'}, {'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'has_physical_activity': True, 'header_snippet': 'Fengjiao Peng MIT Media Lab Cambridge, MA, USA fpeng@mit.edu  A Trip to the Moon: Personalized Animated Movies for Self-reﬂection Veronica Crista LaBelle MIT Cambridge, MA, USA vlabelle@mit.edu Rosalind W. Picard MIT Media Lab Cambridge, MA, USA picard@media.mit.edu  Emily Christen Yue Harvard University Cambridge, MA, USA eyue@college.harvard.edu  ABSTRACT Self-tracking physiological and psychological data poses the challenge of presentation and interpretation. Insightful nar- ratives for self-'}, {'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'has_physical_activity': True, 'header_snippet': 'A Wee Bit More Interaction: Designing and Evaluating   an Overactive Bladder App  Ana-Maria Salai   Heriot-Watt University   Edinburgh, UK   as152@hw.ac.uk   Lynne Baillie   Heriot-Watt University   Edinburgh, UK   l.baillie@hw.ac.uk  ABSTRACT   Overactive  Bladder  (OAB)  is  a  widespread  condition,  affecting  20%  of  the  population.  Even  though  it  is  a  treatable  condition,  people  often  do  not  seek  treatment.  In  this paper, we  describe how we co-designed and evaluated  with'}, {'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'has_physical_activity': False, 'header_snippet': 'ArmSleeve: a Patient Monitoring System to Support  Occupational Therapists in Stroke Rehabilitation  Bernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1,  Vincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4  1Microsoft Research Centre for SocialNUI, The University of Melbourne, Australia  2Queensland University of Technology, Brisbane, Australia  3Department of Mechanical Engineering, The University of Melbourne, Australia  4Augmented Human Lab, Singapor'}]}

exec(code, env_args)
