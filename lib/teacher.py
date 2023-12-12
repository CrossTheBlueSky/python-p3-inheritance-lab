#!/usr/bin/env python

from user import User

import random

class Teacher(User):

    def __init__(self, first, last):
        self.knowledge = ["History", "Maths"]
        super().__init__(first, last)
        

    def teach(self):
        return random.choice(self.knowledge)