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
absent_parent = ['Your parent died', 'Your parent was imprisoned, enslaved, or otherwise taken away.',
                 'Your parent abandoned you.', 'Your parent disappeared to an unknown fate.']