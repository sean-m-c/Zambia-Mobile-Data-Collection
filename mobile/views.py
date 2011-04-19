from django.http import HttpResponse
from xforms.models import xform_received
from django.utils import simplejson

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

def submission(request) :
    #decoded_json = json.loads(json_string)
    #return render_to_response('submission.html',{'results':decoded_json['Result']})

    if request.method == 'POST':
        json_data = simplejson.loads(request.raw_post_data)
    try:
        data = json_data['data']
    except KeyError:
        HttpResponseServerError("Malformed data!")
    HttpResponse("Got json data")
    print("View works")
