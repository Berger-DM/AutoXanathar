from Functions import *
import random

'''FUNCTIONS'''


def alignment_table(d):
    roll = int(roll_3d6())
    for i in d.keys():
        if roll in i:
            if isinstance(d[i], tuple):
                choice_list = list(d[i])
                return random.choice(choice_list)
            else:
                return d[i]


def cause_of_death_table(d):
    roll = int(roll_a_d12())
    return d[roll - 1]


def class_table(d):
    roll = int(roll_a_d100())
    for i in d.keys():
        if roll in i:
            return d[i]


def tragedies_table(d):
    roll = int(roll_a_d12())
    for i in d.keys():
        if roll in i:
            if isinstance(d[i], tuple):
                ret_str = d[i][0]
                sec_str = cause_of_death_table(cause_of_death)
                return " Cause: ".join([ret_str, sec_str])


def boons_table(d):
    roll = int(roll_a_d10())
    return d[roll - 1]


def enemy_adventurer():
    blame_roll = int(roll_a_d6())
    if blame_roll % 2 == 0:
        blame_str = 'You are blameless for the rift.'
    else:
        blame_str = 'You are to blame for the rift.'
    class_str = class_table(klass)
    align_str = alignment_table(aligment)
    return blame_str + " He/She is a " + align_str + ' ' + class_str + "."


def adventures_table(d):
    roll = int(roll_a_d100())
    for i in d:
        if roll in i:
            return d[i]


def supernatural_events_table(d):
    roll = int(roll_a_d100())
    for i in d.keys():
        if roll in i:
            return d[i]


def war_table(d):
    roll = int(roll_a_d12())
    for i in d.keys():
        if roll in i:
            return d[i]


def crime_table(d):
    roll = int(roll_a_d8())
    return d[roll - 1]


def punishment_table(d):
    roll = int(roll_a_d12())
    for i in d.keys():
        if roll in i:
            return d[i]


def arcane_matters_table(d):
    roll = int(roll_a_d10())
    return d[roll - 1]


def weird_stuff_table(d):
    roll = int(roll_a_d12())
    return d[roll - 1]


'''SUPPLEMENTAL TABLES'''

aligment = {frozenset([3]): ('Chaotic Evil', 'Chaotic Neutral'),
            frozenset(range(4, 6)): 'Lawful Evil',
            frozenset(range(6, 9)): 'Neutral Evil',
            frozenset(range(9, 13)): 'Neutral',
            frozenset(range(13, 16)): 'Neutral Good',
            frozenset(range(16, 18)): ('Lawful Good', 'Lawful Neutral'),
            frozenset([18]): ('Chaotic Good', 'Chaotic Neutral')}
cause_of_death = ['Unknown', 'Murdered', 'Killed in Battle', 'Accident related to class or occupation',
                  'Accident unrelated to class or occupation', 'Natural causes, such as disease or old age',
                  'Natural causes, such as disease or old age', 'Apparent suicide',
                  'Torn apart by an animal or a natural disaster', 'Consumed by a monster',
                  'Executed for a crime or tortured to death',
                  'Bizarre event, such as being hit by a meteorite, struck down by an angry god, or '
                  'killed by a hatchling slaad egg']
klass = {frozenset(range(1, 8)): 'Barbarian',
         frozenset(range(8, 15)): 'Bard',
         frozenset(range(15, 30)): 'Cleric',
         frozenset(range(30, 37)): 'Druid',
         frozenset(range(37, 53)): 'Fighter',
         frozenset(range(53, 59)): 'Monk',
         frozenset(range(59, 65)): 'Paladin',
         frozenset(range(65, 71)): 'Ranger',
         frozenset(range(71, 85)): 'Rogue',
         frozenset(range(85, 90)): 'Sorcerer',
         frozenset(range(90, 95)): 'Warlock',
         frozenset(range(95, 101)): 'Wizard'}
occupation = {frozenset(range(1, 6)): 'Academic',
              frozenset(range(6, 11)): ('Adventurer', class_table(klass)),
              frozenset([11]): 'Aristocrat',
              frozenset(range(12, 27)): 'Artisan or guild member',
              frozenset(range(27, 32)): 'Criminal',
              frozenset(range(32, 37)): 'Entertainer',
              frozenset(range(37, 39)): 'Exile, hermit, or refugee',
              frozenset(range(39, 44)): 'Explorer or wanderer',
              frozenset(range(44, 56)): 'Farmer or herder',
              frozenset(range(56, 61)): 'Hunter or trapper',
              frozenset(range(61, 76)): 'Laborer',
              frozenset(range(76, 81)): 'Merchant',
              frozenset(range(81, 86)): 'Politician or bureaucrat',
              frozenset(range(86, 91)): 'Priest',
              frozenset(range(91, 96)): 'Sailor',
              frozenset(range(96, 101)): 'Soldier'}
