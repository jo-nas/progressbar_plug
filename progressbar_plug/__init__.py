# -*- coding: utf-8 -*-
""" Progressbar for other Plugs
This module contains a plug that setup a progressbar and updates it.

To use this plug you must also update the frontend. Installation see README.md.

Example:
    If you want to use this plugs inside a test, import it.
    > from plugs import progress_bar
"""
from openhtf import plugs
import threading
import uuid
import logging
from tqdm import tqdm

_LOG = logging.getLogger(__name__)


class ProgressBarNotCreatedException(Exception):
    pass

class ProgressBar(plugs.FrontendAwareBasePlug):
    def __init__(self):
        super(ProgressBar, self).__init__()
        self._id = None
        self._progress = None
        self._status = None
        self._desc = None
        self._message = None
        self._progressbar_tqdm = None
        self._cond = threading.Condition()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if value != self.id:
            self._id = value
            self.notify_update()

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value != self.status:
            self._status = value
            self.notify_update()

    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, value):
        if self._progressbar_tqdm is None:
            raise ProgressBarNotCreatedException("Created a progressbar before assigning.")

        if value != self.progress:
            self._progress = value
            self._progressbar_tqdm.n = value
            self._progressbar_tqdm.refresh()
            self.notify_update()

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        if value != self.desc:
            self._desc = value
            self._progressbar_tqdm.set_description(value)
            self.notify_update()

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, value):
        self._message = value
        self.notify_update()

    def _asdict(self):
        """Return a dict representation of the current progressbar."""
        with self._cond:
            if self.id is None:
                return None

            return {
                'progressbar': {
                    'id': self.id.hex,
                    'message': self.message,
                    'status': self.status,
                    'desc': self.desc,
                    'progress': self.progress
                }
            }

    def create_progressbar(self, desc, progress=0,  message="", status="", total=100):
        import sys
        self._id = uuid.uuid4()
        _LOG.debug('Displaying progress (%s): "%s"', self.id, 0)

        self._progress = progress
        self._desc = desc+":"
        self._message = message
        self._status = status
        self._progressbar_tqdm = tqdm(
            file=sys.stdout,
            total=total,
            desc=desc,
            ncols=80,
            bar_format="{desc}|{bar}|{percentage:3.0f}%",
            smoothing=0.5
        )
        self.notify_update()
        return self.id

    def tearDown(self):
        self._progressbar_tqdm.close()
        self._progressbar_tqdm = None
        self._id = None
        self.notify_update()
