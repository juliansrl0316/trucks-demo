from django.views import View
from .scraping import GetHtmlInfo
from django.http import JsonResponse

class TruckRouteView(View):
    def get(self, request):
        return JsonResponse(GetHtmlInfo(), safe=False)
