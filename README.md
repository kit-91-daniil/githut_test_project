Implementation Test Automation Framework to testing github.com

# 1) Clone repository: 

$ clone https://github.com/kit-91-daniil/githut_test_project.git

# 2) Install virtual enviroment:

$ pip install -r requirements.txt

# 3) Open file configs/config.py 
#   write login and password of your github.com account

# 4) For launch tests use commands:

# Correct user is logged in:
$ pytest -v -m correct_user_is_logged_in --alluredir=allure_reports/

# Create repository:
$ pytest -v -m create_repository --alluredir=allure_reports/

# Rename repository
$ pytest -v -m rename_repository --alluredir=report_allure/

# Add README
$ pytest -v -m add_readme --alluredir=report_allure/

# Delete repository
$ pytest -v -m delete_repository --alluredir=report_allure/

# OR for launch all the tests
$ pytest -v --alluredir=report_allure/

# To open allure reports use command below:
$ allure serve allure_reports/