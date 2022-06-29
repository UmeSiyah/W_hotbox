#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Toggle View
#
#----------------------------------------------------------------------------------------------------------

viewKnob = nuke.selectedNode()['view']

if viewKnob.getValue() == 1:
        viewKnob.setValue(2)
elif viewKnob.getValue() == 2:
    viewKnob.setValue(1)
