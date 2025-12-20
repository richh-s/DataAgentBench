code = """import json
import collections

# Load the articles
data = locals()['var_function-call-10141879319172260391']

if isinstance(data, str):
    with open(data, 'r') as f:
        articles = json.load(f)
else:
    articles = data

# Define keywords
categories = {
    'Science/Technology': [
        'science', 'technology', 'tech', 'computer', 'software', 'hardware', 'internet', 'web', 'online', 
        'digital', 'mobile', 'phone', 'wireless', 'network', 'broadband', 'satellite', 'space', 'nasa', 
        'astronomy', 'biology', 'physics', 'chemistry', 'research', 'study', 'experiment', 'lab', 'scientist',
        'innovation', 'robot', 'gadget', 'device', 'engine', 'motor', 'battery', 'energy', 'power', 
        'nuclear', 'solar', 'wind', 'medical', 'health', 'disease', 'virus', 'cancer', 'treatment', 'drug', 
        'pharmaceutical', 'gene', 'dna', 'cell', 'microsoft', 'google', 'apple', 'intel', 'ibm', 'linux', 
        'windows', 'browser', 'server', 'data', 'cyber', 'hack', 'security', 'video game', 'gaming', 'console', 
        'nintendo', 'sony', 'xbox', 'playstation', 'wii', 'gameboy', 'ds', 'ipod', 'iphone', 'mp3', 'dvd', 
        'hdtv', 'pixel', 'camera', 'lens', 'telescope', 'microscope', 'silicon', 'chip', 'processor', 
        'semiconductor', 'email', 'spam', 'blog', 'forum', 'chat', 'message', 'search engine', 'download', 
        'upload', 'file', 'format', 'app', 'application', 'program', 'code', 'coding', 'algorithm', 'system',
        'machine', 'electric', 'electronic', 'virtual', 'reality', 'ai', 'artificial intelligence', 'smart',
        'nanotech', 'biotech', 'genetics', 'cloning', 'stem cell', 'laser', 'radiation', 'orbit', 'mission',
        'launch', 'shuttle', 'mars', 'moon', 'planet', 'galaxy', 'universe', 'comet', 'asteroid', 'meteor',
        'fossil', 'evolution', 'climate', 'warming', 'environment', 'ecology', 'nature', 'weather', 'forecast'
    ],
    'Sports': [
        'sport', 'game', 'match', 'team', 'player', 'coach', 'manager', 'season', 'league', 'cup', 
        'championship', 'tournament', 'olympics', 'olympic', 'medal', 'football', 'soccer', 'basketball', 
        'baseball', 'hockey', 'tennis', 'golf', 'cricket', 'rugby', 'racing', 'f1', 'formula 1', 'nascar', 
        'boxing', 'wrestling', 'athlete', 'stadium', 'score', 'goal', 'touchdown', 'run', 'wicket', 'win', 
        'loss', 'defeat', 'victory', 'standings', 'rank', 'club', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 
        'world cup', 'super bowl', 'playoff', 'final', 'semi-final', 'quarter-final', 'round', 'heat', 'race',
        'driver', 'rider', 'cyclist', 'swimmer', 'gymnast', 'skier', 'skater', 'court', 'field', 'pitch', 'bat',
        'ball', 'racket', 'club', 'net', 'basket', 'helmet', 'jersey', 'uniform', 'referee', 'umpire', 'fan',
        'supporter', 'spectator', 'ticket', 'transfer', 'trade', 'draft', 'contract', 'signing', 'injury', 
        'doping', 'drug test', 'record', 'title', 'trophy', 'award', 'mvp', 'all-star', 'pro bowl'
    ],
    'Business': [
        'business', 'economy', 'economic', 'market', 'stock', 'share', 'trade', 'finance', 'financial', 
        'invest', 'investment', 'investor', 'bank', 'banking', 'money', 'currency', 'dollar', 'euro', 'yen', 
        'inflation', 'recession', 'growth', 'profit', 'loss', 'revenue', 'earning', 'sale', 'sales', 'retail', 
        'consumer', 'company', 'corp', 'corporation', 'firm', 'industry', 'sector', 'ceo', 'cfo', 'manager', 
        'executive', 'deal', 'merger', 'acquisition', 'buyout', 'offer', 'bid', 'price', 'cost', 'tax', 'rate', 
        'job', 'unemployment', 'employment', 'hiring', 'strike', 'union', 'oil', 'gas', 'gold', 'commodity', 
        'wall street', 'dow jones', 'nasdaq', 'ftse', 'nikkei', 'exchange', 'index', 'bond', 'debt', 'loan', 
        'credit', 'mortgage', 'interest', 'fed', 'federal reserve', 'treasury', 'budget', 'deficit', 'surplus',
        'gdp', 'gross domestic product', 'export', 'import', 'tariff', 'wto', 'imf', 'world bank', 'commerce',
        'commercial', 'brand', 'marketing', 'advertising', 'product', 'service', 'supply', 'demand', 'forecast',
        'outlook', 'report', 'result', 'quarter', 'fiscal', 'shareholder', 'dividend', 'bankruptcy', 'default'
    ],
    'World': [
        'world', 'international', 'global', 'country', 'nation', 'government', 'politics', 'political', 
        'president', 'minister', 'leader', 'official', 'diplomat', 'diplomacy', 'treaty', 'agreement', 'war', 
        'peace', 'conflict', 'military', 'army', 'navy', 'air force', 'troop', 'soldier', 'weapon', 'bomb', 
        'blast', 'explosion', 'attack', 'terror', 'terrorist', 'terrorism', 'insurgent', 'rebel', 'police', 
        'crime', 'criminal', 'murder', 'killing', 'death', 'dead', 'injure', 'wound', 'casualty', 'victim', 
        'hostage', 'kidnap', 'arrest', 'jail', 'prison', 'court', 'judge', 'trial', 'jury', 'verdict', 'sentence',
        'law', 'legal', 'legislation', 'bill', 'act', 'election', 'vote', 'poll', 'ballot', 'campaign', 'candidate',
        'party', 'parliament', 'congress', 'senate', 'protest', 'demonstration', 'riot', 'strike', 'unrest', 
        'violence', 'crisis', 'disaster', 'earthquake', 'tsunami', 'flood', 'storm', 'hurricane', 'typhoon', 
        'cyclone', 'tornado', 'fire', 'wildfire', 'drought', 'famine', 'hunger', 'poverty', 'refugee', 'migrant',
        'immigration', 'border', 'visa', 'human rights', 'un', 'united nations', 'eu', 'european union', 'nato',
        'security council', 'general assembly', 'foreign', 'overseas', 'abroad', 'middle east', 'iraq', 'iran', 
        'afghanistan', 'pakistan', 'israel', 'palestine', 'syria', 'lebanon', 'egypt', 'libya', 'russia', 
        'china', 'north korea', 'usa', 'america', 'britain', 'uk', 'france', 'germany', 'japan', 'india'
    ]
}

def classify(text):
    text = text.lower()
    scores = {cat: 0 for cat in categories}
    
    for cat, keywords in categories.items():
        for keyword in keywords:
            # Simple substring match might be too aggressive (e.g. 'run' in 'running'), but standard for simple keyword scraping
            # Let's try word boundary aware if possible, or just count occurrences
            # For simplicity in this environment, simple count
            if " " + keyword + " " in " " + text + " ": # Simple word boundary check
                scores[cat] += 1
            elif keyword in text and len(keyword) > 4: # Allow partial match for longer words
                scores[cat] += 1
                
    # Specific adjustments
    if 'game' in text and ('video' in text or 'console' in text or 'software' in text):
        scores['Science/Technology'] += 2
        scores['Sports'] -= 1
        
    if max(scores.values()) == 0:
        return 'Unclassified'
        
    return max(scores, key=scores.get)

sci_tech_count = 0
total_count = 0
results = []

for article in articles:
    text = article.get('title', '') + " " + article.get('description', '')
    category = classify(text)
    results.append({'id': article['article_id'], 'title': article['title'], 'category': category})
    
    if category == 'Science/Technology':
        sci_tech_count += 1
    total_count += 1

print("__RESULT__:")
print(json.dumps({'sci_tech_count': sci_tech_count, 'total_count': total_count, 'fraction': sci_tech_count/total_count if total_count > 0 else 0}))"""

env_args = {'var_function-call-4587699973891036292': [{'author_id': '218'}], 'var_function-call-15977950178095477056': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-1143794527324699311': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-10141879319172260391': [{'_id': '6944b66048879920ec44191a', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944b66048879920ec4420cb', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944b66048879920ec442376', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944b66048879920ec442405', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944b66048879920ec4425d5', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}]}

exec(code, env_args)
