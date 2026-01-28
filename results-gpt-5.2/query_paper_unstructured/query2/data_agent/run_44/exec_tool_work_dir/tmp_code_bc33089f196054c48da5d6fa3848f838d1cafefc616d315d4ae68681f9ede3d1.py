code = """import json

cit = var_call_zSgHJoaZqQZUtnQcB0mm6NTI
if isinstance(cit, str):
    with open(cit,'r',encoding='utf-8') as f:
        cit=json.load(f)

docs = var_call_qcuB7G45SlVxG9i3bj36sxYz
if isinstance(docs, str):
    with open(docs,'r',encoding='utf-8') as f:
        docs=json.load(f)

acm_titles=set()
for d in docs:
    fn=d.get('filename','')
    title=fn[:-4] if fn.lower().endswith('.txt') else fn
    text=d.get('text') or ''
    if 'ACM' in text:
        acm_titles.add(title)

vals=[]
for r in cit:
    if r.get('title') in acm_titles:
        vals.append(int(r.get('citation_count')))

avg = sum(vals)/len(vals) if vals else None
out={"avg":avg,"n":len(vals)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zSgHJoaZqQZUtnQcB0mm6NTI': 'file_storage/call_zSgHJoaZqQZUtnQcB0mm6NTI.json', 'var_call_qcuB7G45SlVxG9i3bj36sxYz': 'file_storage/call_qcuB7G45SlVxG9i3bj36sxYz.json', 'var_call_aUTFjBLjkcJmBNm89MdmCkb7': {'average_citation_count_2018_for_acm_papers': None, 'acm_papers_with_2018_citations_matched': 0}, 'var_call_JAH1dXEdGBTBUJTk7EkoJNg6': {'num_docs': 99, 'num_cit2018': 158, 'num_acm_docs_broad': 0, 'intersection': 0, 'sample_intersection': [], 'sample_cit_titles': ['Using Context to Reveal Factors That Affect Physical Activity', 'QuittyLink: Using Smartphones for Personal Counseling to Help People Quit Smoking', 'TimeAware: Leveraging Framing Effects to Enhance Personal Productivity', 'Sharing Steps in the Workplace: Changing Privacy Concerns Over Time', 'Quantified Recess: Design of an Activity for Elementary Students Involving Analyses of Their Own Movement Data', 'Sharing Automatically Tracked Activity Data: Implications for Therapists and People with Mobility Impairments', 'Understanding Fatigue and Stamina Management Opportunities and Challenges in Wheelchair Basketball', 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'Caring Through Data: Attending to the Social and Emotional Experiences of Health Datafication', 'Low Sampling Rate for Physical Activity Recognition', 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'When Fitness Meets Social Networks: Investigating Fitness Tracking and Social Practices on WeRun', 'Social (Media) Jet Lag: How Usage of Social Technology Can Modulate and Reflect Circadian Rhythms', 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness', 'Understanding the Cost of Driving Trips', 'Health Multimedia: Lifestyle Recommendations Based on Diverse Observations', 'How Do We Engage with Activity Trackers?: A Longitudinal Study of Habito']}, 'var_call_QkVDuEYoKRFIjgxJ8HTkciZn': {'first_doc_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'len_text': 68339, 'acm_index': 1611, 'snippet': 'nformatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location. \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation (e.g., HCI). \n\nINTRODUCTION \nPersonal informatics, or collecting and reflecting on personal \ninformation,  has  become  incr'}, 'var_call_VK1qL183b9bDtcMjWxynPery': {'count': 0, 'sample': []}, 'var_call_0NBjCLUBu8ef5jdJTTtJHJzU': {'found_plain': True, 'context': 'nances; Location. \n\nACM Classification K', 'char_codes': [65, 67, 77]}, 'var_call_7NY9s53axrCoJLLyBTDSxUWd': {'type': "<class 'str'>", 'has_acm': True, 'num_ACM': 3}, 'var_call_CeASkGHIQsEEome44Nkijw1p': [{'i': 0, 'fn': 'A Lived Informatics Model of Personal Informatics.txt', 'acm_in': True, 're_word': True}, {'i': 1, 'fn': 'A Stage-based Model of Personal Informatics Systems.txt', 'acm_in': True, 're_word': True}, {'i': 2, 'fn': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt', 'acm_in': True, 're_word': True}, {'i': 3, 'fn': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt', 'acm_in': True, 're_word': True}, {'i': 4, 'fn': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt', 'acm_in': True, 're_word': True}], 'var_call_ksfbtPeZg6SH5y1lRRBWGoc9': {'count': 0, 'sample': []}, 'var_call_pmOAb4pFJC5ymblT2r1HYMGm': {'count': 99, 'sample': ['A Lived Informatics Model of Personal Informatics', 'A Stage-based Model of Personal Informatics Systems', 'A Trip to the Moon: Personalized Animated Movies for Self-reflection', 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation', 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'Beyond Abandonment to Next Steps: Understanding and Designing for Life After Personal Informatics Tool Use', "Beyond Behavior: The Coach's Perspective on Technology in Health Coaching", 'Blood Pressure Beyond the Clinic: Rethinking a Health Metric for Everyone']}}

exec(code, env_args)
