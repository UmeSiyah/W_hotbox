#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: <img src="/u/sbaykal/.nuke/W_hotbox/img/rgb.png">
#
#----------------------------------------------------------------------------------------------------------

# author: sbaykal

for node in nuke.selectedNodes():
    if 'output' in node.knobs():
        node['output'].setValue('rgb')
    elif 'channels' in node.knobs():
        node['channels'].setValue('rgb')
