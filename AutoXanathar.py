import numpy as np
import PyInstaller

parents = ['You know who your parents are or were.',
           'You do not know who your parents were.']
nonhuman_parents = [{'Half-Elf': ['One parent was an elf and the other was a human.',
                                  'One parent was an elf and the other was a half-elf.',
                                  'One parent was a human and the other was a half-elf,',
                                  'Both parents were half-elves.']},
                    {'Half-Orc': ['One parent was an orc and the other was a human.',
                                  'One parent was an orc and the other was a half-orc.',
                                  'One parent was a human and the other was a half-orc.',
                                  'Both parents were half-orcs.']},
                    {'Tiefling': ['Both parents were humans, their infernal heritage dormant until you came along.',
                                  'One parent was a tiefling and the other was a human.',
                                  'One parent as a tiefling and the other was a devil.',
                                  'One parent was a human and the other was a devil.']}]
birthplace = ['Home', 'Home of a family friend', 'Home of a healer or midwife', 'Carriage, cart or wagon',
              'Barn, shed, or other outbuilding', 'Cave', 'Field', 'Forest', 'Temple', 'Battlefield', 'Alley or street',
              'Brothel, tavern or inn', 'Castle, keep, tower, or palace', 'Sewer or rubbish heap',
              'Among people of a different race', 'On board a boat or a ship',
              'In a prison or in the headquarters of a secret organization', 'In a sage\'s laboratory',
              'In the Feywild', 'In the Shadowfell', 'On the Astral Plane or the Ethereal Plane',
              'On an Inner Plane of your choice', 'On an Outer Plane of your choice']
no_siblings = ['None', str(np.random.randint(low=1, high=3, size=1)[0]),
               str(np.random.randint(low=1, high=4, size=1)[0] + 1),
               str(np.random.randint(low=1, high=6, size=1)[0] + 2),
               str(np.random.randint(low=1, high=8, size=1)[0] + 3)]
birth_order = ['Twin, triplet or quadruplet', 'Older', 'Younger']
family = ['None', 'Institution, such as an asylum', 'Temple', 'Orphanage', 'Guardian',
          'Paternal or maternal aunt, uncle, or both; or extended family such as a tribe or clan',
          'Paternal or maternal grandparent(s)', 'Adoptive family (same or different race',
          'Single father or stepfather', 'Single mother or stepmother', 'Mother and Father']
absent_parent = ['Your parent died', 'Your parent was imprisoned, enslaved, or otherwise taken away.',  # Parent died: Randomized addition
                 'Your parent abandoned you.', 'Your parent disappeared to an unknown fate.']
family_lifestyle = {'Wretched': -40, 'Squalid': -20, 'Poor': -10, 'Modest': 0, 'Comfortable': 10, 'Wealthy': 20,
                    'Aristocratic': 40}
childhood_home = ['On the streets', 'Rundown Shack', 'No permanent residence; you moved around a lot',
                  'Encampment or village in the wilderness', 'Apartment in a rundown neighborhood', 'Small house',
                  'Large house', 'Mansion', 'Palace or castle']
childhood_memories = ['I am still haunted by my childhood, when I was treated badly by my peers.',
                      'I spent most of my childhood alone, with no close friends.',
                      'Others saw me as being different or strange, and so I had few companions.',
                      'I had a few close friends and lived an ordinary childhood',
                      'I had several friends, and my childhood was generally a happy one.',
                      'I always found it easy to make friends, and I loved being around people.',
                      'Everyone knew who I was, and I had friends everywhere I went.']
