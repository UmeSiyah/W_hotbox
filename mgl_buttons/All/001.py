#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: <img src="mglIcon/rgba.png">
#
#----------------------------------------------------------------------------------------------------------

# author: sbaykal

for node in nuke.selectedNodes():
    if 'output' in node.knobs():
        node['output'].setValue('rgba')
    elif 'channels' in node.knobs():
        node['channels'].setValue('rgba')
