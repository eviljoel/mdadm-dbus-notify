# mdadm-dbus-notify

**This program doesn't work yet. Don't use it.**

_mdadm-dbus-notify_ can be used with mdadm to create DBus desktop notifications for RAID failures.

mdadm-dbus-notify is licensed under the GNU GPLv3. A bit of code was borrowed from Douglas J. Hunley's mdadm\_notify (https://github.com/hunleyd/mdadm_notify).

Bug fixes are welcome!

## Prerequisites

The only current method of installation is building and installing your own debian package. I also make the following assumptions:

*    You are already familiar with using a Linux terminal.
*    You are already somewhat familiar with using debuild.
*    You already have mdadm installed and configured.
*    You are installing on a desktop system that uses DBus notification.

## Steps to Build and Install

1.   Clone the latest release tag. (Do not build the master branch. `master` may not be stable.)
2.   Use `debuild` in the project root directory to build the package.
3.   Use `dpkg -i` to install the package.
4.   Use `apt-get -f install` to resolve any missing dependencies.
5.   Add the following line to /etc/mdadm/mdadm.conf: PROGRAM /usr/share/mdadm-dbus-notify/mdadm-dbus-notify.py

## Updates

Updates may change configuration file options, so if you have a configuration file already, check that it has all of the required options in the current example file.
