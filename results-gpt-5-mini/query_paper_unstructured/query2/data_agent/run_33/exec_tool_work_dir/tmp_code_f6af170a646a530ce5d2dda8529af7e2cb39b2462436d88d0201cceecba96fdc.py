code = """import json
with open(var_call_s2L9n5FvYwuoXzIUTTRBT7kd, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)
with open(var_call_mCuZg5iKPsfdwCKdDFRVhAXR, 'r', encoding='utf-8') as f:
    citations = json.load(f)

def title_from_filename(fn):
    return fn[:-4] if fn.lower().endswith('.txt') else fn

title_to_text = { title_from_filename(d.get('filename','')): d.get('text','') for d in paper_docs }

acm_counts = []
for rec in citations:
    title = rec.get('title')
    count_raw = rec.get('citation_count')
    try:
        count = int(count_raw)
    except:
        try:
            count = int(float(count_raw))
        except:
            continue
    text = title_to_text.get(title)
    if text:
        if 'acm' in text.lower():
            acm_counts.append({'title': title, 'citation_count': count})

if acm_counts:
    avg = sum(x['citation_count'] for x in acm_counts) / len(acm_counts)
    avg_rounded = round(avg, 4)
else:
    avg_rounded = None

result = {
    'average_citation_count': avg_rounded,
    'paper_count': len(acm_counts),
    'papers': acm_counts
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_4TLSbqKdwtqhq1Vnnxhqk1BW': ['paper_docs'], 'var_call_s2L9n5FvYwuoXzIUTTRBT7kd': 'file_storage/call_s2L9n5FvYwuoXzIUTTRBT7kd.json', 'var_call_ooNYWIIpdQsyKmBg6iMSVvXp': ['Citations', 'sqlite_sequence'], 'var_call_mCuZg5iKPsfdwCKdDFRVhAXR': 'file_storage/call_mCuZg5iKPsfdwCKdDFRVhAXR.json', 'var_call_oyuZVcUutsJqKKX0IJCFGREN': {'average_citation_count': None, 'paper_count': 0}, 'var_call_F1b6XYpN0JhwkiwgqIMhjuQ3': {'total_citations_2018': 158, 'papers_with_text_in_mongo': 2, 'papers_with_ACM_in_text': 0, 'sample_matches': [{'title': 'Expense Control: A Gamified, Semi-Automated, Crowd-Based Approach For Receipt Capturing', 'citation_count': 95, 'has_text': False, 'has_acm_in_text': False}, {'title': 'Sundroid: Solar Radiation Awareness with Smartphones', 'citation_count': 28, 'has_text': False, 'has_acm_in_text': False}, {'title': 'Why We Use and Abandon Smart Devices', 'citation_count': 58, 'has_text': False, 'has_acm_in_text': False}, {'title': 'One Step Forward, Two Steps Back: The Key to Wearables in the Field is the App', 'citation_count': 20, 'has_text': False, 'has_acm_in_text': False}, {'title': 'Nurturing wearable and mHealth technologies for self-care: Mindset, tool set and skill set', 'citation_count': 13, 'has_text': False, 'has_acm_in_text': False}, {'title': "Closing the Gap: Supporting Patients' Transition to Self-Management After Hospitalization", 'citation_count': 74, 'has_text': False, 'has_acm_in_text': False}, {'title': 'Reviewing Reflection: On the Use of Reflection in Interactive System Design', 'citation_count': 49, 'has_text': False, 'has_acm_in_text': False}, {'title': 'Exploring the Design Space of Glanceable Feedback for Physical Activity Trackers', 'citation_count': 88, 'has_text': False, 'has_acm_in_text': False}, {'title': 'Beyond Self-Tracking and Reminders: Designing Smartphone Apps That Support Habit Formation', 'citation_count': 35, 'has_text': False, 'has_acm_in_text': False}, {'title': 'Reflective Informatics: Conceptual Dimensions for Designing Technologies of Reflection', 'citation_count': 42, 'has_text': False, 'has_acm_in_text': False}, {'title': 'Barriers to Engagement with a Personal Informatics Productivity Tool', 'citation_count': 73, 'has_text': False, 'has_acm_in_text': False}, {'title': 'How to Drive a London Bus: Measuring Performance in a Mobile and Remote Workplace', 'citation_count': 18, 'has_text': False, 'has_acm_in_text': False}, {'title': 'Participant Driven Photo Elicitation for Understanding Activity Tracking: Benefits and Limitations', 'citation_count': 81, 'has_text': False, 'has_acm_in_text': False}, {'title': 'A Lived Informatics Model of Personal Informatics', 'citation_count': 50, 'has_text': True, 'has_acm_in_text': False}, {'title': 'Charting Design Preferences on Wellness Wearables', 'citation_count': 2, 'has_text': False, 'has_acm_in_text': False}, {'title': 'Computational Approaches Toward Integrating Quantified Self Sensing and Social Media', 'citation_count': 97, 'has_text': False, 'has_acm_in_text': False}, {'title': 'Quantifying the Body and Caring for the Mind: Self-Tracking in Multiple Sclerosis', 'citation_count': 82, 'has_text': False, 'has_acm_in_text': False}, {'title': 'Technologies for Everyday Life Reflection: Illustrating a Design Space', 'citation_count': 21, 'has_text': False, 'has_acm_in_text': False}, {'title': 'Personal Tracking of Screen Time on Digital Devices', 'citation_count': 63, 'has_text': False, 'has_acm_in_text': False}, {'title': 'Sensor Requirements for Activity Recognition on Smart Watches', 'citation_count': 9, 'has_text': False, 'has_acm_in_text': False}]}, 'var_call_QK1O5is5NIIZWbvGWeX5NVYR': {'found_patterns': {'ACM': {'index': 1611, 'snippet': 'Lapsing; Physical Activity; Finances; Location. \n\nACM Classification Keywords \nH.5.m. Information in'}, '© ACM': {'index': 3237, 'snippet': 'ptember 7-11, 2015, Osaka, Japan. \nCopyright 2015 © ACM 978-1-4503-3574-4/15/09...$15.00. \nhttp://dx'}, '©': {'index': 3237, 'snippet': 'ptember 7-11, 2015, Osaka, Japan. \nCopyright 2015 © ACM 978-1-4503-3574-4/15/09...$15.00. \nhttp://dx'}, 'Copyright': {'index': 2854, 'snippet': ' and  the  full  citation  on  the  first  page.  Copyrights  for\ncomponents  of  this  work  owned '}, 'http://dx.doi.org': {'index': 3278, 'snippet': 'ght 2015 © ACM 978-1-4503-3574-4/15/09...$15.00. \nhttp://dx.doi.org/10.1145/2750858.2804250 \n\nThe fi'}, 'DOI': {'index': 3288, 'snippet': ' ACM 978-1-4503-3574-4/15/09...$15.00. \nhttp://dx.doi.org/10.1145/2750858.2804250 \n\nThe first and mo'}, 'ACM 978': {'index': 3239, 'snippet': 'ember 7-11, 2015, Osaka, Japan. \nCopyright 2015 © ACM 978-1-4503-3574-4/15/09...$15.00. \nhttp://dx.d'}}, 'ACM_matches_count': 3, 'first_10_matches': ['tivity; Finances; Location. \n\nACM Classification Keywords \nH.5.', 'ork  owned  by  others  than  ACM  must  be  honored.\nAbstracti', 'aka, Japan. \nCopyright 2015 © ACM 978-1-4503-3574-4/15/09...$15']}}

exec(code, env_args)
