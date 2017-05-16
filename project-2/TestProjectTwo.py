import ProjectTwo as p
import unittest

class Test_ProjectTwo(unittest.TestCase):
    def defineTestCaseBankT(self):
        T=[[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        T[0]=[1828, 1856, 1884, 1924, 1952, 1980, 2036,  2064,2008]
        T[1]=[1801, 1807, 1818, 1829, 1835, 1846, 1857, 1863, 1874, 1885, 
              1891, 1903, 1914, 1925, 1931, 1942, 1953, 1959, 1970, 1981, 1987,
              1998, 2015, 2026, 2037, 2043, 2054, 2065, 2071,2009]
        T[2]=[2010, 1802, 1813, 1819, 1830, 1841, 1847, 1858, 1869, 1875, 1886,
              1897, 1909, 1915, 1926, 1937, 1943, 1954, 1965, 1971, 1982, 1993, 1999,
              2021, 2027, 2038, 2049, 2055, 2066]
        T[3]=[2011,1803, 1814, 1825, 1831, 1842, 1853, 1859, 1870, 1881, 1887, 1898,
              1910, 1921, 1927, 1938, 1949, 1955, 1966, 1977, 1983, 1994, 2005, 2022, 2033,
              2039, 2050, 2061, 2067, 2078 ]
        T[4]=[2012, 1804, 1832, 1860, 1888, 1928, 1956, 1984, 2040, 2068]
        T[5]=[2013, 1805, 1811, 1822, 1833, 1839, 1850, 1861, 1867, 1878, 1889, 1895, 
              1901, 1907, 1918, 1929, 1935, 1946, 1957, 1963, 1974, 1985, 1991, 2002, 2019,
              2030, 2041, 2047, 2058, 2069, 2075]
        T[6]=[2014, 1800, 1806, 1817, 1823, 1834, 1845, 1851, 1862, 1873, 1879, 1890, 
              1902, 1913, 1919, 1930, 1941, 1947, 1958, 1969, 1975, 1986, 1997, 2003, 2025,
              2031, 2042, 2053, 2059, 2070]
              #2015=2009
        T[7]=[2016, 1808, 1836, 1864, 1892, 1904, 1932, 1960, 1988, 2044, 2072]
        T[8]=[2017,1809, 1815, 1826, 1837, 1843, 1854, 1865, 1871, 1882, 1893, 1899, 1905,
              1911, 1922, 1933, 1939, 1950, 1961, 1967, 1978, 1989, 1995, 2006, 2023, 2034, 2045,
              2051, 2062, 2073, 2079]
        T[9]=[2018,1810, 1821, 1827, 1838, 1849, 1855, 1866, 1877, 1883, 1894, 1900, 1906,
              1917, 1923, 1934, 1945, 1951, 1962, 1973, 1979, 1990, 2001, 2007, 2029, 2035, 2046, 
              2057, 2063, 2074]
        T[10]=[2020,1812, 1840, 1868, 1896, 1908, 1936, 1964, 1992, 2048, 2076]
        T[11]=[2024,1816, 1844, 1872, 1912, 1940, 1968, 1996, 2052, 2080]
        T[12]=[2028,1820, 1848, 1876, 1916, 1944, 1972, 2000, 2056]
        T[13]=[2032,1824, 1852, 1880, 1920, 1948, 1976, 2004, 2060]
        return T

    def test_isValidDateBasic(self):
        self.assertTrue(p.isValidDate(2000,1,31))
        self.assertFalse(p.isValidDate(2000,1,32))
        self.assertFalse(p.isValidDate(1,1,2000))
        self.assertFalse(p.isValidDate(2000,2,32))

    def test_isValidDateMonthLength(self):
        self.assertFalse(p.isValidDate(2000,1,32))
        self.assertFalse(p.isValidDate(2000,2,30))
        self.assertFalse(p.isValidDate(2000,3,32))
        self.assertFalse(p.isValidDate(2000,4,31))
        self.assertFalse(p.isValidDate(2000,5,32))
        self.assertFalse(p.isValidDate(2000,6,31))
        self.assertFalse(p.isValidDate(2000,7,32))
        self.assertFalse(p.isValidDate(2000,8,32))
        self.assertFalse(p.isValidDate(2000,9,31))
        self.assertFalse(p.isValidDate(2000,10,32))
        self.assertFalse(p.isValidDate(2000,11,31))
        self.assertFalse(p.isValidDate(2000,12,32))

    def test_isValidDateLeapTest(self):
        self.assertTrue(p.isValidDate(2000,2,29))
        self.assertTrue(p.isValidDate(2004,2,29))
        self.assertFalse(p.isValidDate(1800,2,29))
        self.assertFalse(p.isValidDate(1900,2,29))
        self.assertFalse(p.isValidDate(2100,2,29))        
        self.assertFalse(p.isValidDate(2001,2,29))

    def test_intToDayOfWeek(self):
        self.assertEqual(p.intToDayOfWeek(0), 'Saturday')
        self.assertEqual(p.intToDayOfWeek(1), 'Sunday')
        self.assertEqual(p.intToDayOfWeek(2), 'Monday')
        self.assertEqual(p.intToDayOfWeek(3), 'Tuesday')
        self.assertEqual(p.intToDayOfWeek(4), 'Wednesday')
        self.assertEqual(p.intToDayOfWeek(5), 'Thursday')
        self.assertEqual(p.intToDayOfWeek(6), 'Friday')
        self.assertEqual(p.intToDayOfWeek(16), 'ERROR')
        self.assertEqual(p.intToDayOfWeek(7), 'ERROR')

    def test_computeDayOfWeek(self):
        T=self.defineTestCaseBankT()
        s=[3,5,6,0,1, 3,4,6,1,2, 4,2,0,5]
        for i in range(14):#January first test 
            for j in range( len(T[i]) ):
                self.assertEqual(p.computeDayOfWeek(T[i][j],1,1), s[i])
        for i in range(14): #similar years test part one
            for j in range(1,len(T[i])):
                for month in range(1,13):
                    for date2 in range(1,29):
                        self.assertEqual(p.computeDayOfWeek(T[i][j],month,date2), p.computeDayOfWeek(T[i][0], month, date2))
        for i in range(14): #similar years test part two
            for j in range(1,len(T[i])):
                for month in range(1,13):
                    for date2 in range(28,33):
                        self.assertEqual(p.isValidDate(T[i][j],month,date2), p.isValidDate(T[i][0], month, date2))
        


unittest.main()

#http://www.accuracyproject.org/perpetualcalendars.html
#To execute script from within python:
#>> execfile('filename.py')
#To generate pyc code: 
#>> import py_compile
#>> py_compile.compile("file.py")
