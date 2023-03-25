from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q

# local import
from .models import Contact, Company
from .serializers import *

# API to handle all company request
class CompanyView(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

class ContactView(APIView):
    # Get Request
    def get(self, request):

        # Fetching customer detail by mobile number, email or instagram data passed in url query
        if 'email' in request.GET.keys() or 'mobile_number' in request.GET.keys() or 'instagram' in request.GET.keys():
            mobile = request.GET['mobileNumber'] if 'mobileNumber' in request.GET.keys() else ""
            email = request.GET['email'] if 'email' in request.GET.keys() else ""
            insta = request.GET['instagram'] if 'instagram' in request.GET.keys() else ""
            
            # Fetching data from model
            res = Contact.objects.filter(Q(mobile_number=mobile) | Q(email=email) | Q(instagram_handle=insta))

            # serializing data
            data = ContactSerializer(res[0])

            return Response(data.data,status=status.HTTP_200_OK)
        
        # if no params are pass then all contact will be fetched
        contacts = Contact.objects.all()
        
        # serializing data
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    # Post Request
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactDetailView(APIView):
    # Getting contact detail from pk
    def get_object(self, pk):
        try:
            return Contact.objects.get(pk=pk)
        except Contact.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    
    # Put request to update contact detail
    def put(self, request, pk):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete request to delete contact detail
    def delete(self, request, pk):
        contact = self.get_object(pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# API to Fetch All the Customer of Specific Company
class SearchCustomerByCompany(APIView):

    def get(self,request,name):

        # Filtering many to many field
        res = Contact.objects.filter(companies__name__icontains=name).values()
        return Response(res)
