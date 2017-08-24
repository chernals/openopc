class OPCError(Exception):
    def __init__(self, txt):
        Exception.__init__(self, txt)
