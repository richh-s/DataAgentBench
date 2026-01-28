code = """import json, re

docs = var_call_qcuB7G45SlVxG9i3bj36sxYz
if isinstance(docs, str):
    with open(docs,'r',encoding='utf-8') as f:
        docs=json.load(f)

txt = docs[0].get('text') or ''
# try regex findall without word boundary and show unique matches around 'ACM'
m = re.search('ACM', txt)
out={"found_plain": m is not None, "context": txt[m.start()-20:m.start()+20] if m else None, "char_codes": [ord(c) for c in txt[m.start():m.start()+3]] if m else None}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zSgHJoaZqQZUtnQcB0mm6NTI': 'file_storage/call_zSgHJoaZqQZUtnQcB0mm6NTI.json', 'var_call_qcuB7G45SlVxG9i3bj36sxYz': 'file_storage/call_qcuB7G45SlVxG9i3bj36sxYz.json', 'var_call_aUTFjBLjkcJmBNm89MdmCkb7': {'average_citation_count_2018_for_acm_papers': None, 'acm_papers_with_2018_citations_matched': 0}, 'var_call_JAH1dXEdGBTBUJTk7EkoJNg6': {'num_docs': 99, 'num_cit2018': 158, 'num_acm_docs_broad': 0, 'intersection': 0, 'sample_intersection': [], 'sample_cit_titles': ['Using Context to Reveal Factors That Affect Physical Activity', 'QuittyLink: Using Smartphones for Personal Counseling to Help People Quit Smoking', 'TimeAware: Leveraging Framing Effects to Enhance Personal Productivity', 'Sharing Steps in the Workplace: Changing Privacy Concerns Over Time', 'Quantified Recess: Design of an Activity for Elementary Students Involving Analyses of Their Own Movement Data', 'Sharing Automatically Tracked Activity Data: Implications for Therapists and People with Mobility Impairments', 'Understanding Fatigue and Stamina Management Opportunities and Challenges in Wheelchair Basketball', 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'Caring Through Data: Attending to the Social and Emotional Experiences of Health Datafication', 'Low Sampling Rate for Physical Activity Recognition', 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'When Fitness Meets Social Networks: Investigating Fitness Tracking and Social Practices on WeRun', 'Social (Media) Jet Lag: How Usage of Social Technology Can Modulate and Reflect Circadian Rhythms', 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness', 'Understanding the Cost of Driving Trips', 'Health Multimedia: Lifestyle Recommendations Based on Diverse Observations', 'How Do We Engage with Activity Trackers?: A Longitudinal Study of Habito']}, 'var_call_QkVDuEYoKRFIjgxJ8HTkciZn': {'first_doc_filename': 'A Lived Informatics Model of Personal Informatics.txt', 'len_text': 68339, 'acm_index': 1611, 'snippet': 'nformatics; Personal Informatics; Self-Tracking; \nLapsing; Physical Activity; Finances; Location. \n\nACM Classification Keywords \nH.5.m. Information interfaces and presentation (e.g., HCI). \n\nINTRODUCTION \nPersonal informatics, or collecting and reflecting on personal \ninformation,  has  become  incr'}, 'var_call_VK1qL183b9bDtcMjWxynPery': {'count': 0, 'sample': []}}

exec(code, env_args)
