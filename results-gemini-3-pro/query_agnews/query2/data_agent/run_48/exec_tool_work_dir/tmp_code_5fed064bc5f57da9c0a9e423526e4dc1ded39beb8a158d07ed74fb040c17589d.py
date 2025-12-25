code = """import json

# Load the articles from the file
file_path = locals()['var_function-call-15247269977808671868']
with open(file_path, 'r') as f:
    articles = json.load(f)

# Define keywords (simplified for debugging and robustness)
keywords = {
    'Science/Technology': [
        'science', 'technology', 'tech', 'computer', 'software', 'hardware', 'internet', 'web', 'digital', 
        'cyber', 'space', 'nasa', 'astronomy', 'biology', 'physics', 'chemistry', 'research', 'study', 'lab', 
        'robot', 'ai', 'artificial intelligence', 'gadget', 'mobile', 'phone', 'app', 'video game', 'gameboy', 
        'console', 'nintendo', 'sony', 'xbox', 'virus', 'malware', 'hacker', 'innovation', 'engineer', 
        'silicon', 'google', 'microsoft', 'apple', 'linux', 'windows', 'broadband', 'satellite', 'mars', 
        'moon', 'galaxy', 'genome', 'dna', 'stem cell', 'clone', 'fossil', 'climate', 'warming', 'browser',
        'server', 'chip', 'processor', 'wireless', 'network', 'telecom', 'nanotech', 'biotech', 'solar',
        'renewable', 'battery', 'electric car', 'hybrid', 'algorithm', 'data', 'online', 'search engine',
        'spam', 'email', 'blog', 'pixel', 'camera', 'mp3', 'ipod', 'dvd', 'hdtv', 'lcd', 'plasma', 'gps',
        'firefox', 'explorer', 'spyware', 'hubble', 'shuttle', 'station', 'ibm', 'intel', 'hp', 'dell', 'oracle',
        'cisco', 'pharmaceutical', 'drug', 'medicine', 'medical', 'disease', 'health', 'fraud', 'billing', # fraud/billing often business but tech fraud exists
        'xm', 'radio', 'itunes', 'paypal', 'ebay', 'amazon', 'yahoo', 'facebook', 'myspace'
    ],
    'Sports': [
        'sport', 'football', 'baseball', 'basketball', 'tennis', 'cricket', 'rugby', 'soccer', 'golf', 'hockey',
        'race', 'racing', 'formula one', 'f1', 'grand prix', 'olympic', 'medal', 'athlete', 'player', 'team',
        'coach', 'manager', 'referee', 'umpire', 'stadium', 'match', 'game', 'tournament', 'league', 'cup',
        'championship', 'world cup', 'super bowl', 'nfl', 'nba', 'mlb', 'nhl', 'premier league', 'bundesliga',
        'la liga', 'serie a', 'uefa', 'fifa', 'wimbledon', 'us open', 'australian open', 'french open',
        'touchdown', 'goal', 'homerun', 'strike', 'wicket', 'inning', 'quarterback', 'striker', 'defender',
        'midfielder', 'goalkeeper', 'boxer', 'boxing', 'wrestling', 'swimming', 'track and field', 'marathon',
        'red sox', 'yankees', 'lakers', 'bulls', 'broncos', 'patriots', 'cowboys', 'giants', 'jets', 'mets',
        'dodgers', 'cardinals', 'cornerback', 'receiver', 'linebacker', 'pitcher', 'batter', 'cycling', 'cyclist',
        'motogp', 'nascar', 'driver', 'lap', 'circuit'
    ],
    'Business': [
        'business', 'economy', 'economic', 'market', 'stock', 'share', 'trade', 'finance', 'financial',
        'money', 'bank', 'investment', 'investor', 'profit', 'loss', 'revenue', 'sales', 'earnings',
        'quarterly', 'fiscal', 'tax', 'budget', 'debt', 'inflation', 'recession', 'growth', 'merger',
        'acquisition', 'company', 'corporation', 'firm', 'industry', 'ceo', 'cfo', 'executive', 'management',
        'wall street', 'dow jones', 'nasdaq', 'ftse', 'nikkei', 'dollar', 'euro', 'yen', 'currency', 'oil',
        'gold', 'price', 'cost', 'deal', 'contract', 'bid', 'offer', 'auction', 'retail', 'consumer',
        'product', 'brand', 'marketing', 'advertising', 'jobs', 'employment', 'unemployment', 'strike',
        'fed', 'federal reserve', 'rates', 'boeing', 'airbus', 'gm', 'ford', 'toyota', 'wal-mart', 'mining',
        'commodity', 'commodities', 'bhp', 'exxon', 'bp', 'shell', 'enron', 'worldcom', 'airline', 'airways',
        'store', 'shop', 'supermarket', 'retailer', 'mylan', 'astrazeneca', 'citigroup', 'marsh', 'spitzer',
        'index', 'exchange'
    ],
    'World': [
        'world', 'international', 'politics', 'political', 'government', 'election', 'vote', 'president',
        'minister', 'senator', 'congress', 'parliament', 'diplomacy', 'treaty', 'agreement', 'summit',
        'war', 'peace', 'conflict', 'military', 'army', 'navy', 'air force', 'troops', 'soldier', 'weapon',
        'bomb', 'attack', 'terror', 'terrorism', 'police', 'crime', 'court', 'judge', 'law', 'legal',
        'justice', 'prison', 'human rights', 'refugee', 'immigrant', 'border', 'security', 'united nations',
        'un', 'eu', 'european union', 'nato', 'country', 'nation', 'state', 'region', 'middle east',
        'asia', 'europe', 'africa', 'america', 'latin america', 'china', 'russia', 'usa', 'uk', 'france',
        'germany', 'japan', 'india', 'pakistan', 'iran', 'iraq', 'syria', 'israel', 'palestine', 'korea',
        'quake', 'earthquake', 'tsunami', 'flood', 'disaster', 'hurricane', 'typhoon', 'storm', 'baghdad',
        'kabul', 'gaza', 'beijing', 'moscow', 'washington', 'london', 'paris', 'prime minister', 'bush', 'blair',
        'putin', 'clinton', 'kerry', 'arafat', 'sharon', 'settlement', 'hostage', 'kidnap', 'explosion', 'blast',
        'kashmir', 'sudan', 'darfur', 'nepal', 'kathmandu', 'somalia', 'afghanistan', 'ukraine', 'burma',
        'indonesia', 'thailand', 'vietnam', 'brazil', 'venezuela', 'canadian', 'canada', 'ontario', 'quebec'
    ]
}

def classify_article(title, description, debug=False):
    text = (title + " " + description).lower()
    scores = {cat: 0 for cat in keywords}
    
    # Simple string matching (safer than regex for now)
    for cat, kws in keywords.items():
        for kw in kws:
            # Check for word boundary simulated by spaces if needed, but loose matching first
            if kw in text:
                scores[cat] += 1
                
    # Adjustments
    if 'game' in text:
        # If 'video' or 'console' etc is there, it's tech
        if any(w in text for w in ['video', 'console', 'xbox', 'playstation', 'nintendo', 'software']):
            scores['Science/Technology'] += 2
        # If 'match' or 'league' etc is there, it's sports
        elif any(w in text for w in ['match', 'league', 'cup', 'ball', 'score']):
            scores['Sports'] += 2
            
    # Max score
    max_score = -1
    best_cat = 'Unknown'
    
    for cat, score in scores.items():
        if score > max_score:
            max_score = score
            best_cat = cat
        elif score == max_score:
            if cat == 'Science/Technology':
                best_cat = cat
                
    if debug:
        return best_cat, scores
    return best_cat

sci_tech_count = 0
total_count = 0
results = []

# Debug first 5
for i, article in enumerate(articles):
    total_count += 1
    debug_mode = (i < 5)
    if debug_mode:
        cat, scores = classify_article(article['title'], article['description'], debug=True)
        # print(f"DEBUG: {article['title']} -> {cat} (Scores: {scores})")
    else:
        cat = classify_article(article['title'], article['description'])
        
    if cat == 'Science/Technology':
        sci_tech_count += 1
    results.append({'title': article['title'], 'category': cat})

fraction = sci_tech_count / total_count if total_count > 0 else 0

print("__RESULT__:")
print(json.dumps({'total': total_count, 'sci_tech': sci_tech_count, 'fraction': fraction, 'sample_results': results[:20]}))"""

