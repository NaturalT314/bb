from django.shortcuts import render, redirect
from django.views import View
from .models import Frame, Lens
from django.http import JsonResponse
import json

class FrameView(View):
    def get(self, request):
        frames = Frame.objects.filter(status="active")
        serialized_frames = [{'id': frame.id,'name': frame.name,'description': frame.description, 'status': frame.status,'stock': frame.stock, 'price_usd': frame.price_usd, "price_gbp": frame.price_gbp, "price_eur": frame.price_eur, "price_jod": frame.price_jod, "price_jpy": frame.price_jpy} for frame in frames]
        return JsonResponse({"Frames": serialized_frames})
    
    def post(self, request):
        try:
            frame_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data in request body"}, status=400)
        try:
            frame = Frame(**frame_data)
            frame.full_clean()
            frame.save()
        except KeyError as e:
            return JsonResponse({"error": f"Invalid field provided: {e}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Failed to create frame: {str(e)}"}, status=500)
        
        return JsonResponse({"msg": "Frame created successfully", "data": frame_data}, status=201)
    

class LensView(View):
    def get(self, request):
        lenses = Lens.objects.all()
        serialized_lenses = [{'id': lens.id,'colour': lens.colour,'description': lens.description, 'prescription_type': lens.prescription_type,'lens_type': lens.lens_type,'stock': lens.stock, 'price_usd': lens.price_usd, "price_gbp": lens.price_gbp, "price_eur": lens.price_eur, "price_jod": lens.price_jod, "price_jpy": lens.price_jpy} for lens in lenses]
        return JsonResponse({"Lenses": serialized_lenses})

    def post(self, request):
        try:
            lens_data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data in request body"}, status=400)
        try:
            lens = Lens(**lens_data)
            lens.full_clean()
            lens.save()
        except KeyError as e:
            return JsonResponse({"error": f"Invalid field provided: {e}"}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Failed to create frame: {str(e)}"}, status=500)
        
        return JsonResponse({"msg": "Frame created successfully", "data": lens_data}, status=201)
   