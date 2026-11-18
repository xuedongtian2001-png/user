# FedEx Roxo ("SameDay Bot") — research notes

Compiled 2026-11-18. Purpose: fact base for a postgraduate innovation-management case study treating Roxo as a failed innovation.

## READ THIS FIRST — how these notes were verified (and their limits)

1. **No web page could be opened.** Every WebFetch attempt failed: the session's network allowlist blocks the hosts (ENOTFOUND for newsroom.fedex.com, www.fedex.com, www.robotics247.com, www.aol.com, techcrunch.com, dailymemphian.com, onlinepubs.trb.org, www.mdpi.com, en.wikipedia.org; "unable to fetch" for www.theverge.com and web.archive.org). To open sources, those hosts must be allowed in the session's network settings.
2. **Everything below therefore rests on WebSearch result summaries** (about 100 queries). The "quote" given for each fact is the text **as returned by the search tool's result summary**. It usually reproduces the page's wording, but I could not check it against the live page. Treat every quote as "snippet as returned — re-verify before citing verbatim".
3. **The search budget ran out** (200 searches per turn, shared) before five final queries ran (Daily Memphian Kamen interview; Manchester aldermen vote; Memphis council approval; NYC event details; Japan indoor-testing detail). Those gaps are listed in section 7.
4. Confidence tags: **[A]** several independent outlets agree in the search results; **[B]** one source/snippet only; **[C]** conflicting or unconfirmed.
5. "n/c" = publication date not confirmed from the search results.
6. Nothing here comes from memory alone. Where I could not confirm something, it says so.

---

## 0. The "past five years" window (today = 2026-11-18)

