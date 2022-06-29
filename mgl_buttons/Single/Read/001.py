#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Setup from it
#
#----------------------------------------------------------------------------------------------------------

root = nuke.Root()
readNode = nuke.selectedNode()
RnodeMeta = readNode.metadata()

# get frame rate
for keys in RnodeMeta.keys():
    if 'frame_rate' in keys:
        root['fps'].setValue(RnodeMeta[keys])

# set format
root['format'].setValue(readNode['format'].value())

# set frame range
root['first_frame'].setValue(readNode['first'].getValue())
root['last_frame'].setValue(readNode['last'].getValue())
