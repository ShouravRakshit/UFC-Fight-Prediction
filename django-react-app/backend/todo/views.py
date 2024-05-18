from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializers
from rest_framework import status
from .ml.your_ml_script import predict

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializers

    @action(detail=False, methods=['get'])
    def search(self, request):
        query = request.query_params.get('q', None)
        if query is not None:
            queryset = self.queryset.filter(title__icontains=query)
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        return Response([])
    
    @action(detail=False, methods=['post'])
    def add_todo(self, request):
        title = request.data.get('title')
        description = request.data.get('description')
        completed = request.data.get('completed', False)  # Default to False if not provided
        if title and description is not None:
            todo = Todo.objects.create(title=title, description=description, completed=completed)
            serializer = TodoSerializers(todo)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': 'Title and Description are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def predict(self, request):
        input_data = request.data.get('input_data')
        if input_data is not None:
            try:
                input_data = list(map(float, input_data.split(',')))  # Assuming input is comma-separated
                prediction = predict(input_data)
                return Response({'prediction': prediction}, status=status.HTTP_200_OK)
            except ValueError:
                return Response({'error': 'Invalid input data format'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': 'Input data is required'}, status=status.HTTP_400_BAD_REQUEST)