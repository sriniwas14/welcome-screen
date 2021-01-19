# window.py
#
# Copyright 2021 sriniwas14
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

import os
from gi.repository import Gtk

@Gtk.Template(resource_path='/com/sriniwas/welcomescreen/components/welcome_screen_row.ui')
class WelcomeScreenRow(Gtk.Box):
    __gtype_name__ = 'WelcomeScreenRow'

    itemTitle : Gtk.Label = Gtk.Template.Child()
    itemSubtitle : Gtk.Label = Gtk.Template.Child()
    openProjectButton : Gtk.Button = Gtk.Template.Child()

    projectDir = ""

    def __init__(self, title, subtitle, **kwargs):
        super().__init__(**kwargs)
        self.itemTitle.set_label(title)
        self.itemSubtitle.set_label(subtitle)
        self.projectDir = subtitle

        self.openProjectButton.connect("clicked", self.openProjectDir)

    def openProjectDir(self, button):
        os.system("nautilus "+self.projectDir+" &")
