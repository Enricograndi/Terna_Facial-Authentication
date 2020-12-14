import unittest
import sqlite3
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__))))))
import dbmanager as db

class TestInput(unittest.TestCase):
    def setUp(self):
        #sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__))))))
        db.open_or_create_db("../../facialauthentication_package/data/database.db")

     # smoke test: valid inputs
    def test_correct_user(self):
        # we select some valid inputs, for which the output is known
        self.assertEqual(db.check_password("totti","totti"), True)

 
if __name__ == '__main__':
    unittest.main()
    