code = """import json

# Load citations
with open(locals()['var_function-call-15503541887771276820'], 'r') as f:
    citations = json.load(f)

# Map title to citation count
citation_map = {c['title']: int(c['citation_count']) for c in citations}

# Load paper docs
with open(locals()['var_function-call-982611377776759492'], 'r') as f:
    paper_docs = json.load(f)

acm_citation_counts = []

for doc in paper_docs:
    text = doc.get('text', '')
    filename = doc.get('filename', '')
    title = filename.replace('.txt', '')
    
    # Check if ACM
    # Heuristic: 'ACM Classification Keywords' OR 'Copyright ... ACM' OR 'Permission ... ACM'
    # Or just 'ACM' in text? The previous check for 'ACM Classification Keywords' worked for the small sample.
    # I'll use a robust check.
    is_acm = False
    if 'ACM Classification Keywords' in text:
        is_acm = True
    elif 'Copyright' in text and 'ACM' in text:
        # Check if they are close? Or just if both exist?
        # A paper might cite an ACM paper and have Copyright IEEE.
        # But 'Copyright ... ACM' usually appears in the footer.
        # I'll check for "Copyright" followed by "ACM" within some distance, or "ACM" followed by "Copyright"?
        # Actually, let's search for "Permission to make digital ... ACM"
        if "Permission to make digital" in text and "ACM" in text:
            is_acm = True
        elif "Copyright" in text and "ACM" in text:
             # This is a bit weak, but let's try to be specific.
             # "Copyright 20.. ACM"
             # "Copyright (c) 20.. ACM"
             # "Copyright held by the owner/author(s). Publication rights licensed to ACM."
             if "licensed to ACM" in text:
                 is_acm = True
             elif "Copyright" in text and text.find("ACM", text.find("Copyright")) != -1 and text.find("ACM", text.find("Copyright")) - text.find("Copyright") < 50:
                 is_acm = True
             else:
                 # Check if the paper title is in the citation map first to save time? 
                 # No, filtering by ACM first is better logic.
                 pass

    # A simpler heuristic based on the hint "Common sources ... include: 'ACM'"
    # The hint implies we should be able to extract it.
    # If I just check "ACM" in the first 2000 chars, it's probably 99% accurate for this dataset.
    if not is_acm:
        if "ACM" in text[:3000]:
            is_acm = True
    
    if is_acm:
        if title in citation_map:
            count = citation_map[title]
            acm_citation_counts.append(count)

if acm_citation_counts:
    avg = sum(acm_citation_counts) / len(acm_citation_counts)
else:
    avg = 0

print("__RESULT__:")
print(json.dumps({"average": avg, "count": len(acm_citation_counts), "counts": acm_citation_counts}))"""

