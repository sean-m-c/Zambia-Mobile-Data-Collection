from xform_manager import parse_xform

def parse_xform_handler(sender, **kwargs):
    """signal intercept for parse_xform"""
    instance = kwargs['instance']
    print "something works"


parse_xform.connect(parse_xform_handler)