background = {'Acolyte': ['I ran away from home at an early age and found refuge in a temple.',
                          'My family gave me to a temple, since they were unable or unwilling to care for me.',
                          'I grew up in a household with strong religious convictions. '
                          'Entering the service of one or more gods seemed natural.',
                          'An impassioned sermon struck a chord deep in my soul and moved me to serve the faith.',
                          'I followed a childhood friend, a respected acquaintance, '
                          'or someone I loved into religious service.',
                          'After encountering a true servant of the gods, '
                          'I was so inspired that I immediately entered the service of a religious group.'],
              'Charlatan': ['I was left to my own devices, and my knack for manipulating others helped me survive.',
                            'I learned early on that people are gullible and easy to exploit.',
                            'I often got in trouble, but I managed to talk my way out of it every time.',
                            'I took up with a confidence artist, from whom I learned my craft',
                            'After a charlatan fleeced my family, I decided to learn the trade so I '
                            'would never be fooled by such deception again.',
                            'I was poor or I feared becoming poor, so I learned the tricks I needed '
                            'to keep myself out of poverty.'],
              'Criminal': ['I resented authority in my younger days and saw a life of crime '
                           'as the best way to fight against tyranny and oppression.',
                           'Necessity forced me to take up the life, since it was the only way I could survive.',
                           'I fell in with a gang of reprobates and ne’er-do-wells, and I learned '
                           'my specialty from them.',
                           'A parent/relative taught me my criminal specialty to prepare me for the family business.',
                           'I left home and found a place in a thieves’ guild or some other criminal organization.',
                           'I was always bored, so I turned to crime to pass the time and discovered '
                           'I was quite good at it.'],
              'Entertainer': ['Members of my family made ends meet by performing, '
                              'so it was fitting for me to follow their example.',
                              'I always had a keen insight into other people, enough so that I could make them '
                              'laugh or cry with my stories or songs.',
                              'I ran away from home to follow a minstrel troupe.',
                              'I saw a bard perform once, and I knew from that moment on what I was bor to do.',
                              'I earned coin by performing on street corners and eventually made a name for myself.',
                              'A traveling entertainer took me in and taught me the trade.'],
              'Folk Hero': ['I learned what was right and wrong from my family.',
                            'I was always enamored by tales of heroes and wished '
                            'I could be something more than ordinary.',
                            'I hated my mundane life, so when it was time for someone to step up and do '
                            'the right thing, I took my chance.',
                            'A parent or one of my relatives was an adventurer, and I was inspired '
                            'by that person’s courage.',
                            'A mad old hermit spoke a prophecy when I was born, '
                            'saying that I would accomplish great things.',
                            'I have always stood up for those who are weaker than I am.'],
              'Guild Artisan': ['I was apprenticed to a master who taught me the guild’s business.',
                                'I helped a guild artisan keep a secret or complete a task, '
                                'and in return I was taken on as an apprentice.',
                                'One of my family members who belonged to the guild made a place for me.',
                                'I was always good with my hands, so I took the opportunity to learn a trade.',
                                'I wanted to get away from my home situation and start a new life.',
                                'I learned the essentials of my craft from a mentor but had to join the guild '
                                'to finish my training.'],
              'Hermit': ['My enemies ruined my reputation, and I fled to the wilds to avoid further disparagement.',
                         'I am comfortable with being isolated, as I seek inner peace.',
                         'I never liked the people I called my friends, so it was easy for me to strike out on my own.',
                         'I felt compelled to forsake my past, but did so with great reluctance, '
                         'and sometimes I regret making that decision.',
                         'I lost everything — my home, my family, my friends. Going it alone was all I could do.',
                         'Society\'s decadence disgusted me, so I decided to leave it behind.'],
              'Noble': ['I come from an old and storied family, and it fell to me to preserve the family name.',
                        'My family has been disgraced, and I intend to clear our name.',
                        'My family recently came by its title, and that elevation thrust us into '
                        'a new and strange world.',
                        'My family has a title, but none of my ancestors have distinguished themselves '
                        'since we gained it.',
                        'My family is filled with remarkable people. I hope to live up to their example.',
                        'I hope to increase my family’s power and influence.'],
              'Outlander': ['I spent a lot of time in the wilderness as a youngster, '
                            'and I came to love that way of life.',
                            'From a young age, I couldn\'t abide the stink of the cities '
                            'and preferred to spend my time in nature.',
                            'I came to understand the darkness that lurks in the wilds, and I vowed to combat it.',
                            'My people lived on the edges of civilization, '
                            'and I learned the methods of survival from my family.',
                            'After a tragedy I retreated to the wilderness, leaving my old life behind.',
                            'My family moved away from civilization, and I learned to adapt to my new environment.'],
              'Sage': ['I was naturally curious, so I packed up and went to a university '
                       'to learn more about the world.',
                       'My mentor\'s teachings opened my mind to new possibilities in that field of study.',
                       'I was always an avid reader, and I learned much I about my favorite topic on my own.',
                       'I discovered an old library and pored over the texts I found there. '
                       'That experience awakened a hunger for more knowledge.',
                       'I impressed a wizard who told me I was squandering my talents '
                       'and should seek out an education to take advantage of my gifts.',
                       'One of my parents or a relative gave me a basic education that whetted my appetite, '
                       'and I left home to build on what I had learned.'],
              'Sailor': ['I was press-ganged by pirates and forced to serve on their ship until I finally escaped.',
                         'I wanted to see the world, so I signed on as a deckhand for a merchant ship.',
                         'One of my relatives was a sailor who took me to the sea.',
                         'I needed to escape my community quickly, so I stowed away on a ship. '
                         'When the crew found me, I was forced to work for my passage',
                         'Reavers attacked my community, so I found refuge on a ship until I could seek vengeance.',
                         'I had few prospects where l was living, so I left to find my fortune elsewhere.'],
              'Soldier': ['I joined the militia to help protect my community from monsters.',
                          'A relative of mine was a soldier, and I wanted to carry on the family tradition.',
                          'The local lord forced me to enlist in the army.',
                          'War ravaged my homeland while I was growing up. Fighting was the only life I ever knew.',
                          'I wanted fame and fortune, so I joined a mercenary company, '
                          'selling my sword to the highest bidder.',
                          'Invaders attacked my homeland. It was my duty to take up arms in defense of my people.'],
              'Urchin': ['Wanderlust caused me to leave my family to see the world. I look after myself.',
                         'I ran away from a bad situation at home and made my own way in the world.',
                         'Monsters wiped out my village, and I was the sole survivor. I had to find a way to survive.',
                         'A notorious thief looked after me and other orphans, '
                         'and we spied and stole to earn our keep.',
                         'One day I woke up on the streets, alone and hungry, with no memory of my early childhood.',
                         'My parents died, leaving no one to look after me. I raised myself.']}
