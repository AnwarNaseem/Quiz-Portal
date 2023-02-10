from app import application
from src.apis import *
from src.setup import add_questions

"""
[Driver Module] : It is responsible for stating the server for application for apis serving
"""
if __name__ == "__main__":
    
    try:
        add_questions()
    except Exception as e:
        pass
    
    application.run(debug=True, port=8000)
    
    
    