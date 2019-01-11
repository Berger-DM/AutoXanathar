import numpy as np
import PyInstaller
import PySimpleGUI as sg
from Functions import *
from AllTheTables import *

race_options = list(nonhuman_parents.keys())
race_options.append('Other Race')
class_options = list(classes.keys())
class_options.append('Other Class')
bg_options = list(background.keys())
bg_options.append('Other Background')
cha_mod_options = ['-5', '-4', '-3', '-2', '-1', '0', '1', '2', '3', '4', '5']

header = 'Input information needed. Options that start with \'Other\' will make them not be computed.'
race_text = 'Character Race'
class_text = 'Character Class'
bg_text = 'Character Background'
cha_mod_text = 'Cha Mod'
# print(type(race_options), type(class_options), type(bg_options), type(race_text), type(class_text), type(bg_text))

layout = [[sg.Text(header)],
          [sg.Text(race_text), sg.Text(class_text), sg.Text(bg_text), sg.Text(cha_mod_text)],
          [sg.InputCombo(race_options), sg.InputCombo(class_options), sg.InputCombo(bg_options),
           sg.InputCombo(cha_mod_options, default_value='0')],
          [sg.Button('Give me a character story!')]]

# print(type(layout))

window = sg.Window('AutoXanathar - Character Story Generator').Layout(layout)
# print(type(window))
event, values = window.Read()
inputs = values
print(values)

final_story = list()
origins = list()
origins.append('Origins:')

parents_roll = int(roll_a_d100())
for i in parents.keys():
    if parents_roll in i:
        origins.append(parents[i])

pc_race = inputs[0]
pc_class = inputs[1]
pc_bg = inputs[2]
pc_cha_mod = int(inputs[3])

if pc_race != 'Other Race':
    race_roll = int(roll_a_d8())
    for i in nonhuman_parents[pc_race].keys():
        if race_roll in i:
            origins.append(nonhuman_parents[pc_race][i])

birthplace_roll = int(roll_a_d100())
for i in birthplace.keys():
    if birthplace_roll in i:
        origins.append('Birthplace: ' + birthplace[i])

no_siblings_roll = int(roll_a_d10())
for i in no_siblings.keys():
    if no_siblings_roll in i:
        origins.append('Siblings: ' + no_siblings[i])
        if no_siblings[i] != 'None':
            for j in range(1, int(no_siblings[i]) + 1):
                init_str = 'Sibling #' + str(j) + ": "
                birth_order_roll = int(roll_2d6())
                for k in birth_order.keys():
                    if birth_order_roll in k:
                        init_str += birth_order[k] + ", "
                occupation_roll = int(roll_a_d100())
                for k in occupation.keys():
                    if occupation_roll in k:
                        if isinstance(occupation[k], tuple):
                            fst_str = occupation[k][0]
                            sec_str = occupation[k][1]
                            init_str += fst_str + ": " + sec_str + ", "
                        else:
                            init_str += occupation[k] + ', '
                init_str += alignment_table(aligment) + ', '
                status_roll = int(roll_3d6())
                for k in status.keys():
                    if status_roll in k:
                        init_str += status[k] + ', '
                relationship_roll = int(roll_a_d12())
                for k in relationship.keys():
                    if relationship_roll in k:
                        init_str += relationship[k] + ';'
                origins.append(init_str)

family_roll = int(roll_a_d100())
for i in family.keys():
    if family_roll in i:
        origins.append(family[i])
        if family_roll < 36:
            absent_roll = int(roll_a_d4()) - 1
            absent_roll2 = int(roll_a_d4()) - 1
            origins.append("Mother" + absent_parent[absent_roll] + " Father" + absent_parent[absent_roll2])
        elif family_roll < 56:
            absent_roll = int(roll_a_d4()) - 1
            origins.append('Mother' + absent_parent[absent_roll])
        elif family_roll < 76:
            absent_roll = int(roll_a_d4()) - 1
            origins.append('Father' + absent_parent[absent_roll])

childhood_modifier = 0
family_lifestyle_roll = int(roll_3d6())
for i in family_lifestyle.keys():
    if family_lifestyle_roll in i:
        origins.append('Family Lifestyle: ' + family_lifestyle[i][0])
        childhood_modifier = family_lifestyle[i][1]

childhood_home_roll = int(roll_a_d100()) + childhood_modifier
for i in childhood_home.keys():
    if childhood_home_roll in i:
        origins.append('Childhood Home: ' + childhood_home[i])

childhood_memories_roll = int(roll_3d6()) + pc_cha_mod
for i in childhood_memories.keys():
    if childhood_memories_roll in i:
        origins.append('Childhood Memories: ' + childhood_memories[i])

if pc_bg != 'Other Background':
    background_roll = int(roll_a_d6()) - 1
    origins.append('I became a ' + pc_bg + ' because ' + background[pc_bg][background_roll])

if pc_class != 'Other Class':
    class_roll = int(roll_a_d6()) - 1
    origins.append('I became a ' + pc_class + ' because ' + classes[pc_class][class_roll])

final_story.append(origins)

events = list()
events.append('Life Events: ')

no_life_events = 1
age_roll = int(roll_a_d100())
for i in life_events_by_age.keys():
    if age_roll in i:
        events.append('Age: ' + life_events_by_age[i][0])
        no_life_events = int(life_events_by_age[i][1])

for i in range(1, no_life_events + 1):
    life_events_roll = int(roll_a_d100())
    for j in life_events.keys():
        if life_events_roll in j:
            if isinstance(life_events[j], tuple):
                events.append(life_events[j][0] + life_events[j][1])
            else:
                events.append(life_events[j])

final_story.append(events)
print(final_story)

with open('backstory.txt', 'w+') as file:
    for row in final_story:
        for row2 in row:
            file.write(row2 + '\n')
