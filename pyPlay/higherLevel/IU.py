# -*- coding: UTF-8 -*-
class Person():
    def __init__(self, name, score, **kw):
        self.name = name
        self.score = score
        for n, v in kw.iteritems():
            setattr(self, n, v)
