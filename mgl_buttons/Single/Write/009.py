#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Render keyframes
#
#----------------------------------------------------------------------------------------------------------

nWrit = nuke.selectedNode()
nDiss = nuke.dependencies(nWrit)[0]

keyframes = []
k = nDiss['which'].animations()[0]
for i in range (len(k.keys())):
    keyframes.append(int(k.keys()[i].x))

for kframe in keyframes:
    print(kframe, ' Rendered')
    nuke.execute( nWrit, kframe, kframe)