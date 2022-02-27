DOIT_CONFIG = {
    'verbosity': 2
}

def task_cache():
    '''removes all __pycache__, .pytest_cache, and .doit.db files and directories'''
    return {
        'actions': [
            "find . -type d -name '__pycache__' | xargs rm -rf",
            "find . -type d -name '.pytest_cache' | xargs rm -rf",
            "rm .doit.db",
            "clear"
        ]
    }

def task_test():
    '''runs all tests'''
    return {
        'actions': [
            "unbuffer pytest -c tests/pytest.ini"
        ]
    }

def task_cov():
    '''outputs coverage report for test suite'''
    return {
        'actions': [
            "unbuffer pytest -c tests/pytest.ini --cov src/"
        ]
    }

def task_lint():
    '''runs linter on all .py files in src'''
    return {
        'actions': [
        'find src -type f -name "*.py" | xargs pylint'
        ]
    }
