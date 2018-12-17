from django.shortcuts import render
import pyopenstates as po
import requests
from .forms import inputForm
# Create your views here.
def bio (request):

    # recieve value input and store it in estate
    estate = 'NY'
    if request.method == 'POST':
        estate=request.POST.get('name')
        print(request.POST)


    #store legislator API in data to iterate through
    po.set_api_key('001b2e03-a7f3-49b5-a7ed-99afe9e918d6')
    data=po.search_legislators(state=estate)
    form = inputForm()

    #iterate through list of dictionaries in data and store the specific keys in a list
    list= []
    for entry in data:

    #   print(entry['full_name'],entry['offices'][0]['email'])
        dic ={ 'full_name':entry['full_name'],
        'chamber':entry['chamber'],
            'district':entry['district'],
            'party':entry['party'] ,
            'email':entry['offices'][0]['email']}
        list.append(dic)

    #output the full name and email of all legislator in the data dictionary
    return render(request, 'bios/bio.html',{ 'list':list, 'form': form })