race = {frozenset(range(1, 41)): 'Human',
        frozenset(range(41, 51)): 'Dwarf',
        frozenset(range(51, 61)): 'Elf',
        frozenset(range(61, 71)): 'Halfling',
        frozenset(range(71, 76)): 'Dragonborn',
        frozenset(range(76, 81)): 'Gnome',
        frozenset(range(81, 86)): 'Half-elf',
        frozenset(range(86, 91)): 'Half-orc',
        frozenset(range(91, 96)): 'Tiefling',
        frozenset(range(96, 101)): 'DM\'s choice'}
relationship = {frozenset(range(3, 5)): 'Hostile',
                frozenset(range(5, 11)): 'Friendly',
                frozenset(range(11, 13)): 'Indifferent'}
status = {frozenset([3]): 'Dead',  # Randomized addition TODO
          frozenset(range(4, 6)): 'Mising or unknown',
          frozenset(
              range(6, 9)): 'Alive, but doing poorly due to injury, financial trouble, or relationship difficulties',
          frozenset(range(9, 13)): 'Alive and well',
          frozenset(range(13, 16)): 'Alive and quite successful',
          frozenset(range(16, 18)): 'Alive and infamous',
          frozenset([18]): 'Alive and famous'}

'''SECONDARY TABLES'''

adventures = {
    frozenset(range(1, 11)): 'You nearly died. You have nasty scars on your body, and you are missing an ear, ' +
                             roll_a_d3() + ' fingers, or' + roll_a_d4() + ' toes.',
    frozenset(range(11, 21)): 'You suffered a grievous injury. Although the wound healed, '
                              'it still pains you from time to time.',
    frozenset(range(21, 31)): 'You were wounded, but in time you fully recovered.',
    frozenset(range(31, 41)): 'You contracted a disease while exploring a filthy warren. '
                              'You recovered from the disease, but you have a persistent cough, '
                              'pockmarks on your skuin, or prematurely gray hair.',
    frozenset(range(41, 51)): 'You were poisoned by a trap or monster. You recovered, but the next time you '
                              'must make a saving throw against poison, you make the saving throw '
                              'with disadvantage.',
    frozenset(range(51, 61)): 'You lost something of sentimental value to you during your adventure. '
                              'Remove one trinket from your possessions.',
    frozenset(range(61, 71)): 'You were terribly frightened by something you encountered and ran away, '
                              'abandoning your companions to their fate.',
    frozenset(range(71, 81)): 'You learned a great deal during your adventure. The next time you make '
                              'an ability check or a saving throw, you have advantage on the roll.',
    frozenset(range(81, 91)): 'You found some treasure on your adventure. You have ' + roll_2d6() +
                              ' gp from your share of it.',
    frozenset(range(91, 100)): 'You found a considerable amount of treasure on your adventure. You have ' +
                               str(int(roll_a_d20()) + 50) + ' gp left from your share of it.',
    frozenset([100]): 'You came across a common magic item (of the DM\'s choice).'}
arcane_matters = ['You were charmed or frightened by a spell.',
                  'You were injured by the effect of a spell.',
                  'You witnessed a powerful spell being cast by ',  # Randomized addition
                  'You drank a potion (of the DM\'s choice.',
                  'You found a spell scroll (of the DM\'s choice) and succeeded in casting the spell it contained.',
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
         'You found some money. You have ' + roll_a_d20() + ' gp in addition to your regular starting funds.',
         'A relative bequeathed you a simple weapon of your choice.',
         'You found something interesting. You gain one additional trinket.',
         'You once performed a service for a local temple. The next time you visit the temple, you can receive'
         ' healing up to your hit point maximum.',
         'A friendly alchemist gifted you with a potion of healing or a flask of acid, as you choose.',
         'You found a treasure map.',
         'A distant relative left you a stipend that enables you to live at the comfortable lifestyle for ' +
         roll_a_d20() + ' years. If you choose to live at a higher lifestyle, you reduce the price of the lifestyle'
                        ' by 2 gp during that time period.']
