from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from allauth.account.views import LoginView, SignupView


# Create your views here.
class AjaxLoginView(LoginView):
    def is_ajax(self):
        return self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    def form_valid(self, form):
        if self.is_ajax():
            print(1)
            print(self.request.user)
            return JsonResponse({'logged_in': True})
        return super().form_valid(form)
    def form_invalid(self, form):
        if self.is_ajax():
            print(2)
            return JsonResponse({'logged_in': False, 'form_errors': form.errors})
        # return super().form_invalid(form)
        
        
class AjaxSignupView(SignupView):
    def is_ajax(self):
        return self.request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
    def form_valid(self, form):
        response = super().form_valid(form)
        if self.is_ajax():
            print('ajax')
            return redirect('auth_reg:login')
        print('not')
        return response

    def form_invalid(self, form):
        if self.is_ajax():
            return JsonResponse({'form_errors': form.errors})
    
def view_login(request):
    return render(request, 'auth_reg/user_login.html')

def view_signup(request):
    return render(request, 'auth_reg/user_signup.html')