from django.http import HttpResponse
from xforms.models import xform_received

def home(request) :
    return "Here the home page."


# define a listener
def handle_submission(sender, **args):
    submission = args['submission']
    xform = args['xform']

    #if xform.keyword == 'survey' && not submission.has_errors:
      # .. do your own logic here ..

# then wire it to the xform_received signal
    xform_received.connect(handle_submission)