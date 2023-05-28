import pandas
from typing import List, Union
from index import VisitorsAnalyticsUtils
utils = VisitorsAnalyticsUtils("Test", 1)
class Test:
	# def __init__(self):
	# 	self.utils = VisitorsAnalyticsUtils("Test", 1)

	def test_id_greater_than_zero(self):
		assert utils.id > 0

	def test_name_is_string(self):
		assert isinstance(utils.name, str)
	
	def test_year_and_region(self, monkeypatch):
		monkeypatch.setattr("index.VisitorsAnalyticsUtils.get_year_and_region", lambda self: ([" 1998 Jan ", " 2007 Dec "], 2))  # noqa: E501
		tuple_check: Union[tuple[List[str], int], None] = utils.get_year_and_region()
		assert isinstance(tuple_check, tuple)
		assert isinstance(tuple_check[0], list) 
		assert isinstance(tuple_check[1], int) 

	def load_data_file(self):
		dataframe = utils.loadDataFile()
		assert isinstance(dataframe, pandas.DataFrame)
		assert len(dataframe.columns) == 34 # Check no. of column is 34
		assert len(dataframe) == 479 # Check no. of row is 479

	def filter_data(self, monkeypatch):
		monkeypatch.setattr("index.VisitorsAnalyticsUtils.get_year_and_region", lambda self: ([" 1988 Jan ", " 1997 Dec "], 2))  # noqa: E501
		dataframe = utils.filter_by_year_and_region()
		print(dataframe)
		assert isinstance(dataframe, pandas.DataFrame)
		assert len(dataframe.columns) == 12
		assert len(dataframe) == 120

		
	def run_all_functions(self):
		self.test_id_greater_than_zero()
		self.test_name_is_string()
		self.test_year_and_region() # type: ignore
		self.load_data_file()
		self.filter_data() # type: ignore
		# Call other functions from the VisitorsAnalyticsUtils class

# Create an instance of the Test class
test_instance = Test()

# Call the run_all_functions method to test functions of the VisitorsAnalyticsUtils
# test_instance.run_all_functions()