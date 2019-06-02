# coding: utf-8

from . import api
from ihome import db
import logging
from flask import current_app


@api.route('/index/')
def index():
    # logging.error("")  # 错误级别
    # logging.warning("")  # 警告级别
    # logging.info("")   # 消息调试级别
    # logging.debug("")  # 调试级别
    current_app.logger.error('error msg')
    current_app.logger.warning('warning msg')
    current_app.logger.info('info msg')
    current_app.logger.debug('debug msg')
    return 'index page'
