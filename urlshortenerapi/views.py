from rest_framework import viewsets
from django.http import HttpResponse, JsonResponse
from .serializers import URLSerializer, URLVisitSerializer, CustomURLSerializer
from .models import URL, URLVisit, CustomURL
from django.forms.models import model_to_dict
from django.db.models import Q

class URLViewSet(viewsets.ModelViewSet):
    queryset = URL.objects.all().order_by('original_name')
    serializer_class = URLSerializer

class URLVisitViewSet(viewsets.ModelViewSet):
    queryset = URLVisit.objects.all().order_by('date_visited')
    serializer_class = URLVisitSerializer

class CustomURLViewSet(viewsets.ModelViewSet):
    queryset = CustomURL.objects.all().order_by('created_date')
    serializer_class = CustomURLSerializer

# TODO: Refactor this silly aggregation to Pandas or other library to perform GroupBy
def _process_visits(url_visits):
    result = {"total": 0, "grouped": {}}

    for visit in url_visits:
        key = str(visit.date_visited)[0: 10]  # This is error prone and should use datetime or Arrow
        if key in result["grouped"]:
            result["grouped"][key] += 1
        else:
            result["grouped"][key] = 1
        result["total"] += 1

    return result

# There's too much logic in this view since their point is to solely render data.
# It should live in a Controller or Middleware elsewhere.
def show_url_stats(request, url_slug):
    matching_shortened_url = URL.objects.filter(Q(shortened_version=url_slug) | Q(original_name=url_slug)).first()
    matching_custom_url = CustomURL.objects.filter(name=url_slug).first()

    if matching_custom_url:
        matching_shortened_url = matching_custom_url.parent_url

    if matching_shortened_url:
        new_url_visit = URLVisit(url=matching_shortened_url)
        new_url_visit.save()
        url_visits = URLVisit.objects.filter(url=matching_shortened_url)

        url = model_to_dict(matching_shortened_url)
        url["visits"] = _process_visits(url_visits)

        return JsonResponse(url)
    else:
        #TODO: Place method below in proper 404 template
        return HttpResponse(f"<h1>No URL found for: {url_slug}.  Consider making a POST request </h1>")
