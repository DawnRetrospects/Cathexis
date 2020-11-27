import os
from code.main import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(
        # host=app.config.get('HOST', '0.0.0.0'), 
        port=app.config.get('PORT', 8000)
    )