env_args = {'var_function-call-15503541887771276820': 'file_storage/function-call-15503541887771276820.json', 'var_function-call-11206421856392368221': {'count': 158, 'first_10': ['Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing.txt', 'Sundroid: Solar Radiation Awareness with Smartphones.txt', 'Why We Use and Abandon Smart Devices.txt', 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App.txt', 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set.txt', "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization.txt", 'Reviewing Reflection: On the Use of Reflection in Interactive System Design.txt', 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers.txt', 'Beyond Self-Tracking and Reminders: Designing Smartphone Apps That Support Habit Formation.txt', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection.txt']}, 'var_function-call-7875939014614819259': 'file_storage/function-call-7875939014614819259.json', 'var_function-call-509776034096291468': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}], 'var_function-call-2979635559747287389': 5, 'var_function-call-10712887416649131953': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-4898156154949996726': 'file_storage/function-call-4898156154949996726.json', 'var_function-call-18280883742595085125': {'average': 68.5, 'count': 2, 'titles_found': [['A Lived Informatics Model of Personal Informatics', 50], ['ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 87]]}, 'var_function-call-4463771877841554001': {'A Stage-based Model of Personal Informatics Systems': 'A Stage-Based Model of Personal Informatics Systems \nIan Li1, Anind Dey1, and Jodi Forlizzi1,2 \n1Human Computer Interaction Institute, 2School of Design \nCarnegie Mellon University, Pittsburgh, PA 15213 \nianli@cmu.edu, {anind, forlizzi}@cs.cmu.edu \n\nABSTRACT \nPeople  strive  to  obtain  self-knowledge.  A  class  of  systems \ncalled  personal  informatics  is  appearing  that  help  people \ncollect and reflect on personal information. However, there \nis no comprehensive list of problems that use', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection': 'Fengjiao Peng\nMIT Media Lab\nCambridge, MA, USA\nfpeng@mit.edu\n\nA Trip to the Moon: Personalized Animated Movies for\nSelf-reﬂection\nVeronica Crista LaBelle\nMIT\nCambridge, MA, USA\nvlabelle@mit.edu\nRosalind W. Picard\nMIT Media Lab\nCambridge, MA, USA\npicard@media.mit.edu\n\nEmily Christen Yue\nHarvard University\nCambridge, MA, USA\neyue@college.harvard.edu\n\nABSTRACT\nSelf-tracking physiological and psychological data poses the\nchallenge of presentation and interpretation. Insightful nar-\nratives for self-', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App': 'A Wee Bit More Interaction: Designing and Evaluating  \nan Overactive Bladder App\n\nAna-Maria Salai \n Heriot-Watt University \n Edinburgh, UK \n as152@hw.ac.uk \n\nLynne Baillie \n Heriot-Watt University \n Edinburgh, UK \n l.baillie@hw.ac.uk\n\nABSTRACT \n\nOveractive  Bladder  (OAB)  is  a  widespread  condition, \naffecting  20%  of  the  population.  Even  though  it  is  a \ntreatable  condition,  people  often  do  not  seek  treatment.  In \nthis paper, we  describe how we co-designed and evaluated \nwith'}, 'var_function-call-17264758352766299199': [{'title': 'A Lived Informatics Model of Personal Informatics', 'acm_context': 'Lapsing; Physical Activity; Finances; Location. \n\nACM Classification Keywords \nH.5.m. Information in', 'copyright_context': 'Copyrights  for\ncomponents  of  this  work  owned  by  others  than  ACM  must  be  honored.\nAbstrac'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'acm_context': 'matics, collection, reflection, model, barriers \n\nACM Classification Keywords \nH5.m.  Information  i', 'copyright_context': 'Copyright 2010 ACM  978-1-60558-929-9/10/04....$10.00. \n\nto \n\ninformation  brought  by \n\nbecause  of'}, {'title': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'acm_context': 'rs, compared to non-personalized\ncontrol videos.\n\nACM Classiﬁcation Keywords\nH.5.1. Information inte', 'copyright_context': 'Copyrights for components of this work owned by others than the\nauthor(s) must be honored. Abstracti'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'acm_context': 'ign; \nInterviews; Usability; Overactive Bladder \n\nACM Reference format: \n\nAna-Maria  Salai  and  Lyn', 'copyright_context': 'Copyrights for components of this work owned by others than ACM \nmust  be  honored.  Abstracting  wi'}, {'title': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'acm_context': '; \nstroke rehabilitation; occupational therapy  \n\nACM Classification Keywords \nH.5.m. Information in', 'copyright_context': 'Copyrights for components of this work\nowned by others than the author(s) must be honored. Abstracti'}], 'var_function-call-2069983209624899726': {'found': [], 'missing': [['A Stage-based Model of Personal Informatics Systems', None], ['A Trip to the Moon: Personalized Animated Movies for Self-reflection', None], ['A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', None]]}, 'var_function-call-7835225750576298092': ['paper_docs'], 'var_function-call-1643317973773917978': [{'_id': '694f5530284b10b11dc0a869'}, {'_id': '694f5530284b10b11dc0a86a'}, {'_id': '694f5530284b10b11dc0a86b'}, {'_id': '694f5530284b10b11dc0a86c'}, {'_id': '694f5530284b10b11dc0a86d'}, {'_id': '694f5530284b10b11dc0a86e'}, {'_id': '694f5530284b10b11dc0a86f'}, {'_id': '694f5530284b10b11dc0a870'}, {'_id': '694f5530284b10b11dc0a871'}, {'_id': '694f5530284b10b11dc0a872'}, {'_id': '694f5530284b10b11dc0a873'}, {'_id': '694f5530284b10b11dc0a874'}, {'_id': '694f5530284b10b11dc0a875'}, {'_id': '694f5530284b10b11dc0a876'}, {'_id': '694f5530284b10b11dc0a877'}, {'_id': '694f5530284b10b11dc0a878'}, {'_id': '694f5530284b10b11dc0a879'}, {'_id': '694f5530284b10b11dc0a87a'}, {'_id': '694f5530284b10b11dc0a87b'}, {'_id': '694f5530284b10b11dc0a87c'}, {'_id': '694f5530284b10b11dc0a87d'}, {'_id': '694f5530284b10b11dc0a87e'}, {'_id': '694f5530284b10b11dc0a87f'}, {'_id': '694f5530284b10b11dc0a880'}, {'_id': '694f5530284b10b11dc0a881'}, {'_id': '694f5530284b10b11dc0a882'}, {'_id': '694f5530284b10b11dc0a883'}, {'_id': '694f5530284b10b11dc0a884'}, {'_id': '694f5530284b10b11dc0a885'}, {'_id': '694f5530284b10b11dc0a886'}, {'_id': '694f5530284b10b11dc0a887'}, {'_id': '694f5530284b10b11dc0a888'}, {'_id': '694f5530284b10b11dc0a889'}, {'_id': '694f5530284b10b11dc0a88a'}, {'_id': '694f5530284b10b11dc0a88b'}, {'_id': '694f5530284b10b11dc0a88c'}, {'_id': '694f5530284b10b11dc0a88d'}, {'_id': '694f5530284b10b11dc0a88e'}, {'_id': '694f5530284b10b11dc0a88f'}, {'_id': '694f5530284b10b11dc0a890'}, {'_id': '694f5530284b10b11dc0a891'}, {'_id': '694f5530284b10b11dc0a892'}, {'_id': '694f5530284b10b11dc0a893'}, {'_id': '694f5530284b10b11dc0a894'}, {'_id': '694f5530284b10b11dc0a895'}, {'_id': '694f5530284b10b11dc0a896'}, {'_id': '694f5530284b10b11dc0a897'}, {'_id': '694f5530284b10b11dc0a898'}, {'_id': '694f5530284b10b11dc0a899'}, {'_id': '694f5530284b10b11dc0a89a'}, {'_id': '694f5530284b10b11dc0a89b'}, {'_id': '694f5530284b10b11dc0a89c'}, {'_id': '694f5530284b10b11dc0a89d'}, {'_id': '694f5530284b10b11dc0a89e'}, {'_id': '694f5530284b10b11dc0a89f'}, {'_id': '694f5530284b10b11dc0a8a0'}, {'_id': '694f5530284b10b11dc0a8a1'}, {'_id': '694f5530284b10b11dc0a8a2'}, {'_id': '694f5530284b10b11dc0a8a3'}, {'_id': '694f5530284b10b11dc0a8a4'}, {'_id': '694f5530284b10b11dc0a8a5'}, {'_id': '694f5530284b10b11dc0a8a6'}, {'_id': '694f5530284b10b11dc0a8a7'}, {'_id': '694f5530284b10b11dc0a8a8'}, {'_id': '694f5530284b10b11dc0a8a9'}, {'_id': '694f5530284b10b11dc0a8aa'}, {'_id': '694f5530284b10b11dc0a8ab'}, {'_id': '694f5530284b10b11dc0a8ac'}, {'_id': '694f5530284b10b11dc0a8ad'}, {'_id': '694f5530284b10b11dc0a8ae'}, {'_id': '694f5530284b10b11dc0a8af'}, {'_id': '694f5530284b10b11dc0a8b0'}, {'_id': '694f5530284b10b11dc0a8b1'}, {'_id': '694f5530284b10b11dc0a8b2'}, {'_id': '694f5530284b10b11dc0a8b3'}, {'_id': '694f5530284b10b11dc0a8b4'}, {'_id': '694f5530284b10b11dc0a8b5'}, {'_id': '694f5530284b10b11dc0a8b6'}, {'_id': '694f5530284b10b11dc0a8b7'}, {'_id': '694f5530284b10b11dc0a8b8'}, {'_id': '694f5530284b10b11dc0a8b9'}, {'_id': '694f5530284b10b11dc0a8ba'}, {'_id': '694f5530284b10b11dc0a8bb'}, {'_id': '694f5530284b10b11dc0a8bc'}, {'_id': '694f5530284b10b11dc0a8bd'}, {'_id': '694f5530284b10b11dc0a8be'}, {'_id': '694f5530284b10b11dc0a8bf'}, {'_id': '694f5530284b10b11dc0a8c0'}, {'_id': '694f5530284b10b11dc0a8c1'}, {'_id': '694f5530284b10b11dc0a8c2'}, {'_id': '694f5530284b10b11dc0a8c3'}, {'_id': '694f5530284b10b11dc0a8c4'}, {'_id': '694f5530284b10b11dc0a8c5'}, {'_id': '694f5530284b10b11dc0a8c6'}, {'_id': '694f5530284b10b11dc0a8c7'}, {'_id': '694f5530284b10b11dc0a8c8'}, {'_id': '694f5530284b10b11dc0a8c9'}, {'_id': '694f5530284b10b11dc0a8ca'}, {'_id': '694f5530284b10b11dc0a8cb'}], 'var_function-call-982611377776759492': 'file_storage/function-call-982611377776759492.json'}

exec(code, env_args)
