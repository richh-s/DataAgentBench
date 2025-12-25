code = """import json

# Load data from file
with open(locals()['var_function-call-8890472594505631149'], 'r') as f:
    articles = json.load(f)

# Keywords definition
categories = {
    'Science/Technology': [
        'science', 'technology', 'tech', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 'net', 'cyber', 'digital', 'mobile', 'phone', 'wireless', 'broadband', 'satellite', 'space', 'nasa', 'astronomy', 'telescope', 'planet', 'mars', 'robot', 'robotics', 'gadget', 'device', 'console', 'game', 'gaming', 'video game', 'nintendo', 'sony', 'microsoft', 'google', 'apple', 'ibm', 'intel', 'linux', 'windows', 'browser', 'search', 'chip', 'processor', 'data', 'server', 'security', 'virus', 'hacker', 'physics', 'biology', 'chemistry', 'medical', 'research', 'lab', 'scientist', 'discovery', 'innovation', 'invention', 'engine', 'fuel', 'energy', 'battery', 'electric', 'hybrid', 'gps', 'screen', 'display', 'camera', 'video', 'mp3', 'ipod', 'facebook', 'blog', 'app', 'application', 'download', 'upload', 'stream', 'smartphone', 'tablet', 'laptop', 'notebook', 'pc', 'malware', 'spam', 'email', 'genetics', 'genome', 'clone', 'cloning', 'disease', 'vaccine', 'treatment', 'therapy', 'drug', 'pharmaceutical', 'doctor', 'surgeon', 'hospital', 'patient', 'health', 'cancer', 'aids', 'hiv', 'automotive', 'vehicle', 'auto', 'car'
    ],
    'Business': [
        'business', 'economy', 'economic', 'market', 'stock', 'share', 'trade', 'finance', 'financial', 'invest', 'investment', 'investor', 'bank', 'banking', 'money', 'currency', 'dollar', 'euro', 'pound', 'yen', 'inflation', 'rate', 'tax', 'budget', 'debt', 'deficit', 'gdp', 'recession', 'growth', 'profit', 'loss', 'revenue', 'earnings', 'quarter', 'ceo', 'cfo', 'chairman', 'executive', 'manager', 'company', 'corporation', 'inc', 'ltd', 'plc', 'merger', 'acquisition', 'deal', 'buyout', 'bid', 'price', 'oil', 'gold', 'commodity', 'industry', 'manufacturing', 'retail', 'sales', 'consumer', 'spending', 'job', 'unemployment', 'employment', 'labor', 'strike', 'union', 'workforce', 'salary', 'wage', 'bonus', 'compensation', 'wall street', 'dow jones', 'nasdaq', 's&p', 'market', 'exchange'
    ],
    'Sports': [
        'sport', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'cricket', 'rugby', 'hockey', 'f1', 'formula 1', 'racing', 'athlete', 'player', 'team', 'coach', 'manager', 'referee', 'umpire', 'stadium', 'league', 'tournament', 'championship', 'world cup', 'olympic', 'medal', 'gold', 'silver', 'bronze', 'score', 'match', 'vs', 'defeat', 'victory', 'win', 'lose', 'draw', 'season', 'club', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'cup', 'bowl', 'super bowl', 'playoff', 'final', 'semi-final', 'quarter-final', 'record', 'rank', 'ranking', 'title', 'trophy', 'award', 'prize', 'contract', 'trade', 'transfer', 'sign', 'draft', 'roster', 'lineup', 'squad', 'injury', 'injured', 'fitness', 'training', 'practice', 'game', 'play'
    ],
    'World': [
        'world', 'international', 'politic', 'government', 'president', 'minister', 'prime minister', 'senator', 'congress', 'parliament', 'election', 'vote', 'poll', 'campaign', 'party', 'democrat', 'republican', 'war', 'peace', 'military', 'army', 'soldier', 'troop', 'weapon', 'bomb', 'blast', 'attack', 'terror', 'terrorist', 'police', 'crime', 'court', 'judge', 'law', 'legal', 'prison', 'jail', 'crash', 'accident', 'disaster', 'earthquake', 'quake', 'flood', 'storm', 'hurricane', 'typhoon', 'tsunami', 'fire', 'protest', 'strike', 'riot', 'un', 'united nations', 'eu', 'european union', 'nato', 'treaty', 'agreement', 'talks', 'negotiation', 'sanction', 'crisis', 'hostage', 'kidnap', 'kill', 'die', 'death', 'murder', 'assassin', 'iraq', 'iran', 'afghanistan', 'syria', 'israel', 'palestine', 'gaza', 'ukraine', 'russia', 'china', 'usa', 'america', 'britain', 'uk', 'france', 'germany', 'japan', 'korea', 'india', 'pakistan', 'africa', 'asia', 'europe', 'middle east', 'latin america'
    ]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in categories}
    
    # Special handling for "game"
    if 'game' in text:
        if any(x in text for x in ['video', 'console', 'nintendo', 'sony', 'xbox', 'playstation', 'wii', 'psp', 'ds', 'gamer', 'software', 'computer', 'app']):
            scores['Science/Technology'] += 2
        elif any(x in text for x in ['league', 'season', 'coach', 'team', 'score', 'player', 'football', 'soccer', 'basketball', 'baseball', 'sport']):
            scores['Sports'] += 2
        else:
            pass
            
    for cat, keywords in categories.items():
        for kw in keywords:
            if kw in text:
                scores[cat] += 1
                
    # Tie-breaking logic
    if scores['Business'] > 0 and scores['Business'] == scores['Science/Technology']:
        if any(x in text for x in ['profit', 'stock', 'market', 'price', 'revenue', 'earnings']):
            scores['Business'] += 0.5
        else:
            scores['Science/Technology'] += 0.5

    if scores['World'] > 0 and scores['World'] == scores['Business']:
        if any(x in text for x in ['oil', 'price', 'trade', 'economy']):
            scores['Business'] += 0.5
        else:
            scores['World'] += 0.5

    best_cat = max(scores, key=scores.get)
    if scores[best_cat] == 0:
        return 'Unknown'
    return best_cat

count_tech = 0
total = len(articles)
tech_articles = []
unknowns = []

for article in articles:
    content = article['title'] + " " + article['description']
    category = classify(content)
    if category == 'Science/Technology':
        count_tech += 1
        tech_articles.append(article['title'])
    elif category == 'Unknown':
        unknowns.append(article['title'])

fraction = count_tech / total if total > 0 else 0

print("__RESULT__:")
print(json.dumps({
    "total": total,
    "tech_count": count_tech,
    "fraction": fraction,
    "tech_titles": tech_articles,
    "unknown_titles": unknowns
}))"""

