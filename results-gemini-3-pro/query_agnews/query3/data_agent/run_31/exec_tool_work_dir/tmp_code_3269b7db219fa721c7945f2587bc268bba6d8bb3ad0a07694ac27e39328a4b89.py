code = """import json
import re

# Load metadata
with open(locals()['var_function-call-8183838540505517503'], 'r') as f:
    metadata_list = json.load(f)

# Map: article_id (int) -> year (int)
article_year_map = {}
for entry in metadata_list:
    aid = int(entry['article_id'])
    date = entry['publication_date'] # YYYY-MM-DD
    year = int(date[:4])
    if 2010 <= year <= 2020:
        article_year_map[aid] = year

# Load articles
with open(locals()['var_function-call-2099450314476746898'], 'r') as f:
    articles_list = json.load(f)

business_keywords = {
    'market', 'stock', 'stocks', 'share', 'shares', 'economy', 'economic', 'finance', 'financial',
    'bank', 'banking', 'fund', 'funds', 'money', 'trade', 'trading', 'investment', 'investor', 'investing',
    'profit', 'profits', 'revenue', 'revenues', 'loss', 'losses', 'wall st', 'wall street', 
    'dow', 'dow jones', 'nasdaq', 'tax', 'taxes', 'rate', 'rates', 'price', 'prices', 
    'oil', 'crude', 'gas', 'gold', 'dollar', 'euro', 'yen', 'currency', 
    'company', 'companies', 'corp', 'corporation', 'inc', 'business', 'businesses', 
    'industry', 'industrial', 'deal', 'deals', 'merger', 'acquisition', 'bid', 'bidding', 
    'sale', 'sales', 'budget', 'deficit', 'fed', 'federal reserve', 'treasury', 
    'yield', 'loan', 'loans', 'credit', 'debt', 'debts', 'ceo', 'cfo', 'executive', 
    'growth', 'inflation', 'recession', 'spending', 'cost', 'costs', 'retail', 'retailer'
}

def is_business(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    words = set(text.split())
    if words.intersection(business_keywords):
        return True
    return False

counts = {y: 0 for y in range(2010, 2021)}
processed_ids = set()

for article in articles_list:
    try:
        aid = int(article.get('article_id', -1))
    except:
        continue
        
    if aid in article_year_map:
        processed_ids.add(aid)
        year = article_year_map[aid]
        text = (article.get('title', '') + ' ' + article.get('description', ''))
        if is_business(text):
            counts[year] += 1

# Calculate average
total_business = sum(counts.values())
num_years = 11
average = total_business / num_years

missing_count = len(article_year_map) - len(processed_ids)

print("__RESULT__:")
print(json.dumps({
    "counts": counts,
    "average": average,
    "total_business": total_business,
    "processed_articles": len(processed_ids),
    "total_europe_ids": len(article_year_map),
    "missing_ids": missing_count
}))"""

env_args = {'var_function-call-8183838540505517503': 'file_storage/function-call-8183838540505517503.json', 'var_function-call-1505226483977166881': 'file_storage/function-call-1505226483977166881.json', 'var_function-call-5130672257415933786': 14860, 'var_function-call-13256661063451631781': [{'_id': '6944dadf33aefa6592744307', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944dadf33aefa6592744308', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944dadf33aefa6592744309', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944dadf33aefa659274430a', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944dadf33aefa659274430b', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-3261169261183607461': [{'_id': '6944dadf33aefa6592744307', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '6944dadf33aefa6592744308', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '6944dadf33aefa6592744309', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '6944dadf33aefa659274430a', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '6944dadf33aefa659274430b', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-11579754966878934648': 'file_storage/function-call-11579754966878934648.json', 'var_function-call-3405369895194988491': {'counts': {'2010': 79, '2011': 84, '2012': 75, '2013': 87, '2014': 79, '2015': 82, '2016': 81, '2017': 76, '2018': 91, '2019': 72, '2020': 80}, 'average': 80.54545454545455, 'total': 886}, 'var_function-call-7610349528603753187': {'total_europe_articles': 2273, 'rejected_samples': ["Wall St. Bears Claw Back Into the Black  NEW YORK (Reuters) - Short-sellers, Wall Street's dwindling  band of ultra-cynics, are seeing green again.", 'Oldsmobile: The final parking lot Why General Motors dropped the Oldsmobile. The four brand  paradoxes GM had to face - the name, the product, image re-positioning, and the consumer - all added up to a brand that had little hope of rebranding.', "Best Asian Tourism Destinations The new APMF survey of the best Asian tourism destinations has just kicked off, but it's crowded at the top, with Chiang Mai in Thailand just leading from perennial favourites Hong Kong, Bangkok and Phuket in Thailand, and Bali in  Indonesia. Be one of the first to vote and let us know your reasons.", 'IT alligator tales I grew up in New York, where giant alligators -- sometimes more ornately described as albino alligators -- were rumored to roam the citys sewer systems. According to legend, vacationers picked up the tiny crocodilians in Florida, brought them home to New York, and eventually flushed the little buggers when they grew too big for the local concrete jungle.', '\'Madden,\' \'ESPN\' Football Score in Different Ways (Reuters) Reuters - Was absenteeism a little high\\on Tuesday among the guys at the office? EA Sports would like\\to think it was because "Madden NFL 2005" came out that day,\\and some fans of the football simulation are rabid enough to\\take a sick day to play it.'], 'accepted_samples': ['Iraq Halts Oil Exports from Main Southern Pipeline (Reuters) Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.', "Google IPO Auction Off to Rocky Start  WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators.", "Dollar Falls Broadly on Record Trade Gap  NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap.", 'Eurozone economy keeps growing Official figures show the 12-nation eurozone economy continues to grow, but there are warnings it may slow down later in the year.', 'HP shares tumble on profit news Hewlett-Packard shares fall after disappointing third-quarter profits, while the firm warns the final quarter will also fall short of expectations.']}, 'var_function-call-10264674098373291287': 127583, 'var_function-call-2099450314476746898': 'file_storage/function-call-2099450314476746898.json'}

exec(code, env_args)
