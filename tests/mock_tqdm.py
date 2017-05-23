class tqdm(object):
    def __init__(self, file, total, desc, ncols, bar_format, smoothing):
        self.refreshed = 0
        self.desc = desc
        self.n = 0
        self.closed = False

    def refresh(self):
        self.refreshed += 1

    def set_description(self, value):
        self.desc = value

    def close(self):
        self.closed = True

