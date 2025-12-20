code = """import json
import re

file_path = locals()['var_function-call-12538038109257007794']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Expanded keyword lists with plurals and specific terms
categories = {
    'Sci/Tech': {
        'keywords': [
            'science', 'sciences', 'technology', 'technologies', 'tech', 'high-tech', 'computer', 'computers', 'computing', 'software', 'hardware', 'internet', 'net', 'web', 'online', 'digital', 'mobile', 'mobiles', 'phone', 'phones', 'cellphone', 'smartphone', 'gadget', 'gadgets', 'device', 'devices', 'space', 'nasa', 'astronomy', 'biology', 'genetics', 'genome', 'medical', 'medicine', 'health', 'disease', 'diseases', 'virus', 'viruses', 'cancer', 'treatment', 'drug', 'drugs', 'physics', 'chemistry', 'energy', 'power', 'solar', 'nuclear', 'innovation', 'research', 'study', 'studies', 'scientist', 'scientists', 'researcher', 'researchers', 'engineer', 'engineers', 'engineering', 'robot', 'robots', 'robotics', 'ai', 'artificial intelligence', 'data', 'cyber', 'security', 'network', 'networks', 'telecom', 'telecoms', 'wireless', 'broadband', 'satellite', 'satellites', 'game', 'games', 'gaming', 'gamer', 'gamers', 'console', 'consoles', 'nintendo', 'sony', 'microsoft', 'intel', 'amd', 'google', 'apple', 'linux', 'windows', 'browser', 'browsers', 'server', 'servers', 'chip', 'chips', 'processor', 'processors', 'memory', 'storage', 'cloud', 'app', 'apps', 'application', 'applications', 'update', 'updates', 'patch', 'patches', 'version', 'versions', 'release', 'releases', 'beta', 'review', 'reviews', 'preview', 'test', 'tests', 'ibm', 'oracle', 'cisco', 'yahoo', 'amazon', 'facebook', 'ebay', 'videogame', 'videogames', 'xbox', 'playstation', 'wii', 'ipod', 'iphone', 'ipad', 'tablet', 'tablets', 'laptop', 'laptops', 'desktop', 'desktops', 'monitor', 'screen', 'display', 'camera', 'cameras', 'lens', 'sensor', 'biotech', 'nanotech', 'mission', 'missions', 'launch', 'launches', 'orbit', 'mars', 'moon', 'planet', 'planets', 'galaxy', 'galaxies', 'star', 'stars', 'telescope', 'shuttle', 'station', 'astronaut', 'astronauts', 'lab', 'labs', 'laboratory', 'laboratories', 'experiment', 'experiments', 'theory', 'theories', 'discovery', 'discoveries', 'invention', 'inventions', 'hacker', 'hackers', 'malware', 'spyware', 'virus', 'viruses', 'trojan', 'worm', 'spam', 'phishing', 'firewall', 'encryption', 'code', 'coding', 'programming', 'program', 'programs', 'developer', 'developers', 'language', 'script', 'database', 'sql', 'server', 'client', 'protocol', 'http', 'email', 'e-mail', 'blog', 'blogs', 'social media', 'tweet', 'twitter', 'youtube', 'video', 'videos', 'audio', 'mp3', 'download', 'downloads', 'upload', 'stream', 'streaming', 'search engine'
        ],
        'weight': 1.0
    },
    'Sports': {
        'keywords': [
            'sport', 'sports', 'game', 'games', 'match', 'matches', 'team', 'teams', 'player', 'players', 'coach', 'coaches', 'win', 'wins', 'winning', 'winner', 'won', 'loss', 'losses', 'lost', 'score', 'scores', 'scoring', 'league', 'leagues', 'season', 'seasons', 'championship', 'championships', 'champion', 'champions', 'tournament', 'tournaments', 'cup', 'cups', 'olympic', 'olympics', 'medal', 'medals', 'gold', 'silver', 'bronze', 'football', 'soccer', 'basketball', 'baseball', 'tennis', 'golf', 'hockey', 'racing', 'race', 'races', 'driver', 'drivers', 'athlete', 'athletes', 'stadium', 'arena', 'field', 'court', 'gym', 'training', 'practice', 'trade', 'trades', 'draft', 'contract', 'contracts', 'goal', 'goals', 'touchdown', 'touchdowns', 'homerun', 'homeruns', 'strike', 'strikes', 'ball', 'balls', 'bat', 'bats', 'club', 'clubs', 'racket', 'net', 'basket', 'puck', 'helmet', 'jersey', 'fan', 'fans', 'spectator', 'spectators', 'ticket', 'tickets', 'broadcast', 'espn', 'nfl', 'nba', 'mlb', 'nhl', 'fifa', 'uefa', 'ncaa', 'wimbledon', 'open', 'masters', 'pga', 'nascar', 'f1', 'grand prix', 'tour de france', 'world cup', 'super bowl', 'world series', 'stanley cup', 'playoff', 'playoffs', 'final', 'finals', 'semifinal', 'semifinals', 'quarterfinal', 'quarterfinals', 'round', 'rounds', 'heat', 'heats', 'lap', 'laps', 'marathon', 'sprint', 'relay', 'swim', 'swimming', 'diving', 'gymnastics', 'skiing', 'skating', 'boxing', 'wrestling', 'cricket', 'rugby', 'bowling', 'archery'
        ],
        'weight': 1.0
    },
    'Business': {
        'keywords': [
            'business', 'businesses', 'economy', 'economies', 'economic', 'market', 'markets', 'stock', 'stocks', 'share', 'shares', 'trade', 'trades', 'trading', 'profit', 'profits', 'revenue', 'revenues', 'earnings', 'loss', 'losses', 'sale', 'sales', 'company', 'companies', 'corporation', 'corporations', 'corp', 'inc', 'ltd', 'bank', 'banks', 'banking', 'finance', 'finances', 'financial', 'investment', 'investments', 'investor', 'investors', 'currency', 'currencies', 'dollar', 'dollars', 'euro', 'euros', 'yen', 'pound', 'pounds', 'oil', 'gas', 'price', 'prices', 'cost', 'costs', 'inflation', 'interest', 'rate', 'rates', 'fed', 'federal reserve', 'treasury', 'bond', 'bonds', 'debt', 'debts', 'loan', 'loans', 'credit', 'mortgage', 'tax', 'taxes', 'budget', 'gdp', 'job', 'jobs', 'employment', 'unemployment', 'hiring', 'layoff', 'layoffs', 'strike', 'strikes', 'union', 'unions', 'merger', 'mergers', 'acquisition', 'acquisitions', 'deal', 'deals', 'ceo', 'cfo', 'executive', 'executives', 'manager', 'managers', 'management', 'board', 'chairman', 'director', 'shareholder', 'shareholders', 'dividend', 'dividends', 'wall street', 'dow', 'nasdaq', 'nyse', 'exchange', 'exchanges', 'commodity', 'commodities', 'future', 'futures', 'option', 'options', 'hedge fund', 'ipo', 'bankruptcy', 'regulation', 'antitrust', 'monopoly', 'wto', 'imf', 'world bank'
        ],
        'weight': 1.0
    },
    'World': {
        'keywords': [
            'world', 'international', 'nation', 'nations', 'country', 'countries', 'state', 'states', 'government', 'governments', 'politic', 'politics', 'political', 'politician', 'politicians', 'president', 'presidents', 'minister', 'ministers', 'prime minister', 'chancellor', 'king', 'queen', 'parliament', 'congress', 'senate', 'representative', 'representatives', 'diplomat', 'diplomats', 'embassy', 'treaty', 'agreement', 'summit', 'war', 'wars', 'conflict', 'conflicts', 'battle', 'battles', 'military', 'army', 'navy', 'air force', 'marine', 'marines', 'soldier', 'soldiers', 'troop', 'troops', 'weapon', 'weapons', 'gun', 'guns', 'bomb', 'bombs', 'blast', 'blasts', 'explosion', 'explosions', 'attack', 'attacks', 'terrorism', 'terrorist', 'terrorists', 'rebel', 'rebels', 'insurgent', 'insurgents', 'militia', 'coup', 'revolution', 'protest', 'protests', 'demonstration', 'demonstrations', 'riot', 'riots', 'police', 'crime', 'crimes', 'criminal', 'criminals', 'arrest', 'arrests', 'prison', 'jail', 'court', 'courts', 'judge', 'judges', 'jury', 'verdict', 'sentence', 'execution', 'law', 'laws', 'legal', 'right', 'rights', 'refugee', 'refugees', 'immigrant', 'immigrants', 'border', 'borders', 'security', 'intelligence', 'cia', 'fbi', 'un', 'united nations', 'eu', 'nato', 'election', 'elections', 'vote', 'votes', 'voting', 'campaign', 'campaigns', 'candidate', 'candidates', 'party', 'parties', 'democrat', 'democrats', 'republican', 'republicans', 'peace', 'ceasefire', 'truce', 'negotiation', 'negotiations', 'talk', 'talks', 'meeting', 'meetings', 'visit', 'visits', 'disaster', 'disasters', 'accident', 'accidents', 'crash', 'crashes', 'fire', 'fires', 'flood', 'floods', 'storm', 'storms', 'hurricane', 'hurricanes', 'tornado', 'tornadoes', 'earthquake', 'earthquakes', 'tsunami', 'volcano', 'epidemic', 'pandemic', 'outbreak', 'flu', 'vaccine'
        ],
        'weight': 1.0
    }
}

# Specific weighting for ambiguous words
# "game" is in Sports and Sci/Tech.
# If "game" appears with "video", "computer", "console", "software", "boy" -> Sci/Tech
# If "game" appears with "win", "score", "team", "season", "play" -> Sports (unless "video" etc is present)

def classify(title, description):
    text = (title + " " + description).lower()
    # Replace non-alphanumeric with space to handle "game-boy" or "mini-games"
    text_clean = re.sub(r'[^a-z0-9]', ' ', text)
    words = text_clean.split()
    
    scores = {cat: 0.0 for cat in categories}
    
    # Word matching
    for word in words:
        for cat, data in categories.items():
            if word in data['keywords']:
                scores[cat] += data['weight']
    
    # Contextual adjustments
    
    # Tech vs Sports for "game"
    if 'game' in words or 'games' in words:
        tech_indicators = ['video', 'console', 'nintendo', 'sony', 'microsoft', 'xbox', 'playstation', 'wii', 'boy', 'computer', 'software', 'app', 'online', 'digital', 'electronic', 'device', 'mini', 'innovative', 'prize', 'festival']
        sports_indicators = ['team', 'season', 'league', 'coach', 'player', 'score', 'stadium', 'olympic', 'medal', 'match', 'cup', 'field', 'ball', 'sport']
        
        tech_hits = sum(1 for w in tech_indicators if w in words)
        sports_hits = sum(1 for w in sports_indicators if w in words)
        
        if tech_hits > 0:
            scores['Sci/Tech'] += 3
        if sports_hits > 0:
            scores['Sports'] += 2 # Sports words are common in general
    
    # Tech vs Business for "apple", "google", "microsoft", "intel"
    tech_companies = ['apple', 'google', 'microsoft', 'intel', 'ibm', 'cisco', 'oracle']
    for comp in tech_companies:
        if comp in words:
            # Check for business context
            bus_indicators = ['profit', 'revenue', 'stock', 'share', 'market', 'earnings', 'loss', 'sale', 'quarter', 'estimate', 'dow', 'nasdaq', 'investor']
            bus_hits = sum(1 for w in bus_indicators if w in words)
            if bus_hits > 0:
                scores['Business'] += 2
            else:
                scores['Sci/Tech'] += 2
                
    # World vs Business for "oil", "gas"
    if 'oil' in words or 'gas' in words:
        # If "price", "market", "profit" -> Business
        # If "pipeline", "explosion", "blast", "leak", "shortage" -> World or Business? 
        # "Gas stoppage... deadly Belgian blast" -> World/Business? Usually Disaster is World.
        disaster_indicators = ['blast', 'explosion', 'dead', 'kill', 'leak', 'accident', 'disaster']
        bus_indicators = ['price', 'market', 'cost', 'trade']
        
        if any(w in words for w in disaster_indicators):
            scores['World'] += 3
        if any(w in words for w in bus_indicators):
            scores['Business'] += 2

    # Find max
    max_score = max(scores.values())
    if max_score == 0:
        return "Unknown" # Default?
    
    best_cats = [cat for cat, score in scores.items() if score == max_score]
    
    if len(best_cats) > 1:
        # Tie breaker
        # Prioritize Sci/Tech if ambiguous with others and keywords present?
        # Actually, "Students Win Science Competition" -> Win(Sports), Science(Tech). Tech should win.
        if 'Sci/Tech' in best_cats and ('science' in words or 'technology' in words):
            return 'Sci/Tech'
        # Default order
        return best_cats[0]
        
    return best_cats[0]

results = []
count_tech = 0
for article in articles:
    cat = classify(article['title'], article['description'])
    results.append({'title': article['title'], 'cat': cat})
    if cat == 'Sci/Tech':
        count_tech += 1

print("__RESULT__:")
print(json.dumps({'total': len(articles), 'tech_count': count_tech, 'samples': results[:10]}))"""

