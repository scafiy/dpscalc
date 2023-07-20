from functions import *

#character attributes
character = "Ayaka"
constellation = "c0"
character_level = 90
er_requirement = 1

with open("database/characterDB.txt", "r") as file:
    for line in file:
        values = line.strip().split(", ")
        if values[0] == character:
            character_baseHP = int(values[1])
            character_baseATK = int(values[2])
            character_baseDEF = int(values[3])
            ascension_stat_type = values[4]
            ascension_stat_value = float(values[5])
            break 

#weapon attributes
weapon = "Amenoma Kageuchi"
weapon_level = 90
weapon_refinement = 1

with open("database/weaponDB.txt", "r") as file:
    for line in file:
        values = line.strip().split(", ")
        if values[0] == weapon:
            weapon_baseATK = int(values[1])
            weapon_stat_type = str(values[2])
            if "%" in values[3]:
                weapon_stat_value = float(values[3].replace("%", "")) / 100
            else:
                weapon_stat_value = float(values[3])
            break

#artifact mainstats
artifact_set = ""
artifact_rarity = 5
flower_stat = "flatHP"
feather_stat = "flatATK"
sands_stat = "ATK%"
goblet_stat = "Elemental DMG%"
circlet_stat = "CR%"

#artifact distributed substats
flatHP_rolls = 0
HP_percent_rolls = 0
flatATK_rolls = 0
ATK_percent_rolls = 0
flatDEF_rolls = 0
DEF_percent_rolls = 0
EM_rolls = 0
CR_rolls = 0
CD_rolls = 0
ER_rolls = 0
total_rolls = HP_percent_rolls + flatHP_rolls + ATK_percent_rolls + flatATK_rolls + DEF_percent_rolls + flatDEF_rolls + EM_rolls + CR_rolls + CD_rolls + ER_rolls


#fluid stats
fluid_flatHP = 0
fluid_HP_percent = 0
fluid_flatATK = 0
fluid_ATK_percent = 0.88
fluid_flatDEF = 0
fluid_DEF_percent = 0
fluid_EM = 0
fluid_CR = 0.55
fluid_CD = 0
fluid_ER = 0
fluid_DMG = 0
fluid_Elemental_DMG = 1.098
fluid_Physical_DMG = 0
fluid_NA_DMG = 0.3
fluid_CA_DMG = 0.3
fluid_P_DMG = 0
fluid_Skill_DMG = 0.15
fluid_Burst_DMG = 0.15
fluid_HB = 0
total_def_shred = 0
total_def_ignore = 0
elemental_resistance_shred = 0.40 + 0.14
physical_resistance_shred = 0
reaction_bonus = 0


