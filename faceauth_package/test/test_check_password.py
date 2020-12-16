import unittest
import sqlite3
import sys
import os
import dbmanager as db

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname((
                                os.path.abspath(__file__))))))


class TestInput(unittest.TestCase):
    def setUp(self):
        # sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname((os.path.abspath(__file__))))))
        db.open_or_create_db("faceauth_package/data/database.db")

    # smoke test: valid inputs
    def test_correct_user(self):
        # we select some valid inputs, for which the output is known
        self.assertEqual(db.check_password("totti", "totti"), True)

    # invalid inputs
    def test_wrong_user(self):
        # imput of a wrong user
        self.assertEqual(db.check_password("Totto", "totti"), False)

    def test_wrong_password(self):
        # you should input wrong data
        self.assertEqual(db.check_password("Totti", "notmmypasssword"), False)

    # corner case: empty input
    def test_face_authentication_wrong_data(self):
        self.assertEqual(db.check_password("", ""), False)

if __name__ == '__main__':
    unittest.main()
