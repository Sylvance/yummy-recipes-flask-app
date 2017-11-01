""" The app's Entry Point"""
#! /usr/bin/env python
from app import APP

if __name__ == '__main__':
    # set the secret key.  keep this really secret:
	APP.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
	APP.run(debug=True)
