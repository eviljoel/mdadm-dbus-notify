#!/usr/bin/python

# Copyright 2018 Joel Allen Luellwitz
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
import sys

if (len(sys.argv) > 3):
    message = 'FAID Failure. Event: %s, MD Device: %s, Component Device: %s' % \
        (sys.argv[1], sys.argv[2], sys.argv[3])
else:
    message = 'FAID Failure. Event: %s, MD Device: %s' % \
        (sys.argv[1], sys.argv[2])

Notify.init('RAID Notify')
warning=Notify.Notification.new('RAID Error',
                              message,
                              'dialog-warning')
warning.set_urgency(Notify.Urgency.CRITICAL)
warning.show()
