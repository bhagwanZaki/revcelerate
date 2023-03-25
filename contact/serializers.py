
from rest_framework import serializers
from .models import Contact, Company

# Company serializer
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name']

# Contact serializer
class ContactSerializer(serializers.ModelSerializer):

    # companies attribute
    companies = CompanySerializer(required=False,many=True)

    class Meta:
        model = Contact
        fields = ('id', 'name', 'mobile_number', 'address', 'email', 'instagram_handle','companies')

    # Create function
    def create(self, validated_data):

        # Popping companies data
        company_names = validated_data.pop('companies')

        # Creating Contact model
        contact = Contact.objects.create(**validated_data)

        # Adding companies to contact
        companies = []
        for name in company_names:
            company, _ = Company.objects.get_or_create(name=name['name'])
            companies.append(company)
        contact.companies.set(companies)
        return contact

    # Update function
    def update(self, instance, validated_data):

        # Retreiving validated data
        company_names = validated_data.pop('companies', [])
        instance.name = validated_data.get('name', instance.name)
        instance.mobile_number = validated_data.get('mobile_number', instance.mobile_number)
        instance.address = validated_data.get('address', instance.address)
        instance.email = validated_data.get('email', instance.email)
        instance.instagram_handle = validated_data.get('instagram_handle', instance.instagram_handle)

        # updating company data
        if company_names:
            companies = []
            for name in company_names:
                company, _ = Company.objects.get_or_create(name=name['name'])
                companies.append(company)
            instance.companies.set(companies)

        # Updating instance
        instance.save()
        return instance
