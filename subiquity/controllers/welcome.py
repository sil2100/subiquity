# Copyright 2015 Canonical, Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from subiquity.controllers import BaseController
from subiquity.views.welcome import WelcomeView
import subprocess


class WelcomeController(BaseController):
    """WelcomeController"""
    controller_name = "Welcome to Ubuntu"

    def show(self):
        return WelcomeView(self.finish)

    def finish(self, code, val):
        subprocess.check_call("/usr/local/bin/curtin_wrap.sh")
        raise SystemExit("Saw res: {}, val: {}".format(code, val))
