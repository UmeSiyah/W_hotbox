#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: 4
# COLOR: #71c671
# TEXTCOLOR: #111111
#
#----------------------------------------------------------------------------------------------------------

backdropNodes = [backN for backN in nuke.selectedNodes() if backN.Class() == 'BackdropNode']
for node in backdropNodes:
    node['tile_color'].setValue(1908830719)
