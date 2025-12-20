code = """import json
import pandas as pd
import re

# Get the file path
file_path = locals()['var_function-call-12865582274226652090']

# Load the articles
with open(file_path, 'r') as f:
    articles = json.load(f)

df = pd.DataFrame(articles)

# Weighted Keywords
sports_strong = [
    'olympic', 'olympics', 'olympiad', 'medal', 'medals', 'gold', 'silver', 'bronze', 'athens', 
    'nba', 'nfl', 'mlb', 'nhl', 'fifa', 'uefa', 'wimbledon', 'grand slam', 'super bowl', 'world cup', 
    'champion', 'champions', 'championship', 'tournament', 'league', 'athlete', 'athletes', 'sprinter', 
    'marathon', 'gymnastics', 'gymnast', 'swimmer', 'swimming', 'basketball', 'baseball', 'football', 
    'soccer', 'tennis', 'golf', 'rugby', 'cricket', 'hockey', 'volleyball', 'cycling', 'f1', 'formula one', 
    'nascar', 'boxing', 'boxer', 'wrestling', 'quarterback', 'touchdown', 'goalkeeper', 'striker', 'midfielder', 
    'defender', 'inning', 'homerun', 'dunk', 'rebound', 'red sox', 'yankees', 'lakers', 'knicks', 'cowboys',
    'real madrid', 'manchester united', 'arsenal', 'chelsea', 'liverpool', 'ac milan', 'juventus', 'barcelona',
    'us open', 'french open', 'australian open', 'pga', 'lpga', 'tour de france', 'lance armstrong', 'michael phelps',
    'tiger woods', 'serena williams', 'venus williams', 'federer', 'roddick', 'agassi', 'shaq', 'kobe', 'lebron'
]
sports_weak = [
    'sport', 'sports', 'game', 'games', 'match', 'matches', 'win', 'wins', 'won', 'winner', 'victory', 
    'defeat', 'loss', 'lost', 'score', 'scores', 'scored', 'team', 'teams', 'player', 'players', 
    'coach', 'coaches', 'club', 'cup', 'open', 'round', 'final', 'finals', 'semi-final', 'season'
]

tech_strong = [
    'computer', 'software', 'hardware', 'internet', 'web', 'online', 'digital', 'technology', 'tech', 
    'google', 'microsoft', 'apple', 'intel', 'ibm', 'linux', 'windows', 'browser', 'server', 'database', 
    'virus', 'hacker', 'security', 'space', 'nasa', 'satellite', 'robot', 'mobile', 'phone', 'wireless', 
    'broadband', 'chip', 'semiconductor', 'processor', 'search engine', 'blog', 'spam', 'email', 'ipod',
    'dvd', 'mp3', 'download', 'upgrade', 'version', 'beta'
]

business_strong = [
    'stock', 'stocks', 'market', 'markets', 'price', 'prices', 'company', 'companies', 'corp', 'inc', 
    'profit', 'profits', 'loss', 'losses', 'quarter', 'earnings', 'revenue', 'sales', 'ceo', 'cfo', 
    'investor', 'investors', 'investment', 'bank', 'economy', 'economic', 'trade', 'dollar', 'euro', 
    'oil', 'crude', 'gasoline', 'merger', 'acquisition', 'ipo', 'wall street', 'dow', 'nasdaq', 
    'fed', 'federal reserve', 'inflation', 'rates', 'interest rates', 'business', 'industry', 'retail'
]

world_strong = [
    'iraq', 'iraqi', 'war', 'military', 'army', 'soldier', 'soldiers', 'president', 'minister', 'government', 
    'parliament', 'election', 'vote', 'un', 'united nations', 'police', 'court', 'crime', 'bomb', 'blast', 
    'explosion', 'kill', 'killed', 'dead', 'death', 'injured', 'disaster', 'storm', 'hurricane', 'flood', 
    'earthquake', 'country', 'nation', 'international', 'foreign', 'treaty', 'peace', 'nuclear', 'weapon', 
    'gaza', 'israel', 'palestinian', 'iran', 'russia', 'china', 'sudan', 'darfur', 'afghanistan', 'pakistan',
    'baghdad', 'kabul', 'najaf', 'fallujah'
]

def classify_score(row):
    text = (str(row['title']) + " " + str(row['description'])).lower()
    text = re.sub(r'[^\w\s]', ' ', text) # replace punctuation with space to avoid merging words
    words = set(text.split())
    
    scores = {'Sports': 0, 'Tech': 0, 'Business': 0, 'World': 0}
    
    # Sports
    for w in sports_strong:
        if w in text: # simple substring check for phrases
            scores['Sports'] += 3
    for w in sports_weak:
        if w in words: # strict word match for weak keywords
            scores['Sports'] += 1
            
    # Tech
    for w in tech_strong:
        if w in text:
            scores['Tech'] += 3
            
    # Business
    for w in business_strong:
        if w in text:
            scores['Business'] += 3
            
    # World
    for w in world_strong:
        if w in text:
            scores['World'] += 3
            
    # Heuristics adjustments
    # "game" in Tech context
    if 'game' in words and ('video' in text or 'computer' in text or 'console' in text or 'software' in text):
        scores['Tech'] += 2
        scores['Sports'] -= 1
        
    # "win" / "loss" in Business context
    if ('profit' in text or 'quarter' in text or 'stock' in text) and ('win' in words or 'loss' in words):
        scores['Business'] += 1
        scores['Sports'] -= 1
        
    return max(scores, key=scores.get), scores['Sports']

df['category'], df['sports_score'] = zip(*df.apply(classify_score, axis=1))

# Filter
sports_df = df[df['category'] == 'Sports'].copy()

result_info = {}
if len(sports_df) > 0:
    sports_df['desc_len'] = sports_df['description'].astype(str).str.len()
    sports_df = sports_df.sort_values('desc_len', ascending=False)
    
    top_candidates = sports_df[['title', 'description', 'desc_len', 'sports_score']].head(10).to_dict(orient='records')
    result_info['candidates'] = top_candidates
    result_info['count'] = len(sports_df)
else:
    result_info['error'] = "No sports articles found"

print("__RESULT__:")
print(json.dumps(result_info))"""

