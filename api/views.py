from rest_framework.generics import ListAPIView
from books.models import Book
from .serializers import BookSerializers

# Create your views here.
class BookAPIView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers