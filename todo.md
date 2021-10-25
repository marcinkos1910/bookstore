#Signup
1. Model - User
2. Forms - CustomUserCreationForm
3. View:
   1. Create file at 'accounts' views.py
   2. Create class and inherit from generic.CreateView
4. Templates:
   1. Create signup.html -> templates/registration
5. Create urls at accounts app
   1. endpoint sinup/, name='signup'
6. Connect account at main urls
7. Settings - installed apps
8. Add signup to base.html

#Crispy-forms
1. Add bootstrap
2. Pipenv install django-crispy-form
3. Pipenv install crispy-bootstrap5
4. settings -> Installed apps -> 3rd party
5. settings -> CRISPY_TEMPLATE_PACK = 'bootstrap5'
6. templates -> {% load crispy_form_tags %}
7. {{ form.as_p }} replace to {{ form|crispy }}

