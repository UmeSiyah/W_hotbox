#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Generate Copycat render cmd
#
#----------------------------------------------------------------------------------------------------------

def createCopycatCLine():
    # import nukescripts
    SCRIPT = nuke.Root().name()
    NUKEXE = 'copycat'
    gFrameRange = nuke.Panel('Frame range')
    gFrameRange.addSingleLineInput('Frame range', '%s-%s' % (nuke.root().firstFrame(),nuke.root().lastFrame()))
    if not gFrameRange.show():
        return
    fRange = gFrameRange.value('Frame range')
    nodeToExecute = nuke.selectedNode()['name'].getValue()
    first_frame = int(fRange.split('-')[0])
    last_frame  = int(fRange.split('-')[1])
    

    cmd = f'{NUKEXE} -gpu 0 -t -V -x -F {first_frame}-{last_frame} -X {nodeToExecute} {SCRIPT}'
    #pyperclip.copy(cmd)
    print(cmd)

    c2c = nuke.Panel('Result')
    c2c.addSingleLineInput('Command line :', cmd)
    c2c.width()
    c2c.setWidth(len(cmd)*10)
    c2c.width()
    #if c2c.show():
        #pyperclip.paste()

createCopycatCLine()
