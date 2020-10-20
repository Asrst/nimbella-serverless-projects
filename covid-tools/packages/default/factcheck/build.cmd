set -e

virtualenv virtualenv
virtualenv\Scripts\activate
pip install -r requirements.txt
deactivate
