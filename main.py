import re
import unittest
import subprocess
from time import sleep


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_waitforreboot(self):
        subprocess.call("adb reboot", shell=True)
        subprocess.call("adb wait-for-device")
        count = 300
        while count > 0:
            sleep(1)
            #ps = subprocess.Popen("adb shell getprop dev.bootcomplete", stdout=subprocess.PIPE)
            #out, err = ps.communicate()
            result = subprocess.check_output(["adb","shell","getprop","dev.bootcomplete"], text=True).strip()
            print(result)
            if result == "1":
                print("Device Rebooted successfully")
                break
            count = count - 1

        if count == 0:
            print("Device not rebooted successfully ")





if __name__ == '__main__':
    unittest.main()