crime = ['Murder', 'Theft', 'Burglary', 'Assault', 'Smuggling', 'Kidnapping', 'Extortion', 'Counterfeiting']
punishment = {frozenset(range(1, 4)): 'You did not commit the crime and were exonerated after being accused.',
              frozenset(range(4, 7)): 'You committed the crime or helped to do so, but nonetheless the authorities '
                                      'found you not guilty.',
              frozenset(
                  range(7, 9)): 'You were nearly caught in the act. You had to flee and are wanted on the community '
                                'where the crime occurred.',
              frozenset(range(9, 13)): 'You were caught and convicted. You spent time in jail, chained to an oar, '
                                       'or performing hard labor. You served a sentence of ' +
                                       roll_a_d4() + ' years or succeeded in escaping after that much time.'}
supernatural_event = {frozenset(range(1, 6)): 'You were ensorcelled by a fey and enslaved for ' +
                                              roll_a_d6() + ' years before you escaped.',
                      frozenset(range(6, 11)): 'You saw a demon and ran away before it could do anything to you.',
                      frozenset(range(11, 16)): 'A devil tempted you. Make a DC 10 Wisdom saving throw. '
                                                'On a failed save, your alignment shifts one step toward evil '
                                                '(if it\'s not evil already), and you start the game with '
                                                'an additional ' + str(int(roll_a_d20()) + 50) + ' gp.',
                      frozenset(range(16, 21)): 'You woke up one morning miles from your home, '
                                                'with no idea how you got there.',
                      frozenset(range(21, 31)): 'You visited a holy site and felt the presence of the divine there.',
                      frozenset(range(31, 41)): 'You witnessed a falling red star, a face appearing in the frost, '
                                                'or some other bizarre happening. You are certain it was '
                                                'an omen of some sort.',
                      frozenset(range(41, 51)): 'You escaped certain death and believe it was the intervention '
                                                'of a god that saved you.',
                      frozenset(range(51, 61)): 'You witnessed a minor miracle.',
                      frozenset(range(61, 71)): 'You explored an empty house and found it to be haunted.',
                      frozenset(range(71, 76)): 'You were briefly possessed.',  # Randomized addition
                      frozenset(range(76, 81)): 'You saw a ghost.',
                      frozenset(range(81, 86)): 'You saw a ghoul feeding on a corpse.',
                      frozenset(range(86, 91)): 'A celestial or fiend visited you in your dreams to give a warning '
                                                'of dangers to come.',
                      frozenset(range(91, 96)): 'You briefly visited the Feywild or the Shadowfell.',
                      frozenset(
                          range(96, 101)): 'You saw a portal that you believe leads to another plane of existence.'}
tragedies = {frozenset(range(1, 3)): ('A family member or a close friend died.', cause_of_death_table(cause_of_death)),
             frozenset([3]): 'A friendship ended bitterly, and the other person is now hostile to you. The cause '
                             'might have been a misunderstanding or something you or the former friend did.',
             frozenset([4]): 'You lost all possessions in a disaster, and you had to rebuild your life.',
             frozenset([5]): 'You were imprisoned for a crime you didn\'t commit and spent ' +
                             roll_a_d6() + ' years at hard labor, in jail, or shackled to an oar in a slave galley.',
             frozenset([6]): 'War ravaged your home community, reducing everything to rubble and ruin. '
                             'In the aftermath, you either helped your town rebuild or moved somewhere else.',
             frozenset([7]): 'A lover disappeared without a trace. You have been lookiung for that person ever since.',
             frozenset([8]): 'A terrible blight in your home community caused crops to fail, and many starved. '
                             'You lost a sibling'
                             ' or some other family member.',
             frozenset([9]): 'You did something that brought terrible shame to you in the eyes of your family. '
                             'You might have been involved in a scandal, dabbled in dark magic, '
                             'or offended someone important. The attitude of your family members toward '
                             'you becomes indifferent at best, though they might eventually forgive you.',
             frozenset([10]): 'For a reason you were never told, you were exiled from your community. '
                              'You then either wandered in the wilderness for a time '
                              'or promptly found a new place to live.',
             frozenset([11]): 'A romantic relationship ended.',  # Randomized addition
             frozenset([12]): 'A current or prospective romantic partner of yours died.'}  # Randomized addition
