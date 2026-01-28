code = """import json

with open(locals()['var_function-call-14828784749153156618'], 'r') as f:
    papers = json.load(f)

print(f"Total papers in list: {len(papers)}")

eat_tell_found = False
for p in papers:
    if "Eat & Tell" in p['filename']:
        eat_tell_found = True
        print("Eat & Tell is present.")
        break

if not eat_tell_found:
    print("Eat & Tell is NOT present.")"""

env_args = {'var_function-call-18115772371800026671': 'file_storage/function-call-18115772371800026671.json', 'var_function-call-5992210223060542077': 'file_storage/function-call-5992210223060542077.json', 'var_function-call-13564221464732274520': 'file_storage/function-call-13564221464732274520.json', 'var_function-call-7850296922984733998': {'food_papers_count': 0, 'total_citations': 0, 'food_paper_titles': []}, 'var_function-call-6262404583647121035': {'total_papers': 5, 'titles_with_food': [], 'snippets': [{'title': 'A Lived Informatics Model of Personal Informatics', 'snippet': 'o  study  people’s  use  of  commercial  tools  for  tracking \nlocation  [24,30],  finances  [20],  food  [11],  weight  [19,25], \nand  physical  activity  [16,34]  and  to  develop  research \nprototy'}, {'title': 'A Stage-based Model of Personal Informatics Systems', 'snippet': 'ron.com), and Ellie Harrison, \nwho  created  art  projects  on  her  personal  behavior,  such  as \nfood  consumption  and  sneezes  (http://ellieharrison.com). \nThese  are  extreme  examples,  but  r'}, {'title': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App', 'snippet': '  bladder  training). \nThe  lifestyle changes  consist  of  avoiding  bladder  irritants \n(certain  food  and  drinks)  and  consuming  a  proper  amount \nof liquid per day. The PFM training consists '}]}, 'var_function-call-9193793314079207812': [{'_id': '694f5530284b10b11dc0a869', 'filename': 'A Lived Informatics Model of Personal Informatics.txt'}, {'_id': '694f5530284b10b11dc0a86a', 'filename': 'A Stage-based Model of Personal Informatics Systems.txt'}, {'_id': '694f5530284b10b11dc0a86b', 'filename': 'A Trip to the Moon: Personalized Animated Movies for Self-reflection.txt'}, {'_id': '694f5530284b10b11dc0a86c', 'filename': 'A Wee Bit More Interaction: Designing and Evaluating an Overactive Bladder App.txt'}, {'_id': '694f5530284b10b11dc0a86d', 'filename': 'ArmSleeve: A Patient Monitoring System to Support Occupational Therapists in Stroke Rehabilitation.txt'}], 'var_function-call-12448764961698084004': 'file_storage/function-call-12448764961698084004.json', 'var_function-call-3345834275723385797': 'file_storage/function-call-3345834275723385797.json', 'var_function-call-13463632338328999851': {'food_papers_count': 3, 'matched_citations_records': 16, 'total_citations': 695, 'titles': ["It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness']}, 'var_function-call-14828784749153156618': 'file_storage/function-call-14828784749153156618.json', 'var_function-call-16220853225874405631': {'total_citations': 1264, 'count': 5, 'titles': ['Barriers and Negative Nudges: Exploring Challenges in Food Journaling', 'Crumbs: Lightweight Daily Food Challenges to Promote Engagement and Mindfulness', "It's Definitely Been a Journey: A Qualitative Study on How Women with Eating Disorders Use Weight Loss Apps", 'Rethinking the Mobile Food Journal: Exploring Opportunities for Lightweight Photo-Based Capture', 'When Personal Tracking Becomes Social: Examining the Use of Instagram for Healthy Eating']}}

exec(code, env_args)
