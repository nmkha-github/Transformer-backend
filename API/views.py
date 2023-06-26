from rest_framework.decorators import api_view
from rest_framework.response import Response

from Transformer.model import Transformer

# Create your views here.


@api_view(['GET'])
def getData(request):
    return Response({'abc': "abc"})


@api_view(['POST'])
def predict(request):
    
    text = ""
    try:
        text = request.data['content']  # @param {type:"string"}
    except:
        return Response("Data must have content field")
    model = Transformer()
    model.load_model()
    summary_text = model.summarize(text)
    return Response({'summary_text': summary_text})