env_args = {'var_function-call-6028342415498347179': [{'author_id': '218'}], 'var_function-call-15840988656083495380': [{'article_id': '192'}, {'article_id': '2161'}, {'article_id': '2844'}, {'article_id': '2987'}, {'article_id': '3451'}, {'article_id': '3970'}, {'article_id': '4447'}, {'article_id': '5354'}, {'article_id': '6705'}, {'article_id': '6869'}, {'article_id': '8962'}, {'article_id': '9677'}, {'article_id': '9858'}, {'article_id': '14861'}, {'article_id': '15100'}, {'article_id': '15473'}, {'article_id': '17491'}, {'article_id': '19469'}, {'article_id': '20362'}, {'article_id': '21238'}, {'article_id': '22354'}, {'article_id': '23914'}, {'article_id': '24495'}, {'article_id': '25960'}, {'article_id': '26535'}, {'article_id': '27429'}, {'article_id': '28079'}, {'article_id': '29164'}, {'article_id': '29297'}, {'article_id': '33489'}, {'article_id': '35408'}, {'article_id': '35882'}, {'article_id': '36182'}, {'article_id': '36483'}, {'article_id': '37042'}, {'article_id': '38608'}, {'article_id': '39117'}, {'article_id': '39623'}, {'article_id': '40545'}, {'article_id': '41616'}, {'article_id': '46531'}, {'article_id': '47439'}, {'article_id': '48635'}, {'article_id': '48833'}, {'article_id': '49035'}, {'article_id': '52459'}, {'article_id': '54906'}, {'article_id': '57510'}, {'article_id': '57860'}, {'article_id': '57918'}, {'article_id': '62404'}, {'article_id': '62754'}, {'article_id': '64102'}, {'article_id': '66827'}, {'article_id': '68509'}, {'article_id': '68958'}, {'article_id': '69262'}, {'article_id': '69393'}, {'article_id': '70498'}, {'article_id': '70608'}, {'article_id': '72525'}, {'article_id': '73025'}, {'article_id': '73684'}, {'article_id': '78200'}, {'article_id': '80578'}, {'article_id': '80853'}, {'article_id': '81851'}, {'article_id': '82526'}, {'article_id': '82668'}, {'article_id': '83273'}, {'article_id': '88553'}, {'article_id': '88911'}, {'article_id': '89666'}, {'article_id': '91286'}, {'article_id': '91822'}, {'article_id': '92992'}, {'article_id': '93287'}, {'article_id': '93804'}, {'article_id': '94618'}, {'article_id': '96641'}, {'article_id': '96986'}, {'article_id': '99699'}, {'article_id': '100613'}, {'article_id': '101514'}, {'article_id': '103003'}, {'article_id': '103591'}, {'article_id': '103695'}, {'article_id': '104123'}, {'article_id': '104996'}, {'article_id': '104998'}, {'article_id': '105804'}, {'article_id': '106908'}, {'article_id': '107036'}, {'article_id': '108586'}, {'article_id': '109601'}, {'article_id': '110096'}, {'article_id': '111422'}, {'article_id': '112063'}, {'article_id': '112770'}, {'article_id': '113058'}, {'article_id': '116698'}, {'article_id': '119651'}, {'article_id': '119920'}, {'article_id': '120129'}, {'article_id': '120765'}, {'article_id': '122137'}, {'article_id': '123747'}, {'article_id': '124509'}, {'article_id': '126412'}, {'article_id': '126655'}, {'article_id': '126966'}], 'var_function-call-8711651007283274154': [192, 2161, 2844, 2987, 3451, 3970, 4447, 5354, 6705, 6869, 8962, 9677, 9858, 14861, 15100, 15473, 17491, 19469, 20362, 21238, 22354, 23914, 24495, 25960, 26535, 27429, 28079, 29164, 29297, 33489, 35408, 35882, 36182, 36483, 37042, 38608, 39117, 39623, 40545, 41616, 46531, 47439, 48635, 48833, 49035, 52459, 54906, 57510, 57860, 57918, 62404, 62754, 64102, 66827, 68509, 68958, 69262, 69393, 70498, 70608, 72525, 73025, 73684, 78200, 80578, 80853, 81851, 82526, 82668, 83273, 88553, 88911, 89666, 91286, 91822, 92992, 93287, 93804, 94618, 96641, 96986, 99699, 100613, 101514, 103003, 103591, 103695, 104123, 104996, 104998, 105804, 106908, 107036, 108586, 109601, 110096, 111422, 112063, 112770, 113058, 116698, 119651, 119920, 120129, 120765, 122137, 123747, 124509, 126412, 126655, 126966], 'var_function-call-11638954545548119907': [{'_id': '6944bedbfdd647f4b5022793', 'article_id': '192', 'title': 'GameBoy mini-games win prize', 'description': 'A set of GameBoy micro-games is named as the most innovative game of the year at a festival in Scotland.'}, {'_id': '6944bedcfdd647f4b5022f44', 'article_id': '2161', 'title': 'Bailey Tries WR', 'description': "Pro Bowl cornerback Champ Bailey practiced with the offense at wide reciever during the Denver Broncos' practice on Tuesday."}, {'_id': '6944bedcfdd647f4b50231ef', 'article_id': '2844', 'title': 'Students Win \\$100,000 in National Team Science Competition', 'description': 'Lucie Guo, motivated by the death of her grandfather in China before she was born, spent two summers doing research in a Duke University laboratory.'}, {'_id': '6944bedcfdd647f4b502327e', 'article_id': '2987', 'title': 'Energy from waves  teenager wins science award', 'description': 'A teenager from the San Diego, California area has won The Siemens Westinghouse Competition in Math, Science and Technology for his  quot;Gyro-Gen, quot; a machine that produces electricity from ocean waves.'}, {'_id': '6944bedcfdd647f4b502344e', 'article_id': '3451', 'title': 'China #39;s appetite boosts BHP', 'description': 'BHP Billiton, the world #39;s biggest mining company, has doubled its profits in the second half of the year on the back of booming global commodity prices. '}], 'var_function-call-6280440072339944699': {'total': 5, 'sci_tech': 5, 'fraction': 1.0, 'sample_results': [{'title': 'GameBoy mini-games win prize', 'category': 'Science/Technology'}, {'title': 'Bailey Tries WR', 'category': 'Science/Technology'}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'category': 'Science/Technology'}, {'title': 'Energy from waves  teenager wins science award', 'category': 'Science/Technology'}, {'title': 'China #39;s appetite boosts BHP', 'category': 'Science/Technology'}]}, 'var_function-call-15247269977808671868': 'file_storage/function-call-15247269977808671868.json', 'var_function-call-7950543054465166364': {'total': 111, 'sci_tech': 4, 'fraction': 0.036036036036036036, 'sample_results': [{'title': 'GameBoy mini-games win prize', 'category': 'Science/Technology'}, {'title': 'Bailey Tries WR', 'category': 'Unknown'}, {'title': 'Students Win \\$100,000 in National Team Science Competition', 'category': 'Unknown'}, {'title': 'Energy from waves  teenager wins science award', 'category': 'Unknown'}, {'title': 'China #39;s appetite boosts BHP', 'category': 'Unknown'}, {'title': 'Leading Indicators, Jobless Claims Dip (AP)', 'category': 'Unknown'}, {'title': 'Even in win, nasty vibes', 'category': 'Unknown'}, {'title': 'Gas stoppage may have caused deadly Belgian blast: TV report (AFP)', 'category': 'World'}, {'title': 'Raffarin pledges to be  quot;extremely severe quot; against anti-semitism &lt;b&gt;...&lt;/b&gt;', 'category': 'Unknown'}, {'title': 'Somalians sworn in', 'category': 'Unknown'}, {'title': 'Muenzer races for gold', 'category': 'Unknown'}, {'title': 'Israelis to Expand West Bank Settlements', 'category': 'Unknown'}, {'title': 'Stocks End Up as Oil Prices Fall', 'category': 'Business'}, {'title': 'WTO Rejects U.S. Appeal on Canadian Wheat', 'category': 'Unknown'}, {'title': 'Capriati Scrambles Past Chladkova Challenge at Open', 'category': 'Unknown'}, {'title': 'In Iraq, a Quest to Rebuild One More Broken Edifice: Science', 'category': 'Unknown'}, {'title': 'UPDATE: Intel lowers Q3 revenue estimates', 'category': 'Unknown'}, {'title': 'Calm as Kathmandu curfew lifted', 'category': 'Unknown'}, {'title': 'Israeli Missiles Kill 13 Militants', 'category': 'Unknown'}, {'title': 'Serena Blasts Umpire After Dramatic Defeat', 'category': 'Unknown'}, {'title': 'Space Probe Fails to Deploy Its Parachute and Crashes', 'category': 'Science/Technology'}, {'title': 'Producer Prices Drop, Trade Gap Narrows', 'category': 'Business'}, {'title': 'Shuttle repair price tag soars', 'category': 'Science/Technology'}, {'title': 'Microsoft settles with UK phone maker', 'category': 'Unknown'}, {'title': 'Champions League to provide upsets', 'category': 'Unknown'}, {'title': 'The Associated Press', 'category': 'Unknown'}, {'title': 'Not all sweet for Lou', 'category': 'Unknown'}, {'title': 'Law pays tribute to record-breaking Ruud', 'category': 'Unknown'}, {'title': 'Negotiations Seek End to IRA Threat', 'category': 'Unknown'}, {'title': "Kerry Questions Bush's Judgment on Iraq", 'category': 'Unknown'}, {'title': 'Giants gain on Dodgers', 'category': 'Unknown'}, {'title': 'EMC Unveils E-mail Storage For Microsoft Exchange', 'category': 'Unknown'}, {'title': 'Bed Bath   Beyond Profit Up, Shares Fall (Reuters)', 'category': 'Unknown'}, {'title': 'A Strategy for Shell?', 'category': 'Unknown'}, {'title': 'Placer Dome forecasts higher 2005 gold production', 'category': 'Unknown'}, {'title': 'Liverpool prepares for life without Gerrard', 'category': 'Unknown'}, {'title': 'ICC Champions Trophy final today', 'category': 'Unknown'}, {'title': 'Swedes fire into top two spots', 'category': 'Unknown'}, {'title': 'Israel Defense Official Threatens Syria (AP)', 'category': 'Unknown'}, {'title': 'TechBrief: Vodafone seeks new frontiers', 'category': 'Unknown'}, {'title': 'Ex-Astronaut Casts Doubt on Space Tourism', 'category': 'Science/Technology'}, {'title': 'Charging Els moves to the top', 'category': 'Unknown'}, {'title': 'Finance Leaders Urge Vigilance on Terror (Reuters)', 'category': 'Unknown'}, {'title': 'German food retailer Spar sells 50-pct stake in Netto discount to ITM (AFP)', 'category': 'Unknown'}, {'title': 'But hurricanes and more impact in the third quarter', 'category': 'Business'}, {'title': 'Diabetes delay adds to AstraZeneca #39;s ills', 'category': 'Unknown'}, {'title': 'Soldering plays Spadea next', 'category': 'Unknown'}, {'title': 'Stocks: Stocks rise as investors bet on profit reports', 'category': 'Business'}, {'title': 'NZ stocks: Sharemarket softens, but Air NZ takes off', 'category': 'Unknown'}, {'title': 'Devastating blow', 'category': 'Sports'}, {'title': 'Man remanded over Danielle murder', 'category': 'Unknown'}, {'title': 'Two Soldiers Die After Crash in Iraq', 'category': 'Unknown'}, {'title': 'Texas Instruments Posts Higher 3Q Profits (AP)', 'category': 'Unknown'}, {'title': 'Sergeant in Abu Ghraib Case Pleads Guilty to 8 Counts', 'category': 'Unknown'}, {'title': "'Treasure hunt' for bandit's loot", 'category': 'Unknown'}, {'title': 'Citigroup Says SEC May Take Action Against Jones (Update6)', 'category': 'Unknown'}, {'title': 'Burma army intelligence  #39;purged #39;', 'category': 'Unknown'}, {'title': 'Memos Warned of Billing Fraud by Firm in Iraq', 'category': 'Unknown'}, {'title': 'Owenagainlifts Real Madrid from the doldrums', 'category': 'Unknown'}, {'title': 'Brazilian GP Race Report: Montoya claims first win of 2004', 'category': 'Unknown'}, {'title': 'Clinton jumps into campaign, as missing explosives force Bush on defensive (AFP)', 'category': 'Unknown'}, {'title': 'FCC Approves Merger, Wireless Giant Created', 'category': 'Unknown'}, {'title': 'Crude prices fall after good news from Norway', 'category': 'Business'}, {'title': 'Maryland 20, No. 5 Florida State 17', 'category': 'Unknown'}, {'title': 'Satellite write-downs widen DirecTV #39;s loss', 'category': 'Unknown'}, {'title': 'Report: Stottlemyre won #39;t return', 'category': 'Unknown'}, {'title': 'Backs off drastic fare  amp; service plans', 'category': 'Unknown'}, {'title': 'Goodyear Sees Profit; Stock Up', 'category': 'Unknown'}, {'title': 'Israel to free Egyptian students: Cairo media', 'category': 'Unknown'}, {'title': 'Why I had to leave Australia', 'category': 'Unknown'}, {'title': '. . . and Lost Chances', 'category': 'Unknown'}, {'title': 'Coke CEO: the company may face tough times. Earnings targets &lt;b&gt;...&lt;/b&gt;', 'category': 'Unknown'}, {'title': 'Vote Fraud Theories, Spread by Blogs, Are Quickly Buried', 'category': 'Unknown'}, {'title': 'Lord Black is charged with fraud', 'category': 'Unknown'}, {'title': 'AMCC to Lay Off 150', 'category': 'Unknown'}, {'title': 'Revealed: why the fear factor runs with the pack', 'category': 'Unknown'}, {'title': 'Gunshots echo in Indian-controlled Kashmir', 'category': 'Unknown'}, {'title': 'Ontario to dedicate  #36;12.5 million to water studies and watershed protection (Canadian Press)', 'category': 'Unknown'}, {'title': 'India offers unqualified talks on Kashmir', 'category': 'Unknown'}, {'title': 'Mylan Shares Up As Drug Stocks Close Down', 'category': 'Unknown'}, {'title': 'Sorenstam Leads ADT Championship by Three (AP)', 'category': 'Unknown'}, {'title': "Cherkasky says Marsh may settle Spitzer's lawsuit within a month", 'category': 'Unknown'}, {'title': 'Call Service with a Sneer (Reuters)', 'category': 'Unknown'}, {'title': 'Lehmann slams  #39;arrogant #39; ref', 'category': 'Unknown'}, {'title': "Blunkett denies visa 'fast-track'", 'category': 'Unknown'}, {'title': 'Anglican Leader Warns Churches on Gay Hate Message (Reuters)', 'category': 'Unknown'}, {'title': 'After adjusting, Pats get busy', 'category': 'Unknown'}, {'title': 'Asean signs historic deal with China', 'category': 'Unknown'}, {'title': 'Rams not in Pack #39;s league', 'category': 'Unknown'}, {'title': 'Death toll rises to 63 in Shaanxi coalmine explosion', 'category': 'Business'}, {'title': 'HP to launch  #39;virus-throttling #39; software', 'category': 'Unknown'}, {'title': 'XM CEO Sees Satellite Radio on Cell Phones', 'category': 'Unknown'}, {'title': "'Tis the season to be greeted with silliness", 'category': 'Unknown'}, {'title': "EBay Adds 'Want It Now' Feature (Reuters)", 'category': 'Unknown'}, {'title': 'Chinese Firm To Buy IBM #39;s PC Business For \\$1.75 Billion', 'category': 'Unknown'}, {'title': 'Virgin Atlantic Inaugural Flight Lands in Sydney', 'category': 'Unknown'}, {'title': 'Ford #39;s Scheele to Retire as President on Feb. 1 (Update2)', 'category': 'Unknown'}, {'title': 'NBA Wrap: McGrady Leads Rockets to Stunning Win', 'category': 'Unknown'}, {'title': 'Paypal and Apple iTunes link-up', 'category': 'Unknown'}, {'title': 'Arab reform dreams run aground', 'category': 'Unknown'}, {'title': 'US mobile groups confirm merger', 'category': 'Unknown'}, {'title': 'Bush Ordering Better Ocean Oversight (AP)', 'category': 'Unknown'}, {'title': 'Indonesian extremists influence Thai Muslims, prime minister says &lt;b&gt;...&lt;/b&gt;', 'category': 'Unknown'}, {'title': 'Peace delegation leaves Najaf empty-handed as fighting continues', 'category': 'Unknown'}, {'title': 'Schumacher in uncharted territory', 'category': 'Unknown'}, {'title': 'Karzai deputy escapes a roadside bombing', 'category': 'Unknown'}, {'title': 'Ban for former Ahold executives', 'category': 'Unknown'}, {'title': 'Hendrick Motorsports', 'category': 'Unknown'}, {'title': 'Protests in Canada over Ukraine crisis (AFP)', 'category': 'Unknown'}, {'title': 'Log on to be a satellite spy', 'category': 'Unknown'}, {'title': 'NASD Warns of Risky Home-Equity Investing', 'category': 'Unknown'}]}}

exec(code, env_args)