- Strict rolling window = on or after **2021-11-18**.
- Roxo's public life: 2019-02-26 (TV debut) to 2022-10-06 (termination memo) = about 43 months.
- Portion inside the strict window: 2021-11-18 to 2022-10-06 = about 10.5 months (roughly a quarter).
- Dated Roxo events found **inside** the strict window:
  - 2022-04-11 — New Hampshire HB 116 (personal delivery devices) signed into law (DEKA's home state; Roxo cited in the 2021 debate).
  - 2022-06-08 — first international *trial* launched in Dubai (Dubai Silicon Oasis to Dubai Digital Park).
  - 2022-09-22 — DRIVE programme introduced publicly (the programme that killed Roxo).
  - 2022-10-06 — termination memo; 2022-10-07 onward — public reporting.
- Dated Roxo events in **calendar 2021** but before 2021-11-18 (inside a "2021–2026" calendar-year reading only): Feb 2021 Manchester "most advanced" trials; 2021-03-04 Maryland testimony; 2021-06-15 Nuro deal (Roxo repositioned); 2021-07-07 Japan debut; Aug 2021 Richardson, Texas simulated deliveries. A follow-up Richardson test was announced for "later this year" (2021) — I could not confirm it took place or when.
- Implication for the assignment: the *launch* (2019) is outside any five-year reading; the *failure/discontinuation decision* (Oct 2022), the only international trial (June 2022) and the corporate context (new CEO June 2022, DRIVE Sept 2022) are inside.

---

## 1. Timeline

### 1.1 Announcement (February 2019)

**F1. First public appearance on NBC's "The Tonight Show Starring Jimmy Fallon", Tuesday 26 Feb 2019.** [A]
- Source: "FedEx Unveils Future Autonomous Delivery Robot", Robotics 24/7 / Supply Chain 24/7 (reprint of FedEx release), n/c (Feb 2019). https://www.robotics247.com/article/fedex_unveils_future_autonomous_delivery_robot
- Also: "FedEx unveils home delivery robot on US TV chat show", CEP-Research, n/c. https://www.cep-research.com/news/fedex-unveils-home-delivery-robot-on-us-tv-chat-show
- Quote (snippet): "The bot made its first public appearance during NBC's The Tonight Show Starring Jimmy Fallon on Tuesday, Feb. 26."

**F2. Official announcement by press release on 27 Feb 2019: "Delivering the Future: FedEx Unveils Autonomous Delivery Robot".** [A]
- Source: FedEx Newsroom, 2019-02-27. https://newsroom.fedex.com/newsroom/thefuturefedex/ (page not opened; body text seen only via reprints, e.g. ITWeb https://www.itweb.co.za/content/KWEBb7yaoYJ7mRjO)
- Quote (snippet): "With the bot, retailers will be able to accept orders from nearby customers and deliver them by bot directly to customers' homes or businesses the same day."

**F3. Launch retail partners named: AutoZone, Lowe's, Pizza Hut, Target, Walgreens, Walmart.** [A] (one outlet listed only four of them)
- Source: FedEx release as reprinted (Robotics 24/7, as F1); Dallas Morning News 2019-04-16 (F14).
- Quote (snippet): FedEx "is collaborating with companies such as AutoZone, Lowe's, Pizza Hut, Target, Walgreens and Walmart to help assess retailers' autonomous delivery needs."
- Note the wording: partners were to "help assess" needs — not announced as customers or as pilot sites.

**F4. Developed with DEKA Development & Research Corp. and Dean Kamen (iBOT, Segway).** [A]
- Source: as F1/F2.
- Quotes (snippets): "developed in collaboration with DEKA Development & Research Corp. and its founder Dean Kamen, inventor of many life-changing technologies, including the iBot™ Personal Mobility Device and the Segway." Kamen: "The bot has unique capabilities that make it unlike other autonomous vehicles."

**F5. Brie Carere (EVP, chief marketing and communications officer) fronted the announcement.** [B]
- Source: "FedEx will start testing autonomous delivery bots", SiliconANGLE, 2019-02-27. https://siliconangle.com/2019/02/27/fedx-will-start-testing-autonomous-delivery-bots
- Quote (snippet, paraphrased by tool): Carere called the bot "an innovation designed to change the face of local delivery".

**F6. Testing promised for "this summer" (2019) in select markets including Memphis, "pending final city approvals"; first tests to be deliveries between FedEx Office locations.** [A]
- Source: FedEx release reprints (F1); "FedEx unveils new same-day delivery robot that will be tested in Memphis", The Daily Helmsman (Univ. of Memphis), Sept 2019. https://dailyhelmsman.com/article/2019/09/fedex-unveils-new-same-day-delivery-robot-that-will-be-tested-in-memphis
- Quotes (snippets): "FedEx plans to test the bot this summer in select markets, including Memphis, Tenn., pending final city approvals." / "The initial test will have the robot making deliveries between select FedEx office locations which currently offer a SameDay City service."

### 1.2 Design and specifications

**F7. Top speed 10 mph; maximum payload 100 lb.** [A]
- Source: "FedEx to roll out delivery robot capable of 8-mile round-trip trek", FreightWaves, n/c (Feb 2019). https://www.freightwaves.com/news/parce-fed-ex-to-roll-out-same-day-delivery-bot
- Quote (snippet): "can motor up to 10 miles per hour carrying a 100-pound maximum payload, FedEx said."

**F8. Sensors/software: LiDAR and multiple cameras, machine-learning obstacle avoidance; battery-powered, zero-emission.** [A]
- Source: Supply Chain Dive, "FedEx autonomous same-day delivery bot", n/c (Feb 2019). https://www.supplychaindive.com/news/fedex-autonomous-same-day-delivery-bot-last-mile/549341/
- Quote (snippet): "Equipped with lidar and multiple cameras, the battery-powered FedEx bot is designed to travel on sidewalks and along roadsides."

**F9. Built on DEKA's iBOT powered-wheelchair base; can negotiate curbs, unpaved surfaces and steps.** [A]
- Source: as F8; STAT Times (F16).
- Quotes (snippets): "designed to negotiate curbs, unpaved surfaces and small flights of steps to a front porch." / "Roxo uses DEKA's established iBot electric wheelchair base that is capable of negotiating rough terrain, steep inclines and unpaved surfaces."

**F10. Size and weight — FedEx's own page: about 450 lb; 51.50" H x 39" L x 29" W. CONFLICT: Wired (Aug 2020, via reprint) reported about 200 lb; a dimensions database says 200 lb / 58".** [C]
- Source 1: "Meet Roxo™, the FedEx SameDay Bot", FedEx (corporate site), n/c. https://www.fedex.com/en-ge/about/sustainability/our-approach/roxo-delivery-robot.html — snippet: "450 lbs. approx. weight"; "51.50" Height x 39" Length x 29" Width".
- Source 2: "Next-gen home delivery tested in Richardson", Richardson Today (City of Richardson), Aug 2021. https://richardsontoday.com/next-gen-home-delivery-tested-in-richardson/ — snippet: "'Roxo,' which weighs 450 pounds, is about 5.5 feet-tall and can hold about 100 pounds."
- Source 3 (conflict): Wired, "Amazon and FedEx Push to Put Delivery Robots on Your Sidewalk", Aug 2020, seen via Teamsters reprint https://teamster.org/2020/08/amazon-and-fedex-push-to-put-delivery-robots-on-your-sidewalk/ — the search summary reports Roxo "at about 200 pounds".
- Assessment: the FedEx page and the city source agree on 450 lb; prefer those. Height also differs (51.5 in vs "about 5.5 feet").

**F11. Operating range: designed for a three-to-five-mile radius of a retailer; operates on sidewalks, bike lanes and roadsides.** [A]
- Source: FedEx Roxo page (F10). Quote (snippet): "designed to be used in a three-to-five mile radius of a retailer's location"; "operates on sidewalks, bike lanes and roadsides".
- FreightWaves headline (F7) says "8-mile round-trip".

**F12. Supervised by remote human teleoperators.** [A]
- Source: "Won't you be my neighbor? Meet FedEx's new delivery bot", WKNO FM (Memphis NPR), n/c (2019). https://www.wknofm.org/post/wont-you-be-my-neighbor-meet-fedexs-new-delivery-bot
- Quote (snippet): "a remote teleoperator is always connected, and can take over if Roxo needs assistance."

**F13. DEKA base said to have about 10 million hours of real-world operation (FedEx one-pager).** [B]
- Source: "Roxo one-pager, Jan 2021", FedEx document hosted by TRB (NCHRP 20-24(128)). https://onlinepubs.trb.org/onlinepubs/NCHRP/20-24-128/media/w2thr4bn/roxo-onepager-jan2021.pdf (PDF not opened; fragments only).

### 1.3 US pilots and tests

**F14. April 2019 — Plano/Frisco, Texas plan announced by Brian Philips (president and CEO, FedEx Office); customer deliveries promised for 2020; bots would carry no goods in initial tests.** [A]
- Source: Melissa Repko, "FedEx Office's new bots can deliver pizza, groceries or even bring chicken noodle soup to the sick", The Dallas Morning News, 2019-04-16. https://dallasnews.com/business/technology/2019/04/16/fedex-offices-new-bots-can-deliver-pizza-groceries-even-bring-chicken-noodle-soup-sick (republished phys.org 2019-04-17).
- Quotes (snippets): "The bots will start making customer deliveries in 2020, he said." / "During testing, they won't ferry any goods, but will help the company learn more about how they operate."
- Also: "FedEx to Experiment With Driverless Deliveries in Collin County", NBC DFW, n/c (2019). https://www.nbcdfw.com/news/local/fedex-to-experiment-with-driverless-deliveries-in-collin-county/252961 — snippet: "During a test period that begins in late July or early August, the robot will handle internal deliveries between Plano's FedEx Office Headquarters on Legacy Drive and a FedEx retail location a mile and a half away in the Legacy West development."

**F15. 31 July 2019 — FedEx signed an agreement with the City of Memphis allowing testing; two routes under three miles (near University of Memphis; downtown).** [A]
- Source: The Daily Helmsman, Sept 2019 (URL in F6). Also "FedEx preps delivery robot Roxo for Memphis test", Daily Memphian, 2019-08-27. https://dailymemphian.com/article/7066/FedEx-preps-delivery-robot-Roxo-for-Memphis-test
- Quotes (snippets): "FedEx signed an agreement with the city of Memphis on July 31 to allow testing of Roxo." / "Roxo will be tested in two locations; one route near the University of Memphis and another downtown. Each route will be less than three miles."

**F16. 6 Aug 2019 — "Roxo" launched/first demonstration delivery in Manchester, New Hampshire (DEKA's home city). Earliest dated use of the name "Roxo" that I found.** [A for event; C for exact naming date]
- Source: "FedEx launches Roxo for same-day delivery in Manchester", STAT Times, n/c (Aug 2019). https://www.stattimes.com/news/fedex-launches-roxo-for-sameday-delivery-in-manchester-logistics
- Source: "Roxo the robot delivers its first package in historic partnership with FedEx and Kamen's DEKA", Manchester Ink Link, n/c (Aug 2019). https://manchesterinklink.com/roxo-the-robot-delivers-its-first-package-in-historic-partnership-with-fedex-and-kamens-deka/
- Quotes (snippets): "FedEx in association with Manchester-based DEKA Research & Development Corporation has officially launched Roxo, a battery-operated robot on August 6 in Manchester." / Rebecca Yeung: the company wants to fully test it, "so while we don't have a timeline, we're working toward a solo run once the technology is proven."
- Name: Ink Link reports "Roxo" means "purple" in Portuguese (FedEx brand colour). I did not find a separate naming announcement or its date.
- City permission: Manchester adopted a special ordinance / temporarily suspended its rule against driving on sidewalks (Govlaunch project summary, n/c: https://govlaunch.com/stories/manchester-nh-partners-with-fedex-to-test-ai-delivery-bot). Vote date not confirmed.

**F17. By late 2019 FedEx listed four US test markets: Memphis TN; Plano and Frisco TX; Manchester NH.** [A]
- Source: "FedEx robots sent packing by NYC", TechCrunch, 2019-11-26. https://techcrunch.com/2019/11/26/fedex-robots-sent-packing-by-nyc/ ; FleetOwner (F21).
- Quote (snippet): test sites were "Memphis, Tennessee, Plano and Frisco, Texas, and Manchester, New Hampshire, according to a spokesperson."

**F18. 6 Jan 2020 — CES panel (Brie Carere with Walgreens CMO Vineet Mehra), Roxo on stage; FedEx "hopes to partner with retailers on commercial pilots" in summer 2020.** [B]
- Source: "CES 2020: FedEx, Walgreens execs share last-mile delivery solutions", FreightWaves, Jan 2020. https://www.freightwaves.com/news/ces-2020-autonomous-tech-customer-experience-key-to-last-mile-innovation
- Quote (snippet): Roxo is "a battery-operated last-mile delivery robot"; FedEx "hopes to partner with retailers on commercial pilots that summer."

**F19. October 2020 — still pre-commercial. USA Today: no commercial release date; Yeung: Roxo is a niche, same-day/on-demand tool, not suited to high-density routes; Philips: COVID "accelerated the demand".** [A]
- Source: "'Contactless' shipping paving way for FedEx bot", USA Today (US edition, via PressReader), 2020-10-08. https://www.pressreader.com/usa/usa-today-us-edition/20201008/281754156785211 — snippet: "a commercial release date for the bot has not been announced."; it "underwent tests in downtown Memphis and East Memphis ... It also was tested in Manchester, New Hampshire, and the Texas cities of Plano and Frisco."
- Source: "4 takeaways from FedEx's Peak Innovation Showcase" (headline reconstructed from URL slug), Supply Chain Dive, n/c (Oct/Nov 2020). https://www.supplychaindive.com/news/4-takeaways-fedex-peak-innovation-showcase/588102/ — snippet: Philips: "COVID has accelerated the demand for these reliable autonomous last-mile delivery type devices."
- Source: TC Sessions: Mobility 2020 session "The Changing Face of Delivery" (TechCrunch video, recorded 2020-10-06) with Rebecca Yeung. https://techcrunch.com/video/the-changing-face-of-delivery-2

**F20. Jan–Feb 2021 — "most advanced set of trials yet" completed in Manchester NH; FedEx said 2021 would be its "most advanced testing period yet".** [B]
- Source: "Roxo FedEx SameDay Bot", 3BL Media (FedEx-supplied content), 2021-02-05. https://www.3blmedia.com/news/roxo-fedex-sameday-bot — snippet: the bot "recently completed its most advanced set of trials yet in Manchester, New Hampshire."
- Source: FedEx Roxo page (F10) — snippet: "looking forward to our most advanced testing period yet in 2021."
- Source: Roxo one-pager, Jan 2021 (F13) — tested in Manchester, Memphis, Plano, Frisco.

**F21. Aug–Sept 2021 — Richardson, Texas: simulated (not real customer) deliveries in the Marlborough Square neighbourhood near Berkner High School; a follow-up test was planned for later in 2021.** [A]
- Source: "FedEx testing autonomous delivery robot on Richardson streets", The Dallas Morning News, 2021-08-30. https://dallasnews.com/news/2021/08/30/fedex-testing-autonomous-delivery-robot-on-richardson-streets
- Source: "Richardson serves as test location for home delivery robot", Community Impact, 2021-09-27. https://beta2.communityimpact.com/dallas-fort-worth/richardson/technology/2021/09/27/richardson-serves-as-test-location-for-home-delivery-robot
- Source: Richardson Today (F10).
- Quotes (snippets): "Simulated deliveries occurred in a neighborhood near Berkner High School." / "Roxo will be adjusted based on the results from the test, and another test will happen in Richardson later this year, according to the city newsletter." / FedEx "worked with Richardson Police and Fire, as well as City engineers and the Marlborough Square HOA".
- Not confirmed: whether the later 2021 Richardson test happened.

**Scale.** I found no source giving the number of robots built, deliveries made, miles driven, or programme cost.

### 1.4 International demonstrations and trials

**F22. 15 Oct 2019 — Dubai: RTA and FedEx Express signed an MoU; Roxo shown at the Dubai World Congress for Self-Driving Transport; "first international appearance".** [A]
- Source: "Dubai to select community for autonomous delivery device", MEED, Oct 2019. https://meed.com/dubai-select-community-autonomous-delivery-device ; "FedEx to test delivery robot Roxo in Dubai", Gulf News, Oct 2019. https://gulfnews.com/uae/fedex-to-test-delivery-robot-roxo-in-dubai-1.67150601 ; FedEx Newsroom "FedEx Welcomes Roxo, the FedEx SameDay Bot, to the U.A.E." https://newsroom.fedex.com/newsroom/fedex-welcomes-roxo-the-fedex-sameday-bot-to-the-u-a-e/
- Quotes (snippets): "RTA and Fedex signed the memorandum of understanding (MoU) to test Roxo in Dubai on 15 October on the sidelines of the ongoing Dubai Congress for Self-driving Transport." / Dubai "the first city in the world outside the USA to host this appearance."
- Signatories: Ahmed Hashim Bahrozyan (RTA) and James R. Muhs (FedEx Express regional president, MEISA).

**F23. 18 Nov 2019 — Dubai Airports joined the "UAE Customer Advisory Board for Roxo".** [B]
- Source: "FedEx Express welcomes Dubai Airports to Customer Advisory Board for Roxo™, the FedEx SameDay Bot", FedEx Newsroom, 2019-11-18. https://newsroom.fedex.com/newsroom/fedex-express-welcomes-dubai-airports-to-customer-advisory-board-for-roxo-the-fedex-sameday-bot
- Quote (snippet): Eugene Barry (Dubai Airports): "This is a great opportunity to see Roxo operate in a live international travel environment." Other board members not named in results.

**F24. 7 July 2021 — Japan: first Asia-Pacific appearance. Nature of activity is characterised differently across sources.** [A for date; C for nature]
- Source: "The Future of Logistics Arrives in Asia: Autonomous Delivery Device Roxo™, the FedEx SameDay Bot, Lands in Japan", FedEx Newsroom (Hong Kong dateline), 2021-07-07. https://newsroom.fedex.com/newsroom/the-future-of-logistics-arrives-in-asia-autonomous-delivery-device-roxo-the-fedex-sameday-bot-lands-in-japan/
- Quote (snippet): "FedEx Express has announced that Roxo, the FedEx SameDay Bot, will make its first appearance in Asia Pacific in Japan on July 7."; Japan described as "an ideal market for FedEx to explore opportunities to test Roxo in the future."
- Conflict: itnews.asia headline "FedEx brings Roxo bot to Japan in contactless delivery trial" (https://www.itnews.asia/news/fedex-brings-roxo-bot-to-japan-in-contactless-delivery-trial-567259) calls it a trial; Frontier Enterprise (URL not captured) reportedly says FedEx "planned to start indoor testing". FedEx's own wording ("explore opportunities to test ... in the future") suggests an appearance/demonstration, not a public-road pilot. Executive quoted: Kawal Preet (president, FedEx Express AMEA).

**F25. 8 June 2022 — Dubai: first trial outside the US launched, with DIEZ (Dubai Integrated Economic Zones Authority) and RTA; route between Dubai Silicon Oasis HQ and Dubai Digital Park.** [A] — INSIDE THE FIVE-YEAR WINDOW
- Source: "FedEx SameDay Bot, Roxo, debuts in Dubai", Gulf Business, 2022-06-08. https://gulfbusiness.com/en/2022/tech/fedex-sameday-bot-roxo-debuts-in-dubai
- Source: "Roxo rolls on: FedEx's same-day delivery bot to do trials in Dubai", syndicated (appears to be FreightWaves content; original URL not captured), 2022-06-09. https://business.dptribune.com/dptribune/news/read/42470268/roxo_rolls_on
- Source: "FedEx launches first international trial of Roxo, the FedEx SameDay Bot" (press release via Zawya). https://www.zawya.com/en/press-release/companies-news/fedex-launches-first-international-trial-of-roxo-the-fedex-sameday-bot-y4ye9hkh
- Quotes (snippets): "FedEx Express has signed an agreement with the Dubai Integrated Economic Zones Authority (DIEZ) to start autonomous trials. They'll be conducted between the Dubai Silicon Oasis headquarters and Dubai Digital Park." / "the first time Roxo's autonomous capabilities are tested outside of the US".
- Four months later the programme was cancelled.

### 1.5 Regulatory and legal events

**F26. 23–26 Nov 2019 — New York City. Mayor de Blasio tweeted on 23 Nov; NYC DOT lawyers sent a cease-and-desist letter on Monday 25 Nov; FedEx said the bot was visiting for a special event and was not being tested in NYC.** [A]
- Source: TechCrunch, 2019-11-26 (F17). Source: "FedEx's Roxo delivery bot gets chilly reception in New York City", FleetOwner, Nov 2019. https://www.fleetowner.com/technology/autonomous-vehicles/article/21704527/fedexs-roxo-delivery-bot-gets-chilly-reception-in-new-york-city . Source: "New York warns FedEx to keep their delivery robots off the city's streets", CNN wire via Fox17, 2019-11-26. https://fox17online.com/2019/11/26/new-york-warns-fedex-to-keep-their-delivery-robots-off-the-citys-streets
- Quotes (snippets): letter warned failure to stop "may result in the seizure of the property, notices of violation and/or the commencement of legal action." / de Blasio: "never get a robot to do a New Yorker's job" (tool's rendering of the tweet). / FedEx: Roxo was "visiting New York City for a special event and is not currently being tested in that market"; "future testing plans are not yet determined."
- Legal basis (snippet): city vehicle and traffic law prohibits motor vehicles on sidewalks without a special exemption.
- Not confirmed: what the event was; any outcome beyond the letter.

**F27. State "personal delivery device" (PDD) laws: a patchwork with very different weight/speed limits, partly driven by Amazon and FedEx lobbying.** [A]
- Source: Wired, "Amazon and FedEx Push to Put Delivery Robots on Your Sidewalk", Aug 2020 (seen via Teamsters reprint, URL in F10). Snippet: Amazon and FedEx "backed similar delivery-robot bills in more than a dozen states this year, and at least six have become law."
- Source: "Delivery robot bills, laws proliferate in state legislatures", Supply Chain Dive, n/c (2023). https://www.supplychaindive.com/news/delivery-robot-bills-laws-proliferate-state-legislatures/648303/ — snippets: "Amazon and FedEx pushed for legislation in 2019 and 2020 that catered to the different use cases for their particular bots."; "Variance in state laws often depends on which bot operator led the charge to pass a particular bill, said Carl Hansen ... of delivery bot company Coco."; "Bots as heavy as 500 pounds can roam as fast as 4 miles per hour on Georgia sidewalks ... In New Hampshire, robots can travel up to 10 miles per hour on sidewalks, but they can't weigh more than 80 pounds."; "Virginia was the first state to permit personal delivery devices ... in 2017".
- Individual statutes surfaced (statute records, not opened):
  - Texas SB 969 — effective 2019-06-10 (Transportation Code ch. 552A). https://statutes.capitol.texas.gov/Docs/TN/htm/TN.552A.htm
  - Tennessee SB 2836 — effective 2020-07-01; up to 10 mph in pedestrian areas (Tenn. Code § 55-8-209). https://legiscan.com/TN/text/SB2836/2019
  - Pennsylvania SB 1199 / Act 106 of 2020 — enacted 2020-11-01, effective 2021-01-30; 550 lb limit without cargo; PDDs classed as pedestrians; 12 mph in pedestrian areas. Pittsburgh City Paper: https://pghcitypaper.com/news/pennsylvania-legalizes-autonomous-delivery-robots-classifies-them-as-pedestrians-18482040 — snippet: bills "have largely been pushed by delivery companies like Amazon and FedEx, according to WIRED magazine"; opposition from "pedestrian and accessibility advocates, as well as labor unions like the Teamsters."
  - Maryland SB 726 / Ch. 351 — approved 2021-05-18, effective 2021-07-01.
  - New Hampshire HB 116 — signed 2022-04-11 (Chapter 13). https://legiscan.com/NH/bill/HB116/2022
  - Kansas SB 435 — died 2020-05-21; successor SB 161 vetoed by Gov. Kelly in 2022.
- I found **no** source showing FedEx's role in the Texas or Tennessee bills specifically.

**F28. FedEx itself told Maryland legislators (4 Mar 2021) that existing weight limits barred Roxo from the state — direct evidence that Roxo's size/weight collided with PDD rules written around smaller robots.** [B]
- Source: FedEx written testimony on SB 726, Maryland Senate Judicial Proceedings Committee, 2021-03-04 (PDF not opened). https://mgaleg.maryland.gov/cmte_testimony/2021/jpr/1_sbZbQF_zjvgbDtI5JHUyc6o9sQok_ou.pdf
- Quote (snippet): "current weight restrictions prohibit Roxo from operating in the State of Maryland."

**F29. Kansas 2020: FedEx sought to enlarge an Amazon-backed bill to allow bigger, faster devices; the League of Kansas Municipalities objected.** [B]
- Source: Wired via Teamsters reprint (F10); Kansas Legislature testimony records. Snippets: FedEx "sought to expand the proposal to allow bigger and faster automated vehicles than what Amazon originally proposed."; League director: "the weight and speed seem well beyond the bounds of anything that we had worked in good faith with Amazon to reach agreement on."; FedEx's proposal "would increase the force of a collision by 600%" (date of that statement not confirmed).

**F30. New Hampshire 2021: bill debate framed around "legalizing Roxo".** [B]
- Source: "House panel embraces legalizing Roxo bot on NH roads", NH Union Leader via Yahoo, n/c (2021). https://news.yahoo.com/house-panel-embraces-legalizing-roxo-224700540.html ; GovTech "New Hampshire lawmakers consider delivery bot legislation" https://www.govtech.com/fs/new-hampshire-lawmakers-consider-delivery-bot-legislation
- Snippet: amendment would permit devices like Roxo "up to 12 mph on sidewalks and as fast as 20 mph on roadways."
- Not confirmed: whether the law as enacted (2022) accommodates a 450 lb device (Supply Chain Dive reports an 80 lb cap in NH).

### 1.6 Shutdown (October 2022)

**F31. Decision communicated in an internal memo dated 6 Oct 2022 from Sriram Krishnasamy, chief transformation officer, as part of the DRIVE programme.** [A]
- Source: "FedEx powers down delivery robot", Automotive Fleet / Work Truck, Oct 2022. https://www.automotive-fleet.com/10183550/fedex-powers-down-delivery-robot
- Source: "FedEx nixes Roxo SameDay Bot developed in part by DEKA", New Hampshire Union Leader via AOL, 2022-10-10. https://www.aol.com/news/fedex-nixes-roxo-sameday-bot-225300906.html
- Quotes (snippets): "The decision was announced in an Oct. 6 memo from Sriram Krishnasamy, chief transformation officer". Memo wording: **"Although robotics and automation are key pillars of our innovation strategy, Roxo did not meet necessary near-term value requirements for DRIVE."**

**F32. How it became public: Robotics 24/7 obtained the internal memo and FedEx confirmed.** [A; exact date C]
- Source: Cesareo Contreras, "FedEx Shuts Down Roxo Same Day Delivery Service as Amazon Scales Back Scout Program", Robotics 24/7, dated 2022-10-07 according to two search summaries (not confirmed on page). https://www.robotics247.com/article/fedex_shuts_down_robotic_same_day_delivery_service_amazon_scales_back_scout_program
- Quote (snippet): "FedEx Corp. is shutting down its robotic same-day delivery service, according to an internal memo obtained by Robotics 24/7." The article spells the executive "Krishnasam" in at least one place.
- FedEx statement (snippets): **"FedEx has stepped back from the research and development program for a same day bot as we prioritize several nearer-term opportunities."** / "The collaboration with DEKA has been outstanding, and we will continue to explore compelling opportunities arising from the technologies we have developed together." / "We are immensely proud of our role in working with DEKA to advance this cutting-edge technology".

**F33. Follow-on coverage.** [A]
- Union Leader, 2022-10-10 (URL in F31): spokeswoman confirmed by email; nearer-term opportunities "such as robotic technology in its sorting facilities"; "Kamen could not be reached for comment on Monday".
- Rob Moore, "FedEx terminates Roxo, the same-day delivery robot", Daily Memphian, 2022-10-12 (also listed 2022-10-14). https://dailymemphian.com/article/31529/memphis-fedex-ends-development-of-roxo-delivery-robot — snippet: "Less than four years after launching Roxo, the same-day delivery bot, FedEx is ending the project."
- James Vincent, "FedEx is shutting down its robot delivery program", The Verge, mid-Oct 2022 (original URL and exact date NOT confirmed; seen via repost https://pipedot.org/64VGB) — snippet: "first reported by Robotics 24/7"; Roxo "was trialed in the U.S., the United Arab Emirates and Japan, making deliveries three to five miles away from local delivery centers."
- "FedEx shuts down last mile delivery robot programme", Internet Retailing, 2022-10-18. https://internetretailing.net/?p=61586
- "FedEx, Amazon Rethink Last-Mile Autonomous Robot Deliveries", NACS Daily, 2022-10-19. https://www.convenience.org/Media/Daily/2022/Oct/19/3-FedEx-Amazon-Rethink-Last-Mile-Robot-Delive_Tech
- No FedEx press release announcing the shutdown was found; the company appears only to have responded to press queries.

---

## 2. What Roxo was meant to achieve

**F34. Customer problem / business case: same-day, on-demand local delivery for retailers from stores to nearby homes and businesses.** [A]
- Source: FedEx release reprints (F1, F2). Quote (snippet): "On average, more than 60 percent of merchants' customers live within three miles of a store location."

**F35. Link to FedEx SameDay City (a FedEx Office service): the bot was to complement it.** [A]
- Source: FedEx release reprints (ITWeb, F2). Quote (snippet): "FedEx Office currently offers a SameDay City service that operates in 32 markets and 1,900 cities using branded FedEx vehicles and uniformed FedEx employees."

**F36. Economic logic stated by FedEx: remove the inefficiency of a truck/driver carrying a single on-demand box; a niche FedEx did not then serve.** [B]
- Source: USA Today 2020-10-08 (F19); Supply Chain Dive showcase article (F19). Snippets: Roxo would address deliveries "that aren't cost efficient for a FedEx delivery driver"; "the FedEx SameDay bot would address a niche offering the company does not currently provide"; Roxo is "not suited for 'high density' delivery routes."

**F37. Use cases FedEx listed: auto parts, pizza, home-improvement goods, general merchandise, groceries, prescriptions.** [B]
- Source: Community Impact 2021-09-27 (F21) citing FedEx website; Manchester Ink Link (F16).

**F38. Promised versus delivered.** [A for each element; synthesis mine]
- Promised: tests "this summer" 2019 (F6); customer deliveries "in 2020" (F14); commercial pilots with retailers in summer 2020 (F18); "most advanced testing period yet in 2021" (F20).
- Delivered: route tests without goods and internal FedEx Office transfers (2019, F14–F15); a staged first delivery in Manchester (Aug 2019, F16); "no timeline" (Yeung, Aug 2019, F16); "a commercial release date ... has not been announced" (Oct 2020, F19); simulated deliveries in Richardson (Aug 2021, F21); a campus-style trial in Dubai (June 2022, F25); cancellation (Oct 2022, F31).

**F39. Did Roxo ever make paid commercial deliveries? No evidence found that it did.** [C — absence of evidence]
- No source in about 100 searches reports a paid/commercial delivery, a named retailer pilot going live, or delivery volumes. All documented activity is testing, simulation or demonstration. The Verge's post-mortem phrasing ("making deliveries three to five miles away") is not supported by any contemporaneous report of live customer service.
- Critical assessment: "Artificial Intelligence at FedEx", Emerj, n/c. https://emerj.com/artificial-intelligence-at-fedex/ — snippet: FedEx "has repeatedly and consistently trumpeted Roxo in its annual reports, website, and social media while having little to show for it in the way of results."

---

## 3. Reported and analysed reasons for failure

### 3.1 Official reason: "near-term value" under DRIVE
- Memo and statement wording: F31, F32.

### 3.2 Corporate context (dates)

**F40. CEO change: announced 28 Mar 2022; Raj Subramaniam became president and CEO on 1 June 2022; founder Fred Smith became executive chairman.** [A]
- Source: "FedEx Names Operating Chief Subramaniam to Succeed Smith as CEO", Bloomberg, 2022-03-28. https://www.bloomberg.com/news/articles/2022-03-28/fedex-names-operating-chief-subramaniam-to-succeed-smith-as-ceo
- Snippet: Smith to oversee "sustainability, innovation, public policy and other global issues" as executive chairman.

**F41. Krishnasamy became EVP and chief transformation officer effective 1 Aug 2022 (offer letter dated 11 July 2022, signed by Subramaniam).** [B]
- Source: FedEx executive offer letter (SEC exhibit) via Justia. https://contracts.justia.com/companies/fedex-512/contract/1289797

**F42. 15 Sept 2022: FedEx pre-announced weak Q1 FY23 results and withdrew FY23 guidance; cost actions included closing 90+ FedEx Office locations; shares fell about 21% on 16 Sept (largest one-day drop in its history).** [A]
- Source: "FedEx Has Biggest Drop In Over 40 Years After Pulling Forecast", Bloomberg via BNN Bloomberg, 2022-09-15/16. https://www.bnnbloomberg.ca/fedex-has-biggest-drop-in-over-40-years-after-pulling-forecast-1.1819473
- Source: "FedEx's disastrous announcement raises concerns about company's core direction", FreightWaves, Sept 2022. https://www.freightwaves.com/news/fedexs-disastrous-announcement-raises-concerns-about-companys-core-direction
- Relevance: FedEx Office, Roxo's original organisational home, was itself a cost-cutting target three weeks before the memo.

**F43. 22 Sept 2022: Q1 FY23 release introduced DRIVE publicly — FY23 savings of $2.2–2.7bn and about $4.0bn of further savings by FY25; DRIVE supports the "Deliver Today, Innovate for Tomorrow" strategy "introduced in June".** [A]
- Source: "FedEx Corp. Reports First Quarter Results", FedEx Newsroom / SEC Ex-99.1, 2022-09-22. https://newsroom.fedex.com/newsroom/global-english/fedex-corp-reports-first-quarter-fy23-results ; https://www.sec.gov/Archives/edgar/data/1048911/000095017022018764/fdx-ex99_1.htm
- Later: FedEx said DRIVE reached its $4bn target by end of FY25 (STAT Times, 2025). https://www.stattimes.com/logistics/fedex-drive-to-save-4bn-by-fy25-1347403
- Sequence: new CEO (1 Jun) -> transformation officer (1 Aug) -> profit warning (15 Sep) -> DRIVE (22 Sep) -> Roxo memo (6 Oct): two weeks from DRIVE's launch to Roxo's termination.

### 3.3 Journalist / analyst / practitioner explanations

**F44. Cost-cutting amid slowing demand.** [A]
- Source: Supply Chain Dive feature on Roxo, Scout and mass adoption of delivery robots (exact headline NOT captured; URL slug "fedex-roxo-amazon-scout-delivery-robots-mass-adoption"; also run by Smart Cities Dive), n/c (after Oct 2022). https://www.supplychaindive.com/news/fedex-roxo-amazon-scout-delivery-robots-mass-adoption/646702/ — snippet: FedEx "canceled Roxo to 'prioritize several nearer term opportunities' as overall demand for its services was slowing."; Smart Cities Dive version: "FedEx canned Roxo less than four years after its flashy debut."
- Source: Granite Geek (Concord Monitor) blog relaying the Union Leader, Oct 2022. https://granitegeek.concordmonitor.com/?p=12425 — describes it as a cost-cutting move.

**F45. Unit economics need scale and density that sidewalk robots had not reached; range and capacity limits; thinner venture funding.** [B]
- Source: Supply Chain Dive feature (F44). Snippets: "'You need a lot of scale and you need a lot of density,' Rash said" (speaker's affiliation not visible in results); Bern Grush (Urban Robotics Foundation): "This whole industry needs to deliver a million things an hour."; bots "don't have the range or capacity of gas-powered vehicles"; "Economic uncertainty has thinned the pool of funds available from venture capital and private equity firms".
- No published per-delivery cost figure for Roxo was found.

**F46. Technology/industry immaturity (general, not Roxo-specific).** [B]
- Source: Eugene Demaitre, "Robotics Company Setbacks Belie Industry Strength, Say Experts", Robotics 24/7, 2022-07-15. https://www.robotics247.com/article/robotics_company_setbacks_belie_industry_strength_say_experts — Aaron Prather (senior technical adviser, FedEx Express, writing personally on LinkedIn): some companies are "overpromising and underdelivering" because the technology is not there yet. Said three months before Roxo was cancelled; not about Roxo by name.
- Source: Urbanism Next / Knight Foundation report (A14 below), 2022-09-06 — key finding: value in city-level control "while business models and technologies are maturing but not yet ready to scale"; Axios headline same day: "Delivery robots aren't quite ready to roll". https://www.axios.com/2022/09/06/delivery-robots-study

**F47. Product judged ineffective / over-promoted.** [B]
- Gizmodo, "FedEx Gives Up On Its 'Roxo' Delivery Robot", Oct 2022. https://gizmodo.com/fedex-roxo-delivery-robot-amazon-1849669187 — described (per syndicated copy) as "cute but mostly ineffective".
- Emerj (F39).

**F48. Regulation and design fit.** [B; my synthesis flagged]
- Evidence: 450 lb vehicle (F10) vs PDD statutes often written for far lighter robots (F27); FedEx's own Maryland testimony that weight limits barred Roxo (F28); FedEx lobbying for bigger/faster limits in Kansas (F29); NYC cease-and-desist (F26); Wired's finding that laws track whichever operator lobbied (F27).
- Caveat: **no source found links regulation to FedEx's cancellation decision**; FedEx never cited it. Treat as a contributing-constraint hypothesis, not a reported cause.

**F49. Weak or unproven demand.** [C]
- Evidence for: partners only ever "help[ed] assess" needs (F3); no named retailer pilot went live (F39); Yeung called it a "niche" (F36); Amazon said Scout had "aspects of the program that weren't meeting customers' needs" (F55).
- Evidence against / FedEx's view: Philips said COVID "accelerated the demand" (F19).
- No demand or willingness-to-pay data for Roxo was found.

### 3.4 Where sources disagree
- **Firm-specific vs sector-wide.** FedEx's memo frames it as failing an internal "near-term value" hurdle (portfolio/cost decision). Supply Chain Dive, Gizmodo and Axios/Urbanism Next frame it as sector immaturity (scale, density, infrastructure). Robotics 24/7's expert piece argues setbacks "belie industry strength".
- **Outlook.** Supply Chain Dive: "many of the executives, researchers and regulators interviewed say yes" to eventual mass adoption; Starship kept growing (F56). So Roxo's end is not straightforward evidence that the category failed.
- **Was it a "service"?** Robotics 24/7's headline says FedEx shut down a "Same Day Delivery Service"; FedEx's statement calls it a "research and development program". The evidence supports the latter (F39).
- **Facts in dispute:** weight (450 vs 200 lb, F10); Japan as "trial" vs "appearance" (F24); trial geography in post-mortems (some say US + Dubai, The Verge adds Japan).
- **Academic explanations of Roxo's failure specifically: none found.**

---

## 4. Process and internal factors

**F50. Origin: a personal relationship between Fred Smith and Dean Kamen; Smith phoned Kamen about local delivery; DEKA adapted the iBOT.** [B]
- Source: "FedEx Robot Could Soon Be Delivering Packages In Manchester, NH", CBS Boston, n/c (2019). https://www.cbsnews.com/amp/boston/news/fedex-robot-delivering-packages-manchester-nh — snippets (tool paraphrase): Kamen "is good friends with FedEx CEO Fred Smith"; Smith phoned Kamen about being in local delivery.
- Source: Manchester Ink Link (F16): Kamen described a "favor" Smith asked "a couple of years" earlier — "the world's best last-mile pedestrian-friendly delivery device"; Smith "flew into Manchester for a demo". (Snippet fragmentary.)
- Source: "Dean Kamen's iBot saved FedEx years of R&D on delivery robot, inventor says", Daily Memphian, n/c (2019). https://dailymemphian.com/article/7411/Dean-Kamens-iBot-saved-FedEx-years-of-RD-on-delivery-robot-inventor-says (headline only seen).
- FedEx's own framing (FedEx internal publication, Feb 2019 special edition, PDF not opened: https://www.fedex.com/content/dam/fedex/us-united-states/about-us/images/2022/FTC_2019_FEB_SpecEdition.pdf): FedEx contacted "a longtime friend, Dean Kamen" to apply proven technology to its idea.

**F51. Partnership structure: DEKA designed and built the device on its existing iBOT platform; FedEx was the sponsor/customer and ran tests. Contract terms, funding, IP ownership and exclusivity: NOT found.** [C]
- FedEx statement at shutdown hints at shared IP: "technologies we have developed together" (F32).

**F52. Who led it inside FedEx.** [A for names/titles; C for reporting lines]
- **Brian Philips**, president and CEO of FedEx Office (Plano, TX): US public lead 2019–2020; announced Texas tests (F14); quoted at 2020 showcase (F19).
- **Brie Carere**, EVP chief marketing and communications officer: fronted the launch (F5) and CES 2020 (F18).
- **Rebecca Yeung**, VP advanced technology and innovation, FedEx Corp. (later "operations science and advanced technology"): at the Manchester launch (F16); described in a TechCrunch event preview (seen via a scraped copy only) as "the lead officer for FedEx's same-day robot known as Roxo". She also fronted the Nuro (F61) and Dexterity (F65) deals.
- **FedEx Express regional presidents** fronted international activity: James R. Muhs (MEISA, Dubai 2019), Kawal Preet (AMEA, Japan 2021).
- **Sriram Krishnasamy**, chief transformation officer: ended it (F31).
- Organisational home: conceived as an extension of FedEx Office's SameDay City service (F35) with first tests between FedEx Office stores (F6, F14), alongside the corporate advanced-technology team. I found no source stating which unit held the budget or P&L.

**F53. Customer/user research and iterative piloting reported.** [B]
- Retailer input: six retailers "to help assess retailers' autonomous delivery needs" (F3); UAE Customer Advisory Board (F23). No findings published.
- Consumer emotion research: "FedEx seeks to understand consumer emotions", WARC, 2020-01-30. https://www.warc.com/newsandopinion/news/fedex-seeks-to-understand-consumer-emotions/en-gb/43169 — Carere at CES: FedEx has "started to measure emotion"; "How do you feel about Roxo going down the sidewalk when you're walking your dog or you're out with a stroller? Because most of us are not used to a robot walking by."
- Iteration: 2019 route tests with no goods (F14); Feb 2021 "most advanced" trials (F20); Richardson 2021: "Roxo will be adjusted based on the results from the test" (F21); community liaison with police, fire, HOA (F21).
- Sequence observation (mine): publicity-first launch (national TV, Feb 2019) preceded any field test (summer 2019) and any regulatory clearance (NYC, Nov 2019).

**F54. Internal champions or resistance.** [C]
- Champion: Fred Smith's personal sponsorship is reported (F50); he ceased to be CEO on 1 June 2022 (F40) and the project ended four months later under his successor's DRIVE programme. **The causal link is my inference; no source states it.**
- Resistance: no reporting found of internal opposition, union objection inside FedEx, or dissent. External opposition came from the Teamsters and pedestrian/accessibility advocates in state legislatures (F27).

---

## 5. External context

### 5.1 Comparable efforts

**F55. Amazon Scout — field tests began early 2019 (Snohomish County, WA; later Irvine CA, Atlanta GA, Franklin TN); Amazon ended field testing on 6 Oct 2022, the same day as FedEx's Roxo memo; about 400 staff to be reassigned.** [A]
- Source: "Amazon Abandons Home Delivery Robot Tests in Latest Cost Cuts", Bloomberg, 2022-10-06. https://www.bloomberg.com/news/articles/2022-10-06/amazon-abandons-autonomous-home-delivery-robot-in-latest-cut
- Source: "Amazon scraps Scout home delivery robot", FreightWaves, Oct 2022. https://www.freightwaves.com/news/amazon-scraps-scout-home-delivery-robot ; TechCrunch 2022-10-07 https://techcrunch.com/2022/10/07/amazon-scales-back-scout-delivery-robot-program/
- Quote (snippet): "During our Scout limited field test, we worked to create a unique delivery experience, but learned through feedback that there were aspects of the program that weren't meeting customers' needs."

**F56. Starship Technologies — the counter-example: 3 million commercial deliveries by Mar 2022, $100m raised in 30 days; but 11% layoffs and site closures in June 2022; 6 million deliveries and a further $90m by Feb 2024.** [A]
- Sources: TechCrunch 2022-03-01 https://techcrunch.com/2022/03/01/starship-technologies-raises-another-42m-to-fuel-the-growth-of-its-fleet-of-self-driving-delivery-robots ; The Robot Report, June 2022 https://www.therobotreport.com/delivery-robot-maker-starship-technologies-layoffs/ ; TechCrunch 2024-02-05 https://techcrunch.com/2024/02/05/starship-technologies-raises-90m-as-its-sidewalk-robots-pass-6m-deliveries
- Note: Starship's robots are small and light and work mostly on campuses — a different design point from a 450 lb Roxo.

**F57. Nuro (road-going delivery pods; FedEx's partner from 2021) — about 20% layoffs (about 300 people) Nov 2022; about 30% more in May 2023; paused commercial scale-up and delayed its R3 vehicle.** [A]
- Sources: IoT World Today https://www.iotworldtoday.com/transportation-logistics/self-driving-company-nuro-cuts-jobs-stalls-commercialization ; Food On Demand 2023-05-17 https://foodondemand.com/05172023/after-lofty-heights-nuro-again-lays-off-hundreds/

**F58. Kiwibot — Feb 2022: $7.5m pre-Series A and a $20m Sodexo campus deal (target 1,200 robots, 50 campuses by end-2022); semi-autonomous/teleoperated.** [A]
- Sources: The Robot Report https://www.therobotreport.com/kiwibot-brings-in-7-5-million-in-pre-series-a-funding/ ; FreightWaves https://www.freightwaves.com/news/kiwibot-announces-funding-teams-with-sodexho-to-take-delivery-bots-to-college

**F59. Serve Robotics — spun out of Uber/Postmates in early 2021; Uber Eats partnership in Los Angeles from 2022; deal for up to 2,000 robots (2023); reverse merger Aug 2023; Nasdaq listing Apr 2024 ($40m at $4/share).** [A; exact spin-out month n/c]
- Sources: Smart Cities Dive https://www.smartcitiesdive.com/news/serve-robotics-2000-robots-uber-eats/651723/ ; TechCrunch via Yahoo (Apr 2024) https://uk.news.yahoo.com/uber-nvidia-backed-serve-robotics-142601959.html

**F60. Pattern.** Survivors (Starship, Kiwibot, Serve) are small, light, food/campus-focused, venture-backed pure plays; the two programmes run inside large parcel/e-commerce incumbents (Roxo, Scout) were both cut in the same week of October 2022 during corporate cost reviews. [synthesis]

### 5.2 What FedEx pursued instead (and alongside)

**F61. Nuro — pilot began April 2021 in Houston; multi-year, multi-phase agreement announced 15 June 2021. FedEx said Roxo and Nuro "will serve different use cases".** [A]
- Sources: "FedEx and Nuro Team Up to Advance Last Mile Logistics with Autonomous Vehicles", Business Wire, 2021-06-15. https://www.businesswire.com/news/home/20210615005425/en/FedEx-and-Nuro-Team-Up-to-Advance-Last-Mile-Logistics-with-Autonomous-Vehicles ; TechCrunch 2021-06-15 https://techcrunch.com/2021/06/15/autonomous-delivery-startup-nuro-moves-into-logistics-with-fedex/amp/ ; Reuters via Investing.com https://www.investing.com/news/stock-market-news/fedex-to-test-package-deliveries-with-selfdriving-startup-nuro-2532594/
- Quotes (snippets): Yeung: "FedEx was built on innovation"; a "very serious, long-term commitment" (Reuters). Spokesperson: "Roxo and Nuro will serve different use cases given their differences in size, range and cargo capacity differences."

**F62. Aurora + PACCAR — autonomous linehaul trucks, Dallas–Houston, announced 22 Sept 2021.** [A]
- Source: FedEx Newsroom https://newsroom.fedex.com/newsroom/fedex-teams-up-with-aurora-and-paccar-to-test-autonomous-linehaul-technology/ ; TechCrunch 2021-09-22 https://techcrunch.com/2021/09/22/fedex-to-test-auroras-self-driving-trucks-on-dallas-to-houston-route/
- The Daily Memphian's Roxo obituary noted FedEx was continuing the Aurora pilot (F33).

**F63. Elroy Air — Chaparral autonomous VTOL cargo aircraft for middle-mile; agreement announced late March 2022 (sources dated 28–30 Mar); flight tests planned for 2023 (outcome not verified).** [A]
- Source: Aviation Today 2022-03-30 https://www.aviationtoday.com/2022/03/30/fedex-express-test-elroy-vtol-autonomous-middle-mile-cargo-delivery/ ; AIN https://ainonline.com/news-article/2022-03-28/fedex-test-autonomous-drone-cargo-delivery-elroy-air

**F64. Berkshire Grey — robotic sortation; expanded relationship announced 2 Aug 2022, with a warrant for FedEx vesting on up to $200m of purchases by end-2025; RPSi systems already in eight FedEx Ground facilities.** [A]
- Source: FedEx Newsroom https://newsroom.fedex.com/newsroom/global-english/berkshire-grey-and-fedex-expand-their-robotic-automation-solutions-relationship
- This matches the "robotic technology in its sorting facilities" named as the nearer-term priority (F33).

**F65. Dexterity AI — truck/trailer-loading robots (DexR), announced 26 Sept 2023; Yeung quoted.** [A]
- Source: Supply Chain Dive https://www.supplychaindive.com/news/fedex-testing-ai-powered-trailer-loading-robots-dexterity-ai/694837/ ; FreightWaves https://www.freightwaves.com/news/fedex-leverages-ai-to-improve-trailer-loading-process

**F66. Pattern.** After Roxo, FedEx's automation bets were (a) inside controlled facilities (sortation, trailer loading) and (b) middle-mile/linehaul, and all were partnerships with specialist firms rather than a FedEx-branded device. [synthesis]

---

## 6. Academic and practitioner sources

**Status for every item below: listing/abstract seen in search results only. No paper was opened.** I could not confirm that any of them discusses Roxo by name. No peer-reviewed article, teaching case or thesis analysing Roxo or FedEx's innovation management of it was found.

### 6.1 Peer-reviewed

- A1. Jennings, D., & Figliozzi, M. (2019). Study of sidewalk autonomous delivery robots and their potential impacts on freight efficiency and travel. *Transportation Research Record*, 2673(6), 317–326. https://doi.org/10.1177/0361198119849398 — economics/operations: cost and time savings in some scenarios, less on-road travel per parcel.
- A2. Jennings, D., & Figliozzi, M. (2020). Study of road autonomous delivery robots and their potential effects on freight efficiency and travel. *Transportation Research Record*, 2674(9). https://doi.org/10.1177/0361198120933633 (page range not confirmed).
- A3. Figliozzi, M. (2020). Carbon emissions reductions in last mile and grocery deliveries utilizing air and ground autonomous vehicles. *Transportation Research Part D*, 85, 102443. https://doi.org/10.1016/j.trd.2020.102443
- A4. Hoffmann, T., & Prause, G. (2018). On the regulatory framework for last-mile delivery robots. *Machines*, 6(3), 33. https://doi.org/10.3390/machines6030033 — regulation (traffic law, liability, data protection); Starship case; open access.
- A5. Pani, A., Mishra, S., Golias, M., & Figliozzi, M. (2020). Evaluating public acceptance of autonomous delivery robots during COVID-19 pandemic. *Transportation Research Part D*, 89, 102600. https://doi.org/10.1016/j.trd.2020.102600 — acceptance and willingness to pay; 483 consumers in Portland; co-authors at University of Memphis.
- A6. Kapser, S., & Abdelrahman, M. (2020). Acceptance of autonomous delivery vehicles for last-mile delivery in Germany – Extending UTAUT2 with risk perceptions. *Transportation Research Part C*, 111, 210–225. https://doi.org/10.1016/j.trc.2019.12.016 — technology-acceptance model; n = 501.
- A7. Lemardelé, C., Estrada, M., Pagès, L., & Bachofner, M. (2021). Potentialities of drones and ground autonomous delivery devices for last-mile logistics. *Transportation Research Part E*, 149, 102325. https://doi.org/10.1016/j.tre.2021.102325 — cost model: ground robots cheapest at high delivery density; truck-launched drones at low density (supports the "density" argument in F45).
- A8. Srinivas, S., Ramachandiran, S., & Rajendran, S. (2022). Autonomous robot-driven deliveries: A review of recent developments and future directions. *Transportation Research Part E*, 165, 102834. https://doi.org/10.1016/j.tre.2022.102834 — DOI: I supplied it and the search tool reported it as matching; confirm on ScienceDirect.
- A9. Engesser, V., Rombaut, E., Vanhaverbeke, L., & Lebeau, P. (2023). Autonomous delivery solutions for last-mile logistics operations: A literature review and research agenda. *Sustainability*, 15(3), 2774. https://doi.org/10.3390/su15032774 — open access.
- A10. Gehrke, S. R., Phair, C. D., Russo, B. J., & Smaglik, E. J. (2023). Observed sidewalk autonomous delivery robot interactions with pedestrians and bicyclists. *Transportation Research Interdisciplinary Perspectives*, 18, 100789. https://doi.org/10.1016/j.trip.2023.100789 — DOI from a single secondary source; confirm.
- A11. Alverhed, Hellgren, Isaksson, Olsson, Palmqvist, & Flodén (2024). Autonomous last-mile delivery robots: a literature review. *European Transport Research Review*, 16, article 4. https://doi.org/10.1186/s12544-023-00629-7 — open access; themes: operations, infrastructure, regulation, acceptance; notes most studies are theoretical and calls for real-world case studies. (Only surnames were returned by the search; authors' initials are NOT confirmed — take them from the article page before citing.)
- A12. Thomasen, K. (2020). Robots, regulation, and the changing nature of public space. *Ottawa Law Review*, 51(2). SSRN: https://papers.ssrn.com/abstract=3589896 ; journal PDF: https://rdo-olr.org/wp-content/uploads/2020/04/OLR-51-2-04-Thomasen-Robots-FINAL.pdf — no DOI found; page range not confirmed.

### 6.2 Reports and practitioner sources

- A13. Joerss, M., Schröder, J., Neuhaus, F., Klink, C., & Mann, F. (2016, September). *Parcel delivery: The future of last mile*. McKinsey & Company. Hosted PDF copy: https://www.bringg.com/wp-content/uploads/2016/10/Parcel_delivery_The_future_of_last_mile-1.pdf — source of the industry expectation that autonomous ground vehicles with lockers would dominate; last mile "often reaching or even exceeding 50 percent" of parcel cost.
- A14. Howell, A., Steckler, B., & Larco, N. (2022, September 6). *Piloting sidewalk delivery robots in Pittsburgh, Miami-Dade County, Detroit, and San Jose*. Urbanism Next Center, University of Oregon (Knight Foundation funded). https://scholarsbank.uoregon.edu/xmlui/handle/1794/28377 — about 3,000 trips, no reported pedestrian safety incidents; robots struggled with poor sidewalks; not ready to scale.
- A15. Wired (Aug 2020), "Amazon and FedEx Push to Put Delivery Robots on Your Sidewalk" — investigative journalism on lobbying (original URL not captured; reprint in F10).
- A16. Supply Chain Dive features (F27, F44) and "Will delivery robots take over sidewalks 10 years from now?" (expert roundtable). https://www.supplychaindive.com/news/expert-roundtable-sidewalk-delivery-robots/649805/
- A17. Emerj, "Artificial Intelligence at FedEx" (F39) — the only piece found that criticises FedEx's management/communication of Roxo directly.
- A18. FedEx Roxo one-pager, Jan 2021 (F13) and FedEx Maryland testimony (F28) — primary documents.

### 6.3 Checked and not confirmed
- Figliozzi & Jennings, "Autonomous delivery robots and their potential impacts on urban freight energy consumption and emissions", *Transportation Research Procedia* 46 (2020): the search could not confirm this citation or a DOI. Only a 2019 City Logistics conference slide deck with a similar title was found. Do not cite without checking.

---

## 7. Could not verify (explicit list)

1. Any page content first-hand — WebFetch blocked for all hosts tried (see top).
2. Exact date and manner the name "Roxo" was announced (earliest dated use found: Manchester launch, 6 Aug 2019).
3. Exact publication date of the Robotics 24/7 scoop (reported as 7 Oct 2022 by search summaries) and of The Verge article (mid-Oct 2022; original URL not captured).
4. Full text of the Krishnasamy memo beyond the one sentence quoted.
5. Whether Roxo ever made a paid commercial delivery (no evidence that it did; cannot prove the negative).
6. Number of robots built, deliveries, miles, staffing, and programme cost.
7. Contract, funding and IP terms between FedEx and DEKA; any DEKA or Kamen statement after cancellation.
8. Which FedEx unit owned the budget; any internal resistance.
9. Roxo's weight (450 lb per FedEx page vs 200 lb per Wired) — not checked on the pages.
10. Nature of the July 2021 Japan activity (appearance vs trial vs indoor test).
11. Whether the second 2021 Richardson test took place; any US activity in 2022.
12. Dates of Manchester and Memphis municipal approvals; what the Nov 2019 NYC "special event" was.
13. Whether NH HB 116 as enacted permits a 450 lb device; FedEx's role in the Texas and Tennessee PDD bills.
14. Whether FedEx mentioned Roxo in earnings calls or 10-Ks (one search found nothing; Emerj says annual reports featured it).
15. Whether any academic paper in section 6 discusses Roxo; authors' initials for A11; DOIs for A8 and A10; page ranges for A2 and A12.
16. Outcomes of the Nuro and Elroy Air programmes.
17. Dates marked "n/c" throughout.
