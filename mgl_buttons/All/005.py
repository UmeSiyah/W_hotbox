#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Localize All
#
#----------------------------------------------------------------------------------------------------------

# author: sbaykal

readKnobList = []
readNode = nuke.allNodes('Read')
#for itm in readNode:
#    itm['cacheLocal'].setValue(0)
for n in readNode:
    readKnob = nuke.getReadFileKnob(n)
    if readKnob != None:
        if nuke.localisationEnabled(readKnob):
            readKnobList.append(readKnob)
nuke.localiseFiles(readKnobList)
