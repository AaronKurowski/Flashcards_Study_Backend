from .models import Flashcard
from .models import Collection
from .serializers import CollectionSerializer
from .serializers import FlashcardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404


# Create your views here.
class CollectionList(APIView):

    def get(self, request):
        collection = Collection.objects.all()
        serializer = CollectionSerializer(collection, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# gets collection by id
class CollectionDetail(APIView):

    def get_collection(self, collection_id):
        try:
            return Collection.objects.get(pk=collection_id)
        except Collection.DoesNotExist:
            raise Http404

    def get(self, request, collection_id):
        collection = self.get_collection(collection_id)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data)


class FlashcardList(APIView):

    def get(self, request, collection_id):
        flashcard = Flashcard.objects.filter(collection=collection_id)
        serializer = FlashcardSerializer(flashcard, many=True)
        return Response(serializer.data)

    def post(self, request, collection_id):
        serializer = FlashcardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlashcardDetail(APIView):

    def get_object(self, pk):
        try:
            return Flashcard.objects.get(pk=pk)
        except Flashcard.DoesNotExist:
            raise Http404

    def put(self, request, collection_id, card_id):
        flashcard = self.get_object(card_id)
        serializer = FlashcardSerializer(flashcard, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, collection_id, card_id):
        flashcard = self.get_object(card_id)
        flashcard.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
