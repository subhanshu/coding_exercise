import unittest
from start import  download_file, upload_file
file_id=""
class testGDriveFunctions(unittest.TestCase):
    def test_upload(self):

        self.assertIsInstance(upload_file('sample_excel.xlsx'), unicode)
        self.assertRaises(IOError,upload_file,"non_exixtent_file")

    def test_download(self):
        self.assertEqual(download_file("1u77jtpjXhE4h7hAoglBidtoEetHOxQCu63VXA-Sa_OE"), True)
        self.assertRaises(TypeError, download_file, 123)
