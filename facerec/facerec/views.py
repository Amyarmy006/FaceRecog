from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
import os
import cv2
import csv
from .takeimage import TakeImage

# Correct Paths to your Haar Cascade XML and directories
haarcasecade_path = os.path.join(settings.BASE_DIR, 'haarcascade_frontalface_default.xml')
trainimage_path = os.path.join(settings.BASE_DIR, 'train_images')
csv_file_path = os.path.join(settings.BASE_DIR, 'empdetails', 'empdetails.csv')

# Function to handle the form submission and call TakeImage
def take_photo(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        name = request.POST.get('name')

        # Call the TakeImage function with the captured inputs
        TakeImage(employee_id, name, haarcasecade_path, trainimage_path, csv_file_path)

        return HttpResponse(f"Photos captured for {name} with Employee ID: {employee_id}")
    
    return render(request, 'templates/atten.html')  # Correct template path