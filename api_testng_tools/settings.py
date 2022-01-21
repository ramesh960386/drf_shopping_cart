# settings.py

# Step-1
######################################################################################################################
INSTALLED_APPS = [
    'rest_framework',
    'rest_framework.authtoken'
]


REST_FRAMEWORK = {
   'DEFAULT_AUTHENTICATION_CLASSES': (
       'rest_framework.authentication.TokenAuthentication',
       'rest_framework.authentication.SessionAuthentication',
   ),
   'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
   ),
}

# Step-2
######################################################################################################################
# python manage makemigrations
# python manage migrate

# Step-3 Create Token in PowerShell and Copy to CLipboard using clip keyword
######################################################################################################################
# python manage.py drf_create_token <admin/any username> | clip 
# Generated token c0efa4be06a92f8b60dc4f818b30eb468041fdd7 for user admin


# Step-4
# in using Curl
######################################################################################################################
# curl http://localhost:8000/api/cart-items/ -H 'Authorization: Token c0efa4be06a92f8b60dc4f818b30eb468041fdd7'
# or
# curl -X GET http://localhost:8000/api/cart-items/ -H "Authorization: token c0efa4be06a92f8b60dc4f818b30eb468041fdd7"

# in using Postman
######################################################################################################################
# Key: Authorization
# Value: token c0efa4be06a92f8b60dc4f818b30eb468041fdd7
# Add to: Header