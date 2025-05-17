
from hash_table import *
import unittest

class TestHashTable(unittest.TestCase):
    def setUp(self):
        self.hs = create_hash_table(10)

    def test_create_hash_table(self):
        hs = create_hash_table(5)
        self.assertEqual(hs['size'], 5)
        self.assertEqual(len(hs['table']), 5)
        self.assertEqual(hs['count'], 0)
        self.assertTrue(all(x is None for x in hs['table']))
    
    def test_find_key(self):
        self.assertEqual(find_key('абв'), 1)  
        self.assertEqual(find_key('вгд'), 69)  
        self.assertEqual(find_key('яяя'), 1088)  
        with self.assertRaises(IndexError):
            find_key('а')  
        with self.assertRaises(IndexError):
            find_key('')  

    def test_hash1(self):
        key = find_key('абв') 
        self.assertEqual(hash1(key, self.hs), 1 % 10) 
        key = find_key('вгд') 
        self.assertEqual(hash1(key, self.hs), 69 % 10) 

    def test_hash2(self):
        key = find_key('абв')  
        self.assertEqual(hash2(key, self.hs), 1 + (1 % 9))  
        key = find_key('вгд') 
        self.assertEqual(hash2(key, self.hs), 1 + (69 % 9))  

    def test_insert_no_collision(self):
        insert(self.hs, 'абв', 'value1')
        self.assertEqual(self.hs['count'], 1)
        self.assertEqual(self.hs['table'][1], {'абв': 'value1'})
        self.assertTrue(all(x is None for x in self.hs['table'][:1] + self.hs['table'][2:]))

    def test_insert_with_collision(self):
        insert(self.hs, 'абв', 'value1')  
        insert(self.hs, 'баа', 'value2') 
        self.assertEqual(self.hs['count'], 2)
        self.assertEqual(self.hs['table'][1], {'абв': 'value1'})
        self.assertEqual(self.hs['table'][3], {'баа': 'value2'})

    def test_find(self):
        insert(self.hs, 'абв', 'value1')
        self.assertEqual(find(self.hs, 'абв'), 'value1')
        insert(self.hs, 'баа', 'value2') 
        self.assertEqual(find(self.hs, 'баа'), 'value2')
        with self.assertRaises(KeyError):
            find(self.hs, 'вгд') 
 
    def test_deleting(self):
        insert(self.hs, 'абв', 'value1')
        insert(self.hs, 'баа', 'value2')
        deleting(self.hs, 'абв')
        self.assertEqual(self.hs['count'], 1)
        self.assertIsNone(self.hs['table'][1])
        self.assertEqual(self.hs['table'][3], {'баа': 'value2'})
        deleting(self.hs, 'баа')
        self.assertEqual(self.hs['count'], 0)
        self.assertIsNone(self.hs['table'][3])
        deleting(self.hs, 'вгд') 
        self.assertEqual(self.hs['count'], 0)

    def test_deleting_2(self):
        insert(self.hs, 'абв', 'value1')
        insert(self.hs, 'баа', 'value2')
        insert(self.hs, 'баааа', 'value3')
        insert(self.hs, 'абыы', 'value4')
        print(self.hs)
        deleting(self.hs, 'абыы')
        deleting(self.hs, 'баа')
        self.assertEqual(self.hs['count'], 2)

    def test_update_hash_table(self):
        insert(self.hs, 'абв', 'value1')
        insert(self.hs, 'баа', 'value2')
        new_hs = update_hash_table(self.hs)
        self.assertEqual(new_hs['size'], 20)
        self.assertEqual(new_hs['count'], 2)
        self.assertEqual(find(new_hs, 'абв'), 'value1')
        self.assertEqual(find(new_hs, 'баа'), 'value2')

if __name__ == '__main__':
    unittest.main()