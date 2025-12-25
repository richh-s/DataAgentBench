code = """import json

# Load articles
articles = locals()['var_function-call-5633925291875905896']
if isinstance(articles, str):
    # It might be a file path if large, though for ~100 articles it might be direct list
    # But let's handle the case if it's a string (file path) or list
    pass 
    # Check type
# Actually the tool output says "The result is: [...]" so it is a list in the variable if it fits.
# If it was large, it would be a file path. The preview was short but the key contains the data.
# Wait, if the data is large, the variable holds a file path string.
# The previous output was a list in the preview, but usually the system stores the full result in the variable.
# If the full result is large, the variable is a filename.
# Let's check the type of the variable.

# Define keywords
categories = {
    'Science/Technology': [
        'science', 'technology', 'tech', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 'digital', 'mobile', 'phone', 
        'game', 'gaming', 'video game', 'console', 'nintendo', 'sony', 'microsoft', 'apple', 'google', 'space', 'nasa', 'astronomy', 
        'biology', 'physics', 'chemistry', 'research', 'study', 'innovation', 'robot', 'ai', 'cyber', 'network', 'data', 'chip', 
        'processor', 'satellite', 'rocket', 'mars', 'moon', 'intel', 'amd', 'linux', 'windows', 'browser', 'virus', 'hacker', 
        'security', 'patent', 'lab', 'scientist', 'engineer', 'math', 'ipod', 'iphone', 'gadget', 'device', 'electronic', 
        'telecom', 'wireless', 'broadband', 'gps', 'voip', 'blog', 'spam', 'spyware', 'malware', 'server', 'database', 'algorithm',
        'supercomputer', 'nanotech', 'biotech', 'cloning', 'stem cell', 'genetics', 'genome', 'dna', 'fossil', 'archeology', 'climate change',
        'global warming', 'environment', 'energy', 'solar', 'wind power', 'nuclear', 'battery', 'fuel cell', 'hybrid'
    ],
    'Business': [
        'business', 'economy', 'market', 'stock', 'share', 'profit', 'loss', 'revenue', 'sale', 'deal', 'merger', 'acquisition', 
        'company', 'corp', 'inc', 'firm', 'bank', 'finance', 'financial', 'invest', 'investor', 'trade', 'tariff', 'budget', 
        'tax', 'ceo', 'cfo', 'executive', 'manager', 'industry', 'sector', 'retail', 'sales', 'consumer', 'price', 'cost', 
        'inflation', 'rate', 'dollar', 'euro', 'currency', 'oil', 'gold', 'commodity', 'audit', 'accounting', 'scandal', 
        'bankruptcy', 'debt', 'loan', 'credit', 'mortgage', 'insurance', 'fund', 'hedge', 'equity', 'venture', 'capital', 
        'nasdaq', 'dow', 'wall street', 'fed', 'federal reserve', 'treasury', 'imf', 'wto', 'opec', 'gdp', 'growth', 'recession'
    ],
    'Sports': [
        'sport', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'cricket', 'rugby', 'hockey', 'f1', 'racing', 
        'olympic', 'league', 'cup', 'championship', 'tournament', 'match', 'game', 'score', 'win', 'lose', 'team', 'player', 
        'coach', 'athlete', 'medal', 'stadium', 'club', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'premier league', 'bundesliga', 
        'serie a', 'liga', 'wimbledon', 'open', 'grand slam', 'super bowl', 'world series', 'playoff', 'final', 'semi-final', 
        'quarter-final', 'goal', 'touchdown', 'homerun', 'basket', 'points', 'record', 'rank', 'seed', 'draw', 'fixture', 
        'result', 'standings', 'table', 'transfer', 'contract', 'draft', 'season', 'injury', 'suspended', 'ban', 'doping'
    ],
    'World': [
        'world', 'politics', 'government', 'president', 'minister', 'election', 'vote', 'war', 'peace', 'military', 'army', 
        'police', 'court', 'law', 'crime', 'attack', 'bomb', 'terror', 'disaster', 'quake', 'flood', 'storm', 'country', 
        'nation', 'international', 'treaty', 'un', 'eu', 'nato', 'iraq', 'iran', 'china', 'usa', 'uk', 'russia', 'afghanistan',
        'israel', 'palestine', 'syria', 'korea', 'japan', 'germany', 'france', 'canada', 'australia', 'india', 'pakistan', 
        'africa', 'asia', 'europe', 'middle east', 'latin america', 'diplomat', 'ambassador', 'embassy', 'foreign', 'policy', 
        'parliament', 'congress', 'senate', 'democrat', 'republican', 'prime minister', 'chancellor', 'premier', 'official', 
        'authority', 'regime', 'rebel', 'insurgent', 'guerrilla', 'militant', 'troop', 'force', 'weapon', 'nuclear', 'missile'
    ]
}

# Adjust weights or handle specific overlaps
# e.g. "game" in Sports vs Science/Tech
# We can give "video game" a high weight in Science/Tech.
# We can make "game" in Sports have normal weight, but if "video" is present, it's likely Tech.

def classify(title, desc):
    text = (title + " " + desc).lower()
    scores = {cat: 0 for cat in categories}
    
    for cat, keywords in categories.items():
        for kw in keywords:
            if kw in text:
                # Simple presence check or count? Count is better.
                count = text.count(kw)
                scores[cat] += count
    
    # Refinements
    if "video game" in text or "computer game" in text or "gameboy" in text or "xbox" in text or "playstation" in text:
        scores['Science/Technology'] += 5
    if "football" in text or "soccer" in text or "baseball" in text or "basketball" in text or "nfl" in text:
        scores['Sports'] += 5
    if "oil prices" in text or "wall street" in text:
        scores['Business'] += 5
    if "iraq" in text or "president" in text or "prime minister" in text:
        scores['World'] += 2
        
    # Find max
    best_cat = max(scores, key=scores.get)
    # If all zero, default? Or maybe check for specific named entities.
    # Assuming the keywords cover most cases.
    return best_cat

sci_tech_count = 0
total = 0
classified_articles = []

if isinstance(articles, str):
    with open(articles, 'r') as f:
        articles = json.load(f)

for art in articles:
    cat = classify(art['title'], art['description'])
    if cat == 'Science/Technology':
        sci_tech_count += 1
    total += 1
    classified_articles.append({'title': art['title'], 'category': cat})

fraction = sci_tech_count / total if total > 0 else 0

print("__RESULT__:")
print(json.dumps({"sci_tech_count": sci_tech_count, "total": total, "fraction": fraction, "examples": classified_articles[:10]}))"""

env_args = {'var_function-call-6662935517033330840': [{'author_id': '218'}], 'var_function-call-15748058870014949447': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-6181483843519041997': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-16210141842112754731': {'collection': 'articles', 'filter': {'article_id': {'$in': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966]}}}, 'var_function-call-5633925291875905896': [{'_id': '69448fb5a863498f5fcef985', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '69448fb5a863498f5fcf0136', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '69448fb5a863498f5fcf03e1', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '69448fb5a863498f5fcf0470', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '69448fb5a863498f5fcf0640', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