classes = {'Barbarian': ['My devotion to my people lifted me in battle, making me powerful and dangerous.',
                         'The spirits of my ancestors called on me to carry out a great task.',
                         'I lost control in battle one day, and it was as if something else was manipulating my body,'
                         ' forcing it to kill every foe I could reach.',
                         'went on a spiritual journey to find myself and instead found a spirit animal to guide, '
                         'protect, and inspire me.',
                         'I was struck by lightning and lived. Afterward, I found a new strength within me '
                         'that let me push beyond my limitations.',
                         'My anger needed to be channeled into battle, or I risked becoming an indiscriminate killer.'],
           'Bard': ['I awakened my latent bardic abilities through trial and error.',
                    'I was a gifted performer and attracted the attention of a master bard who schooled me '
                    'in the old techniques.',
                    'I joined a loose society of scholars and orators to learn new techniques '
                    'of performance and magic.',
                    'I felt a calling to recount the deeds of champions and heroes, '
                    'to bring them alive in song and story.',
                    'I joined one of the great colleges to learn old lore, the secrets of magic, '
                    'and the art of performance.',
                    'I picked up a musical instrument one day and instantly discovered that I could play it.'],
           'Cleric': ['A supernatural being in service to the gods called me to become a divine agent in the world.',
                      'I saw the injustice and horror in the world and felt moved to take a stand against them.',
                      'My god gave me an unmistakable sign. I dropped everything to serve the divine.',
                      'Although I was always devout, it wasn\'t until I completed a pilgrimage '
                      'that I knew my true calling.',
                      'I used to serve in my religion\'s bureaucracy but found I needed to work in the world, '
                      'to bring the message of my faith to the darkest corners of the land.',
                      'I realize that my god works through me, and I do as commanded, even though I don\'t know why '
                      'I was chosen to serve.'],
           'Druid': ['I saw too much devastation in the wild places, too much of nature\'s splendor ruined '
                     'by the despoilers. I joined a circle of druids to fight back against the enemies of nature.',
                     'I found a place among a group of druids after I fled a catastrophe.',
                     'I have always had an affinity for animals, so I explored my talent to see '
                     'how I could best use it.',
                     'I befriended a druid and was moved by druidic teachings. I decided to follow my friend\'s '
                     'guidance and give something back to the world.',
                     'Whiie I was growing up, I saw spirits all around me — entities no one else could perceive. '
                     'I sought out the druids to help me understand the visions and communicate with these beings.',
                     'I have always felt disgust for creatures of unnatural origin. For this reason, '
                     'I immersed myself in the study of the druidic mysteries and became a champion '
                     'of the natural order.'],
           'Fighter': ['I wanted to hone my combat skills, and so I joined a war college.',
                       'I squired for a knight who taught me how to fight, care for a steed, '
                       'and conduct myself with honor. I decided to take up that path for myself.',
                       'Horrible monsters descended on my community, killing someone I loved. '
                       'I took up arms to destroy those creatures and others ofa similar nature',
                       'I joined the army and learned how to fight as part of a group.',
                       'I grew up fighting, and I refined my talents by defending myself '
                       'against people who crossed me.',
                       'I could always pick up just about any weapon and know how to use it effectively.'],
           'Monk': ['I was chosen to study at a secluded monastery. There, '
                    'I was taught the fundamental techniques required to eventually master a tradition.',
                    'I sought instruction to gain a deeper understanding of existence and my place in the world.',
                    'I stumbled into a portal to the Shadowfell and took refuge in a strange monastery, '
                    'where I learned how to defend myself against the forces of darkness.',
                    'I was overwhelmed with grief after losing someone close to me, '
                    'and I sought the advice of philosophers to help me cope with my loss.',
                    'I could feel that a special sort of power lay within me, '
                    'so I sought out those who could help me call it forth and master it.',
                    'I was wild and undisciplined as a youngster, but then I realized the error of my ways. '
                    'I applied to a monastery and became a monk as a way to live a life of discipline.'],
           'Paladin': ['A fantastical being appeared before me and called on me to undertake a holy quest.',
                       'One of my ancestors left a holy quest unfulfilled, so I intend to finish that work.',
                       'The world is a dark and terrible place. I decided to serve as a beacon of light '
                       'shining out against the gathering shadows.',
                       'I served as a paladin’s squire, learning all I needed to swear my own sacred oath.',
                       'Evil must be opposed on all fronts. I feel compelled to seek out wickedness '
                       'and purge it from the world.',
                       'Becoming a paladin was a natural consequence of my unwavering faith. In taking my vows, '
                       'I became the holy sword of my religion.'],
           'Ranger': ['I found purpose while I honed my hunting skills by bringing down dangerous animals '
                      'at the edge of civilization.',
                      'I always had a way with animals, able to calm them with a soothing word and a touch.',
                      'I suffer from terrible wanderlust, so being a ranger gave me a reason '
                      'not to remain in one place for too long.',
                      'I have seen what happens when the monsters come out from the dark. '
                      'I took it upon myself to become the first line of defense against the evils '
                      'that lie beyond civilization\'s borders.',
                      'I met a grizzled ranger who taught me woodcraft and the secrets of the wild lands.',
                      'I served in an army, learning the precepts of my profession while blazing trails '
                      'and scouting enemy encampments.'],
           'Rogue': ['I\'ve always been nimble and quick of wit, so I decided to use those talents '
                     'to help me make my way in the world.',
                     'An assassin or a thief wronged me, so I focused my training on mastering the skills '
                     'of my enemy to better combat foes of that sort.',
                     'An experienced rogue saw something in me and taught me several useful tricks.',
                     'I decided to turn my natural lucky streak into the basis of a career, '
                     'though I still realize that improving my skills is essential.',
                     'I took up with a group of ruffians who showed me how to get what I want through '
                     'sneakiness rather than direct confrontation.',
                     'I\'m a sucker for a shiny bauble or a sack of coins, '
                     'as long as I can get my hands on it without risking life and limb.'],
           'Sorcerer': ['When I was born, all the water in the house froze solid, the milk spoiled, '
                        'or all the iron turned to copper. My family is convinced that this event '
                        'was a harbinger of stranger things to come for me.',
                        'I suffered a terrible emotional or physical strain, which brought forth '
                        'my latent magical power. I have fought to control it ever since.',
                        'My immediate family never spoke of my ancestors, and when I asked, '
                        'they would change the subject. It wasn\'t until I started displaying '
                        'strange talents that the full truth of my heritage came out.',
                        'When a monster threatened one of my friends, I became filled with anxiety. '
                        'I lashed out instinctively and blasted the wretched thing '
                        'with a force that came from within me.',
                        'Sensing something special in me, a stranger taught me how to control my gift.',
                        'After I escaped from a magical conflagration, I realized that though I was unharmed, '
                        'I was not unchanged. I began to exhibit unusual abilities that '
                        'I am just beginning to understand.'],
           'Warlock': ['While wandering around in a forbidden place, I encountered an otherworldly being '
                       'that offered to enter into a pact with me.',
                       'I was examining a strange tome I found in an abandoned library when the entity '
                       'that would become my patron suddenly appeared before me.',
                       'I stumbled into the clutches of my patron after I accidentally '
                       'stepped through a magical doorway.',
                       'When I was faced with a terrible crisis, I prayed to any being who would listen, '
                       'and the creature that answered became my patron.',
                       'My future patron visited me in my dreams and offered great power in exchange for my service.',
                       'One of my ancestors had a pact with my patron, so that entity was determined to bind me '
                       'to the same agreement.'],
           'Wizard': ['An old wizard chose me from among several candidates to serve an apprenticeship.',
                      'When I became lost in a forest, a hedge wizard found me, took me in, '
                      'and taught me the rudiments of magic.',
                      'I grew up listening to tales of great wizards and knew I wanted to follow their path. '
                      'I strove to be accepted at an academy of magic and succeeded.',
                      'One of my relatives was an accomplished wizard who decided I '
                      'was smart enough to learn the craft.',
                      'While exploring an old tomb, library, or temple, I found a spellbook. '
                      'I was immediately driven to learn all I could about becoming a wizard.',
                      'I was a prodigy who demonstrated mastery of the arcane arts at an early age. '
                      'When I became old enough to set out on my own, I did so to learn more magic '
                      'and expand my power.']}
