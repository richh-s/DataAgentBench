code = """import json

# Load citations
with open(locals()['var_function-call-15503541887771276820'], 'r') as f:
    citations = json.load(f)

citation_titles = set(c['title'] for c in citations)

target_titles = [
    "A Stage-based Model of Personal Informatics Systems",
    "A Trip to the Moon: Personalized Animated Movies for Self-reflection",
    "A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App"
]

found = []
missing = []

for t in target_titles:
    if t in citation_titles:
        found.append(t)
    else:
        # Try case insensitive match
        match = None
        for ct in citation_titles:
            if ct.lower() == t.lower():
                match = ct
                break
        missing.append((t, match))

print("__RESULT__:")
print(json.dumps({"found": found, "missing": missing}))"""

env_args = {'var_function-call-15503541887771276820': 'file_storage/function-call-15503541887771276820.json', 'var_function-call-11206421856392368221': {'count': 158, 'first_10': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing.txt', 'Sundroid: Solar Radiation Awareness with Smartphones.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set.txt', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'Reviewing Reflection: On the Use of Reflection in Interactive System Design.txt', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt', 'Beyond Self-Tracking and Reminders: Designing Smartphone Apps That Support Habit Formation.txt', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection.txt']}, 'var_function-call-7875939014614819259': 'file_storage/function-call-7875939014614819259.json', 'var_function-call-509776034096291468': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-2979635559747287389': 5, 'var_function-call-10712887416649131953': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-4898156154949996726': 'file_storage/function-call-4898156154949996726.json', 'var_function-call-18280883742595085125': {'average': 68.5, 'count': 2, 'titles_found': [['A Lived Informatics Model of Personal Informatics', 50], ['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 87]]}, 'var_function-call-4463771877841554001': {'A Stage-based Model of Personal Informatics Systems': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that use', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith'}, 'var_function-call-17264758352766299199': [{'title': 'A Lived Informatics Model of Personal Informatics', 'acm_context': 'Lapsing; Physical Activity; Finances; Location. \n\nACM Classification Keywords \nH.5.m. Information in', 'copyright_context': 'Copyrights  for\ncomponents  of  this  work  owned  by  others  than  ACM  must  be  honored.\nAbstrac'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'acm_context': 'matics, collection, reflection, model, barriers \n\nACM Classification Keywords \nH5.m.  Information  i', 'copyright_context': 'Copyright 2010 ACM  978-1-60558-929-9/10/04....$10.00. \n\nto \n\ninformation  brought  by \n\nbecause  of'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'acm_context': 'rs, compared to non-personalized\ncontrol videos.\n\nACM Classiﬁcation Keywords\nH.5.1. Information inte', 'copyright_context': 'Copyrights for components of this work owned by others than the\nauthor(s) must be honored. Abstracti'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'acm_context': 'ign; \nInterviews; Usability; Overactive Bladder \n\nACM Reference format: \n\nAna-Maria  Salai  and  Lyn', 'copyright_context': 'Copyrights for components of this work owned by others than ACM \nmust  be  honored.  Abstracting  wi'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'acm_context': '; \nstroke rehabilitation; occupational therapy  \n\nACM Classification Keywords \nH.5.m. Information in', 'copyright_context': 'Copyrights for components of this work\nowned by others than the author(s) must be honored. Abstracti'}]}

exec(code, env_args)
