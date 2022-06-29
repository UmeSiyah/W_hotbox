#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Generate render cmd
#
#----------------------------------------------------------------------------------------------------------

def createRenderLine():
    # import nukescripts
    JOBS = [str(n) for n in range(2, 10, 2)]
    SCRIPT = nuke.Root().name()
    NUKEXE = '' #nuke.env['ExecutablePath']
    gFrameRange = nuke.Panel('Frame range')
    gFrameRange.addSingleLineInput('Frame range', '%s-%s' % (nuke.root().firstFrame(),nuke.root().lastFrame()))
    if not gFrameRange.show():
        return
    fRange = gFrameRange.value('Frame range')
    nukeToRender = nuke.selectedNode()['name'].getValue()
    first_frame = int(fRange.split('-')[0])
    last_frame  = int(fRange.split('-')[1])
    

    cmd = f'"{NUKEXE}" -t -V -x -F {first_frame}-{last_frame} -X {nukeToRender} {SCRIPT}'
    #pyperclip.copy(cmd)
    print(cmd)

    c2c = nuke.Panel('Result')
    c2c.addSingleLineInput('Command line :', cmd)
    c2c.width()
    c2c.setWidth(len(cmd)*10)
    c2c.width()
    #if c2c.show():
        #pyperclip.paste()
createRenderLine()
