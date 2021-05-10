# ***** BEGIN LICENSE BLOCK *****
# Version: MPL 1.1/GPL 2.0/LGPL 2.1
#
# The contents of this file are subject to the Mozilla Public License Version
# 1.1 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
# http://www.mozilla.org/MPL/
#
# Software distributed under the License is distributed on an "AS IS" basis,
# WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License
# for the specific language governing rights and limitations under the
# License.
#
# The Original Code is the Python Computer Graphics Kit.
#
# The Initial Developer of the Original Code is Matthias Baas.
# Portions created by the Initial Developer are Copyright (C) 2004
# the Initial Developer. All Rights Reserved.
#
# Contributor(s):
#
# Alternatively, the contents of this file may be used under the terms of
# either the GNU General Public License Version 2 or later (the "GPL"), or
# the GNU Lesser General Public License Version 2.1 or later (the "LGPL"),
# in which case the provisions of the GPL or the LGPL are applicable instead
# of those above. If you wish to allow use of your version of this file only
# under the terms of either the GPL or the LGPL, and not to allow others to
# use your version of this file under the terms of the MPL, indicate your
# decision by deleting the provisions above and replace them with the notice
# and other provisions required by the GPL or the LGPL. If you do not delete
# the provisions above, a recipient may use your version of this file under
# the terms of any one of the MPL, the GPL or the LGPL.
#
# ***** END LICENSE BLOCK *****
# $Id: draw.py,v 1.1.1.1 2004/12/12 14:30:59 mbaas Exp $

## \file draw.py
## Contains the Draw class.

from . import protocols
from .Interfaces import *
from .cgtypes import vec3
from .worldobject import WorldObject
from .drawgeom import DrawGeom

# Draw
class Draw(WorldObject):

    protocols.advise(instancesProvide=[ISceneItem])

    def __init__(self,
                 name="Draw",
                 **params):
        WorldObject.__init__(self, name=name, **params)
        self.geom = DrawGeom()

    def clear(self):
        self.geom.clear()

    def marker(self, pos, col=(1,1,1), size=1.0):
        self.geom.marker(vec3(pos), vec3(col), size)

    def line(self, pos1, pos2, col=(1,1,1), size=1.0):
        self.geom.line(vec3(pos1), vec3(pos2), vec3(col), size)
        