def updatestat(returnstat):

    #total stats
    total_flatHP = fluid_flatHP
    if artifact_rarity == 5:
        total_flatHP = total_flatHP + 4780 + ((flatHP_rolls + 2)*253.94)
    elif artifact_rarity == 4:
        total_flatHP = total_flatHP + 3571 + ((flatHP_rolls + 2)*203.15)

    total_HP_percent = fluid_HP_percent
    if ascension_stat_type == "HP%":
        total_HP_percent = total_HP_percent + ascension_stat_value
    if weapon_stat_type == "HP%":
        total_HP_percent = total_HP_percent + weapon_stat_value
    if artifact_rarity == 5:
        if sands_stat == "HP%":
            total_HP_percent = total_HP_percent + 0.466
        if goblet_stat == "HP%":
            total_HP_percent = total_HP_percent + 0.466
        if circlet_stat == "HP%":
            total_HP_percent = total_HP_percent + 0.466
        total_HP_percent = total_HP_percent + ((HP_percent_rolls + 2)*0.0496)
    elif artifact_rarity == 4:
        if sands_stat == "HP%":
            total_HP_percent = total_HP_percent + 0.348
        if goblet_stat == "HP%":
            total_HP_percent = total_HP_percent + 0.348
        if circlet_stat == "HP%":
            total_HP_percent = total_HP_percent + 0.348
        total_HP_percent = total_HP_percent + ((HP_percent_rolls + 2)*0.0397)


    total_HP = (character_baseHP * (1+total_HP_percent)) + total_flatHP

    total_flatATK = fluid_flatATK
    if artifact_rarity == 5:
        total_flatATK = total_flatATK + 311 + ((flatATK_rolls + 2)*16.54)
    elif artifact_rarity == 4:
        total_flatATK = total_flatATK + 232 + ((flatATK_rolls + 2)*13.23)

    total_ATK_percent = fluid_ATK_percent
    if ascension_stat_type == "ATK%":
        total_ATK_percent = total_ATK_percent + ascension_stat_value
    if weapon_stat_type == "ATK%":
        total_ATK_percent = total_ATK_percent + weapon_stat_value
    if artifact_rarity == 5:
        if sands_stat == "ATK%":
            total_ATK_percent = total_ATK_percent + 0.466
        if goblet_stat == "ATK%":
            total_ATK_percent = total_ATK_percent + 0.466
        if circlet_stat == "ATK%":
            total_ATK_percent = total_ATK_percent + 0.466
        total_ATK_percent = total_ATK_percent + ((ATK_percent_rolls + 2)*0.0496)
    elif artifact_rarity == 4:
        if sands_stat == "ATK%":
            total_ATK_percent = total_ATK_percent + 0.348
        if goblet_stat == "ATK%":
            total_ATK_percent = total_ATK_percent + 0.348
        if circlet_stat == "ATK%":
            total_ATK_percent = total_ATK_percent + 0.348
        total_ATK_percent = total_ATK_percent + ((ATK_percent_rolls + 2)*0.0397)

    total_ATK = ((character_baseATK + weapon_baseATK) * (1+total_ATK_percent)) + total_flatATK

    total_flatDEF = fluid_flatDEF
    if artifact_rarity == 5:
        total_flatDEF = total_flatDEF + 311 + ((flatDEF_rolls + 2)*19.68)
    elif artifact_rarity == 4:
        total_flatDEF = total_flatDEF + 232 + ((flatDEF_rolls + 2)*15.74)

    total_DEF_percent = 0
    if ascension_stat_type == "DEF%":
        total_DEF_percent = total_DEF_percent + ascension_stat_value
    if weapon_stat_type == "DEF%":
        total_DEF_percent = total_DEF_percent + weapon_stat_value
    if artifact_rarity == 5:
        if sands_stat == "DEF%":
            total_DEF_percent = total_DEF_percent + 0.583
        if goblet_stat == "DEF%":
            total_DEF_percent = total_DEF_percent + 0.583
        if circlet_stat == "DEF%":
            total_DEF_percent = total_DEF_percent + 0.583
        total_DEF_percent = total_DEF_percent + ((DEF_percent_rolls + 2)*0.0620)
    elif artifact_rarity == 4:
        if sands_stat == "DEF%":
            total_DEF_percent = total_DEF_percent + 0.435
        if goblet_stat == "DEF%":
            total_DEF_percent = total_DEF_percent + 0.435
        if circlet_stat == "DEF%":
            total_DEF_percent = total_DEF_percent + 0.435
        total_DEF_percent = total_DEF_percent + ((DEF_percent_rolls + 2)*0.0496)

    total_DEF = (character_baseDEF * (1+total_DEF_percent)) + total_flatDEF


    total_EM = fluid_EM
    if ascension_stat_type == "EM":
        total_EM = total_EM + ascension_stat_value
    if weapon_stat_type == "EM":
        total_EM = total_EM + weapon_stat_value
    if artifact_rarity == 5:
        if sands_stat == "EM":
            total_EM = total_EM + 186.5
        if goblet_stat == "EM":
            total_EM = total_EM + 186.5
        if circlet_stat == "EM":
            total_EM = total_EM + 186.5
        total_EM = total_EM + ((EM_rolls + 2)*19.82)
    elif artifact_rarity == 4:
        if sands_stat == "EM":
            total_EM = total_EM + 139.3
        if goblet_stat == "EM":
            total_EM = total_EM + 139.3
        if circlet_stat == "EM":
            total_EM = total_EM + 139.3
        total_EM = total_EM + ((EM_rolls + 2)*15.86)


    total_CR = fluid_CR + 0.05
    if ascension_stat_type == "CR%":
        total_CR = total_CR + ascension_stat_value
    if weapon_stat_type == "CR%":
        total_CR = total_CR + weapon_stat_value
    if artifact_rarity == 5:
        if circlet_stat == "CR%":
            total_CR = total_CR + 0.311
        total_CR = total_CR + ((CR_rolls + 2)*0.0331)
    elif artifact_rarity == 4:
        if circlet_stat == "CR%":
            total_CR = total_CR + 0.232
        total_CR = total_CR + ((CR_rolls + 2)*0.0265)


    total_CD = fluid_CD + 0.5
    if ascension_stat_type == "CD%":
        total_CD = total_CD + ascension_stat_value
    if weapon_stat_type == "CD%":
        total_CD = total_CD + weapon_stat_value
    if artifact_rarity == 5:
        if circlet_stat == "CD%":
            total_CD = total_CD + 0.622
        total_CD = total_CD + ((CD_rolls + 2)*0.0662)
    elif artifact_rarity == 4:
        if circlet_stat == "CD%":
            total_CD = total_CD + 0.464
        total_CD = total_CD + ((CD_rolls + 2)*0.0530)

    total_CM = 1+(total_CR * total_CD)

    total_ER = fluid_ER + 1
    if ascension_stat_type == "ER%":
        total_ER = total_ER + ascension_stat_value
    if weapon_stat_type == "ER%":
        total_ER = total_ER + weapon_stat_value
    if artifact_rarity == 5:
        if sands_stat == "ER%":
            total_ER = total_ER + 0.518
        total_ER = total_ER + ((ER_rolls + 2)*0.0551)
    elif artifact_rarity == 4:
        if sands_stat == "ER%":
            total_ER = total_ER + 0.387
        total_ER = total_ER + ((ER_rolls + 2)*0.0441)

    total_DMG = fluid_DMG

    total_Elemental_DMG = fluid_Elemental_DMG
    if ascension_stat_type == "Elemental DMG%":
        total_Elemental_DMG = total_Elemental_DMG + ascension_stat_value
    if artifact_rarity == 5:
        if goblet_stat == "Elemental DMG%":
            total_Elemental_DMG = total_Elemental_DMG + 0.466
    elif artifact_rarity == 4:
        if goblet_stat == "Elemental DMG%":
            total_Elemental_DMG = total_Elemental_DMG + 0.348

    total_Physical_DMG = fluid_Physical_DMG
    if ascension_stat_type == "Physical DMG%":
        total_Physical_DMG = total_Physical_DMG + ascension_stat_value
    if weapon_stat_type == "Physical DMG%":
        total_Physical_DMG = total_Physical_DMG + weapon_stat_value
    if artifact_rarity == 5:
        if goblet_stat == "Physical DMG%":
            total_Physical_DMG = total_Physical_DMG + 0.466
    elif artifact_rarity == 4:
        if goblet_stat == "Physical DMG%":
            total_Physical_DMG = total_Physical_DMG + 0.348

    total_NA_DMG = fluid_NA_DMG
    total_CA_DMG = fluid_CA_DMG
    total_P_DMG = fluid_P_DMG
    total_Skill_DMG = fluid_Skill_DMG
    total_Burst_DMG = fluid_Burst_DMG
    total_HB = fluid_HB
    if ascension_stat_type == "HB%":
        total_HB = total_HB + ascension_stat_value
    if artifact_rarity == 5:
        if circlet_stat == "HB%":
            total_HB = total_HB + 0.359
    elif artifact_rarity == 4:
        if circlet_stat == "HB%":
            total_HB = total_HB + 0.268

    #enemy attributes

    enemy_level = 100
    enemy_elemental_resistance = 0.10
    enemy_physical_resistance = 0.10

    DEF_multiplier = (character_level+100)/((character_level+100)+(enemy_level+100)*(1-total_def_shred)*(1-total_def_ignore))

    if ((enemy_elemental_resistance - elemental_resistance_shred) < 0):
        enemy_elemental_resistance_multiplier = 1-(enemy_elemental_resistance - elemental_resistance_shred)/2
    else:
        enemy_elemental_resistance_multiplier = 1- (enemy_elemental_resistance - elemental_resistance_shred)

    if ((enemy_physical_resistance - physical_resistance_shred) < 0):
        enemy_physical_resistance_multiplier = 1-(enemy_physical_resistance - physical_resistance_shred)/2
    else:
        enemy_physical_resistance_multiplier = 1- (enemy_physical_resistance - physical_resistance_shred)

    #multipliers

    infused_NA_multiplier = (
        (((character_baseATK + weapon_baseATK)*(1+total_ATK_percent))+total_flatATK)
        * (1+(total_CR * total_CD))
        * (1+(total_DMG + total_Elemental_DMG + total_NA_DMG))
        * (DEF_multiplier * enemy_elemental_resistance_multiplier)
    )

    Infused_CA_multiplier = (
        (((character_baseATK + weapon_baseATK)*(1+total_ATK_percent))+total_flatATK)
        * (1+(total_CR * total_CD))
        * (1+(total_DMG + total_Elemental_DMG + total_CA_DMG))
        * (DEF_multiplier * enemy_elemental_resistance_multiplier)
    )

    Skill_multiplier = (
        (((character_baseATK + weapon_baseATK)*(1+total_ATK_percent))+total_flatATK)
        * (1+(total_CR * total_CD))
        * (1+(total_DMG + total_Elemental_DMG + total_Skill_DMG))
        * (DEF_multiplier * enemy_elemental_resistance_multiplier)
    )
    foward_amplifying_multiplier = 2*(1+(2.78*total_EM)/(1400+total_EM)+reaction_bonus)
    reverse_amplifying_multiplier = 1.5*(1+(2.78*total_EM)/(1400+total_EM)+reaction_bonus)

    Burst_multiplier = (
        (((character_baseATK + weapon_baseATK)*(1+total_ATK_percent))+total_flatATK)
        * (1+(total_CR * total_CD))
        * (1+(total_DMG + total_Elemental_DMG + total_Burst_DMG))
        * (DEF_multiplier * enemy_elemental_resistance_multiplier)
    )



    #rotation config
    damage = []

    damage.append( Burst_multiplier * ( 19 *1.91))
    damage.append(1 * Burst_multiplier * 2.86)
    
    if returnstat == "bm":
        print(Burst_multiplier)

    
    #output
    dpr = sum(damage)

    if returnstat == all:
        return dpr
    
    if returnstat == "er":
        return total_ER

    



