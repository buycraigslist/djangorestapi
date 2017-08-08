from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import photo_card
from api.serializers import PhotoCardSerializer


@api_view(['GET', 'POST'])
def photo_card_list(request, format=None):
    """
    List all photo cards, or create a new photo card.
    """
    if request.method == 'GET':
        photo_cards = photo_card.objects.all()
        serializer = PhotoCardSerializer(photo_cards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PhotoCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def photo_card_detail(request, pk, format=None):
    """
    Retrieve, update or delete a photo card instance.
    """
    try:
        photo_card_ = photo_card.objects.get(pk=pk)
    except photo_card.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PhotoCardSerializer(photo_card_)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PhotoCardSerializer(photo_card_, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        photo_card_.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)