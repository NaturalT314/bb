from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import View
from adminsapi.models import Frame, Lens
from .models import Glasses, User
import json

class GlassView(View):
    def get(self, request):
        user_id = int(request.GET['user_id'])
        glasses_queryset = Glasses.objects.select_related('frame', 'lens').filter(owner = user_id)
        glasses_list = []
        for glasses in glasses_queryset:
            glasses_data = {
                'id': glasses.id,
                "owner": glasses.owner.id,
                'frame': {
                    'id': glasses.frame.id,
                    'name': glasses.frame.name,
                    'description': glasses.frame.description,
                    'status': glasses.frame.status,
                    'stock': glasses.frame.stock,
                    'price_usd': glasses.frame_price_usd,
                },
                'lens': {
                    'id': glasses.lens.id,
                    'colour': glasses.lens.colour,
                    'description': glasses.lens.description,
                    'prescription_type': glasses.lens.prescription_type,
                    'lens_type': glasses.lens.lens_type,
                    'stock': glasses.lens.stock,
                    'price_usd': glasses.lens_price_usd,
                }
            }
            glasses_list.append(glasses_data)
        return JsonResponse({"Glasses": glasses_list})
    
    def post(self, request):
        try:
            frame_id, lens_id, user_id = json.loads(request.body).values()
        except (ValueError, TypeError):
            return JsonResponse({'error': 'Invalid frame_id, lens_id, user_id'}, status=400)

        selected_frame = get_object_or_404(Frame, id=frame_id)
        selected_lens = get_object_or_404(Lens, id=lens_id)
        selected_user = get_object_or_404(User, id=user_id)

        if selected_frame.stock < 1 or selected_frame.status == 'inactive':
            return JsonResponse({'error': 'Selected frame is out of stock or inactive'}, status=400)
        if selected_lens.stock < 1:
            return JsonResponse({'error': 'Selected lens is out of stock'}, status=400)
        if not selected_user:
            return JsonResponse({'error': 'Selected user not found'}, status=400)

        frame_price_usd = selected_frame.price_usd
        lens_price_usd = selected_lens.price_usd

        glasses = Glasses.objects.create(
            frame=selected_frame,
            lens=selected_lens,
            frame_price_usd=frame_price_usd,
            lens_price_usd=lens_price_usd,
            owner=selected_user
        )

        selected_frame.stock -= 1
        selected_lens.stock -= 1

        try:
            selected_frame.save()
            selected_lens.save()
        except Exception as e:
            glasses.delete()  # Rollback creation if saving fails
            return JsonResponse({'error': str(e)}, status=500)

        return JsonResponse({'message': 'Glasses created successfully'}, status=201)