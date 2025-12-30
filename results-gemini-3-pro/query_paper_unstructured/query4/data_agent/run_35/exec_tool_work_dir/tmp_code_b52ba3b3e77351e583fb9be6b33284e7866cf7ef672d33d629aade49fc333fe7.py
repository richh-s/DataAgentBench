code = """import json

with open(locals()['var_function-call-3854438315303576261'], 'r') as f:
    papers = json.load(f)

matches = []
debug_info = []

for p in papers:
    text = p.get('text', '')
    title = p.get('filename', '').replace('.txt', '')
    
    # Check for Year 2016
    # Look for "2016" in the first 2000 chars.
    # Also look for patterns like "CHI '16", "CHI 2016", "UbiComp '16", "UbiComp 2016"
    
    header = text[:2000]
    
    # Simplest check
    is_2016 = "2016" in header or "'16" in header
    
    # Check Domain
    content_sample = text[:5000].lower() # checking first 5000 chars
    is_domain = "physical activity" in content_sample
    
    if is_2016 and is_domain:
        matches.append(title)
        if len(debug_info) < 5:
            # Find the line with 2016
            year_context = "N/A"
            if "2016" in header:
                idx = header.find("2016")
                year_context = header[max(0, idx-20):min(len(header), idx+20)].replace('\n', ' ')
            elif "'16" in header:
                idx = header.find("'16")
                year_context = header[max(0, idx-20):min(len(header), idx+20)].replace('\n', ' ')
            
            debug_info.append({"title": title, "year_match": year_context})

print("__RESULT__:")
print(json.dumps({"count": len(matches), "examples": debug_info, "matches": matches}))"""

env_args = {'var_function-call-13095614406444105074': 'file_storage/function-call-13095614406444105074.json', 'var_function-call-3854438315303576261': 'file_storage/function-call-3854438315303576261.json', 'var_function-call-9873108506542894991': [], 'var_function-call-15842212210833916133': [{'title': 'A Lived Informatics Model of Personal Informatics.txt', 'excerpt': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz"}, {'title': 'A Stage-based Model of Personal Informatics Systems.txt', 'excerpt': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that use'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'excerpt': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'excerpt': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'excerpt': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The University of Melbourne, Australia \n2Queensland University of Technology, Brisbane, Australia \n3Department of Mechanical Engineering, The University of Melbourne, Australia \n4Augmented Human Lab, Singapor'}]}

exec(code, env_args)
