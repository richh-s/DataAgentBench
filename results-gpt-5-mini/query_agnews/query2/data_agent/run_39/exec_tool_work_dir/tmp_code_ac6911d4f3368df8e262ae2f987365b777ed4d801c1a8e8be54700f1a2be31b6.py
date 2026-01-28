code = """import json

md = var_call_hMJYovjKgf1YoLFOHcQXIrA7
articles = var_call_3lmny9zBE5mQ02lbOsOCJfuP

# Build article dict by article_id (int)
article_dict = {}
for a in articles:
    try:
        aid = int(a.get('article_id'))
    except:
        continue
    article_dict[aid] = a

total_articles = len(md)

science_keywords = ['science','scientist','technology','technolog','tech','research','laborator','lab','experiment','electricit','energy','robot','ai','artificial intelligence','computer','innovation','siemens','westinghouse','gyro-gen','micro-game','gameboy']
sports_keywords = ['team','match','cornerback','pro bowl','coach','goal','score','basketball','football','wide receiver','receiver','practice','season','league','tournament','player','broncos','reciever']
business_keywords = ['profit','company','market','mining','commodity','billiton','acquisition','shares','revenue','profits','bank','investment','industry','business']

science_count = 0
classified_count = 0
missing_ids = []
classified_by_id = {}

for row in md:
    try:
        aid = int(row.get('article_id'))
    except:
        continue
    rec = article_dict.get(aid)
    if rec is None:
        missing_ids.append(aid)
        continue
    classified_count += 1
    text = (str(rec.get('title','')) + ' ' + str(rec.get('description',''))).lower()
    cat = 'World'
    # Science first
    if any(k in text for k in science_keywords):
        cat = 'Science/Technology'
        science_count += 1
    elif any(k in text for k in sports_keywords):
        cat = 'Sports'
    elif any(k in text for k in business_keywords):
        cat = 'Business'
    else:
        cat = 'World'
    classified_by_id[aid] = cat

# Fraction over all articles (use total_articles as denominator)
fraction = science_count / total_articles if total_articles>0 else None

result = {
    'science_count': science_count,
    'total_articles': total_articles,
    'fraction': round(fraction, 6) if fraction is not None else None,
    'ratio': f"{science_count}/{total_articles}",
    'classified_count': classified_count,
    'missing_count': len(missing_ids)
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_bgnGIpU8LUkPErfX3YbAbP3r': [{'author_id': '218'}], 'var_call_hMJYovjKgf1YoLFOHcQXIrA7': [{'article_id': '192', 'region': 'Africa', 'publication_date': '2013-06-20'}, {'article_id': '2161', 'region': 'South America', 'publication_date': '2011-06-22'}, {'article_id': '2844', 'region': 'Africa', 'publication_date': '2005-03-04'}, {'article_id': '2987', 'region': 'South America', 'publication_date': '2004-01-24'}, {'article_id': '3451', 'region': 'North America', 'publication_date': '2005-12-25'}, {'article_id': '3970', 'region': 'North America', 'publication_date': '2011-11-03'}, {'article_id': '4447', 'region': 'Asia', 'publication_date': '2005-01-22'}, {'article_id': '5354', 'region': 'Europe', 'publication_date': '2008-04-08'}, {'article_id': '6705', 'region': 'Africa', 'publication_date': '2005-12-06'}, {'article_id': '6869', 'region': 'Europe', 'publication_date': '2008-03-25'}, {'article_id': '8962', 'region': 'Africa', 'publication_date': '2020-04-19'}, {'article_id': '9677', 'region': 'Asia', 'publication_date': '2004-06-12'}, {'article_id': '9858', 'region': 'Asia', 'publication_date': '2006-04-13'}, {'article_id': '14861', 'region': 'South America', 'publication_date': '2007-09-11'}, {'article_id': '15100', 'region': 'Africa', 'publication_date': '2009-01-28'}, {'article_id': '15473', 'region': 'Asia', 'publication_date': '2010-02-14'}, {'article_id': '17491', 'region': 'South America', 'publication_date': '2022-04-22'}, {'article_id': '19469', 'region': 'North America', 'publication_date': '2022-09-29'}, {'article_id': '20362', 'region': 'North America', 'publication_date': '2017-10-12'}, {'article_id': '21238', 'region': 'Asia', 'publication_date': '2022-12-30'}, {'article_id': '22354', 'region': 'Europe', 'publication_date': '2015-11-05'}, {'article_id': '23914', 'region': 'Africa', 'publication_date': '2012-05-12'}, {'article_id': '24495', 'region': 'Europe', 'publication_date': '2006-05-03'}, {'article_id': '25960', 'region': 'Asia', 'publication_date': '2013-06-01'}, {'article_id': '26535', 'region': 'Asia', 'publication_date': '2009-11-28'}, {'article_id': '27429', 'region': 'Asia', 'publication_date': '2006-12-12'}, {'article_id': '28079', 'region': 'Africa', 'publication_date': '2019-05-10'}, {'article_id': '29164', 'region': 'South America', 'publication_date': '2016-02-17'}, {'article_id': '29297', 'region': 'Europe', 'publication_date': '2008-06-13'}, {'article_id': '33489', 'region': 'Africa', 'publication_date': '2010-07-29'}, {'article_id': '35408', 'region': 'North America', 'publication_date': '2015-05-24'}, {'article_id': '35882', 'region': 'North America', 'publication_date': '2022-10-13'}, {'article_id': '36182', 'region': 'Africa', 'publication_date': '2015-10-27'}, {'article_id': '36483', 'region': 'North America', 'publication_date': '2015-04-22'}, {'article_id': '37042', 'region': 'Asia', 'publication_date': '2004-05-23'}, {'article_id': '38608', 'region': 'Europe', 'publication_date': '2004-04-29'}, {'article_id': '39117', 'region': 'North America', 'publication_date': '2006-07-01'}, {'article_id': '39623', 'region': 'North America', 'publication_date': '2012-03-27'}, {'article_id': '40545', 'region': 'Asia', 'publication_date': '2014-10-11'}, {'article_id': '41616', 'region': 'Asia', 'publication_date': '2019-09-05'}, {'article_id': '46531', 'region': 'Europe', 'publication_date': '2004-09-22'}, {'article_id': '47439', 'region': 'Europe', 'publication_date': '2004-08-20'}, {'article_id': '48635', 'region': 'North America', 'publication_date': '2014-01-09'}, {'article_id': '48833', 'region': 'Asia', 'publication_date': '2017-12-15'}, {'article_id': '49035', 'region': 'Europe', 'publication_date': '2019-09-02'}, {'article_id': '52459', 'region': 'Asia', 'publication_date': '2021-07-11'}, {'article_id': '54906', 'region': 'Africa', 'publication_date': '2005-05-05'}, {'article_id': '57510', 'region': 'Asia', 'publication_date': '2006-04-22'}, {'article_id': '57860', 'region': 'South America', 'publication_date': '2012-11-04'}, {'article_id': '57918', 'region': 'South America', 'publication_date': '2022-09-08'}, {'article_id': '62404', 'region': 'Europe', 'publication_date': '2012-01-16'}, {'article_id': '62754', 'region': 'Europe', 'publication_date': '2020-05-27'}, {'article_id': '64102', 'region': 'South America', 'publication_date': '2021-03-23'}, {'article_id': '66827', 'region': 'Europe', 'publication_date': '2020-11-26'}, {'article_id': '68509', 'region': 'Asia', 'publication_date': '2006-04-18'}, {'article_id': '68958', 'region': 'South America', 'publication_date': '2004-03-14'}, {'article_id': '69262', 'region': 'Europe', 'publication_date': '2021-07-27'}, {'article_id': '69393', 'region': 'Asia', 'publication_date': '2010-04-05'}, {'article_id': '70498', 'region': 'Europe', 'publication_date': '2008-09-30'}, {'article_id': '70608', 'region': 'North America', 'publication_date': '2012-11-26'}, {'article_id': '72525', 'region': 'Africa', 'publication_date': '2009-07-04'}, {'article_id': '73025', 'region': 'North America', 'publication_date': '2020-09-09'}, {'article_id': '73684', 'region': 'Africa', 'publication_date': '2022-07-09'}, {'article_id': '78200', 'region': 'North America', 'publication_date': '2018-07-10'}, {'article_id': '80578', 'region': 'South America', 'publication_date': '2015-09-07'}, {'article_id': '80853', 'region': 'South America', 'publication_date': '2004-05-07'}, {'article_id': '81851', 'region': 'North America', 'publication_date': '2012-11-01'}, {'article_id': '82526', 'region': 'Asia', 'publication_date': '2013-10-22'}, {'article_id': '82668', 'region': 'Africa', 'publication_date': '2008-06-13'}, {'article_id': '83273', 'region': 'Europe', 'publication_date': '2011-10-05'}, {'article_id': '88553', 'region': 'Asia', 'publication_date': '2017-10-22'}, {'article_id': '88911', 'region': 'South America', 'publication_date': '2011-01-29'}, {'article_id': '89666', 'region': 'Europe', 'publication_date': '2011-03-12'}, {'article_id': '91286', 'region': 'Asia', 'publication_date': '2008-09-24'}, {'article_id': '91822', 'region': 'Asia', 'publication_date': '2022-03-03'}, {'article_id': '92992', 'region': 'Europe', 'publication_date': '2005-05-12'}, {'article_id': '93287', 'region': 'Europe', 'publication_date': '2014-09-05'}, {'article_id': '93804', 'region': 'Africa', 'publication_date': '2018-12-08'}, {'article_id': '94618', 'region': 'Africa', 'publication_date': '2005-03-26'}, {'article_id': '96641', 'region': 'Asia', 'publication_date': '2012-10-23'}, {'article_id': '96986', 'region': 'Asia', 'publication_date': '2009-03-26'}, {'article_id': '99699', 'region': 'Africa', 'publication_date': '2022-07-15'}, {'article_id': '100613', 'region': 'Asia', 'publication_date': '2013-12-10'}, {'article_id': '101514', 'region': 'Europe', 'publication_date': '2017-01-14'}, {'article_id': '103003', 'region': 'Africa', 'publication_date': '2010-03-21'}, {'article_id': '103591', 'region': 'Africa', 'publication_date': '2007-08-11'}, {'article_id': '103695', 'region': 'South America', 'publication_date': '2006-12-14'}, {'article_id': '104123', 'region': 'Africa', 'publication_date': '2017-09-15'}, {'article_id': '104996', 'region': 'Africa', 'publication_date': '2005-09-21'}, {'article_id': '104998', 'region': 'South America', 'publication_date': '2016-02-13'}, {'article_id': '105804', 'region': 'Africa', 'publication_date': '2021-09-10'}, {'article_id': '106908', 'region': 'North America', 'publication_date': '2009-04-22'}, {'article_id': '107036', 'region': 'Asia', 'publication_date': '2004-09-16'}, {'article_id': '108586', 'region': 'Africa', 'publication_date': '2011-10-10'}, {'article_id': '109601', 'region': 'Africa', 'publication_date': '2015-08-02'}, {'article_id': '110096', 'region': 'Asia', 'publication_date': '2006-07-12'}, {'article_id': '111422', 'region': 'South America', 'publication_date': '2019-10-29'}, {'article_id': '112063', 'region': 'North America', 'publication_date': '2009-09-05'}, {'article_id': '112770', 'region': 'Asia', 'publication_date': '2010-03-23'}, {'article_id': '113058', 'region': 'Asia', 'publication_date': '2022-07-09'}, {'article_id': '116698', 'region': 'South America', 'publication_date': '2022-10-18'}, {'article_id': '119651', 'region': 'Europe', 'publication_date': '2021-12-28'}, {'article_id': '119920', 'region': 'Asia', 'publication_date': '2005-11-10'}, {'article_id': '120129', 'region': 'North America', 'publication_date': '2007-03-27'}, {'article_id': '120765', 'region': 'Europe', 'publication_date': '2019-03-05'}, {'article_id': '122137', 'region': 'South America', 'publication_date': '2008-10-06'}, {'article_id': '123747', 'region': 'Europe', 'publication_date': '2022-05-06'}, {'article_id': '124509', 'region': 'Africa', 'publication_date': '2019-05-23'}, {'article_id': '126412', 'region': 'Asia', 'publication_date': '2004-02-14'}, {'article_id': '126655', 'region': 'Asia', 'publication_date': '2008-04-24'}, {'article_id': '126966', 'region': 'North America', 'publication_date': '2022-01-30'}], 'var_call_3lmny9zBE5mQ02lbOsOCJfuP': [{'_id': '695992c0a2d3bcbb1e68453a', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '695992c0a2d3bcbb1e684ceb', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '695992c0a2d3bcbb1e684f96', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '695992c0a2d3bcbb1e685025', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '695992c0a2d3bcbb1e6851f5', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
