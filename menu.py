import os
import nuke

W_hotboxCommonPath = os.getenv('W_HOTBOXCOMON_REPO')
nuke.pluginAddPath(W_hotboxCommonPath)

os.environ['W_HOTBOX_ICONS'] = f"{W_hotboxCommonPath}default_buttons/icons"
os.environ['W_HOTBOX_REPO_PATHS'] = f"{W_hotboxCommonPath}default_buttons:{W_hotboxCommonPath}mgl_buttons"
os.environ['W_HOTBOX_REPO_NAMES'] = "default_buttons:mgl_buttons"
os.environ['W_HOTBOX_HIDE_ICON_LOC'] = 'True'
os.environ['W_HOTBOX_MGLICONS'] = f"{W_hotboxCommonPath}mgl_buttons/icons"

import W_hotbox, W_hotboxManager