war = {frozenset([1]): 'You were knocked out and left for dead. You woke up hours later '
                       'with no recollection of the battle.',
       frozenset(range(2, 4)): 'You were badly injured in the fight, and you still bear '
                               'the awful scars of those wounds.',
       frozenset([4]): 'You ran away from the battle to save your life, but you still feel shame for your cowardice.',
       frozenset(range(5, 8)): 'You suffered only minor injuries, an the wounds all healed without leaving scars.',
       frozenset(range(8, 10)): 'You survived the battle, but you suffer from terrible nightmares in which you '
                                'relive the experience.',
       frozenset(range(10, 12)): 'You escaped the battle unscathed, though many of your friends were injured or lost.',
       frozenset([12]): 'You acquitted yourself well in battle and are as a hero. You might have '
                        'received a medal for your bravery.'}
weird_stuff = ['You were turned into a toad and remained in that form for ' + roll_a_d4() + ' weeks.',
               'You were petrified and remained a stone statue for a time until someone freed you.',
               'You were enslaved by a hag, a satyr, or some other being and lived in that creature\'s thrall for ' +
               roll_a_d6() + ' years.',
               'A dragon held you as a prisoner for ' + roll_a_d4() + ' months until adventurers killed it.',
               'You were taken captive by a race of evil humanoids such as drow, kuo-toa, or quaggoths. You lived '
               'as a slave in the Underdark until you escaped.',
               'You served a powerful adventurer as a hireling. You have only recently left that service. '
               'Use the supplemental tables and work with your DM to determine the basic details '
               'about your former employer.',
               'You went insane for ' + roll_a_d6() + ' years and recently regained your sanity. '
                                                      'A tic or some other bit of odd behavior might linger.',
               'A lover of yours was secretly a silver dragon.',
               'You were captured by a cult and nearly sacrificed on an altar to the foul being the cultists served.'
               ' You escaped, but you fear they will find you.',
               'You met a demigod, an archdevil, an archfey, a demon lord, or a titan, and you lived to tell the tale.',
               'You were swallowed by a giant fish and spent a month in its gullet before you escaped.',
               'A powerful being granted you a wish, but you squandered it on something frivolous.']

'''MAIN TABLES'''

parents = {frozenset(range(1, 96)): 'You know who your parents are or were.',
           frozenset(range(96, 101)): 'You do not know who your parents were.'}
nonhuman_parents = {'Half-Elf': {frozenset(range(1, 6)): 'One parent was an elf and the other was a human.',
                                 frozenset([6]): 'One parent was an elf and the other was a half-elf.',
                                 frozenset([7]): 'One parent was a human and the other was a half-elf,',
                                 frozenset([8]): 'Both parents were half-elves.'},
                    'Half-Orc': {frozenset(range(1, 4)): 'One parent was an orc and the other was a human.',
                                 frozenset(range(4, 6)): 'One parent was an orc and the other was a half-orc.',
                                 frozenset(range(6, 8)): 'One parent was a human and the other was a half-orc.',
                                 frozenset([8]): 'Both parents were half-orcs.'},
                    'Tiefling': {frozenset(range(1, 5)): 'Both parents were humans, their infernal heritage dormant '
                                                         'until you came along.',
                                 frozenset(range(5, 7)): 'One parent was a tiefling and the other was a human.',
                                 frozenset([7]): 'One parent as a tiefling and the other was a devil.',
                                 frozenset([8]): 'One parent was a human and the other was a devil.'}}
birthplace = {frozenset(range(1, 51)): 'Home',
              frozenset(range(51, 56)): 'Home of a family friend',
              frozenset(range(56, 64)): 'Home of a healer or midwife',
              frozenset(range(64, 66)): 'Carriage, cart or wagon',
              frozenset(range(66, 69)): 'Barn, shed, or other outbuilding',
              frozenset(range(69, 71)): 'Cave',
              frozenset(range(71, 73)): 'Field',
              frozenset(range(73, 75)): 'Forest',
              frozenset(range(75, 78)): 'Temple',
              frozenset([78]): 'Battlefield',
              frozenset(range(79, 81)): 'Alley or street',
              frozenset(range(81, 83)): 'Brothel, tavern or inn',
              frozenset(range(83, 85)): 'Castle, keep, tower, or palace',
              frozenset([85]): 'Sewer or rubbish heap',
              frozenset(range(86, 89)): 'Among people of a different race',
              frozenset(range(89, 92)): 'On board a boat or a ship',
              frozenset(range(92, 94)): 'In a prison or in the headquarters of a secret organization',
              frozenset(range(94, 96)): 'In a sage\'s laboratory',
              frozenset([96]): 'In the Feywild',
              frozenset([97]): 'In the Shadowfell',
              frozenset([98]): 'On the Astral Plane or the Ethereal Plane',
              frozenset([99]): 'On an Inner Plane of your choice',
              frozenset([100]): 'On an Outer Plane of your choice'}