#substat constraints 

if artifact_rarity == 5:
    flatHP_roll_constraint = 10
    HP_percent_roll_constraint = 10
    flatATK_roll_constraint = 10
    ATK_percent_roll_constraint = 10
    flatDEF_roll_constraint = 10
    DEF_percent_roll_constraint = 10
    EM_roll_constraint = 10
    CR_roll_constraint = 10
    CD_roll_constraint = 10
    ER_roll_constraint = 10
    total_roll_constraint = 20
    if sands_stat == "HP%":
        HP_percent_roll_constraint = HP_percent_roll_constraint - 2
    if sands_stat == "ATK%":
        ATK_percent_roll_constraint = ATK_percent_roll_constraint - 2
    if sands_stat == "DEF%":
        DEF_percent_roll_constraint = DEF_percent_roll_constraint - 2
    if sands_stat == "EM":
        EM_roll_constraint = EM_roll_constraint - 2
    if sands_stat == "ER%":
        ER_roll_constraint = ER_roll_constraint - 2
    if goblet_stat == "HP%":
        HP_percent_roll_constraint = HP_percent_roll_constraint - 2
    if goblet_stat == "ATK%":
        ATK_percent_roll_constraint = ATK_percent_roll_constraint - 2
    if goblet_stat == "DEF%":
        DEF_percent_roll_constraint = DEF_percent_roll_constraint - 2
    if goblet_stat == "EM":
        EM_roll_constraint = EM_roll_constraint - 2
    if circlet_stat == "HP%":
        HP_percent_roll_constraint = HP_percent_roll_constraint - 2
    if circlet_stat == "ATK%":
        ATK_percent_roll_constraint = ATK_percent_roll_constraint - 2
    if circlet_stat == "DEF%":
        DEF_percent_roll_constraint = DEF_percent_roll_constraint - 2
    if circlet_stat == "EM":
        EM_roll_constraint = EM_roll_constraint - 2
    if circlet_stat == "CR%":
        CR_roll_constraint = CR_roll_constraint - 2
    if circlet_stat == "CD%":
        CD_roll_constraint = CD_roll_constraint - 2

