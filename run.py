""" The app's Entry Point"""
#! /usr/bin/env python
from app import APP
import os


if __name__ == '__main__':
	APP.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
	port = int(os.environ.get('PORT', 5000))
	APP.run('', port=port,debug=True)
    