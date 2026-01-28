code = """import json
from collections import defaultdict
# Load file paths from storage variables
meta_path = var_call_lHFXpsi061JUb8EbGXOJcodE
articles_path = var_call_HuLfLNSbIXDT1miY00fXNOPn
# Load data
with open(meta_path, 'r') as f:
    meta_records = json.load(f)
with open(articles_path, 'r') as f:
    articles_records = json.load(f)
# Build article_id -> text mapping
articles_map = {}
for a in articles_records:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    title = a.get('title') or ''
    desc = a.get('description') or ''
    articles_map[aid] = (title + ' ' + desc).lower()
# Define keyword-based classifier
business_kw = ['economy','economic','economics','stock','stocks','market','markets','bank','banks','invest','investment','investor','investors','share','shares','ipo','profit','profits','company','companies','firm','trade','trading','revenue','earnings','financial','finance','oil','oil prices','merger','acquisition','acquires','acquired','billion','million']
sports_kw = ['game','goal','season','match','tournament','championship','score','team','coach','league','cup','player','players','win','won','defeat','olympic','race','racing','boxing','football','soccer','basketball','baseball','hockey','tennis']
tech_kw = ['technology','tech','software','internet','google','iphone','nuclear','nasa','scientist','scientists','research','study','scientific','robot','robotics','ai','artificial intelligence','phone','smartphone','semiconductor','chip','cyber','space']

def classify_text(text):
    if not text:
        return 'World'
    # check business
    for kw in business_kw:
        if kw in text:
            return 'Business'
    for kw in sports_kw:
        if kw in text:
            return 'Sports'
    for kw in tech_kw:
        if kw in text:
            return 'Science/Technology'
    return 'World'

# Count business articles per year
counts = defaultdict(int)
for rec in meta_records:
    try:
        aid = int(rec.get('article_id'))
        pub = rec.get('publication_date')
        year = int(pub.split('-')[0])
    except:
        continue
    if year < 2010 or year > 2020:
        continue
    text = articles_map.get(aid, '')
    cat = classify_text(text)
    if cat == 'Business':
        counts[year] += 1
# Ensure all years present
result_counts = {str(y): counts.get(y, 0) for y in range(2010, 2021)}
total = sum(result_counts.values())
average = total / 11.0
# Prepare output
out = {
    'counts_by_year': result_counts,
    'total_business_articles_2010_2020': total,
    'average_business_articles_per_year': round(average, 2)
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_lHFXpsi061JUb8EbGXOJcodE': 'file_storage/call_lHFXpsi061JUb8EbGXOJcodE.json', 'var_call_MYieP3VHImPqo3NeFvrsroIP': 'file_storage/call_MYieP3VHImPqo3NeFvrsroIP.json', 'var_call_HuLfLNSbIXDT1miY00fXNOPn': 'file_storage/call_HuLfLNSbIXDT1miY00fXNOPn.json'}

exec(code, env_args)
