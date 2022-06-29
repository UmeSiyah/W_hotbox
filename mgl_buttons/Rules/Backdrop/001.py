#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: 0
# COLOR: #000000
#
#----------------------------------------------------------------------------------------------------------

backdropNodes = [backN for backN in nuke.selectedNodes() if backN.Class() == 'BackdropNode']
for node in backdropNodes:
    node['tile_color'].setValue(255)
