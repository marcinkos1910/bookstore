#Signup
1. Model - User
2. Forms - CustomUserCreationForm
3. View:
   * Create file at 'accounts' views.py
   * Create class and inherit from generic.CreateView
4. Templates:
   * Create signup.html -> templates/registration
5. Create urls at accounts app
   * endpoint signup/, name='signup'
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

