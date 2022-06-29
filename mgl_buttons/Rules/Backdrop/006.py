#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: 5
# COLOR: #70567e
#
#----------------------------------------------------------------------------------------------------------

backdropNodes = [backN for backN in nuke.selectedNodes() if backN.Class() == 'BackdropNode']
for node in backdropNodes:
    node['tile_color'].setValue(1884716799)