env_args = {'var_function-call-7824498463487359527': [{'author_id': '218'}], 'var_function-call-12299435220607160936': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-1259592477097744164': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-1246676392852871560': [{'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-17050363897638211259': 5, 'var_function-call-11640760222079090320': [{'_id': '6944ad769b77b04b15165539', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944ad779b77b04b15165cea', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944ad779b77b04b15165f95', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944ad779b77b04b15166024', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944ad779b77b04b151661f4', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-12538038109257007794': 'file_storage/function-call-12538038109257007794.json', 'var_function-call-7994051037362226199': {'total': 111, 'tech_count': 23, 'samples': [{'title': 'GameBoy mini-games win prize', 'cat': 'Sports'}, {'title': 'Bailey Tries WR', 'cat': 'Sports'}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'cat': 'Sci/Tech'}, {'title': 'Energy from waves  teenager wins science award', 'cat': 'Sci/Tech'}, {'title': 'China #39;s appetite boosts BHP', 'cat': 'Business'}, {'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'cat': 'Business'}, {'title': 'Even in win, nasty vibes', 'cat': 'Sports'}, {'title': 'Gas stoppage may have caused deadly Belgian blast: TV report (AFP)', 'cat': 'Business'}, {'title': 'Raffarin pledges to be  quot;extremely severe quot; against anti-semitism &lt;b&gt;...&lt;/b&gt;', 'cat': 'World'}, {'title': 'Somalians sworn in', 'cat': 'World'}]}}

exec(code, env_args)