life_events_by_age = {'20 years or younger': 1, '21-30 years': str(np.random.randint(low=1, high=4, size=1)[0]),
                      '31-40 years': str(np.random.randint(low=1, high=6, size=1)[0]),
                      '41-50 years': str(np.random.randint(low=1, high=8, size=1)[0]),
                      '51-60 years': str(np.random.randint(low=1, high=10, size=1)[0]),
                      '61 years or older': str(np.random.randint(low=1, high=12, size=1)[0])}
life_events = ['You suffered a tragedy.', 'You gained a bit of good fortune.',
               'You fell in love or got married. If you get this result more than once, '
               'you can choose to have a child instead. Work with your DM to '
               'determine the identity of your love interest.',
               'You made an enemy of an adventurer. Roll a d6. An odd number indicates you are to blame for the rift,'
               'and an even number indicates you are blameless. Use the supplemental tables and work with your'
               'DM to determine this hostile character\'s identity and the danger this enemy poses to you.',
               'You made a friend oan adventurer. Use the supplemental tables and work with your DM to add '
               'more detail to this friendly character and establish how your friendship began.',
               'You spent time working in a job related to your background. Start the game with an extra 2d6 gp.',
               'You met someone important. Use the supplemental tables to determine this character\'s identity and '
               'how this individual feels about you. Work out additional details with your DM as needed to fit this '
               'character into your backstory.',
               'You went on an adventure.',
               'You had a supernatural experience.',
               'You fought in a battle.',
               'You committed a crime or were wrongly accused of doing so.',
               'You encountered something magical.',
               'Something truly strange happened to you.']  # Most have randomized additions
