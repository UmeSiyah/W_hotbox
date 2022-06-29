#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: 2
# COLOR: #388e8e
#
#----------------------------------------------------------------------------------------------------------

backdropNodes = [backN for backN in nuke.selectedNodes() if backN.Class() == 'BackdropNode']
for node in backdropNodes:
    node['tile_color'].setValue(948866815)
