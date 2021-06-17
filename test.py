import unittest
import application 
import pyrebase

class TestHello(unittest.TestCase):

    def setUp(self):
        application.application.testing = True
        self.app = application.application.test_client()


    def test_hello(self):
        rv = self.app.get('/')
        firebaseConfig = {
    "apiKey": "AIzaSyA7C4qwXDACuVNNJjbyHpGi_mDzuvfYZQQ",
    "authDomain": "aire-ed2c0.firebaseapp.com",
    "databaseURL": "https://aire-ed2c0-default-rtdb.firebaseio.com/",
    "projectId": "aire-ed2c0",
    "storageBucket": "aire-ed2c0.appspot.com",
    "messagingSenderId": "885283015139",
    "appId": "1:885283015139:web:9b0adc7e08b87443ddb8d6",
    "measurementId": "G-65KNQLBSBX"
    };
        firebase = pyrebase.initialize_app(firebaseConfig)

        db = firebase.database()
        users = db.child("User_info").get()
        if users is not None:
            self.assertEqual(rv.status, '200 OK')






if __name__ == '__main__':
    import xmlrunner

    with open('test-reports/output.xml', 'a') as output:
        unittest.main(
            testRunner=xmlrunner.XMLTestRunner(output=output),
            failfast=False, buffer=False, catchbreak=False)


    #unittest.main()