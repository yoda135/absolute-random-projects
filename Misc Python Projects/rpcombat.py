__version__ = 0.1
__maintainer__ = "maintainer@website.com"
__status__ = "Prototype"

# Import modules

import random

# set up constant data.

stock = {'shield':(15,20,50),
         'sword':(60,60,40),
         'dagger':(25,30,50),
         'halberd':(80,80,30),
         'club':(15,30,30),
         'flail':(50,70,45),
         'hammer':(99,100,20),
         'cuirass':(30,45,20),
         'armour':(101,100,0),
         'lantern':(10,5,30),
         'pole':(10,5,50),
         'rope':(10,5,70)}
armour_types = set(['shield','cuirass','armour'])
hits = ('hits','bashes','smites','whacks','shreds','mutilates','lacerates','annihilates')
misses = ('misses','nearly hits','fails to connect with','swipes wildly at','flails ineffectually at','gets nowhere near','nearly decapitates self instead of','hits self on the foot, to the amusement of')
damage_report = ('small insult','flesh wound','deep slash','ragged gash','savage laceration','fractrued rib-cage','smashed-up face','split skull')
life_changing = ('a scar.','bruising.','serious blood-los.','total debilitation.','chronic concussion.','a severed limb.','multiple fractures.','an amputated head.')

# Prefrences
#Set to 'true' to trace variable.
trace = False
max_players = 2

# This is a global variable
players = []

#generate characters
while len(players) < max_players:
    print()
    print("New Character")
    # Create empty profile dictionary
    profile = {'Name':"",'Desc':"", 'Gender':"", 'Race':"", 'Muscle':0,'Brainz':0,'Speed':0,'Charm':0,'life':0,'magic':0,'prot':0,'gold':0,'inventory':[]}

    # Prompt user for user-defined information (Name, Desc, Gender, Race)
    name = input('What is your name? ')
    desc = input('Describe yourself: ')
    gender = input('What gender are you? (male/female/unsure): ')
    race = input('What race are you? (Pixie/Vulcan/Gelfling/Troll): ')

    profile['Name'] = name.capitalize()
    profile['Desc'] = desc.capitalize()
    gender = gender.lower()
    if gender.startswith('f'):
        profile['Gender'] = 'female'
    elif gender.startswith('m'):
        profile['Gender'] = 'male'
    else:
        profile['Gender'] = 'neuter'
    race = race.capitalize()
    if race.startswith('P'):
        profile['Race'] = 'Pixie'
    elif race.startswith('V'):
        profile['Race'] = 'Vulcan'
    elif race.startswith('G'):
        profile['Race'] = 'Gelfling'
    elif race.startswith('T'):
        profile['Race'] = 'Troll'
    else:
        profile['Race'] = 'Goblin'

    # Generate stats
    profile['Muscle'] = random.randint(3,33) + random.randint(3,33) + random.randint(3,33)
    profile['Brainz'] = random.randint(3,33) + random.randint(3,33) + random.randint(3,33)
    profile['Speed'] = random.randint(3,33) + random.randint(3,33) + random.randint(3,33)
    profile['Charm'] = random.randint(3,33) + random.randint(3,33) + random.randint(3,33)

    # work out combat stats
    life = (profile['Muscle'] + (profile['Speed']/2) + random.randint(9,49))/2
    magic = (profile['Brainz'] + (profile['Charm']/2) + random.randint(9,49))/2
    prot = (profile['Speed'] + (profile['Brainz']/2) + random.randint(9,49))/2
    gold = random.randint(9,49) + random.randint(9,49) + random.randint(9,49)

    
    # validate stats
    if life > 0 and life < 100:
        profile['life'] = life
    else:
        life = random.randint(9,99)
    if magic > 0 and magic < 100:
        profile['magic'] = magic
    else:
        magic = random.randint(9,99)
    if prot > 0 and prot < 100:
        profile['prot'] = prot
    else:
        prot = random.randint(9,99)
    if gold > 0:
        profile['gold'] = gold
    else:
        gold = random.randint(9,99)



    #ouput character sheet
    fancy_line = "<~~==|#|==~~++**\@/**++~~==|#|==~~>"
    print()
    print(fancy_line)
    print("\t", profile['Name'])
    print("\t", profile['Race'], profile['Gender'])
    print("\t", profile['Desc'])
    print(fancy_line)
    print()
    print("\tMuscle: ", profile['Muscle'], "\tlife: ", profile['life'])
    print("\tBrainz: ", profile['Brainz'], "\tmagic: ", profile['magic'])
    print("\tSpeed: ", profile['Speed'], "\tprotection: ", profile['prot'])
    print("\tCharm: ", profile['Charm'], "\tgold: ", profile['gold'])
    print()

    # prompt user to buy equipment
    purchase = input("Would you like to buy some equipment? ")
    while purchase != 'done':
        # display shop stock list with prices
        print()
        print("<==|#|==\SHOP/==|#|==>")
        for item in stock:
            print("\t", item, stock[item][0])
        print("<==|#|==\@@@@/==|#|==>")    
        print()
        print("You have", profile['gold'], "pieces of gold.")
        # prompt user to make a purchase
        purchase = input('Please choose an item or type "done" to quit: ')
        #if item in stock and player has enough gold, buy it
        if purchase in stock:
            if stock[purchase][0] <= profile['gold']:
                print("You buy a", purchase, "for", stock[purchase][0], "gold pieces.")
                profile['gold'] -= stock[purchase][0]
                profile['inventory'].append(purchase)
                print("You have a", " ".join(profile['inventory']), "in your bag.")
                print("You have", profile['gold'], "gold pieces left.")
            elif purchase == 'done':
                break
            else:
                print("You dont have enough gold to buy that.")
        else:
            print("We dont have", purchase, "in stock.")
    print("You own a", " ".join(profile['inventory']))

    #prompt user to enter combat and choose a weapon
    print(profile['Name'], "Are you ready for mortal combat?")
    weapon = input("Then choose your weapon: ")

    weapon = weapon.lower()
    if weapon in profile['inventory']:
        profile['weapon'] = stock[weapon]
    else:
        profile['weapon'] = (0,20,50)

    profile['armour'] = (0,0,50)
    for armour_type in armour_types:
        if armour_type in profile['inventory']:
            profile['armour'] = stock[armour_type]

    print(profile['Name'], "is now ready for battle.")

    players.append(profile)

