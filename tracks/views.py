from django.shortcuts import render
from tracks.models import Track

def track_index(request):
    tracks = Track.objects.all()
    context = {
        'tracks': tracks
    }
    return render(request, 'track_index.html', context)

def track_detail(request, pk):
    track = Track.objects.get(pk=pk)
    context = {
        'track': track
    }
    return render(request, 'track_detail.html', context)