adventures = ['You nearly died. You have nasty scars on your body, and you are missing an ear, ' + 
             str(np.random.randint(low=1, high=3, size=1)[0]) + ' fingers, or' + 
             str(np.random.randint(low=1, high=4, size=1)[0] + ' toes.',
             'You suffered a grievous injury. Although the wound healed, it still pains you from time to time.',
             'You were wounded, but in time you fully recovered.',
             'You contracted a disease while exploring a filthy warren. You recovered from the disease, '
             'but you have a persistent cough, pockmarks on your skuin, or prematurely gray hair.',
             'You were poisoned by a trap or monster. You recovered, but the next time yo must make '
             'a saving throw against poison, you make the saving throw with disadvantage.',
             'You lost something of sentimental value to you during your adventure. Remove one trinket '
             'from your possessions.',
             'You were terribly frightened by something you encountered and ran away, abandoning your '
             'companions to their fate.',
             'You learned a great deal during your adventure. The next time you make an ability check or '
             'a saving throw, you have advantage on the roll.',
             'You found some treasure on your adventure. You have ' + 
             str(np.random.randint(low=2, high=12, size=1)[0]) + ' gp from your share of it.',
             'You found a considerable amount of treasure on your adventure. You have ' + 
             str(np.random.randint(low=1, high=20, size=1)[0] + 50) + ' gp left from your share of it.',
             'You came across a common magic item (of the DM\'s choice).']
arcane_matters = ['You were charmed or frightened by a spell.',
                 'You were injured by the effect of a spell.',
                 'You witnessed a powerful spell being cast by ',  # Randomized addition
                 'You drank a potion (of the DM\'s choice.',
                 'You found a spell scroll (of the DM\'s choice) and succeeded in casting the spell it contained.,
                 'You were affected by teleportation magic.', 
                 'You turned invisible for a time.',
                 'You identified an illusion for what it was.',
                 'You saw a creature being conjured by magic.',
                 'Your fortune was read by a diviner. ']  # Randomized addition
boons = ['A friendly wizard gave you a spell scroll containing a cantrip (of the DM\'s choice).',
        'You saved a commoner, who now owes you a life debt. The individual accompanies you on your travels'
        ' and performs mundane tasks for you, but will leave if neglected, abused, or imperiled. Determine '
        'details about this character working with the DM.',  # Randomized addition
        'You found a riding horse.',
        'You found some money. You have ' + str(np.random.randint(low=1, high=20. size=1)[0]) + ' gp in addition'
        ' to yor regular starting funds.',
        'A relative bequeathed you a simple weapon of your choice.',
        'You found something interesting. You gain one additional trinket.',
        'You once performed a service for a local temple. The next time you visit the temple, you can receive'
        ' healing up to your hit point maximum.',
        'A friendly alchemist gifted you with a potion of healing or a flask of acid, as you choose.',
        'You found a treasure map.',
        'A distant relative left you a stipend that enables you to live at the comfortable lifestyle for ' + 
        str(np.random.randint(low=1, high=20, size=1)[0]) + ' years. If you choose to live at a higher lifestyle,'
        ' you reduce the price of the lifestyle by 2 gp during that time period.']
crime = ['Murder', 'Theft', 'Burglary', 'Assault', 'Smuggling', 'Kidnapping', 'Extortion', 'Counterfeiting']
punishment = ['You did not commit the crime and were exonerated after being accused.', 
             'You committed the crime or helped to do so, but nonetheless the authorities found you not guilty.',
             'You were nearly caught in the act. You had to flee and are wanted on the community where the crime'
             'occurred.',
             'You were caught and convicted.']  # Randomized addition
supernatural_event = ['You were ensorcelled by a fey and enslaved for ' + 
                      str(np.random.randint(low=1, high=6, size=1)[0]) + ' years before you escaped.',
                     'You saw a demon and ran away before it could do anything to you.',
                     'A devil tempted you.',  #Randomized addition
                     'You woke up one morning miles from your home, with no idea how you got there.',
                     'You visited a holy site and felt the presence of the divine there.',
                     'You witnessed a falling red star, a face appearing in the frost, or some other bizarre'
                     ' happening. You are certain it was an omen of some sort.',
                     'You escaped certain death and believe it was the intervention of a god that saved you.',
                     'You witnessed a minor miracle.',
                     'You explored an empty house and found it to be haunted.',
                     'You were briefly possessed.',  # Randomized addition
                     'You saw a ghost.',
                     'You saw a ghoul feeding on a corpse.',
                     'A celestial or fiend visited you in your dreams to give a warning of dangers to come.',
                     'You briefly visited the Feywild or the Shadowfell.',
                     'You saw a portal that you believe leads to another plane of existence.']
tragedies = ['A family member or a close friend died.',  # Randomized addition
            'A friendship ended bitterly, and the other person is now hostile to you. The cause might have '
            'been a misunderstanding or something you or the former friend did.',
            'You lost all possessions in a disaster, and you had to rebuild your life.',
            'You were imprisoned for a crime you didn\'t commit and spent ' + 
            str(np.random.randint(low=1, high=6, size=1)[0] + ' years at hard labor, in jail, or shackled '
            'to an oar in a slave galley.',
            'War ravaged your home community, reducing everything to rubble and ruin. In the aftermath, '
            'you either helped your town rebuild or moved somewhere else.',
            'A lover disappeared without a trace. You have been lookiung for that person ever since.',
            'A terrible blight in your home community caused crops to fail, and many starved. You lost a sibling'
            ' or some other family member.',
            'You did something that brought terrible shame to you in the eyes of your family. '
            'You might have been involved in a scandal, dabbled in dark magic, or offended someone important. '
            'The attitude of your family members toward you becomes indifferent at best, '
            'though they might eventually forgive you.',
            'A romantic relationship ended.',  # Randomized addition
            'A current or prospective romantic partner of yours died.']  # Randomized addition
war = ['You were knocked out and left for dead. You woke up hours later with no recollection of the battle.',
      'You were badly injured in the fight, and you still bear the awful scars of those wounds.',
      'You ran away from the battle to save your life, but you still feel shame for your cowardice.',
      'You suffered only minor injuries, an the wounds all healed without leaving scars.',
      'You survived the battle, but you suffer from terrible nightmares in which you relive the experience.',
      'You escaped the battle unscathed, though many of your friends were injured or lost.',
      'You acquitted yourself well in battle and are as a hero. You might have received a medal for your bravery.']
weird_stuff = ['You were turned into a toad and remained in that form for ' + 
               str(np.random.randint(low=1, high=4, size=1)[0]) + ' weeks.',
              'You were petrified and remained a stone statue for a time until someone freed you.',
              'You were enslaved by a hag, a satyr, or some other being and lived in that creature\'s thrall for ' +
              str(np.random.randint(low=1, high=6, size=1)[0]) + ' years.',
              'A dragon held you as a prisoner for ' + str(np.random.randint(low=1, high=4, size=1)[0]) + ' months '
              'until adventurers killed it.',
              'You were taken captive by a race of evil humanoids such as drow, kuo-toa, or quaggoths. You lived '
              'as a slave in the Underdark until you escaped.',
              'You served a powerful adventurer as a hireling. You have only recently left that service. '
              'Use the supplemental tables and work with your DM to determine the basic details '
              'about your former employer.', 
              'You went insane for ' + str(np.random.randint(low=1, high=6, size=1)[0]) + ' years and recently'
              ' regained your sanity. A tic or some other bit of odd behavior might linger.',
              'A lover of yours was secretly a silver dragon.',
              'You were captured by a cult and nearly sacrificed on an altar to the foul being the cultists served.'
              ' You escaped, but you fear they will find you.',
              'You met a demigod, an archdevil, an archfey, a demon lord, or a titan, and you lived to tell the tale.',
              'You were swallowed by a giant fish and spent a month in its gullet before you escaped.',
              'A powerful being granted you a wish, but you squandered it on something frivolous.']
aligment = ['Chaotic Evil', 'Chaotic Neutral', 'Lawful Evil', 'Neutral Evil', 'Neutral', 'Neutral Good', 
           'Lawful Good', 'Lawful Neutral', 'Chaotic Good', 'Chaotic Neutral']
cause_of_death = ['Unknown', 'Murdered', 'Killed in Battle', 'Accident related to class or occupation', 
                 'Accident unrelated to class or occupation', 'Natural causes, such as disease or old age',
                 'Apparent suicide', 'Torn apart by an animal or a natural disaster',
                 'Consumed by a monster', 'Executed for a crime or tortured to death',
                 'Bizarre event, such as being hit by a meteorite, struck down by an angry god, '
                  'or killed by a hatchling slaad egg']
klass = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 
        'Warlock', 'Wizard']
occupation = ['Academic', 'Adventurer',  # Randomized addition/replacement
             'Aristocrat', 'Artisan or guild member', 'Criminal', 'Entertainer', 'Exile, hermit, or refugee',
             'Explorer or wanderer', 'Farmer or herder', 'Hunter or trapper', 'Laborer', 'Merchant',
             'Politician or bureaucrat', 'Priest', 'Sailor', 'Soldier']
race = ['Human', 'Dwarf', 'Elf', 'Halfling', 'Dragonborn', 'Gnome', 'Half-elf', 'Half-orc', 'Tiefling', 'DM\'s choice']
relationship = ['Hostile', 'Friendly', 'Indifferent']
status = ['Dead',  # Randomized addition
         'Mising or unknown', 'Alive, but doing poorly due to injury, financial trouble, or relationship difficulties',
         'Alive and well', 'Alive and quite successful', 'Alive and infamous', 'Alive and famous']
