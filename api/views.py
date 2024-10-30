from .serializers import PlanSerializer
from .models import devPlanning
from .serializers import PlanSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView,UpdateAPIView

class PlanListView(ListAPIView):
    queryset = devPlanning.objects.all()
    serializer_class = PlanSerializer
    
class PlanCreateView(CreateAPIView):
    queryset = devPlanning.objects.all()
    serializer_class = PlanSerializer

class PlanDestroyView(DestroyAPIView):
    queryset = devPlanning.objects.all()
    serializer_class = PlanSerializer  
      
class PlanupdateView(UpdateAPIView):
    queryset = devPlanning.objects.all()
    serializer_class = PlanSerializer    