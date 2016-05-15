#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import math


# ConcreteImplementor 1/2
class SmsSoapWebService(object):
    def send_message(self, message_body, length):
        print('Sms soap web service sent message: {}: with {} count'.format(message_body, length))


# ConcreteImplementor 2/2
class SmsRestWebService(object):
    def send_message(self, message_body, length):
        print('Sms rest web service sent message: {}: with {} count'.format(message_body, length))


# Refined Abstraction
class SmsNotify(object):
    def __init__(self, message_body, sms_api):
        self._message_body = message_body
        self._sms_api = sms_api
        self._length = 0

    # low-level i.e. Implementation specific
    def send(self):
        self._sms_api.send_message(self._message_body, self._length)

    # high-level i.e. Abstraction specific
    def calculate_length(self):
        self._length = int(math.ceil(len(self._message_body) / 140))


if __name__ == '__main__':
    messages = (
        SmsNotify('Hello World', SmsSoapWebService()),
        SmsNotify('Hello world !!!', SmsRestWebService())
    )

    for message in messages:
        message.calculate_length()
        message.send()
