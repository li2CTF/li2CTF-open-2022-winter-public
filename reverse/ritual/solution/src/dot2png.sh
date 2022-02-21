#!/bin/sh

# to generate .dot graph, I used radare2 (see 'ag' command)
replace "c19c00" "d5d5d5" -- ritual.dot
dot -Tpng ritual.dot -o ritual.png
