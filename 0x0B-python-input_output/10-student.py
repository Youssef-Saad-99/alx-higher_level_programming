#!/usr/bin/python3
"""contains the class Student"""


class Student:
        """Representation of a student class"""
            def __init__(self, first_name, last_name, age):
                        """initialires the student"""
                                self.first_name = first_name
                                        self.last_name = last_name
                                                self.age = age

                                                    def to_json(self, attrs=None):
                                                                """retrieves a dictionary representation of a Student instance"""
                                                                        try:
                                                                                        for att in attrs:
                                                                                                            if type(att) is not str:
                                                                                                                                    return self.__dict__
                                                                                                                                        except:
                                                                                                                                                        return self.__dict__
                                                                                                                                                            my_dict = dict()
                                                                                                                                                                    for key, value in self.__dict__.items():
                                                                                                                                                                                    if key in attrs:
                                                                                                                                                                                                        my_dict[key] = value
                                                                                                                                                                                                                return my_dict
