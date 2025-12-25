code = """import json
import re

with open(locals()['var_function-call-5617771522699572231'], 'r') as f:
    articles = json.load(f)

def classify_refined(title, description):
    text = (title + " " + (description or "")).lower()
    tokens = set(re.findall(r'\b[a-z0-9]+\b', text))
    
    scores = {'Sci/Tech': 0, 'Business': 0, 'Sports': 0, 'World': 0}
    
    # Helper to add scores
    def check(category, words, weight=1):
        for w in words:
            if w in tokens:
                scores[category] += weight

    # Sci/Tech Keywords (including plurals/variations)
    st_words = [
        'science', 'sciences', 'technology', 'technologies', 'tech', 'computer', 'computers', 'computing',
        'internet', 'net', 'web', 'website', 'online', 'software', 'hardware', 'digital', 'cyber',
        'mobile', 'phone', 'phones', 'cellphone', 'smartphone', 'wireless', 'wifi', 'bluetooth',
        'network', 'networks', 'satellite', 'satellites', 'space', 'nasa', 'astronomy', 'telescope',
        'universe', 'galaxy', 'planet', 'mars', 'moon', 'orbit', 'robot', 'robots', 'robotics',
        'gadget', 'gadgets', 'device', 'devices', 'innovation', 'innovative', 'research', 'lab', 'labs',
        'scientist', 'scientists', 'engineer', 'engineers', 'biology', 'biological', 'genetics', 'gene',
        'genome', 'dna', 'stem', 'cell', 'cloning', 'physics', 'physicist', 'nuclear', 'laser',
        'microsoft', 'google', 'apple', 'intel', 'ibm', 'hp', 'linux', 'windows', 'browser', 'firefox',
        'explorer', 'server', 'servers', 'database', 'data', 'algorithm', 'code', 'programming',
        'virus', 'viruses', 'worm', 'hacker', 'hackers', 'spam', 'spyware', 'security', 'firewall',
        'chip', 'chips', 'processor', 'processors', 'semiconductor', 'solar', 'energy', 'fuel',
        'battery', 'batteries', 'video', 'game', 'games', 'gaming', 'gamer', 'nintendo', 'sony', 'xbox',
        'playstation', 'console', 'wii', 'gameboy', 'ipod', 'itunes', 'mp3', 'dvd', 'gps', 'biotech',
        'nanotech', 'telecom', 'broadband', 'voip', 'skype', 'ebay', 'amazon', 'yahoo', 'facebook',
        'youtube', 'myspace', 'blog', 'blogs'
    ]
    check('Sci/Tech', st_words)
    
    # Business Keywords
    biz_words = [
        'business', 'businesses', 'economy', 'economic', 'market', 'markets', 'stock', 'stocks',
        'trade', 'trading', 'finance', 'financial', 'bank', 'banks', 'banking', 'invest', 'investment',
        'investor', 'investors', 'company', 'companies', 'corporation', 'corp', 'inc', 'firm', 'firms',
        'profit', 'profits', 'profitability', 'loss', 'losses', 'revenue', 'revenues', 'earnings',
        'sales', 'deal', 'deals', 'merger', 'mergers', 'acquisition', 'acquisitions', 'acquire',
        'bought', 'buy', 'sell', 'sold', 'bid', 'tender', 'ipo', 'share', 'shares', 'shareholder',
        'dividend', 'ceo', 'cfo', 'executive', 'executives', 'management', 'manager', 'price', 'prices',
        'rate', 'rates', 'interest', 'inflation', 'recession', 'debt', 'loan', 'credit', 'budget',
        'deficit', 'tax', 'taxes', 'dollar', 'euro', 'currency', 'exchange', 'oil', 'gold', 'commodity',
        'retail', 'retailer', 'consumer', 'spending', 'job', 'jobs', 'hiring', 'layoff', 'layoffs',
        'unemployment', 'strike', 'union', 'fed', 'federal', 'reserve', 'treasury', 'wall', 'street',
        'dow', 'nasdaq', 'index', 'forecast', 'outlook', 'quarter', 'quarterly', 'industry', 'industrial',
        'airline', 'airlines', 'automaker', 'manufacturing', 'production', 'product', 'products'
    ]
    check('Business', biz_words)
    
    # Sports Keywords
    sp_words = [
        'sport', 'sports', 'football', 'baseball', 'basketball', 'soccer', 'hockey', 'tennis', 'golf',
        'cricket', 'rugby', 'boxing', 'racing', 'race', 'races', 'driver', 'team', 'teams', 'club',
        'clubs', 'player', 'players', 'coach', 'coaches', 'manager', 'game', 'games', 'match', 'matches',
        'tournament', 'championship', 'champion', 'champions', 'league', 'leagues', 'season', 'cup',
        'series', 'playoff', 'playoffs', 'final', 'finals', 'semifinal', 'quarterfinal', 'round',
        'win', 'wins', 'winning', 'winner', 'won', 'lose', 'loses', 'losing', 'lost', 'loss', 'tie',
        'draw', 'score', 'scores', 'scoring', 'goal', 'goals', 'touchdown', 'homerun', 'basket',
        'point', 'points', 'medal', 'medals', 'gold', 'silver', 'bronze', 'olympic', 'olympics',
        'stadium', 'arena', 'field', 'pitch', 'court', 'track', 'lap', 'penalty', 'foul', 'red', 'card',
        'referee', 'umpire', 'offense', 'defense', 'quarterback', 'pitcher', 'batter', 'striker',
        'goalie', 'seed', 'ranking', 'rank', 'beat', 'defeat', 'victory', 'nfl', 'nba', 'mlb', 'nhl',
        'fifa', 'uefa', 'nascar', 'f1', 'formula', 'williams', 'woods', 'armstrong', 'phelps',
        'red', 'sox', 'yankees', 'mets', 'bulls', 'lakers', 'spurs', 'pistons', 'patriots', 'eagles',
        'colts', 'steelers', 'united', 'city', 'real', 'madrid', 'barcelona', 'liverpool', 'arsenal',
        'chelsea', 'milan', 'juventus', 'bayern'
    ]
    check('Sports', sp_words)
    
    # World Keywords
    wd_words = [
        'world', 'international', 'nation', 'nations', 'national', 'country', 'countries', 'state',
        'government', 'governments', 'politics', 'political', 'politician', 'president', 'minister',
        'premier', 'chancellor', 'official', 'officials', 'leader', 'leaders', 'parliament', 'congress',
        'senate', 'election', 'elections', 'vote', 'votes', 'voting', 'poll', 'polls', 'campaign',
        'party', 'parties', 'democrat', 'republican', 'labor', 'conservative', 'liberal', 'candidate',
        'diplomat', 'treaty', 'agreement', 'talks', 'summit', 'conference', 'un', 'eu', 'nato',
        'war', 'wars', 'military', 'army', 'navy', 'air', 'force', 'troops', 'soldiers', 'police',
        'security', 'court', 'courts', 'trial', 'trials', 'judge', 'judges', 'jury', 'verdict',
        'ruling', 'law', 'laws', 'legal', 'crime', 'crimes', 'criminal', 'prison', 'jail', 'arrest',
        'arrested', 'police', 'kill', 'killed', 'killing', 'death', 'deaths', 'dead', 'die', 'died',
        'wound', 'wounded', 'injured', 'injury', 'attack', 'attacks', 'bomb', 'bombs', 'bombing',
        'blast', 'explosion', 'terror', 'terrorism', 'terrorist', 'suicide', 'hostage', 'kidnap',
        'conflict', 'crisis', 'disaster', 'emergency', 'storm', 'hurricane', 'typhoon', 'cyclone',
        'quake', 'earthquake', 'flood', 'floods', 'tsunami', 'fire', 'fires', 'accident', 'crash',
        'protest', 'protests', 'riot', 'riots', 'strike', 'demonstration', 'refugee', 'migrant',
        'border', 'immigration', 'visa', 'asylum', 'human', 'rights', 'religion', 'religious',
        'iraq', 'iraqi', 'baghdad', 'afghanistan', 'kabul', 'iran', 'tehran', 'korea', 'china',
        'chinese', 'russia', 'russian', 'usa', 'us', 'american', 'uk', 'british', 'britain',
        'france', 'french', 'germany', 'german', 'japan', 'japanese', 'israel', 'israeli',
        'palestine', 'palestinian', 'gaza', 'syria', 'egypt', 'sudan', 'darfur', 'africa', 'asia',
        'europe', 'latin', 'america'
    ]
    check('World', wd_words)
    
    # Multi-word phrase checks (add bonus)
    if "video game" in text: scores['Sci/Tech'] += 3
    if "computer game" in text: scores['Sci/Tech'] += 3
    if "mobile phone" in text: scores['Sci/Tech'] += 3
    if "cell phone" in text: scores['Sci/Tech'] += 3
    if "solar power" in text: scores['Sci/Tech'] += 3
    if "stem cell" in text: scores['Sci/Tech'] += 3
    if "space shuttle" in text: scores['Sci/Tech'] += 3
    
    if "stock market" in text: scores['Business'] += 3
    if "wall street" in text: scores['Business'] += 3
    if "interest rate" in text: scores['Business'] += 3
    
    if "world cup" in text: scores['Sports'] += 3
    if "premier league" in text: scores['Sports'] += 3
    if "champions league" in text: scores['Sports'] += 3
    if "formula one" in text: scores['Sports'] += 3
    if "grand slam" in text: scores['Sports'] += 3
    
    if "prime minister" in text: scores['World'] += 3
    if "human rights" in text: scores['World'] += 3
    if "united nations" in text: scores['World'] += 3
    if "middle east" in text: scores['World'] += 3
    
    # Context Logic
    # 1. "Game": If "video", "computer", "console" not present, likely Sports.
    if 'game' in tokens and scores['Sci/Tech'] == 1 and scores['Sports'] == 0:
        # Check for context
        if not any(x in tokens for x in ['video', 'console', 'nintendo', 'sony', 'xbox', 'computer', 'software', 'app']):
            scores['Sports'] += 2
    
    # 2. "Company" / "Apple" / "Google" + "Profit" / "Stock" -> Business
    if scores['Sci/Tech'] > 0 and scores['Business'] > 0:
        if any(x in tokens for x in ['profit', 'stock', 'share', 'revenue', 'earning', 'market', 'deal', 'buy', 'sell']):
            scores['Business'] += 2 # Business usually dominates financial news of tech companies
            
    # 3. "Oil" -> Business (usually)
    if 'oil' in tokens:
        if any(x in tokens for x in ['price', 'market', 'barrel', 'supply', 'opec']):
            scores['Business'] += 2

    # 4. "Space" -> can be "office space" (Business)
    if 'space' in tokens and scores['Sci/Tech'] == 1:
        if not any(x in tokens for x in ['nasa', 'shuttle', 'station', 'launch', 'orbit', 'planet', 'astronomy', 'science']):
            # ambiguous.
            pass

    # 5. "Discovery" -> Sci/Tech (removed from keywords to avoid errors)
    
    # Decision
    if scores['Sci/Tech'] == 0:
        return 'Other'
    
    best_cat = max(scores, key=scores.get)
    return best_cat

sci_tech_count = 0
total_count = len(articles)
sci_tech_titles = []

for article in articles:
    cat = classify_refined(article['title'], article['description'])
    if cat == 'Sci/Tech':
        sci_tech_count += 1
        sci_tech_titles.append(article['title'])

print("__RESULT__:")
print(json.dumps({
    "sci_tech_count": sci_tech_count,
    "total": total_count,
    "sci_tech_titles": sci_tech_titles
}))"""

