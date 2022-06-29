#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: frame range from input
#
#----------------------------------------------------------------------------------------------------------

for w in nuke.selectedNodes('Write'):
    w['first'].setExpression('[value first_frame]')
    w['last'].setExpression('[value last_frame]')