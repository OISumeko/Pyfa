# shipMissileEMDamageCF2
#
# Used by:
# Ship: Caldari Navy Hookbill
# Ship: Garmur
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("Missile Launcher Operation"),
                                    "emDamage", ship.getModifiedItemAttr("shipBonusCF2"), skill="Caldari Frigate")