env_args = {'var_function-call-1906537309967263117': [{'author_id': '218'}], 'var_function-call-5709472438726771711': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-17909720089859425106': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-297000811844011230': [{'_id': '694490f02428956e8cd47527', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '694490f02428956e8cd47cd8', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '694490f02428956e8cd47f83', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '694490f02428956e8cd48012', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '694490f02428956e8cd481e2', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-15914433034883532203': {'total': 5, 'tech_count': 2, 'fraction': 0.4, 'tech_titles': ['Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award']}, 'var_function-call-10807431161713777386': {'collection': 'articles', 'filter': {'article_id': {'$in': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966']}}, 'limit': 1000}, 'var_function-call-8381450025324353668': [], 'var_function-call-3659053493903667129': [{'_id': '694490f02428956e8cd483e9', 'article_id': '3970', 'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'description': "AP - A closely watched measure of future economic activity fell in July for the second consecutive month, reinforcing evidence that the nation's financial recovery is slackening."}], 'var_function-call-545561953397492683': [{'_id': '694490f02428956e8cd483e9', 'article_id': '3970', 'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'description': "AP - A closely watched measure of future economic activity fell in July for the second consecutive month, reinforcing evidence that the nation's financial recovery is slackening."}, {'_id': '694490f02428956e8cd485c6', 'article_id': '4447', 'title': 'Even in win, nasty vibes', 'description': 'ATHENS -- As you saw yesterday, they #39;re fighting back now. Not with the world, but with themselves. When you #39;ve been humiliated at your own game, ridiculed and laughed at back home and can #39;t intimidate Australia anymore, someone #39;s bound to mope. '}, {'_id': '694490f02428956e8cd48951', 'article_id': '5354', 'title': 'Gas stoppage may have caused deadly Belgian blast: TV report (AFP)', 'description': 'AFP - A Belgian gas explosion in which 20 people were killed may have resulted from a combination of a halt in the gas circulation in a pipeline and existing damage to the main, Belgian television said.'}, {'_id': '694490f02428956e8cd48e98', 'article_id': '6705', 'title': 'Raffarin pledges to be  quot;extremely severe quot; against anti-semitism &lt;b&gt;...&lt;/b&gt;', 'description': 'French Prime Minister Jean-Pierre Raffarin declared Sunday that  quot;France will be extremely severe against those who perpetrate anti-semitism, quot; after visiting the Jewish social '}, {'_id': '694490f02428956e8cd48f3c', 'article_id': '6869', 'title': 'Somalians sworn in', 'description': 'NAIROBI International mediators swore in members of Somalia #39;s new Parliament on Sunday, a move seen as a crucial step toward establishing the first central government in the country since 1991.'}], 'var_function-call-7892788794540350277': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}, 'limit': 200}, 'var_function-call-8890472594505631149': 'file_storage/function-call-8890472594505631149.json'}

exec(code, env_args)
