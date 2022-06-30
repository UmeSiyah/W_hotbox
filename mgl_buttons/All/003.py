#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: <img src="mglIcon/a.png">
#
#----------------------------------------------------------------------------------------------------------

# author: sbaykal

for node in nuke.selectedNodes():
    if 'output' in node.knobs():
        node['output'].setValue('alpha')
    elif 'channels' in node.knobs():
        node['channels'].setValue('alpha')
