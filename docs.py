from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = ''  # URL for exposing Swagger UI (without trailing '/')
API_URL = '/static/swagger.json'  # Our API local resource

# Call factory function to create our blueprint
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    API_URL,
    config={  # Swagger UI config overrides
        'app_name': "Iris Prediction API"
    },
)