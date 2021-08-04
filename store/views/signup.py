from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.views import View

from store.models.customer import Customer


class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone_number = postData.get('phone_number')
        email = postData.get('email')
        password = postData.get('password')

        # validation

        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone_number,
            'email': email,

        }

        error_message = None

        customer = Customer(first_name=first_name, last_name=last_name,
                            phone_number=phone_number, email=email, password=password)

        error_message = self.validateCustomer(customer)

        # saving
        if not error_message:
            print(first_name, last_name, phone_number, email, password)
            customer.password = make_password(customer.password)

            customer.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }

            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if not customer.first_name:
            error_message = "First Name Required !!"
        elif len(customer.first_name) < 4:
            error_message = "First Name Must be minimum 4 character Long"
        elif not customer.last_name:
            error_message = "Last Name Required !!"
        elif len(customer.last_name) < 1:
            error_message = "Last Name Must be minimum 1 character Long"
        elif not customer.phone_number:
            error_message = 'Phone Number Required'
        elif len(customer.phone_number) < 10:
            error_message = "Phone Number Must be 10 numbers long"
        elif len(customer.password) == 0:
            error_message = "Enter the Password"
        elif len(customer.password) < 6:
            error_message = "Password Must be 6 Character long"
        elif len(customer.email) < 5:
            error_message = "Enter Valid Email Address"
        elif customer.isExists():

            error_message = 'Email Address Already Registered'

        return error_message
