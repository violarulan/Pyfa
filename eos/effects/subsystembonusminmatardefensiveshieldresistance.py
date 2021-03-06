# subsystemBonusMinmatarDefensiveShieldResistance
#
# Used by:
# Subsystem: Loki Defensive - Adaptive Shielding
type = "passive"


def handler(fit, module, context):
    for type in ("Em", "Explosive", "Kinetic", "Thermal"):
        fit.ship.boostItemAttr("shield{0}DamageResonance".format(type),
                               module.getModifiedItemAttr("subsystemBonusMinmatarDefensive"),
                               skill="Minmatar Defensive Systems")
