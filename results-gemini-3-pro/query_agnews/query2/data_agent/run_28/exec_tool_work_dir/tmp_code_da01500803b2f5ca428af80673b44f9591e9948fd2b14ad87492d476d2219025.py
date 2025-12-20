code = """import json
import re

with open(locals()['var_function-call-5617771522699572231'], 'r') as f:
    articles = json.load(f)

def classify_final(title, description):
    text = (title + " " + (description or "")).lower()
    
    # Pre-scoring based on phrases
    scores = {'Sci/Tech': 0, 'Business': 0, 'Sports': 0, 'World': 0}
    
    phrases = {
        'Sci/Tech': [
            'video game', 'mobile phone', 'cell phone', 'smart phone', 'artificial intelligence', 
            'virtual reality', 'solar power', 'fuel cell', 'open source', 'operating system', 
            'search engine', 'space shuttle', 'space station', 'stem cell', 'silicon valley',
            'science fiction', 'hard drive', 'mp3 player', 'digital camera', 'flat panel'
        ],
        'Business': [
            'stock market', 'wall street', 'interest rate', 'fed chief', 'federal reserve',
            'chief executive', 'dow jones', 'nasdaq', 's&p', 'initial public offering', 'hostile takeover',
            'quarterly profit', 'quarterly earnings', 'trade deficit', 'budget deficit'
        ],
        'Sports': [
            'red sox', 'white sox', 'yankees', 'mets', 'dodgers', 'giants', 'jets', 'patriots', 'cowboys',
            'packers', 'steelers', 'eagles', 'lakers', 'bulls', 'knicks', 'celtics', 'pistons', 'spurs',
            'heat', 'suns', 'warriors', 'manchester united', 'real madrid', 'barcelona', 'liverpool',
            'arsenal', 'chelsea', 'ac milan', 'juventus', 'bayern munich', 'formula one', 'tiger woods',
            'lance armstrong', 'michael phelps', 'serena williams', 'venus williams', 'maria sharapova',
            'pro bowl', 'super bowl', 'world cup', 'champions league', 'premier league', 'major league',
            'grand slam', 'ryder cup', 'davis cup', 'stanley cup', 'world series', 'olympic games'
        ],
        'World': [
            'united nations', 'prime minister', 'human rights', 'middle east', 'west bank', 'gaza strip',
            'white house', 'supreme court', 'security council', 'european union', 'red cross',
            'al qaeda', 'bin laden', 'saddam hussein', 'yasser arafat', 'ariel sharon', 'vladimir putin',
            'tony blair', 'george bush', 'john kerry', 'bill clinton', 'colin powell', 'condoleezza rice',
            'kofi annan', 'hillary clinton', 'pope john paul', 'dalai lama', 'nobel prize', 'war crimes'
        ]
    }
    
    for cat, plist in phrases.items():
        for p in plist:
            if p in text:
                scores[cat] += 3

    # Tokenize
    tokens = set(re.findall(r'\b[a-z0-9]+\b', text))
    
    # Word Lists (Single words)
    # Be careful with common words
    
    keywords = {
        'Sci/Tech': {
            'science', 'technology', 'computer', 'internet', 'software', 'hardware', 'web', 'online',
            'digital', 'cyber', 'robot', 'robotics', 'gadget', 'device', 'phone', 'mobile', 'wireless',
            'satellite', 'space', 'nasa', 'astronomy', 'telescope', 'planet', 'mars', 'moon', 'orbit',
            'biology', 'genetics', 'genome', 'dna', 'cloning', 'physics', 'laser', 'electron', 'quantum',
            'laboratory', 'lab', 'scientist', 'researcher', 'engineer', 'innovation', 'invention', 'patent',
            'microsoft', 'google', 'apple', 'intel', 'ibm', 'linux', 'unix', 'windows', 'java', 'browser',
            'server', 'database', 'network', 'broadband', 'wifi', 'bluetooth', 'virus', 'worm', 'hacker',
            'spam', 'spyware', 'phishing', 'encryption', 'firewall', 'chip', 'processor', 'semiconductor',
            'nintendo', 'sony', 'xbox', 'playstation', 'console', 'gameboy', 'wii', 'gamer', 'gaming',
            'pixel', 'resolution', 'sensor', 'battery', 'nanotech', 'biotech', 'solar', 'energy', 'fuel'
        },
        'Business': {
            'business', 'economy', 'market', 'finance', 'financial', 'corporate', 'company', 'firm',
            'profit', 'loss', 'revenue', 'earnings', 'income', 'sales', 'debt', 'loan', 'credit', 'bank',
            'banking', 'investment', 'investor', 'stock', 'share', 'equity', 'bond', 'currency', 'dollar',
            'euro', 'yen', 'yuan', 'inflation', 'recession', 'tax', 'budget', 'deficit', 'fiscal', 'ceo',
            'cfo', 'executive', 'manager', 'management', 'merger', 'acquisition', 'takeover', 'bid',
            'offer', 'retail', 'consumer', 'spending', 'commodity', 'oil', 'gold', 'price', 'cost',
            'trade', 'export', 'import', 'tariff', 'outsourcing', 'layoff', 'job', 'employment', 'unemployment',
            'strike', 'union', 'contract', 'deal', 'negotiation', 'partner', 'partnership', 'industry',
            'manufacturing', 'production', 'automaker', 'airline', 'carrier', 'logistics', 'telecom'
        },
        'Sports': {
            'sport', 'sports', 'football', 'baseball', 'basketball', 'soccer', 'hockey', 'tennis', 'golf',
            'cricket', 'rugby', 'boxing', 'racing', 'motorsport', 'athlete', 'player', 'coach', 'team',
            'club', 'squad', 'league', 'tournament', 'championship', 'olympic', 'olympics', 'medal',
            'match', 'game', 'race', 'round', 'final', 'semifinal', 'quarterfinal', 'score', 'result',
            'victory', 'defeat', 'winner', 'loser', 'win', 'lose', 'draw', 'tie', 'cup', 'trophy', 'title',
            'stadium', 'arena', 'field', 'court', 'pitch', 'track', 'lap', 'goal', 'point', 'run', 'basket',
            'touchdown', 'homerun', 'wicket', 'penalty', 'foul', 'referee', 'umpire', 'offense', 'defense',
            'goalkeeper', 'striker', 'defender', 'midfielder', 'quarterback', 'receiver', 'pitcher', 'batter',
            'manager', 'captain', 'roster', 'draft', 'season', 'playoff', 'ranking', 'seed'
        },
        'World': {
            'world', 'international', 'nation', 'country', 'state', 'government', 'politics', 'political',
            'politician', 'president', 'minister', 'senator', 'governor', 'mayor', 'ambassador', 'diplomat',
            'parliament', 'congress', 'senate', 'election', 'vote', 'voter', 'poll', 'campaign', 'candidate',
            'party', 'democrat', 'republican', 'conservative', 'liberal', 'socialist', 'communist', 'dictator',
            'regime', 'authority', 'official', 'police', 'military', 'army', 'navy', 'force', 'troop',
            'soldier', 'war', 'battle', 'conflict', 'fight', 'attack', 'bomb', 'blast', 'explosion',
            'terror', 'terrorism', 'terrorist', 'rebel', 'insurgent', 'guerrilla', 'weapon', 'gun', 'nuclear',
            'missile', 'peace', 'treaty', 'agreement', 'ceasefire', 'talks', 'summit', 'conference',
            'court', 'trial', 'judge', 'jury', 'verdict', 'sentence', 'prison', 'jail', 'crime', 'criminal',
            'murder', 'homicide', 'killing', 'death', 'casualty', 'disaster', 'tragedy', 'crisis',
            'storm', 'hurricane', 'typhoon', 'earthquake', 'flood', 'drought', 'famine', 'disease', 'virus',
            'epidemic', 'flu', 'hospital', 'doctor', 'patient', 'health', 'refugee', 'migrant', 'border',
            'protest', 'demonstration', 'riot', 'mob', 'violence', 'religion', 'religious', 'church', 'mosque'
        }
    }
    
    for cat, wset in keywords.items():
        for w in wset:
            if w in tokens:
                scores[cat] += 1
                
    # Overrides / Refinements
    if "game" in tokens:
        if scores['Sci/Tech'] > scores['Sports']:
            # Likely video game
            pass
        elif scores['Sports'] == 0 and scores['Sci/Tech'] == 0:
            # "Game" without context -> Sports usually
            scores['Sports'] += 1
            
    if "oil" in tokens and scores['Business'] > 0:
        scores['Business'] += 2
        
    best_cat = max(scores, key=scores.get)
    # Tie-breaking: World is often the most generic, Sci/Tech usually requires specific terms.
    # If tie between Sci/Tech and Business (e.g. "Tech Company Profits"):
    # Usually "Business" if focus is money.
    if scores['Business'] == scores['Sci/Tech'] and scores['Business'] > 0:
        if any(w in tokens for w in ['profit', 'stock', 'share', 'market', 'revenue']):
            best_cat = 'Business'
            
    return best_cat, scores

sci_tech_count = 0
sci_tech_examples = []
results = []

for article in articles:
    cat, scores = classify_final(article['title'], article['description'])
    if cat == 'Sci/Tech':
        sci_tech_count += 1
        sci_tech_examples.append(article['title'])
    results.append((article['title'], cat, scores))

print("__RESULT__:")
print(json.dumps({
    "sci_tech_count": sci_tech_count,
    "total": len(articles),
    "sci_tech_examples": sci_tech_examples
}))"""

