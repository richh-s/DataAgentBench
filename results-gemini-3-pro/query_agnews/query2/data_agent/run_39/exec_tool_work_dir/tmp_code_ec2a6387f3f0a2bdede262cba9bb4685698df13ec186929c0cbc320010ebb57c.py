code = """import json

# Load the articles from the file
file_path = locals()['var_function-call-9199530308123591561']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords
keywords = {
    'Sci/Tech': [
        'science', 'technology', 'computer', 'tech', 'software', 'hardware', 'internet', 'web', 'mobile', 'phone', 
        'digital', 'data', 'electronic', 'device', 'gadget', 'robot', 'space', 'nasa', 'mars', 'moon', 'orbit', 
        'biotech', 'biology', 'physics', 'chemistry', 'research', 'study', 'experiment', 'innovat', 'invent', 
        'google', 'microsoft', 'apple', 'ibm', 'intel', 'linux', 'window', 'server', 'network', 'virus', 'security', 
        'hack', 'gaming', 'video game', 'console', 'nintendo', 'sony', 'xbox', 'playstation', 'wii', 'browser', 
        'chip', 'satellite', 'telescope', 'astronomy', 'genetics', 'stem cell', 'lab', 'laboratory', 'scientist', 'gameboy', 
        'sendo', 'emc', 'shuttle', 'mission', 'probe', 'capsule', 'sun', 'solar', 'physicist', 'nuclear', 'online'
    ],
    'Sports': [
        'sport', 'football', 'soccer', 'baseball', 'basketball', 'hockey', 'tennis', 'golf', 'team', 'match', 
        'cup', 'league', 'tournament', 'player', 'coach', 'champion', 'olympic', 'medal', 'athlete', 'stadium', 
        'club', 'nba', 'nfl', 'mlb', 'nhl', 'fifa', 'espn', 'racing', 'f1', 'rugby', 'cricket', 'bowling', 
        'boxing', 'wrestling', 'red sox', 'broncos', 'cornerback', 'touchdown', 'quarterback', 'sox', 'yankees', 
        'mets', 'dodgers', 'giants', 'game', 'open', 'final', 'round', 'score', 'win', 'loss', 'defeat', 'victory', 'prize'
    ],
    'Business': [
        'business', 'company', 'corp', 'inc', 'market', 'stock', 'share', 'trade', 'economy', 'economic', 
        'finance', 'financial', 'money', 'profit', 'revenue', 'bank', 'invest', 'inflation', 'dollar', 'euro', 
        'oil', 'price', 'ceo', 'manager', 'industry', 'deal', 'merger', 'acquisition', 'nasdaq', 'dow', 
        'wall street', 'fed', 'sales', 'retail', 'kroger', 'bhp', 'earnings', 'wto'
    ],
    'World': [
        'world', 'international', 'nation', 'country', 'government', 'politic', 'president', 'minister', 'war', 
        'peace', 'military', 'army', 'terror', 'bomb', 'attack', 'treaty', 'un', 'united nations', 'eu', 'europe', 
        'asia', 'africa', 'america', 'china', 'russia', 'iraq', 'iran', 'korea', 'israel', 'palestin', 'election', 
        'vote', 'law', 'court', 'police', 'crime', 'blast', 'kill', 'soldier', 'troop', 'baghdad', 'kabul', 
        'gaza', 'nepal', 'kathmandu', 'somalia', 'parliament', 'premier', 'settlement'
    ]
}

def classify_article(title, description):
    text = (title + " " + description).lower()
    scores = {cat: 0 for cat in keywords}
    
    for cat, kws in keywords.items():
        for kw in kws:
            if kw in text:
                scores[cat] += 1
    
    # Heuristics
    if 'gameboy' in text: scores['Sci/Tech'] += 5
    if 'video game' in text: scores['Sci/Tech'] += 5
    if 'space' in text and 'nasa' in text: scores['Sci/Tech'] += 5
    if 'company' in text and 'profit' in text: scores['Business'] += 3
    if 'stock' in text: scores['Business'] += 2
    
    # Title override
    title_lower = title.lower()
    if 'science' in title_lower or 'technology' in title_lower:
        scores['Sci/Tech'] += 5
    
    # Iraq Science case
    if 'physicist' in text and 'science' in text:
        scores['Sci/Tech'] += 3

    if max(scores.values()) == 0:
        return 'Unclassified'
    
    return max(scores, key=scores.get)

sci_tech_count = 0
total_articles = len(articles)
results = []
sci_tech_titles = []

for article in articles:
    cat = classify_article(article['title'], article['description'])
    if cat == 'Sci/Tech':
        sci_tech_count += 1
        sci_tech_titles.append(article['title'])
    results.append({'title': article['title'], 'category': cat})

fraction = sci_tech_count / total_articles if total_articles > 0 else 0

print("__RESULT__:")
print(json.dumps({
    "total": total_articles,
    "sci_tech_count": sci_tech_count,
    "fraction": fraction,
    "sci_tech_titles": sci_tech_titles
}))"""