env_args = {'var_function-call-7032265624609699214': ['articles'], 'var_function-call-7032265624609701055': ['authors', 'article_metadata'], 'var_function-call-1088229014867811489': [{'_id': '69446a7d3891de6179ce8f35', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446a7d3891de6179ce8f36', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446a7d3891de6179ce8f37', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446a7d3891de6179ce8f38', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446a7d3891de6179ce8f39', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-1286037897333998160': [{'article_id': '0', 'author_id': '779', 'region': 'Asia', 'publication_date': '2022-09-18'}, {'article_id': '1', 'author_id': '992', 'region': 'North America', 'publication_date': '2004-03-20'}, {'article_id': '2', 'author_id': '820', 'region': 'South America', 'publication_date': '2021-02-04'}, {'article_id': '3', 'author_id': '478', 'region': 'Europe', 'publication_date': '2020-03-04'}, {'article_id': '4', 'author_id': '39', 'region': 'Africa', 'publication_date': '2012-02-01'}], 'var_function-call-14093300406947084892': [{'_id': '69446a7d3891de6179ce8f35', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446a7d3891de6179ce8f36', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446a7d3891de6179ce8f37', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446a7d3891de6179ce8f38', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446a7d3891de6179ce8f39', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-6219379591243311347': [{'_id': '69446a7d3891de6179ce8f35', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '69446a7d3891de6179ce8f36', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '69446a7d3891de6179ce8f37', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '69446a7d3891de6179ce8f38', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '69446a7d3891de6179ce8f39', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_function-call-17044733738529564342': {'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'desc_len': 94, 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, 'var_function-call-12865582274226652090': 'file_storage/function-call-12865582274226652090.json', 'var_function-call-11739956000307329855': 'Done', 'var_function-call-4672694431234522107': {'error': "[Errno 2] No such file or directory: 'var_function-call-12865582274226652090.json'"}, 'var_function-call-12674620457936421364': {'top_10_sports': [{'title': 'Open Source, Performance, and Innovation', 'description': "\\\\At work we're mostly an OSS shop.  Partly because I have a strong bias towards\\OSS but cost, reliability, security, etc are all leading factors.\\\\For the last several months now I've been in an interesting position to prove\\the benefits of OSS in a real-world environment.\\\\We've had to extend a number of OSS tools to fit into our production\\environment.  These are significant additions and non-trivial.\\\\Open Source allows you to STAND on the shoulders of gods.  For example we've\\been having a problem with the Jakarta DBCP  connection pool.  It was running\\out of connections in highly threaded environments and is slow.  Certainly\\slower than would be necessary.\\\\Long story short.  Last night  ...\\\\", 'desc_len': 708}, {'title': "Why Windows isn't Unix", 'description': '\\\\"I first heard about this from one of the developers of the hit game SimCity, who\\told me that there was a critical bug in his application: it used memory right\\after freeing it, a major no-no that happened to work OK on DOS but would not\\work under Windows where memory that is freed is likely to be snatched up by\\another running application right away. The testers on the Windows team were\\going through various popular applications, testing them to make sure they\\worked OK, but SimCity kept crashing. They reported this to the Windows\\developers, who disassembled SimCity, stepped through it in a debugger, found\\the bug, and added special code that checked if SimCity was running, and if it\\did ...\\\\', 'desc_len': 708}, {'title': 'Microsoft, IE and Bloat', 'description': '\\\\Zawodny  threads off of Scoble  on the IE issue:\\\\"I have to say, when I first read that I nearly fell off my chair laughing. I was\\thinking "how stupid ARE these IE guys?!?!?!" But we all know that Microsoft is\\full of smart people who care about what they\'re doing. So something really\\doesn\'t compute here."\\\\"Last time I checked, IE wasn\'t even close to feature parity with Mozilla\'s\\browsers. No popup blocking, no tabbed browsing, etc."\\\\"Does the IE team really not know what their product is missing?"\\\\Perhaps.  It\'s highly likely that they just don\'t know.\\\\The bigger issue here is that Microsoft products can\'t fail and they can\'t\\succeed.  Microsoft has 40-50 billion in the bank.  There ...\\\\', 'desc_len': 708}, {'title': 'THECHAT', 'description': '&lt;em&gt; Dean Cain has spent much of his life in a uniform. He\'s done time as an all-American safety at Princeton (where he established a since-broken single-season Division I-AA record for interceptions), an undrafted free agent with the Buffalo Bills (before a preseason knee injury ended his football career), a sportsman of the future (in the aptly named movie "Futuresport") and an iconic superhero (in television\'s "Lois and Clark: The New Adventures of Superman"). Next up is a set of pinstripes -- Cain plays star third baseman Conrad Dean in the CBS drama "Clubhouse," which is scheduled to debut next month. &lt;/em&gt;', 'desc_len': 631}, {'title': 'In Brief: Sleepycat releases Berkeley DB XML 2.0 (InfoWorld)', 'description': 'InfoWorld - Sleepycat Software this week announced the general availability of Berkeley DB XML 2.0, a major upgrade to its open source database for telecommunication infrastructure and enterprise data centers. This release adds support for XQuery 1.0, an emerging standard for XML data access, as well as improvements in performance and usability. Other enhancements include support for XPath 2.0, which allows the selection of a portion of an XML document, and support for the PHP API, which enables developers using the PHP scripting languages to work with XML documents.', 'desc_len': 573}, {'title': 'New Technique to Advance Semiconductor Performance', 'description': "By MATTHEW FORDAHL    (AP) -- In an advance that could lead to lighter spacecraft and smarter cars, researchers have developed a new technique for producing a high-quality semiconductor that's much more resistant to extreme conditions than the silicon found in most of today's electronics.    Devices built with the rugged material would not require cooling and other protections that add size, weight and cost to traditional silicon electronics in power systems, jet engines, rockets, wireless transmitters and other equipment exposed to harsh environments...", 'desc_len': 560}, {'title': 'Canadian Ansari X Prize Entrant Takes the Plunge in Test (SPACE.com)', 'description': 'SPACE.com - A Canadian team of rocketeers has moved one step closer to\\launching its own manned spacecraft with the successful parachute drop test of a\\crew capsule today.\\\\ nbsp;\\\\The backers of Canadian Arrow, a rocket entry in the  #36;10 million\\Ansari X Prize competition, watched happily as their crew compartment drifted\\down into Lake Ontario.\\\\ nbsp;\\\\Today totally proves our Canadian Arrow design, said\\Geoff Sheerin, leader of the London, Ontario-based Arrows bid for the X Prize.\\It went really well and everything worked as it should. ...', 'desc_len': 552}, {'title': "Unit's Report Supports Kerry's Version", 'description': "WASHINGTON - The Navy task force overseeing John Kerry's swift boat squadron in Vietnam reported that his group of boats came under enemy fire during a March 13, 1969, incident that three decades later is being challenged by the Democratic presidential nominee's critics.    The March 18, 1969, weekly report from Task Force 115, which was located by The Associated Press during a search of Navy archives, is the latest document to surface that supports Kerry's description of an event for which he won a Bronze Star and a third Purple Heart...", 'desc_len': 544}, {'title': 'U.S. Bounces Back to Beat Greece 77-71', 'description': "ATHENS, Greece - Lamar Odom made a key defensive play on Greece's Dimitris Pipanikoulaou, preventing him from getting a clean layup attempt that could have cut the United States' lead to two points, and the Americans won 77-71 Tuesday night in the second round of the Olympic men's basketball tournament.    In a much closer game than expected, the Americans bounced back from their embarrassing loss to Puerto Rico in their opener and avoided dropping to 0-2, which would have matched their loss total from the previous 68 years...", 'desc_len': 532}, {'title': 'U.S. Prepares for Possible Flu Outbreak', 'description': "WASHINGTON - Closing schools, restricting travel and rationing scarce medications may be the nation's first protections if a powerful new flu strain spurs a worldwide outbreak because it will take months to brew a vaccine, say government preparations for the next pandemic.    Specialists say it's only a matter of time before the next one strikes, and concern is rising that the recurring bird flu in Asia could be the trigger if it mutates in a way that lets it spread easily among people...", 'desc_len': 493}], 'count': 2827}}

exec(code, env_args)