#combat

print()
print("Then let combat begin.")
print()

vel_max = 23
vel_min = 1
dam_max = 23

# loop while both players still alive
while players[0]['life'] > 0 and players[1]['life'] > 0:
    for attacker, player in enumerate(players):

        input(players[attacker]['Name'] + " wants to attack, press enter...")
        
        target = int(not bool(attacker))
        life_left = players[target]['life']

        # calc velocity of blow
        attack_speed = players[attacker]['Speed']
        weapon_speed = players[attacker]['weapon'][2]
        attack_chance = random.randint(1, players[attacker]['Brainz'])
        attack_velocity = attack_speed + weapon_speed + attack_chance
        target_prot = players[target]['prot']
        armour_speed = players[target]['armour'][2]
        target_velocity = target_prot + armour_speed
        velocity = (attack_velocity - target_velocity) / 2
        
        if trace:
            print("\t", velocity)
        if velocity > 0:
            if velocity > vel_max:
                vel_max = velocity
            hit_type = int(7 * velocity / vel_max)
            if hit_type > 7:
                hit_type = 7
            if trace:
                print("\t\tHit#", hit_type)
            print(players[attacker]['Name'], hits[hit_type], players[target]['Name'])
        else:
            if velocity < vel_min:
                vel_min = velocity
            miss_type = int(velocity / vel_max)
            if miss_type > 7:
                miss_type = 7
            if trace:
                print("\t\tMiss#", miss_type)
            print(players[attacker]['Name'], misses[miss_type], players[target]['Name'])
            continue

        # calc damage
        attack_strength = players[attacker]['Muscle']
        weapon_damage = players[attacker]['weapon'][1]
        attack_damage = attack_strength + weapon_damage + velocity
        target_strength = players[target]['Muscle']
        armour_strength = players[target]['armour'][1]
        target_chance = random.randint(9, players[target]['Brainz'])
        target_defence = target_strength + armour_strength + target_chance
        potential_damage = (attack_damage - target_defence)

        if potential_damage < 1:
            potential_damage = 2
        damage = random.randint(1, int(potential_damage))
        if trace:
            print()
        print("\t\tDamage:", damage)
        if damage > dam_max:
            dam_max = damage

        # print damage report
        damage_type = int(7 * damage/dam_max)
        if damage_type > 7:
            damage_type = 7
        if trace:
            print("\t\t\tDamage#", damage_type)
        change_type = int(5 * damage/life_left)
        if change_type > 7:
            change_type = 7
        if trace:
            print("\t\t\tChange#", change_type)

        print("inflicting a", damage_report[damage_type], "and", life_changing[change_type])

        #inflict damage on target
        players[target]['life'] -= damage
        #player still alive?
        if players[target]['life'] <= 0:
            #print winner
            print()
            print(players[target]['Name'], "collapses in a pool of blood")
            print(players[attacker]['Name'], "wins the fight.")
            print()
            break
        
        
    
    

