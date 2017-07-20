import wia
import unittest2
import time
import os

def on_connect():
    print("on_connect called in test")

class StreamTest(unittest2.TestCase):

    @classmethod
    def setUpClass(cls):
        wia.secret_key = 'u_sk_0kl0z2W45SEs1SWk7Bu0hDxe'


    def test_stream_connect(self):
        # wia.Stream.client.on_connect = on_connect
        wia.Stream.connect()
        count = 0
        while count < 6:
            time.sleep(0.5)
            count += 1
            if wia.Stream.connected:
                break
        if not wia.Stream.connected:
            raise Exception("Unable to connect")

if __name__ == '__main__':
    unittest2.main()
