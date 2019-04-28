from django.utils.deprecation import MiddlewareMixin
import datetime
from user import models

class myMiddleware(MiddlewareMixin):

    def process_request(self, request):

        print("This is process_request : ",datetime.datetime.now())
        print(
            models.userprofile.objects.all()
        )

        return None