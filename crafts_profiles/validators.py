from django.core.validators import RegexValidator

# Custom validator for the username field
username_validator = RegexValidator(
    regex=r'^[\w.@+-]+$',
    message='Enter a valid username. This value may contain only letters, numbers, and @/./+/-/_ characters.',
    code='invalid_username'
)