elif artifact_rarity == 4:
    flatHP_roll_constraint = 8
    HP_percent_roll_constraint = 8
    flatATK_roll_constraint = 8
    ATK_percent_roll_constraint = 8
    flatDEF_roll_constraint = 8
    DEF_percent_roll_constraint = 8
    EM_roll_constraint = 8
    CR_roll_constraint = 8
    CD_roll_constraint = 8
    ER_roll_constraint = 8
    total_roll_constraint = 18
    if sands_stat == "HP%":
        HP_percent_roll_constraint = HP_percent_roll_constraint - 2
    if sands_stat == "ATK%":
        ATK_percent_roll_constraint = ATK_percent_roll_constraint - 2
    if sands_stat == "DEF%":
        DEF_percent_roll_constraint = DEF_percent_roll_constraint - 2
    if sands_stat == "EM":
        EM_roll_constraint = EM_roll_constraint - 2
    if sands_stat == "ER%":
        ER_roll_constraint = ER_roll_constraint - 2
    if goblet_stat == "HP%":
        HP_percent_roll_constraint = HP_percent_roll_constraint - 2
    if goblet_stat == "ATK%":
        ATK_percent_roll_constraint = ATK_percent_roll_constraint - 2
    if goblet_stat == "DEF%":
        DEF_percent_roll_constraint = DEF_percent_roll_constraint - 2
    if goblet_stat == "EM":
        EM_roll_constraint = EM_roll_constraint - 2
    if circlet_stat == "HP%":
        HP_percent_roll_constraint = HP_percent_roll_constraint - 2
    if circlet_stat == "ATK%":
        ATK_percent_roll_constraint = ATK_percent_roll_constraint - 2
    if circlet_stat == "DEF%":
        DEF_percent_roll_constraint = DEF_percent_roll_constraint - 2
    if circlet_stat == "EM":
        EM_roll_constraint = EM_roll_constraint - 2
    if circlet_stat == "CR%":
        CR_roll_constraint = CR_roll_constraint - 2
    if circlet_stat == "CD%":
        CD_roll_constraint = CD_roll_constraint - 2


