code = """import json
import re
# Data from previous tool calls
meta = var_call_1ST5yQXMCfov2jGnfA5bNeej
articles = var_call_UocbpNESMGsRpJHGa4Yqh8I6

# Build sets and maps
meta_ids = [str(int(x['article_id'])) for x in meta]
article_docs = {str(int(a['article_id'])): a for a in articles}

total_meta = len(meta_ids)
total_docs = len(article_docs)

# Classifier keyword lists
science_kw = ['science','scientist','research','laboratory','laboratory','lab','technology','tech','computer','robot','engineer','engineering','electric','electricity','machine','experiment','scientific','innovation','innovative']
sports_kw = ['pro bowl','cornerback','practice','wide receiver','wr','quarterback','soccer','football','basketball','baseball','goal','match','tournament','athlete','coach','team','reciever','receiver','nba','mlb','nhl']
business_kw = ['company','profit','profits','economy','share','shares','stock','market','business','commerce','commodity','billion','dollar','bank','merger','acquire','acquisition']

def classify_text(text):
    t = text.lower()
    # check science first
    for kw in science_kw:
        if kw in t:
            return 'Science/Technology'
    for kw in sports_kw:
        if kw in t:
            return 'Sports'
    for kw in business_kw:
        if kw in t:
            return 'Business'
    return 'World'

# Classify available docs
science_count = 0
classified_count = 0
classified_by_id = {}
for aid in meta_ids:
    doc = article_docs.get(aid)
    if doc is None:
        # can't classify
        classified_by_id[aid] = None
        continue
    text = (doc.get('title') or '') + ' ' + (doc.get('description') or '')
    cat = classify_text(text)
    classified_by_id[aid] = cat
    classified_count += 1
    if cat == 'Science/Technology':
        science_count += 1

# Prepare result
result = {
    'science_count_classified_docs': science_count,
    'total_articles_in_metadata': total_meta,
    'total_articles_with_content': total_docs,
    'classified_docs_count': classified_count,
}
# Fractions
result['fraction_of_all_authored_in_science_over_metadata'] = None
if total_meta > 0:
    result['fraction_of_all_authored_in_science_over_metadata'] = f"{science_count}/{total_meta}"
    result['fraction_of_all_authored_in_science_over_metadata_decimal'] = science_count/total_meta

result['fraction_over_classified_docs'] = None
if classified_count > 0:
    result['fraction_over_classified_docs'] = f"{science_count}/{classified_count}"
    result['fraction_over_classified_docs_decimal'] = science_count/classified_count

# Also include list of article_ids classified as Science/Technology
science_ids = [aid for aid,cat in classified_by_id.items() if cat == 'Science/Technology']
result['science_article_ids'] = science_ids

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_RKxF8ESVCh7Gv1HRLuC9I23F': [{'author_id': '218'}], 'var_call_1ST5yQXMCfov2jGnfA5bNeej': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_call_UocbpNESMGsRpJHGa4Yqh8I6': [{'_id': '695991a44acf36fc24d2ae08', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '695991a44acf36fc24d2b5b9', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '695991a44acf36fc24d2b864', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '695991a44acf36fc24d2b8f3', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '695991a44acf36fc24d2bac3', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