env_args = {'var_function-call-5520770230741570478': [{'author_id': '218'}], 'var_function-call-1765907926053791448': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-17752405224963583855': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-12633397177033374312': [{'_id': '6944b32529e792ed571cb552', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944b32529e792ed571cbd03', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944b32529e792ed571cbfae', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944b32529e792ed571cc03d', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944b32629e792ed571cc20d', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-4123908612029420578': {'total': 5, 'sci_tech_count': 2, 'fraction': 0.4, 'samples': [{'title': 'GameBoy mini-games win prize', 'category': 'Sports'}, {'title': 'Bailey Tries WR', 'category': 'Unclassified'}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'category': 'Sci/Tech'}, {'title': 'Energy from waves  teenager wins science award', 'category': 'Sci/Tech'}, {'title': 'China #39;s appetite boosts BHP', 'category': 'Business'}]}, 'var_function-call-8297460590678966374': ['192', '2161', '2844', '2987', '3451', '3970', '4447', '5354', '6705', '6869', '8962', '9677', '9858', '14861', '15100', '15473', '17491', '19469', '20362', '21238', '22354', '23914', '24495', '25960', '26535', '27429', '28079', '29164', '29297', '33489', '35408', '35882', '36182', '36483', '37042', '38608', '39117', '39623', '40545', '41616', '46531', '47439', '48635', '48833', '49035', '52459', '54906', '57510', '57860', '57918', '62404', '62754', '64102', '66827', '68509', '68958', '69262', '69393', '70498', '70608', '72525', '73025', '73684', '78200', '80578', '80853', '81851', '82526', '82668', '83273', '88553', '88911', '89666', '91286', '91822', '92992', '93287', '93804', '94618', '96641', '96986', '99699', '100613', '101514', '103003', '103591', '103695', '104123', '104996', '104998', '105804', '106908', '107036', '108586', '109601', '110096', '111422', '112063', '112770', '113058', '116698', '119651', '119920', '120129', '120765', '122137', '123747', '124509', '126412', '126655', '126966'], 'var_function-call-157265943838128203': [], 'var_function-call-10224826839132847756': [{'_id': '6944b32529e792ed571cb552', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}], 'var_function-call-16376811892770501229': [], 'var_function-call-9199530308123591561': 'file_storage/function-call-9199530308123591561.json', 'var_function-call-15853279929925465012': {'total': 111, 'sci_tech_count': 18, 'fraction': 0.16216216216216217, 'samples': [{'title': 'GameBoy mini-games win prize', 'category': 'Sci/Tech'}, {'title': 'Bailey Tries WR', 'category': 'Sports'}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'category': 'Sci/Tech'}, {'title': 'Energy from waves  teenager wins science award', 'category': 'Sci/Tech'}, {'title': 'China #39;s appetite boosts BHP', 'category': 'Business'}, {'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'category': 'Business'}, {'title': 'Even in win, nasty vibes', 'category': 'World'}, {'title': 'Gas stoppage may have caused deadly Belgian blast: TV report (AFP)', 'category': 'World'}, {'title': 'Raffarin pledges to be  quot;extremely severe quot; against anti-semitism &lt;b&gt;...&lt;/b&gt;', 'category': 'World'}, {'title': 'Somalians sworn in', 'category': 'World'}, {'title': 'Muenzer races for gold', 'category': 'Sports'}, {'title': 'Israelis to Expand West Bank Settlements', 'category': 'World'}, {'title': 'Stocks End Up as Oil Prices Fall', 'category': 'Business'}, {'title': 'WTO Rejects U.S. Appeal on Canadian Wheat', 'category': 'World'}, {'title': 'Capriati Scrambles Past Chladkova Challenge at Open', 'category': 'World'}, {'title': 'In Iraq, a Quest to Rebuild One More Broken Edifice: Science', 'category': 'World'}, {'title': 'UPDATE: Intel lowers Q3 revenue estimates', 'category': 'Business'}, {'title': 'Calm as Kathmandu curfew lifted', 'category': 'World'}, {'title': 'Israeli Missiles Kill 13 Militants', 'category': 'World'}, {'title': 'Serena Blasts Umpire After Dramatic Defeat', 'category': 'World'}]}}

exec(code, env_args)