no_siblings = {frozenset(range(1, 3)): 'None',
               frozenset(range(3, 5)): roll_a_d3(),
               frozenset(range(5, 7)): str(int(roll_a_d4()) + 1),
               frozenset(range(7, 9)): str(int(roll_a_d6()) + 2),
               frozenset(range(9, 11)): str(int(roll_a_d8()) + 3)}
birth_order = {frozenset([2]): 'Twin, triplet or quadruplet',
               frozenset(range(3, 8)): 'Older',
               frozenset(range(8, 13)): 'Younger'}
family = {frozenset([1]): 'None',
          frozenset([2]): 'Institution, such as an asylum',
          frozenset([3]): 'Temple',
          frozenset(range(4, 6)): 'Orphanage',
          frozenset(range(6, 8)): 'Guardian',
          frozenset(range(8, 16)): 'Paternal or maternal aunt, uncle, or both; '
                                   'or extended family such as a tribe or clan',
          frozenset(range(16, 26)): 'Paternal or maternal grandparent(s)',
          frozenset(range(26, 36)): 'Adoptive family (same or different race',
          frozenset(range(36, 56)): 'Single father or stepfather',
          frozenset(range(56, 76)): 'Single mother or stepmother',
          frozenset(range(76, 101)): 'Mother and Father'}
absent_parent = [' died', ' was imprisoned, enslaved, or otherwise taken away.',
                 ' abandoned you.', ' disappeared to an unknown fate.']
family_lifestyle = {frozenset([3]): ('Wretched', -40),
                    frozenset(range(4, 6)): ('Squalid', -20),
                    frozenset(range(6, 9)): ('Poor', -10),
                    frozenset(range(9, 13)): ('Modest', 0),
                    frozenset(range(13, 16)): ('Comfortable', 10),
                    frozenset(range(16, 18)): ('Wealthy', 20),
                    frozenset([18]): ('Aristocratic', 40)}
childhood_home = {frozenset(range(-40, 1)): 'On the streets',
                  frozenset(range(1, 21)): 'Rundown Shack',
                  frozenset(range(21, 31)): 'No permanent residence; you moved around a lot',
                  frozenset(range(31, 41)): 'Encampment or village in the wilderness',
                  frozenset(range(41, 51)): 'Apartment in a rundown neighborhood',
                  frozenset(range(51, 71)): 'Small house',
                  frozenset(range(71, 91)): 'Large house',
                  frozenset(range(91, 111)): 'Mansion',
                  frozenset(range(111, 141)): 'Palace or castle'}
childhood_memories = {
    frozenset(range(-10, 4)): 'I am still haunted by my childhood, when I was treated badly by my peers.',
    frozenset(range(4, 6)): 'I spent most of my childhood alone, with no close friends.',
    frozenset(range(6, 9)): 'Others saw me as being different or strange, and so I had few companions.',
    frozenset(range(9, 13)): 'I had a few close friends and lived an ordinary childhood',
    frozenset(range(13, 16)): 'I had several friends, and my childhood was generally a happy one.',
    frozenset(range(16, 18)): 'I always found it easy to make friends, and I loved being around people.',
    frozenset(range(18, 30)): 'Everyone knew who I was, and I had friends everywhere I went.'}
