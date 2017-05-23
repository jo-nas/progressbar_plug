class plugs(object):
    class FrontendAwareBasePlug(object):
        def __init__(self):
            self.notifyed = 0

        def notify_update(self):
            self.notifyed += 1

