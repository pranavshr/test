import unittest

class TestSequence(unittest.TestCase):
	def setUp(self):
	#Gets called before EACH test
		pass
	def tearDown(self):
	#Gets called after EACH test
		pass

	#The Tests:
	def test_add_simple(self):
		self.assertEqual(1, 1)

if __name__=="__main__":
	unittest.main()


#test
