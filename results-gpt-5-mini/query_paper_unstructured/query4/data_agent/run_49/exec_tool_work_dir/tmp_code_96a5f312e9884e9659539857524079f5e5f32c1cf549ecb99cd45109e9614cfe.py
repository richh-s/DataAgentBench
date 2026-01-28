code = """import json, re
# load mongo docs from previous call
docs = None
try:
    if isinstance(var_call_Fg1KBal7XjXiQo84W1y8oWkp, str):
        with open(var_call_Fg1KBal7XjXiQo84W1y8oWkp, 'r', encoding='utf-8') as f:
            docs = json.load(f)
    else:
        docs = var_call_Fg1KBal7XjXiQo84W1y8oWkp
except Exception as e:
    docs = var_call_Fg1KBal7XjXiQo84W1y8oWkp

# load citations query result
citations = None
try:
    if isinstance(var_call_jBPOkEPIh0ctKA8k0oKbj4v6, str):
        with open(var_call_jBPOkEPIh0ctKA8k0oKbj4v6, 'r', encoding='utf-8') as f:
            citations = json.load(f)
    else:
        citations = var_call_jBPOkEPIh0ctKA8k0oKbj4v6
except Exception as e:
    citations = var_call_jBPOkEPIh0ctKA8k0oKbj4v6

cit_map = {c['title']: int(c['total_citations']) for c in citations}

results = []
for doc in docs:
    fn = doc.get('filename','')
    title = fn[:-4] if fn.endswith('.txt') else fn
    text = doc.get('text','')
    # search for 2016 exact
    found = bool(re.search(r"\b2016\b", text))
    # also search for patterns like "2016." or "2016,"
    if not found:
        found = bool(re.search(r"2016[\.,]", text))
    # try to find a publication line like '2016.' or 'Publication date: 2016' etc
    pub_year = None
    m = re.search(r"Publication date:\s*(\w+\s*)*(\b2016\b)", text, re.I)
    if m:
        pub_year = 2016
    else:
        m2 = re.search(r"\b(19|20)\d{2}\b", text)
        if m2:
            # take first year occurrence
            pub_year = int(m2.group(0))
    # but prefer explicit 2016 match
    if found:
        pub_year = 2016
    results.append({'title': title, 'pub_year_found': pub_year, 'has_2016_token': found, 'total_citations': cit_map.get(title)})

# filter for pub_year_found == 2016 or has_2016_token True
filtered = [ {'title': r['title'], 'total_citations': r['total_citations']} for r in results if r['pub_year_found']==2016 or r['has_2016_token']]

print("__RESULT__:")
print(json.dumps(filtered))"""

env_args = {'var_call_1Bqplr3rh53ChNvtEOW1gjRS': 'file_storage/call_1Bqplr3rh53ChNvtEOW1gjRS.json', 'var_call_RHJMqRHzPZhLQ42EZ5csdelr': [], 'var_call_I9tf0clGC8oTadzuC6RDDAPU': 'file_storage/call_I9tf0clGC8oTadzuC6RDDAPU.json', 'var_call_U44SEcLG6zWizxmxE0Aypv5k': [], 'var_call_CR3mHeGx2Vc5CLD705Vvdb00': [], 'var_call_MdHRAbGQSZUCx0toe578graa': ['Defining Adherence: Making Sense of Physical Activity Tracker Data.txt', 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal.txt', 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices.txt'], 'var_call_jBPOkEPIh0ctKA8k0oKbj4v6': [{'title': 'Defining Adherence: Making Sense of Physical Activity Tracker Data', 'total_citations': '259'}, {'title': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal', 'total_citations': '133'}, {'title': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices', 'total_citations': '278'}], 'var_call_j4fG1UHF84Arl4vMCadNzJNk': [], 'var_call_j43hDSFtHKWATdMpBWV7gMcu': [], 'var_call_Fg1KBal7XjXiQo84W1y8oWkp': 'file_storage/call_Fg1KBal7XjXiQo84W1y8oWkp.json', 'var_call_UxK3ohs3qKw8feM2CLyc4D7C': [{'filename': 'Defining Adherence: Making Sense of Physical Activity Tracker Data.txt', 'year_found': None, 'snippet': 'Defining Adherence: Making Sense of Physical Activity Tracker Data\n\nLIE MING TANG, University of Sydney, Australia\nJOCHEN MEYER, OFFIS Institute for Informatics, Germany\nDANIEL A. EPSTEIN, University of Washington, United States\nKEVIN BRAGG, University of Sydney, Australia\nLINA ENGELEN, University of Sydney, Australia\nADRIAN BAUMAN, University of Sydney, Australia\nJUDY KAY, University of Sydney, Australia\n\nIncreasingly, people are collecting detailed personal activity data from commercial trackers. Such data should\nbe able to give important insights about their activity levels. However, people do not wear or carry tracking\ndevices all day, every day and this means that tracker data is typically incomplete. This paper aims to provide a\nsystematic way to take account of this incompleteness, by defining adherence, a measure of data completeness,\nbased on how much people wore their tracker. We show the impact of different adherence definitions on 12 diverse\ndatasets, for 753 users, with ov'}, {'filename': 'Goal-setting And Achievement In Activity Tracking Apps: A Case Study Of MyFitnessPal.txt', 'year_found': None, 'snippet': 'Goal-setting And Achievement In Activity Tracking Apps: A Case\nStudy Of MyFitnessPal\n\nMitchell L. Gordon\nStanford University\nmgord@cs.stanford.edu\n\nTim Althoff\nUniversity of Washington\nalthoff@cs.washington.edu\n\nJure Leskovec\nStanford University\njure@cs.stanford.edu\n\nABSTRACT\nActivity tracking apps often make use of goals as one of their\ncore motivational tools. There are two critical components to this\ntool: setting a goal, and subsequently achieving that goal. Despite\nits crucial role in how a number of prominent self-tracking apps\nfunction, there has been relatively little investigation of the goal-\nsetting and achievement aspects of self-tracking apps.\n\nHere we explore this issue, investigating a particular goal setting\nand achievement process that is extensive, recorded, and crucial for\nboth the app and its users’ success: weight loss goals in MyFitness-\nPal. We present a large-scale study of 1.4 million users and weight\nloss goals, allowing for an unprecedented detailed view of h'}, {'filename': 'Technologies to Engage Young Children in Physical Activity: An Online Study of Parenting Practices.txt', 'year_found': None, 'snippet': 'Technologies to Engage Young Children in Physical Activity: \nAn Online Study of Parenting Practices \n\nBernd Ploderer, Yaman Mazyed S. Alsahﬁ, Stewart G. Trost† \nQueensland University of Technology (QUT), Brisbane, Australia \nb.ploderer@qut.edu.au, yamanmazyeds.alsahﬁ@connect.qut.edu.au, s.trost@qut.edu.au \n\nABSTRACT \n\nThis paper explores how parents use interactive technologies to \nencourage young  children  (under  the  age  of 5)  to  be physically \nactive,  as  well  as  how  technologies  might  undermine  physical \nactivity. Based on an analysis of 1528 posts made online on Reddit \nand Quora, we found that many parents regard time spent with \ntechnologies as time taken away from physical activity. However, \nwe  also  identified  how  parents  appropriated  technology  to \npromote  physical  activity,  i.e.,  through  rewarding,  modelling, \nfacilitating,  participating,  tracking  and  documenting.  We  hope \nthese  practices  will  inspire  design  work  with  families  to  creat'}]}

exec(code, env_args)
