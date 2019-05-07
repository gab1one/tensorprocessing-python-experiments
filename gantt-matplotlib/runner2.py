#!/usr/bin/env python

"""
Wrapper function to use the Gantt class
"""
from gantt import Gantt

g = Gantt('/home/gabriel/University/Master/experiments/Row1_dup.json')
#g = Gantt('sample.json')
g.render()
#g.save('foo.png')
g.show()
