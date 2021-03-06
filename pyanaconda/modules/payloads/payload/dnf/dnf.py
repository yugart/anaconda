#
# Kickstart module for DNF payload.
#
# Copyright (C) 2019 Red Hat, Inc.
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY expressed or implied, including the implied warranties of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.  You should have received a copy of the
# GNU General Public License along with this program; if not, write to the
# Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.  Any Red Hat trademarks that are incorporated in the
# source code or documentation are not subject to the GNU General Public
# License and may only be used or replicated with the express permission of
# Red Hat, Inc.
#
from pyanaconda.modules.payloads.constants import PayloadType, SourceType
from pyanaconda.modules.payloads.payload.payload_base import PayloadBase
from pyanaconda.modules.payloads.payload.dnf.dnf_interface import DNFInterface

from pyanaconda.anaconda_loggers import get_module_logger
log = get_module_logger(__name__)


class DNFModule(PayloadBase):
    """The DNF payload module."""

    def for_publication(self):
        """Get the interface used to publish this source."""
        return DNFInterface(self)

    @property
    def type(self):
        """Get type of this payload.

        :return: value of the payload.base.constants.PayloadType enum
        """
        return PayloadType.DNF

    @property
    def supported_source_types(self):
        """Get list of sources supported by DNF module."""
        return [
            SourceType.CDROM,
            SourceType.HDD,
            SourceType.HMC,
            SourceType.NFS,
            SourceType.REPO_FILES,
            SourceType.URL
        ]

    def process_kickstart(self, data):
        """Process the kickstart data."""
        pass

    def setup_kickstart(self, data):
        """Setup the kickstart data."""
        pass

    def pre_install_with_tasks(self):
        """Execute preparation steps.

        :return: list of tasks
        """
        # TODO: Implement this method
        pass

    def install_with_tasks(self):
        """Install the payload.

        :return: list of tasks
        """
        # TODO: Implement this method
        pass

    def post_install_with_tasks(self):
        """Execute post installation steps.

        :return: list of tasks
        """
        # TODO: Implement this method
        pass

    def set_up_sources_with_task(self):
        """Set up installation sources."""
        # TODO: Implement this method
        pass

    def tear_down_sources_with_task(self):
        """Tear down installation sources."""
        # TODO: Implement this method
        pass
