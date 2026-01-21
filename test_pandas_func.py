import unittest
import pandas as pd

class TestPandas(unittest.TestCase):
    def test_basic_dataframe(self):
        """测试 Pandas DataFrame 的基本创建和访问 verify pandas installation"""
        data = {
            'name': ['Alice', 'Bob'],
            'age': [25, 30]
        }
        df = pd.DataFrame(data)
        
        # 验证形状
        self.assertEqual(df.shape, (2, 2))
        
        # 验证数据访问
        self.assertEqual(df.iloc[0]['name'], 'Alice')
        self.assertEqual(df['age'].mean(), 27.5)

if __name__ == '__main__':
    unittest.main()
