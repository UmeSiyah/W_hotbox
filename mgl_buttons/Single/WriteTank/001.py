#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Import
#
#----------------------------------------------------------------------------------------------------------

import ntpath
for wNode in nuke.selectedNodes():
    nuke.tcl('drop', ntpath.dirname(wNode['cached_path'].evaluate()))