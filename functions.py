#multiplier calculations


#buffs
def bennett_buff(weapon_baseATK):
    total_baseATK = 191 + weapon_baseATK
    flatATK_buff = total_baseATK*(1.12+0.20)
    return flatATK_buff
