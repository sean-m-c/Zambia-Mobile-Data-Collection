from django.http import HttpResponse
#from xforms.models import xform_received
from xml.dom import minidom
from mobile.models import Person

def home(request) :
    return "Here the home page."


def parse(request):

    #Retrieve xml from the POST
    xml = request.FILES['xml_submission_file'].read()

    #Parse the xml and then grab the values
    data = minidom.parseString(xml)

    last_name = data.getElementsByTagName('last_name')[0].firstChild.data
    #lat/long, altitude, and accuracy are in one string, so split it
    first_name = data.getElementsByTagName('first_name')[0].firstChild.data.split(" ")
    gender = data.getElementsByTagName('gender')[0].firstChild.data


    #create and save a new result object
    g = Person(last_name = last_name, first_name = first_name,
                      gender = gender)
    g.save()

    return HttpResponse(request)
