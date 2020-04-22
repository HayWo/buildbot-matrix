from __future__ import absolute_import
from __future__ import print_function

from twisted.internet import defer
from twisted.python import log

from buildbot.process.properties import Interpolate
from buildbot.process.properties import Properties
from buildbot.process.results import CANCELLED
from buildbot.process.results import EXCEPTION
from buildbot.process.results import FAILURE
from buildbot.process.results import RETRY
from buildbot.process.results import SKIPPED
from buildbot.process.results import SUCCESS
from buildbot.process.results import WARNINGS
from buildbot.reporters import http
from buildbot.util import httpclientservice

class MatrixStatusPush(http.HttpStatusPushBase):
    name = "MatrixStatusPush"
    neededDetails = dict(wantProperties=True)
    