env_args = {'var_function-call-15528725958592451348': [{'author_id': '218'}], 'var_function-call-1578166081036399350': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-16030178928395895073': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-10746133605277861360': [{'_id': '6944a74a0741a8bd2860bc34', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944a74a0741a8bd2860c3e5', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944a74a0741a8bd2860c690', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944a74a0741a8bd2860c71f', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944a74b0741a8bd2860c8ef', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-2352657671891290551': ['GameBoy mini-games win prize', 'Bailey Tries WR', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award', 'China #39;s appetite boosts BHP'], 'var_function-call-4959353213615004144': 5, 'var_function-call-5617771522699572231': 'file_storage/function-call-5617771522699572231.json', 'var_function-call-14598211073292394500': {'total': 111, 'sci_tech_count': 17, 'sci_tech_titles': ['GameBoy mini-games win prize', 'Bailey Tries WR', 'Energy from waves  teenager wins science award', 'Space Probe Fails to Deploy Its Parachute and Crashes', 'Shuttle repair price tag soars', 'Microsoft settles with UK phone maker', 'EMC Unveils E-mail Storage For Microsoft Exchange', 'Liverpool prepares for life without Gerrard', 'Ex-Astronaut Casts Doubt on Space Tourism', 'Texas Instruments Posts Higher 3Q Profits (AP)', 'Burma army intelligence  #39;purged #39;', 'Satellite write-downs widen DirecTV #39;s loss', 'HP to launch  #39;virus-throttling #39; software', 'Chinese Firm To Buy IBM #39;s PC Business For \\$1.75 Billion', 'Paypal and Apple iTunes link-up', 'US mobile groups confirm merger', 'Log on to be a satellite spy']}, 'var_function-call-18002209419715159437': {'sci_tech_count': 10, 'total': 111, 'sci_tech_examples': ['Space Probe Fails to Deploy Its Parachute and Crashes', 'Shuttle repair price tag soars', 'Liverpool prepares for life without Gerrard', 'Texas Instruments Posts Higher 3Q Profits (AP)', 'HP to launch  #39;virus-throttling #39; software', "EBay Adds 'Want It Now' Feature (Reuters)", 'Virgin Atlantic Inaugural Flight Lands in Sydney', 'Paypal and Apple iTunes link-up', 'US mobile groups confirm merger', 'Log on to be a satellite spy']}, 'var_function-call-14470226197933513685': {'sci_tech_count': 79, 'total': 111, 'sci_tech_examples': ['GameBoy mini-games win prize', 'Students Win \\$100,000 in National Team Science Competition', 'Energy from waves  teenager wins science award', 'China #39;s appetite boosts BHP', 'Leading Indicators, Jobless Claims Dip (AP)', 'Even in win, nasty vibes', 'Gas stoppage may have caused deadly Belgian blast: TV report (AFP)', 'Somalians sworn in', 'Muenzer races for gold', 'Stocks End Up as Oil Prices Fall', 'Capriati Scrambles Past Chladkova Challenge at Open', 'In Iraq, a Quest to Rebuild One More Broken Edifice: Science', 'UPDATE: Intel lowers Q3 revenue estimates', 'Calm as Kathmandu curfew lifted', 'Space Probe Fails to Deploy Its Parachute and Crashes', 'Producer Prices Drop, Trade Gap Narrows', 'Shuttle repair price tag soars', 'Microsoft settles with UK phone maker', 'The Associated Press', 'Negotiations Seek End to IRA Threat', 'EMC Unveils E-mail Storage For Microsoft Exchange', 'A Strategy for Shell?', 'Placer Dome forecasts higher 2005 gold production', 'ICC Champions Trophy final today', 'Swedes fire into top two spots', 'Israel Defense Official Threatens Syria (AP)', 'TechBrief: Vodafone seeks new frontiers', 'Ex-Astronaut Casts Doubt on Space Tourism', 'Finance Leaders Urge Vigilance on Terror (Reuters)', 'German food retailer Spar sells 50-pct stake in Netto discount to ITM (AFP)', 'But hurricanes and more impact in the third quarter', 'Diabetes delay adds to AstraZeneca #39;s ills', 'Soldering plays Spadea next', 'Stocks: Stocks rise as investors bet on profit reports', 'NZ stocks: Sharemarket softens, but Air NZ takes off', 'Man remanded over Danielle murder', 'Two Soldiers Die After Crash in Iraq', 'Texas Instruments Posts Higher 3Q Profits (AP)', 'Sergeant in Abu Ghraib Case Pleads Guilty to 8 Counts', "'Treasure hunt' for bandit's loot", 'Citigroup Says SEC May Take Action Against Jones (Update6)', 'Memos Warned of Billing Fraud by Firm in Iraq', 'Brazilian GP Race Report: Montoya claims first win of 2004', 'FCC Approves Merger, Wireless Giant Created', 'Crude prices fall after good news from Norway', 'Maryland 20, No. 5 Florida State 17', 'Satellite write-downs widen DirecTV #39;s loss', 'Backs off drastic fare  amp; service plans', 'Goodyear Sees Profit; Stock Up', 'Israel to free Egyptian students: Cairo media', 'Why I had to leave Australia', 'Coke CEO: the company may face tough times. Earnings targets &lt;b&gt;...&lt;/b&gt;', 'Vote Fraud Theories, Spread by Blogs, Are Quickly Buried', 'Lord Black is charged with fraud', 'Revealed: why the fear factor runs with the pack', 'Ontario to dedicate  #36;12.5 million to water studies and watershed protection (Canadian Press)', 'Mylan Shares Up As Drug Stocks Close Down', 'Sorenstam Leads ADT Championship by Three (AP)', 'Call Service with a Sneer (Reuters)', "Blunkett denies visa 'fast-track'", 'Anglican Leader Warns Churches on Gay Hate Message (Reuters)', 'Asean signs historic deal with China', 'Death toll rises to 63 in Shaanxi coalmine explosion', 'HP to launch  #39;virus-throttling #39; software', 'XM CEO Sees Satellite Radio on Cell Phones', "'Tis the season to be greeted with silliness", "EBay Adds 'Want It Now' Feature (Reuters)", 'Chinese Firm To Buy IBM #39;s PC Business For \\$1.75 Billion', 'Virgin Atlantic Inaugural Flight Lands in Sydney', 'Ford #39;s Scheele to Retire as President on Feb. 1 (Update2)', 'Paypal and Apple iTunes link-up', 'Arab reform dreams run aground', 'US mobile groups confirm merger', 'Peace delegation leaves Najaf empty-handed as fighting continues', 'Karzai deputy escapes a roadside bombing', 'Ban for former Ahold executives', 'Hendrick Motorsports', 'Protests in Canada over Ukraine crisis (AFP)', 'Log on to be a satellite spy']}}

exec(code, env_args)
