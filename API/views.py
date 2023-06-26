from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def getData(request):
    return Response({'abc': "abc"})


@api_view(['POST'])
def predict(request):
    print(request.data)
    print(request.data['content'])

    return Response({'summary_text': "abc"})
