#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from app import create_app

# config_name = "development"

config_name = os.getenv('APP_SETTINGS') 
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
