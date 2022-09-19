#!/usr/bin/python3
"""Input Output"""


Student = __import__('10-student').Student
def reload_from_json(self, json):
    self.json = json
    for i in json:
        setattr(self, i, json[i])