#meeting energy recharge requirements 
while er_requirement >= updatestat("er"):
    if ER_rolls > ER_roll_constraint:
        break
    ER_rolls = ER_rolls + 1
    updatestat(all)

ERR_for_ERreq = ER_rolls
if er_requirement > updatestat("er"):
    print("Warning: Energy Recharge requirments cannot be met with substats.")


#substat optimization

max_dpr = updatestat(all)

for i in range((ER_roll_constraint + 1) - ERR_for_ERreq):
    ER_rolls = i
    total_rolls = ER_rolls
    if total_rolls <= total_roll_constraint - ERR_for_ERreq:
        newdpr = updatestat(all)

        for i in range(flatATK_roll_constraint + 1):
            flatATK_rolls = i
            total_rolls = ER_rolls + flatATK_rolls
            if total_rolls <= total_roll_constraint - ERR_for_ERreq:
                newdpr = updatestat(all)
                for i in range(ATK_percent_roll_constraint + 1):
                    ATK_percent_rolls = i
                    total_rolls = ER_rolls + flatATK_rolls + ATK_percent_rolls
                    if total_rolls <= total_roll_constraint - ERR_for_ERreq:
                        newdpr = updatestat(all)
                        for i in range(CR_roll_constraint + 1):
                            CR_rolls = i
                            total_rolls = ER_rolls + flatATK_rolls + ATK_percent_rolls + CR_rolls
                            if total_rolls <= total_roll_constraint - ERR_for_ERreq:
                                newdpr = updatestat(all)
                                for i in range(CD_roll_constraint + 1):
                                    CD_rolls = i
                                    total_rolls = ER_rolls + flatATK_rolls + ATK_percent_rolls + CR_rolls + CD_rolls
                                    if total_rolls <= total_roll_constraint - ERR_for_ERreq:
                                        newdpr = updatestat(all)
                                        for i in range(EM_roll_constraint + 1):
                                            EM_rolls = i
                                            total_rolls = ER_rolls + flatATK_rolls + ATK_percent_rolls + CR_rolls + CD_rolls + EM_rolls
                                            if total_rolls <= total_roll_constraint - ERR_for_ERreq:
                                                newdpr = updatestat(all)
                                                if newdpr > max_dpr:
                                                    max_dpr = newdpr
                                                    O_flatATK = flatATK_rolls
                                                    O_ATK = ATK_percent_rolls
                                                    O_CR = CR_rolls
                                                    O_CD = CD_rolls
                                                    O_EM = EM_rolls
                                                    O_ER = ER_rolls + ERR_for_ERreq
                                                    O_total_rolls = total_rolls + ERR_for_ERreq

                                                   
                



print("flatATK rolls", O_flatATK)
print("ATK rolls", O_ATK)
print("CR rolls", O_CR)
print("CD rolls", O_CD)
print("EM rolls", O_EM)
print("ER rolls", O_ER)
print("total rolls", O_total_rolls)

rotation_length = 20
dps = max_dpr/rotation_length
print("DPS:", round(dps))