background = {'Acolyte': ['I ran away from home at an early age and found refuge in a temple.',
                          'my family gave me to a temple, since they were unable or unwilling to care for me.',
                          'I grew up in a household with strong religious convictions. '
                          'entering the service of one or more gods seemed natural.',
                          'an impassioned sermon struck a chord deep in my soul and moved me to serve the faith.',
                          'I followed a childhood friend, a respected acquaintance, '
                          'or someone I loved into religious service.',
                          'after encountering a true servant of the gods, '
                          'I was so inspired that I immediately entered the service of a religious group.'],
              'Charlatan': ['I was left to my own devices, and my knack for manipulating others helped me survive.',
                            'I learned early on that people are gullible and easy to exploit.',
                            'I often got in trouble, but I managed to talk my way out of it every time.',
                            'I took up with a confidence artist, from whom I learned my craft',
                            'after a charlatan fleeced my family, I decided to learn the trade so I '
                            'would never be fooled by such deception again.',
                            'I was poor or I feared becoming poor, so I learned the tricks I needed '
                            'to keep myself out of poverty.'],
              'Criminal': ['I resented authority in my younger days and saw a life of crime '
                           'as the best way to fight against tyranny and oppression.',
                           'necessity forced me to take up the life, since it was the only way I could survive.',
                           'I fell in with a gang of reprobates and ne’er-do-wells, and I learned '
                           'my specialty from them.',
                           'a parent/relative taught me my criminal specialty to prepare me for the family business.',
                           'I left home and found a place in a thieves’ guild or some other criminal organization.',
                           'I was always bored, so I turned to crime to pass the time and discovered '
                           'I was quite good at it.'],
              'Entertainer': ['members of my family made ends meet by performing, '
                              'so it was fitting for me to follow their example.',
                              'I always had a keen insight into other people, enough so that I could make them '
                              'laugh or cry with my stories or songs.',
                              'I ran away from home to follow a minstrel troupe.',
                              'I saw a bard perform once, and I knew from that moment on what I was bor to do.',
                              'I earned coin by performing on street corners and eventually made a name for myself.',
                              'a traveling entertainer took me in and taught me the trade.'],
              'Folk Hero': ['I learned what was right and wrong from my family.',
                            'I was always enamored by tales of heroes and wished '
                            'I could be something more than ordinary.',
                            'I hated my mundane life, so when it was time for someone to step up and do '
                            'the right thing, I took my chance.',
                            'a parent or one of my relatives was an adventurer, and I was inspired '
                            'by that person’s courage.',
                            'a mad old hermit spoke a prophecy when I was born, '
                            'saying that I would accomplish great things.',
                            'I have always stood up for those who are weaker than I am.'],
              'Guild Artisan': ['I was apprenticed to a master who taught me the guild’s business.',
                                'I helped a guild artisan keep a secret or complete a task, '
                                'and in return I was taken on as an apprentice.',
                                'one of my family members who belonged to the guild made a place for me.',
                                'I was always good with my hands, so I took the opportunity to learn a trade.',
                                'I wanted to get away from my home situation and start a new life.',
                                'I learned the essentials of my craft from a mentor but had to join the guild '
                                'to finish my training.'],
              'Hermit': ['my enemies ruined my reputation, and I fled to the wilds to avoid further disparagement.',
                         'I am comfortable with being isolated, as I seek inner peace.',
                         'I never liked the people I called my friends, so it was easy for me to strike out on my own.',
                         'I felt compelled to forsake my past, but did so with great reluctance, '
                         'and sometimes I regret making that decision.',
                         'I lost everything — my home, my family, my friends. Going it alone was all I could do.',
                         'society\'s decadence disgusted me, so I decided to leave it behind.'],
              'Noble': ['I come from an old and storied family, and it fell to me to preserve the family name.',
                        'my family has been disgraced, and I intend to clear our name.',
                        'my family recently came by its title, and that elevation thrust us into '
                        'a new and strange world.',
                        'my family has a title, but none of my ancestors have distinguished themselves '
                        'since we gained it.',
                        'my family is filled with remarkable people. I hope to live up to their example.',
                        'I hope to increase my family’s power and influence.'],
              'Outlander': ['I spent a lot of time in the wilderness as a youngster, '
                            'and I came to love that way of life.',
                            'from a young age, I couldn\'t abide the stink of the cities '
                            'and preferred to spend my time in nature.',
                            'I came to understand the darkness that lurks in the wilds, and I vowed to combat it.',
                            'my people lived on the edges of civilization, '
                            'and I learned the methods of survival from my family.',
                            'after a tragedy I retreated to the wilderness, leaving my old life behind.',
                            'my family moved away from civilization, and I learned to adapt to my new environment.'],
              'Sage': ['I was naturally curious, so I packed up and went to a university '
                       'to learn more about the world.',
                       'my mentor\'s teachings opened my mind to new possibilities in that field of study.',
                       'I was always an avid reader, and I learned much I about my favorite topic on my own.',
                       'I discovered an old library and pored over the texts I found there. '
                       'That experience awakened a hunger for more knowledge.',
                       'I impressed a wizard who told me I was squandering my talents '
                       'and should seek out an education to take advantage of my gifts.',
                       'one of my parents or a relative gave me a basic education that whetted my appetite, '
                       'and I left home to build on what I had learned.'],
              'Sailor': ['I was press-ganged by pirates and forced to serve on their ship until I finally escaped.',
                         'I wanted to see the world, so I signed on as a deckhand for a merchant ship.',
                         'one of my relatives was a sailor who took me to the sea.',
                         'I needed to escape my community quickly, so I stowed away on a ship. '
                         'When the crew found me, I was forced to work for my passage',
                         'reavers attacked my community, so I found refuge on a ship until I could seek vengeance.',
                         'I had few prospects where l was living, so I left to find my fortune elsewhere.'],
              'Soldier': ['I joined the militia to help protect my community from monsters.',
                          'a relative of mine was a soldier, and I wanted to carry on the family tradition.',
                          'the local lord forced me to enlist in the army.',
                          'war ravaged my homeland while I was growing up. Fighting was the only life I ever knew.',
                          'I wanted fame and fortune, so I joined a mercenary company, '
                          'selling my sword to the highest bidder.',
                          'Invaders attacked my homeland. It was my duty to take up arms in defense of my people.'],
              'Urchin': ['wanderlust caused me to leave my family to see the world. I look after myself.',
                         'I ran away from a bad situation at home and made my own way in the world.',
                         'monsters wiped out my village, and I was the sole survivor. I had to find a way to survive.',
                         'a notorious thief looked after me and other orphans, '
                         'and we spied and stole to earn our keep.',
                         'one day I woke up on the streets, alone and hungry, with no memory of my early childhood.',
                         'my parents died, leaving no one to look after me. I raised myself.']}
