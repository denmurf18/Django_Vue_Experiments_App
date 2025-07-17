from django.shortcuts import render
from django.http import JsonResponse
import json

def vue_page(request):
    context = {
        'vue_data': json.dumps({
            'message': 'Hi There from Django!'
        })
    }
    print('the context is ', context)
    return render(request, 'core/vue_page.html', context)



def api_data(request):
    data = {
        'message': 'JSON from Django!'
    }
    return JsonResponse(data)
