import time

class RequestTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # So'rov kelgan vaqtni belgilaymiz
        start_time = time.time()

        # So'rovni keyingi qatlamga (view'ga) yuboramiz
        response = self.get_response(request)

        # Javob qaytgach, ketgan umumiy vaqtni hisoblaymiz
        duration = time.time() - start_time

        # Konsolga manzil va vaqtni chiqaramiz
        print(f"⏱️ [SO'ROV] Manzil: {request.path} | Metod: {request.method} | Vaqt: {duration:.4f} soniya")

        return response