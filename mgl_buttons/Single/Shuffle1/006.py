#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Black Alpha
#
#----------------------------------------------------------------------------------------------------------

for i in nuke.selectedNodes():
    i.knob('in').setValue('rgba')
    i.knob('alpha').setValue('black')
    #i.knob('tile_color').setValue(4000)