code = """import json

docs = var_call_qcuB7G45SlVxG9i3bj36sxYz
if isinstance(docs, str):
    with open(docs,'r',encoding='utf-8') as f:
        docs=json.load(f)

t = docs[0].get('text','')
# show whether 'ACM' present and some tail snippet containing copyright
idx = t.lower().find('acm')
snippet = t[idx-100:idx+200] if idx!=-1 else t[:300]

out={"first_doc_filename":docs[0].get('filename'),"len_text":len(t),"acm_index":idx,"snippet":snippet[:500]}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_zSgHJoaZqQZUtnQcB0mm6NTI': 'file_storage/call_zSgHJoaZqQZUtnQcB0mm6NTI.json', 'var_call_qcuB7G45SlVxG9i3bj36sxYz': 'file_storage/call_qcuB7G45SlVxG9i3bj36sxYz.json', 'var_call_aUTFjBLjkcJmBNm89MdmCkb7': {'average_citation_count_2018_for_acm_papers': None, 'acm_papers_with_2018_citations_matched': 0}, 'var_call_JAH1dXEdGBTBUJTk7EkoJNg6': {'num_docs': 99, 'num_cit2018': 158, 'num_acm_docs_broad': 0, 'intersection': 0, 'sample_intersection': [], 'sample_cit_titles': ['Using Context to Reveal Factors That Affect Physical Activity', 'QuittyLink: Using Smartphones for Personal Counseling to Help People Quit Smoking', 'TimeAware: Leveraging Framing Effects to Enhance Personal Productivity', 'Sharing Steps in the Workplace: Changing Privacy Concerns Over Time', 'Quantified Recess: Design of an Activity for Elementary Students Involving Analyses of Their Own Movement Data', 'Sharing Automatically Tracked Activity Data: Implications for Therapists and People with Mobility Impairments', 'Understanding Fatigue and Stamina Management Opportunities and Challenges in Wheelchair Basketball', 'Persuasive Technology in the Real World: A Study of Long-term Use of Activity Sensing Devices for Fitness', 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'Caring Through Data: Attending to the Social and Emotional Experiences of Health Datafication', 'Low Sampling Rate for Physical Activity Recognition', 'Leveraging Intermediated Interactions to Support Utilization of Persuasive Personal Health Informatics', 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'When Fitness Meets Social Networks: Investigating Fitness Tracking and Social Practices on WeRun', 'Social (Media) Jet Lag: How Usage of Social Technology Can Modulate and Reflect Circadian Rhythms', 'ConCap: Designing to Empower Individual Reflection on Chronic Conditions Using Mobile Apps', 'Designing a Wellness Self-management Tool for Older Adults: Results from a Field Trial of YourWellness', 'Understanding the Cost of Driving Trips', 'Health Multimedia: Lifestyle Recommendations Based on Diverse Observations', 'How Do We Engage with Activity Trackers?: A Longitudinal Study of Habito']}}

exec(code, env_args)
