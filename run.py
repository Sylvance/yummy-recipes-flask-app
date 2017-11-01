""" The app's Entry Point"""
#! /usr/bin/env python
from app import APP
import oS


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    APP.run('', port=port,debug=True)
    