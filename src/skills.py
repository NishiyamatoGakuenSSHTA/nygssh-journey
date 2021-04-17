def panch(chara):
    retVal = {
        "toHp": chara.attack,
        "toMental": 0,
        "attribute": 0,
    }
    return retVal

skill_id_table = {
    0: panch
}