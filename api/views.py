from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import googleapiclient.discovery

@csrf_exempt
def snippet_list(request):
    if request.method == 'GET':
        return JsonResponse(obj, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        api_service_name = "youtube"
        api_version = "v3"
        # API key
        DEVELOPER_KEY = "AIzaSyAK-YNx0FUq9UoRxlNpTUHuyHrBvaOxNWk"
        # API client
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, developerKey = DEVELOPER_KEY)
        # 'request' variable is the only thing you must change
        # depending on the resource and method you need to use
        # in your query
        #query = "Chelsea vs Manchester City"
        query = data["query"]
        #date = "08/18/2024"
        date = data["date"]
        items = date.split("/")
        month, day, year = items[0], items[1], items[2]

        request = youtube.search().list(
            part="snippet",
            maxResults=25,
            publishedAfter=year + "-" + month + "-" + day + "T00:00:00+00:00",
            publishedBefore=year + "-" + month + "-" + day +"T23:59:00+00:00",
            q=query
        )

        """request = youtube.search().list(
            part="snippet",
            maxResults=25,
            q=query
        )"""

        #print(year, month, day)
        #val = input()
        """request = youtube.search().list(
            part="snippet",
            maxResults=25,
            publishedAfter=year + "-" + month + "-" + day + "T00:00:00Z",
            q=query
        )"""
        """request = youtube.search().list(
            part="snippet",
            maxResults=25,
            publishedAfter="2024-08-19T00:00:00Z",
            q="Atletico Madrid vs Villareal ESPN FC"
        )"""
        # Query execution
        response = request.execute()

        if len(response['items']) < 1:
            print("Running request without date filter")
            request = youtube.search().list(
                part="snippet",
                maxResults=25,
                q=query
            )
            response = request.execute()

        # Print the results
        video_id = response['items'][0]['id']['videoId']
        url_prefix = "https://www.youtube.com/watch?v="
        url = url_prefix + video_id
        obj = {
            "vid": video_id
        }
        return JsonResponse(obj, status=201)

@csrf_exempt
def snippet_detail(request, pk):

    if request.method == 'GET':
        obj = {
            "key1": pk,
        }
        return JsonResponse(obj)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        return JsonResponse(data, status=200)