classes = {'Barbarian': ['my devotion to my people lifted me in battle, making me powerful and dangerous.',
                         'the spirits of my ancestors called on me to carry out a great task.',
                         'I lost control in battle one day, and it was as if something else was manipulating my body,'
                         ' forcing it to kill every foe I could reach.',
                         'went on a spiritual journey to find myself and instead found a spirit animal to guide, '
                         'protect, and inspire me.',
                         'I was struck by lightning and lived. Afterward, I found a new strength within me '
                         'that let me push beyond my limitations.',
                         'my anger needed to be channeled into battle, or I risked becoming an indiscriminate killer.'],
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
           'Cleric': ['a supernatural being in service to the gods called me to become a divine agent in the world.',
                      'I saw the injustice and horror in the world and felt moved to take a stand against them.',
                      'my god gave me an unmistakable sign. I dropped everything to serve the divine.',
                      'although I was always devout, it wasn\'t until I completed a pilgrimage '
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
                     'whiie I was growing up, I saw spirits all around me — entities no one else could perceive. '
                     'I sought out the druids to help me understand the visions and communicate with these beings.',
                     'I have always felt disgust for creatures of unnatural origin. For this reason, '
                     'I immersed myself in the study of the druidic mysteries and became a champion '
                     'of the natural order.'],
           'Fighter': ['I wanted to hone my combat skills, and so I joined a war college.',
                       'I squired for a knight who taught me how to fight, care for a steed, '
                       'and conduct myself with honor. I decided to take up that path for myself.',
                       'horrible monsters descended on my community, killing someone I loved. '
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
           'Paladin': ['a fantastical being appeared before me and called on me to undertake a holy quest.',
                       'one of my ancestors left a holy quest unfulfilled, so I intend to finish that work.',
                       'the world is a dark and terrible place. I decided to serve as a beacon of light '
                       'shining out against the gathering shadows.',
                       'I served as a paladin’s squire, learning all I needed to swear my own sacred oath.',
                       'evil must be opposed on all fronts. I feel compelled to seek out wickedness '
                       'and purge it from the world.',
                       'becoming a paladin was a natural consequence of my unwavering faith. In taking my vows, '
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
                     'an assassin or a thief wronged me, so I focused my training on mastering the skills '
                     'of my enemy to better combat foes of that sort.',
                     'an experienced rogue saw something in me and taught me several useful tricks.',
                     'I decided to turn my natural lucky streak into the basis of a career, '
                     'though I still realize that improving my skills is essential.',
                     'I took up with a group of ruffians who showed me how to get what I want through '
                     'sneakiness rather than direct confrontation.',
                     'I\'m a sucker for a shiny bauble or a sack of coins, '
                     'as long as I can get my hands on it without risking life and limb.'],
           'Sorcerer': ['when I was born, all the water in the house froze solid, the milk spoiled, '
                        'or all the iron turned to copper. My family is convinced that this event '
                        'was a harbinger of stranger things to come for me.',
                        'I suffered a terrible emotional or physical strain, which brought forth '
                        'my latent magical power. I have fought to control it ever since.',
                        'my immediate family never spoke of my ancestors, and when I asked, '
                        'they would change the subject. It wasn\'t until I started displaying '
                        'strange talents that the full truth of my heritage came out.',
                        'when a monster threatened one of my friends, I became filled with anxiety. '
                        'I lashed out instinctively and blasted the wretched thing '
                        'with a force that came from within me.',
                        'sensing something special in me, a stranger taught me how to control my gift.',
                        'after I escaped from a magical conflagration, I realized that though I was unharmed, '
                        'I was not unchanged. I began to exhibit unusual abilities that '
                        'I am just beginning to understand.'],
           'Warlock': ['while wandering around in a forbidden place, I encountered an otherworldly being '
                       'that offered to enter into a pact with me.',
                       'I was examining a strange tome I found in an abandoned library when the entity '
                       'that would become my patron suddenly appeared before me.',
                       'I stumbled into the clutches of my patron after I accidentally '
                       'stepped through a magical doorway.',
                       'when I was faced with a terrible crisis, I prayed to any being who would listen, '
                       'and the creature that answered became my patron.',
                       'my future patron visited me in my dreams and offered great power in exchange for my service.',
                       'one of my ancestors had a pact with my patron, so that entity was determined to bind me '
                       'to the same agreement.'],
           'Wizard': ['an old wizard chose me from among several candidates to serve an apprenticeship.',
                      'when I became lost in a forest, a hedge wizard found me, took me in, '
                      'and taught me the rudiments of magic.',
                      'I grew up listening to tales of great wizards and knew I wanted to follow their path. '
                      'I strove to be accepted at an academy of magic and succeeded.',
                      'one of my relatives was an accomplished wizard who decided I '
                      'was smart enough to learn the craft.',
                      'while exploring an old tomb, library, or temple, I found a spellbook. '
                      'I was immediately driven to learn all I could about becoming a wizard.',
                      'I was a prodigy who demonstrated mastery of the arcane arts at an early age. '
                      'when I became old enough to set out on my own, I did so to learn more magic '
                      'and expand my power.']}
life_events_by_age = {frozenset(range(1, 21)): ('20 years or younger', 1),
                      frozenset(range(21, 60)): ('21-30 years', roll_a_d4()),
                      frozenset(range(60, 70)): ('31-40 years', roll_a_d6()),
                      frozenset(range(70, 90)): ('41-50 years', roll_a_d8()),
                      frozenset(range(90, 101)): ('51-60 years', roll_a_d10()),
                      frozenset([100]): ('61 years or older', roll_a_d12())}
life_events = {frozenset(range(1, 21)): ('You suffered a tragedy: ', tragedies_table(tragedies)),
               frozenset(range(11, 21)): ('You gained a bit of good fortune. ', boons_table(boons)),
               frozenset(range(21, 31)): 'You fell in love or got married. If you get this result more than once, '
                                         'you can choose to have a child instead. Work with your DM to '
                                         'determine the identity of your love interest.',
               frozenset(range(31, 41)): 'You made an enemy of an adventurer. ' + enemy_adventurer() +
                                         'Use the supplemental tables and work with your DM to determine this hostile '
                                         'character\'s identity and the danger this enemy poses to you.',
               frozenset(range(41, 51)): 'You made a friend oan adventurer. Use the supplemental tables and work with '
                                         'your DM to add more detail to this friendly character and establish '
                                         'how your friendship began.',
               frozenset(range(51, 71)): 'You spent time working in a job related to your background. '
                                         'Start the game with an extra ' + roll_2d6() + ' gp.',
               frozenset(range(71, 76)): 'You met someone important. Use the supplemental tables to determine this '
                                         'character\'s identity and how this individual feels about you. '
                                         'Work out additional details with your DM as needed to fit '
                                         'this character into your backstory.',
               frozenset(range(76, 81)): ('You went on an adventure:', adventures_table(adventures)),
               frozenset(range(81, 86)): ('You had a supernatural experience:',
                                          supernatural_events_table(supernatural_event)),
               frozenset(range(86, 91)): 'You fought in a battle. ' +
                                         war_table(war) + ' Work with your DM to come up with the reason for the battle'
                                                          ' and the factions involved. It might have been '
                                                          'a small conflict between your community and a band of orcs, '
                                                          'or it could have been a major battle in a larger war.',
               frozenset(range(91, 96)): (
                   'You committed a crime or were wrongly accused of doing so.', crime_table(crime),
                   punishment_table(punishment)),
               frozenset(range(96, 100)): ('You encountered something magical:', arcane_matters_table(arcane_matters)),
               frozenset([100]): ('Something truly strange happened to you:', weird_stuff_table(weird_stuff))}