env_args = {'var_function-call-15528725958592451348': [{'author_id': '218'}], 'var_function-call-1578166081036399350': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-16030178928395895073': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-10746133605277861360': [{'_id': '6944a74a0741a8bd2860bc34', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944a74a0741a8bd2860c3e5', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944a74a0741a8bd2860c690', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944a74a0741a8bd2860c71f', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944a74b0741a8bd2860c8ef', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-2352657671891290551': ['GameBoy mini-games win prize', 'Bailey Tries WR', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award', 'China #39;s appetite boosts BHP'], 'var_function-call-4959353213615004144': 5, 'var_function-call-5617771522699572231': 'file_storage/function-call-5617771522699572231.json', 'var_function-call-14598211073292394500': {'total': 111, 'sci_tech_count': 17, 'sci_tech_titles': ['GameBoy mini-games win prize', 'Bailey Tries WR', 'Energy from waves  teenager wins science award', 'Space Probe Fails to Deploy Its Parachute and Crashes', 'Shuttle repair price tag soars', 'Microsoft settles with UK phone maker', 'EMC Unveils E-mail Storage For Microsoft Exchange', 'Liverpool prepares for life without Gerrard', 'Ex-Astronaut Casts Doubt on Space Tourism', 'Texas Instruments Posts Higher 3Q Profits (AP)', 'Burma army intelligence  #39;purged #39;', 'Satellite write-downs widen DirecTV #39;s loss', 'HP to launch  #39;virus-throttling #39; software', 'Chinese Firm To Buy IBM #39;s PC Business For \\$1.75 Billion', 'Paypal and Apple iTunes link-up', 'US mobile groups confirm merger', 'Log on to be a satellite spy']}, 'var_function-call-18002209419715159437': {'sci_tech_count': 10, 'total': 111, 'sci_tech_examples': ['Space Probe Fails to Deploy Its Parachute and Crashes', 'Shuttle repair price tag soars', 'Liverpool prepares for life without Gerrard', 'Texas Instruments Posts Higher 3Q Profits (AP)', 'HP to launch  #39;virus-throttling #39; software', "EBay Adds 'Want It Now' Feature (Reuters)", 'Virgin Atlantic Inaugural Flight Lands in Sydney', 'Paypal and Apple iTunes link-up', 'US mobile groups confirm merger', 'Log on to be a satellite spy']}}

exec(code, env_args)
