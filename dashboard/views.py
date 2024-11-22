from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cropgrowthprediction.models import Crop, EnvironmentalData

@login_required
def dashboard(request):
    crops = Crop.objects.all()
    latest_env_data = EnvironmentalData.objects.last()

    context = {
        'crops':crops,
        'latest_env_data': latest_env_data,
    }
    print(Crop.objects.all())
    return render(request, 'dashboard/dashboard.html', context)  # Ensure the template exists

