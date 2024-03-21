
# class CustomeMiddleware:

#     def __init__(self,get_response):
#         self.get_response = get_response
#         self.num_exceptions = 0

#     def __call__(self,request):
#         print("Hi there ")      
#         response = self.get_response(request)

#         return response

# def process_view(self,request,view_func,view_args,view_kwargs):
#     prin(f"view name: {view_func.__name__}")


# def process_exception(self,request,exception):
#     self.num_exceptions += 1
#     print(f"Exception count: {self.num_exceptions} ")


# class CustomeMiddleware:

#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.context_response = {
#             "msg": {"Be careful!": "No way Bro"}
#         }


#     def __call__(self, request):

#         response = self.get_response(request)

#         return response


# def process_template_response(self,request,response):
#     response.context_data["new_data"] = self.context_response
#     return response


# from rest_framework.authtoken.models import Token
# from django.utils import timezone
# from datetime import datetime
# class CustomeMiddleware:

#     def __init__(self, get_response):
#         self.get_response = get_response
#         self.num_exceptions = 0
#         self.context_response = {
#             "msg": {"Be careful!": "No way Bro"}
#         }
    
#     def stats(self,os_info):
#         if "mac" in os_info:
#             newstats.objects.all().update(mac=F('mac') + 1)
#         elif "windows" in os_info:
#             newstats.objects.all().update(windows=F('windows') + 1)
#         elif "Android" in os_info:
#             newstats.objects.all().update(android=F('android') + 1)
#         else:
#             newstats.objects.all().update(oth=F('oth') + 1)








#     def __call__(self, request):
#         print(request.path)
#         print(request.headers["HOST"])
#         print(request.headers["Accept-Language"])
#         print(request.META["REQUEST_METHOD"])
#         print(request.META["HTTP_USER_AGENT"])

        




#         response = self.get_response(request)

#         return response


# def process_template_response(self, request, response):
#     response.context_data["new_data"] = self.context_response
#     self.num_exceptions += 1
#     print(f"Exception coun: {self.num_exceptions}")
#     return response




