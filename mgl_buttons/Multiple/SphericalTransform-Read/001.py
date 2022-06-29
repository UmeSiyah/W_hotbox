#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Connect to Read
#
#----------------------------------------------------------------------------------------------------------

# author: sbaykal
# Connect the SphericalTransform to the right read base on his name

import re
sphericalNode = ''
for sNode in nuke.selectedNodes('SphericalTransform'):
    sphericalNode = sNode
sphericalNode['input'].setValue(2)
reFront =  re.compile('FRONT')
reBack = re.compile('BACK')
reLeft = re.compile('LEFT')
reRight = re.compile('RIGHT')
reTop = re.compile('TOP')
reBot = re.compile('BOTTOM')

dico = {}

for readNode in nuke.selectedNodes('Read'):
    readPath = readNode['file'].getValue()
    if reBack.search(readPath):
        dico[0] = readNode['name'].value()
    elif reFront.search(readPath):
        dico[1] = readNode['name'].value()
    elif reLeft.search(readPath):
        dico[2] = readNode['name'].value()
    elif reRight.search(readPath):
        dico[3] = readNode['name'].value()
    elif reBot.search(readPath):
        dico[4] = readNode['name'].value()
    elif reTop.search(readPath):
        dico[5] = readNode['name'].value()
    else:
        print("Unkown Position : ", readNode['name'].value())

for inputValue in dico.keys():
        sphericalNode.setInput(inputValue, nuke.toNode(dico[inputValue]))
