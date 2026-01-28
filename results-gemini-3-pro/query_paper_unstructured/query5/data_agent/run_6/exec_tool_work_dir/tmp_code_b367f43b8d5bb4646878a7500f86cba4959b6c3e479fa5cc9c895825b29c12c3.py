code = """import json

with open(locals()['var_function-call-9485982252767693581'], 'r') as f:
    citations = json.load(f)

filenames = [c['title'] + ".txt" for c in citations]

# Split into 2 batches
mid = len(filenames) // 2
batch1 = filenames[:mid]
batch2 = filenames[mid:]

q1 = {
    "collection": "paper_docs",
    "filter": {"filename": {"$in": batch1}},
    "projection": {"filename": 1, "text": 1}
}
q2 = {
    "collection": "paper_docs",
    "filter": {"filename": {"$in": batch2}},
    "projection": {"filename": 1, "text": 1}
}

print("__RESULT__:")
print(json.dumps([q1, q2]))"""

env_args = {'var_function-call-9485982252767693581': 'file_storage/function-call-9485982252767693581.json', 'var_function-call-9485982252767692568': 'file_storage/function-call-9485982252767692568.json', 'var_function-call-2245160326568444986': 188, 'var_function-call-11048170535639833603': 'file_storage/function-call-11048170535639833603.json', 'var_function-call-18114231173969465501': 'file_storage/function-call-18114231173969465501.json', 'var_function-call-12581163801840341244': 0, 'var_function-call-11683251788560511537': {'common_titles_count': 4, 'samples': [{'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'snippet': 'ArmSleeve: a Patient Monitoring System to Support \nOccupational Therapists in Stroke Rehabilitation \nBernd Ploderer1,2, Justin Fong1,3, Anusha Withana1,4, Marlena Klaic1,5, Siddharth Nair1, \nVincent Crocher1,3, Frank Vetere1, Suranga Nanayakkara1,4 \n1Microsoft Research Centre for SocialNUI, The University of Melbourne, Australia \n2Queensland University of Technology, Brisbane, Australia \n3Department of Mechanical Engineering, The University of Melbourne, Australia \n4Augmented Human Lab, Singapor'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'snippet': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'snippet': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-'}, {'title': 'A Lived Informatics Model of Personal Informatics', 'snippet': "UBICOMP '15, SEPTEMBER 7–11, 2015, OSAKA, JAPAN\n\nA Lived Informatics Model of Personal Informatics \n\nDaniel A. Epstein1, An Ping2, James Fogarty1, Sean A. Munson2 \n1Computer Science & Engineering, 2Human Centered Design & Engineering \nDUB Group, University of Washington \n{depstein, jfogarty}@cs.washington.edu, {anping, smunson}@uw.edu \n\nABSTRACT \nCurrent  models  of  how  people  use  personal  informatics \nsystems are largely based in behavior change goals. They do \nnot  adequately  characteriz"}]}}

exec(code, env_args)
