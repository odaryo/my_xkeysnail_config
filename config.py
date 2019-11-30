# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# [Global modemap] Change modifier keys as in xmodmap
define_modmap({
    Key.CAPSLOCK: Key.LEFT_CTRL,
})

# original keybindings in non-Emacs applications
define_keymap(lambda wm_class: wm_class not in ("Emacs", "URxvt"), {
    # Cursor
    K("C-k"): with_mark(K("left")),
    K("C-l"): with_mark(K("right")),
    K("C-p"): with_mark(K("up")),
    K("C-n"): with_mark(K("down")),
    # Forward/Backward word
    K("M-k"): with_mark(K("C-left")),
    K("M-l"): with_mark(K("C-right")),
    # Beginning/End of line
    K("C-j"): with_mark(K("home")),
    K("C-Semicolon"): with_mark(K("end")),
    # Page up/down
    K("C-m"): with_mark(K("page_up")),
    K("C-o"): with_mark(K("page_down")),
    # Beginning/End of file
    K("M-h"): with_mark(K("C-home")),
    K("M-Semicolon"): with_mark(K("C-end")),
    # Delete
    K("C-d"): [K("delete"), set_mark(False)],
    K("M-d"): [K("C-delete"), set_mark(False)],
    # Kill line
    K("C-i"): [K("Shift-end"), K("C-x"), set_mark(False)],
    # Zenkaku/Hankaku
    K("M-GRAVE"): with_mark(K("Super-Space")),
    #K("M-GRAVE"): with_mark(K("M-Space")),
}, "original keys")

