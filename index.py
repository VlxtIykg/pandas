'''
All comments here are for markus/daneesh or docstring/javadocs or comments
## is for them
# are comments
\''' is for docstring
'''
from math import isnan
from mimetypes import add_type  # noqa: F401
from typing import Any, List, Optional, Tuple
import pandas
import os
import sys
# import glob
# import pyperclip # apparently I've set up pylance to auto detect conda packages! 

# pandas.set_option('display.max_columns',20000)
pandas.set_option('display.max_rows',20000)

class VisitorsAnalyticsUtils:

	# class attribute
	test: str = 'testify'

	# instance attribute
	def __init__(self, name, id):
		"""summary __init__

		Args:
				name ([str]): [Just a casual name for me to know which class I'm calling from]
				id ([int]): [This is the id that depicts the different classes and 
				if needed can be used to call id specific methods]
				date (dict[int, list[str]]): [The different years in the csv files]
				region (dict[int, list[str]]): [The different region encompassing the countries]
		"""
		assert id > 0
		self.name: str = name
		self.id:  int = id
		self.date: dict[int, list[str]] = {
			1: [
				" 1978 Jan ",
				" 1978 Feb ",
				" 1978 Mar ",
				" 1978 Apr ",
				" 1978 May ",
				" 1978 Jun ",
				" 1978 Jul ",
				" 1978 Aug ",
				" 1978 Sep ",
				" 1978 Oct ",
				" 1978 Nov ",
				" 1978 Dec "
				" 1979 Jan ",
				" 1979 Feb "
				" 1979 Mar ",
				" 1979 Apr ",
				" 1979 May ",
				" 1979 Jun ",
				" 1979 Jul ",
				" 1979 Aug ",
				" 1979 Sep ",
				" 1979 Oct ",
				" 1979 Nov ",
				" 1979 Dec ",
				" 1980 Jan ",
				" 1980 Feb ",
				" 1980 Mar ",
				" 1980 Apr ",
				" 1980 May ",
				" 1980 Jun ",
				" 1980 Jul ",
				" 1980 Aug ",
				" 1980 Sep ",
				" 1980 Oct ",
				" 1980 Nov ",
				" 1980 Dec ",
				" 1981 Jan ",
				" 1981 Feb ",
				" 1981 Mar ",
				" 1981 Apr ",
				" 1981 May ",
				" 1981 Jun ",
				" 1981 Jul ",
				" 1981 Aug ",
				" 1981 Sep ",
				" 1981 Oct ",
				" 1981 Nov ",
				" 1981 Dec ",
				" 1982 Jan ",
				" 1982 Feb ",
				" 1982 Mar ",
				" 1982 Apr ",
				" 1982 May ",
				" 1982 Jun ",
				" 1982 Jul ",
				" 1982 Aug ",
				" 1982 Sep ",
				" 1982 Oct ",
				" 1982 Nov ",
				" 1982 Dec ",
				" 1983 Jan ",
				" 1983 Feb ",
				" 1983 Mar ",
				" 1983 Apr ",
				" 1983 May ",
				" 1983 Jun ",
				" 1983 Jul ",
				" 1983 Aug ",
				" 1983 Sep ",
				" 1983 Oct ",
				" 1983 Nov ",
				" 1983 Dec ",
				" 1984 Jan ",
				" 1984 Feb ",
				" 1984 Mar ",
				" 1984 Apr ",
				" 1984 May ",
				" 1984 Jun ",
				" 1984 Jul ",
				" 1984 Aug ",
				" 1984 Sep ",
				" 1984 Oct ",
				" 1984 Nov ",
				" 1984 Dec ",
				" 1985 Jan ",
				" 1985 Feb ",
				" 1985 Mar ",
				" 1985 Apr ",
				" 1985 May ",
				" 1985 Jun ",
				" 1985 Jul ",
				" 1985 Aug ",
				" 1985 Sep ",
				" 1985 Oct ",
				" 1985 Nov ",
				" 1985 Dec ",
				" 1986 Jan ",
				" 1986 Feb ",
				" 1986 Mar ",
				" 1986 Apr ",
				" 1986 May ",
				" 1986 Jun ",
				" 1986 Jul ",
				" 1986 Aug ",
				" 1986 Sep ",
				" 1986 Oct ",
				" 1986 Nov ",
				" 1986 Dec ",
				" 1987 Jan ",
				" 1987 Feb ",
				" 1987 Mar ",
				" 1987 Apr ",
				" 1987 May ",
				" 1987 Jun ",
				" 1987 Jul ",
				" 1987 Aug ",
				" 1987 Sep ",
				" 1987 Oct ",
				" 1987 Nov ",
				" 1987 Dec "
			],
			2: [
				" 1988 Jan ",
				" 1988 Feb ",
				" 1988 Mar ",
				" 1988 Apr ",
				" 1988 May ",
				" 1988 Jun ",
				" 1988 Jul ",
				" 1988 Aug ",
				" 1988 Sep ",
				" 1988 Oct ",
				" 1988 Nov ",
				" 1988 Dec ",
				" 1989 Jan ",
				" 1989 Feb ",
				" 1989 Mar ",
				" 1989 Apr ",
				" 1989 May ",
				" 1989 Jun ",
				" 1989 Jul ",
				" 1989 Aug ",
				" 1989 Sep ",
				" 1989 Oct ",
				" 1989 Nov ",
				" 1989 Dec ",
				" 1990 Jan ",
				" 1990 Feb ",
				" 1990 Mar ",
				" 1990 Apr ",
				" 1990 May ",
				" 1990 Jun ",
				" 1990 Jul ",
				" 1990 Aug ",
				" 1990 Sep ",
				" 1990 Oct ",
				" 1990 Nov ",
				" 1990 Dec ",
				" 1991 Jan ",
				" 1991 Feb ",
				" 1991 Mar ",
				" 1991 Apr ",
				" 1991 May ",
				" 1991 Jun ",
				" 1991 Jul ",
				" 1991 Aug ",
				" 1991 Sep ",
				" 1991 Oct ",
				" 1991 Nov ",
				" 1991 Dec ",
				" 1992 Jan ",
				" 1992 Feb ",
				" 1992 Mar ",
				" 1992 Apr ",
				" 1992 May ",
				" 1992 Jun ",
				" 1992 Jul ",
				" 1992 Aug ",
				" 1992 Sep ",
				" 1992 Oct ",
				" 1992 Nov ",
				" 1992 Dec ",
				" 1993 Jan ",
				" 1993 Feb ",
				" 1993 Mar ",
				" 1993 Apr ",
				" 1993 May ",
				" 1993 Jun ",
				" 1993 Jul ",
				" 1993 Aug ",
				" 1993 Sep ",
				" 1993 Oct ",
				" 1993 Nov ",
				" 1993 Dec ",
				" 1994 Jan ",
				" 1994 Feb ",
				" 1994 Mar ",
				" 1994 Apr ",
				" 1994 May ",
				" 1994 Jun ",
				" 1994 Jul ",
				" 1994 Aug ",
				" 1994 Sep ",
				" 1994 Oct ",
				" 1994 Nov ",
				" 1994 Dec ",
				" 1995 Jan ",
				" 1995 Feb ",
				" 1995 Mar ",
				" 1995 Apr ",
				" 1995 May ",
				" 1995 Jun ",
				" 1995 Jul ",
				" 1995 Aug ",
				" 1995 Sep ",
				" 1995 Oct ",
				" 1995 Nov ",
				" 1995 Dec ",
				" 1996 Jan ",
				" 1996 Feb ",
				" 1996 Mar ",
				" 1996 Apr ",
				" 1996 May ",
				" 1996 Jun ",
				" 1996 Jul ",
				" 1996 Aug ",
				" 1996 Sep ",
				" 1996 Oct ",
				" 1996 Nov ",
				" 1996 Dec ",
				" 1997 Jan ",
				" 1997 Feb ",
				" 1997 Mar ",
				" 1997 Apr ",
				" 1997 May ",
				" 1997 Jun ",
				" 1997 Jul ",
				" 1997 Aug ",
				" 1997 Sep ",
				" 1997 Oct ",
				" 1997 Nov ",
				" 1997 Dec "
			],
			3: [
				" 1998 Jan ",
				" 1998 Feb ",
				" 1998 Mar ",
				" 1998 Apr ",
				" 1998 May ",
				" 1998 Jun ",
				" 1998 Jul ",
				" 1998 Aug ",
				" 1998 Sep ",
				" 1998 Oct ",
				" 1998 Nov ",
				" 1998 Dec ",
				" 1999 Jan ",
				" 1999 Feb ",
				" 1999 Mar ",
				" 1999 Apr ",
				" 1999 May ",
				" 1999 Jun ",
				" 1999 Jul ",
				" 1999 Aug ",
				" 1999 Sep ",
				" 1999 Oct ",
				" 1999 Nov ",
				" 1999 Dec ",
				" 2000 Jan ",
				" 2000 Feb ",
				" 2000 Mar ",
				" 2000 Apr ",
				" 2000 May ",
				" 2000 Jun ",
				" 2000 Jul ",
				" 2000 Aug ",
				" 2000 Sep ",
				" 2000 Oct ",
				" 2000 Nov ",
				" 2000 Dec ",
				" 2001 Jan ",
				" 2001 Feb ",
				" 2001 Mar ",
				" 2001 Apr ",
				" 2001 May ",
				" 2001 Jun ",
				" 2001 Jul ",
				" 2001 Aug ",
				" 2001 Sep ",
				" 2001 Oct ",
				" 2001 Nov ",
				" 2001 Dec ",
				" 2002 Jan ",
				" 2002 Feb ",
				" 2002 Mar ",
				" 2002 Apr ",
				" 2002 May ",
				" 2002 Jun ",
				" 2002 Jul ",
				" 2002 Aug ",
				" 2002 Sep ",
				" 2002 Oct ",
				" 2002 Nov ",
				" 2002 Dec ",
				" 2003 Jan ",
				" 2003 Feb ",
				" 2003 Mar ",
				" 2003 Apr ",
				" 2003 May ",
				" 2003 Jun ",
				" 2003 Jul ",
				" 2003 Aug ",
				" 2003 Sep ",
				" 2003 Oct ",
				" 2003 Nov ",
				" 2003 Dec ",
				" 2004 Jan ",
				" 2004 Feb ",
				" 2004 Mar ",
				" 2004 Apr ",
				" 2004 May ",
				" 2004 Jun ",
				" 2004 Jul ",
				" 2004 Aug ",
				" 2004 Sep ",
				" 2004 Oct ",
				" 2004 Nov ",
				" 2004 Dec ",
				" 2005 Jan ",
				" 2005 Feb ",
				" 2005 Mar ",
				" 2005 Apr ",
				" 2005 May ",
				" 2005 Jun ",
				" 2005 Jul ",
				" 2005 Aug ",
				" 2005 Sep ",
				" 2005 Oct ",
				" 2005 Nov ",
				" 2005 Dec ",
				" 2006 Jan ",
				" 2006 Feb ",
				" 2006 Mar ",
				" 2006 Apr ",
				" 2006 May ",
				" 2006 Jun ",
				" 2006 Jul ",
				" 2006 Aug ",
				" 2006 Sep ",
				" 2006 Oct ",
				" 2006 Nov ",
				" 2006 Dec ",
				" 2007 Jan ",
				" 2007 Feb ",
				" 2007 Mar ",
				" 2007 Apr ",
				" 2007 May ",
				" 2007 Jun ",
				" 2007 Jul ",
				" 2007 Aug ",
				" 2007 Sep ",
				" 2007 Oct ",
				" 2007 Nov ",
				" 2007 Dec "
			],
			4: [
				" 2008 Jan ",
				" 2008 Feb ",
				" 2008 Mar ",
				" 2008 Apr ",
				" 2008 May ",
				" 2008 Jun ",
				" 2008 Jul ",
				" 2008 Aug ",
				" 2008 Sep ",
				" 2008 Oct ",
				" 2008 Nov ",
				" 2008 Dec ",
				" 2009 Jan ",
				" 2009 Feb ",
				" 2009 Mar ",
				" 2009 Apr ",
				" 2009 May ",
				" 2009 Jun ",
				" 2009 Jul ",
				" 2009 Aug ",
				" 2009 Sep ",
				" 2009 Oct ",
				" 2009 Nov ",
				" 2009 Dec ",
				" 2010 Jan ",
				" 2010 Feb ",
				" 2010 Mar ",
				" 2010 Apr ",
				" 2010 May ",
				" 2010 Jun ",
				" 2010 Jul ",
				" 2010 Aug ",
				" 2010 Sep ",
				" 2010 Oct ",
				" 2010 Nov ",
				" 2010 Dec ",
				" 2011 Jan ",
				" 2011 Feb ",
				" 2011 Mar ",
				" 2011 Apr ",
				" 2011 May ",
				" 2011 Jun ",
				" 2011 Jul ",
				" 2011 Aug ",
				" 2011 Sep ",
				" 2011 Oct ",
				" 2011 Nov ",
				" 2011 Dec ",
				" 2012 Jan ",
				" 2012 Feb ",
				" 2012 Mar ",
				" 2012 Apr ",
				" 2012 May ",
				" 2012 Jun ",
				" 2012 Jul ",
				" 2012 Aug ",
				" 2012 Sep ",
				" 2012 Oct ",
				" 2012 Nov ",
				" 2012 Dec ",
				" 2013 Jan ",
				" 2013 Feb ",
				" 2013 Mar ",
				" 2013 Apr ",
				" 2013 May ",
				" 2013 Jun ",
				" 2013 Jul ",
				" 2013 Aug ",
				" 2013 Sep ",
				" 2013 Oct ",
				" 2013 Nov ",
				" 2013 Dec ",
				" 2014 Jan ",
				" 2014 Feb ",
				" 2014 Mar ",
				" 2014 Apr ",
				" 2014 May ",
				" 2014 Jun ",
				" 2014 Jul ",
				" 2014 Aug ",
				" 2014 Sep ",
				" 2014 Oct ",
				" 2014 Nov ",
				" 2014 Dec ",
				" 2015 Jan ",
				" 2015 Feb ",
				" 2015 Mar ",
				" 2015 Apr ",
				" 2015 May ",
				" 2015 Jun ",
				" 2015 Jul ",
				" 2015 Aug ",
				" 2015 Sep ",
				" 2015 Oct ",
				" 2015 Nov ",
				" 2015 Dec ",
				" 2016 Jan ",
				" 2016 Feb ",
				" 2016 Mar ",
				" 2016 Apr ",
				" 2016 May ",
				" 2016 Jun ",
				" 2016 Jul ",
				" 2016 Aug ",
				" 2016 Sep ",
				" 2016 Oct ",
				" 2016 Nov ",
				" 2016 Dec ",
				" 2017 Jan ",
				" 2017 Feb ",
				" 2017 Mar ",
				" 2017 Apr ",
				" 2017 May ",
				" 2017 Jun ",
				" 2017 Jul ",
				" 2017 Aug ",
				" 2017 Sep ",
				" 2017 Oct ",
				" 2017 Nov "
			],
		}
		self.region: dict[int, list[str]] = {
			1: [
			' Brunei Darussalam ', 
			' Indonesia ', 
			' Malaysia ', 
			' Philippines ', 
			' Thailand ', 
			' Viet Nam ', 
			' Myanmar ', 
			' Japan ', 
			' Hong Kong ', 
			' China ', 
			' Taiwan ', 
			' Korea, Republic Of ', 
			' India ', 
			' Pakistan ', 
			' Sri Lanka ', 
			' Saudi Arabia ', 
			' Kuwait ', 
			' UAE '
			],

			2: [
				' United Kingdom ',
				' Germany ',
				' France ',
				' Italy ',
				' Netherlands ',
				' Greece ',
				' Belgium & Luxembourg ',
				' Switzerland ',
				' Austria ',
				' Scandinavia ',
				' CIS & Eastern Europe '
			],
			
			3: [
				' USA ',
				' Canada ',
				' Australia ',
				' New Zealand ',
				' Africa '
			]
		}


	def get_year_and_region(self) -> Optional[Tuple[List[str], int]]:
		"""summary get_year_and_region

		Returns:
				tuple[int, int]: gets user response and converts it into numbers and return them
		"""
		year_period: int = int(input("\nEnter year period: \n1: 1978-1987\n2: 1988-1997\n3: 1998-2007\n4: 2008-2017 \033[4A\033[6C"))  # noqa: E501

		sys.stdout.write("\033[0J\r")

		region_question = "Enter the region: "
		region_choices = "\n1: Asia\n2: Europe\n3: Others"
		region: int = int(input(f"{region_question+region_choices}\033[3F\033[{len(region_question)}C")) # noqa

		sys.stdout.write("\033[2J")

		cursor_pos = "\033[6n"
		if cursor_pos != "[0;0R":
			sys.stdout.write("\033[H")

		if year_period <= 0 or isnan(year_period) or year_period > 4:
			print("Error at L584!\n\t\033[48;5;196m\033[48;5;222m⟶   Not a number or number too small/big (Try 1-4)!\033[0m") # noqa
			exit()

		if year_period == 0 or year_period == 1:
			year = [" 1978 Jan "," 1987 Dec "]  
			return year, region

		if year_period == 2: 
			year = [" 1988 Jan "," 1997 Dec "]   # noqa: E701
			return year, region

		if year_period == 3:
			year = [" 1998 Jan "," 2007 Dec "]   # noqa: E701
			return year, region

		if year_period == 4:
			year = [" 2008 Jan "," 2017 Nov "]   # noqa: E701
			return year, region

		else: 
			year = [" 1978 Jan "," 1987 Dec "] # noqa: E701

		return year, region
	
	def loadDataFile(self, printData=False, dataframe=None) -> pandas.DataFrame: 
		"""summary loadDataFile

		Returns:
				pandas.DataFrame: Reads the csv file and returns as a dataframe for use
		"""

		cwd = os.getcwd()
		if cwd.startswith("/"):
			data: pandas.DataFrame = pandas.read_csv(filepath_or_buffer='/home/Kami/Documents/resources/pandas/Int_Monthly_Visitor.csv', thousands=",", na_values=" na ", index_col=0) ## Markus if you hover over filepath_or_buffer or read_csv you can see it accepts filepath_or_buffer, same for most predefined functions in packages.   # noqa: E501
		else:
			# print("Getting data!\033[177m-")
			data: pandas.DataFrame = pandas.read_csv(filepath_or_buffer='./resources/Int_Monthly_Visitor.csv', thousands=",", na_values=" na ", index_col=0) # noqa: E501
		if printData and dataframe is not None:
			# print(dataframe.head(5)) not sure if I should filter data or not
			print(data.head(5).fillna(value=0))
		return data


	def filter_by_year_and_region(self) -> pandas.DataFrame:
		"""summary filter_by_year_region

		Returns:
				pandas.DataFrame: Filters by the year the user chose and the region the user chose
		"""

		csv: pandas.DataFrame = self.loadDataFile()
		csv: pandas.DataFrame = csv.fillna(value=0) 

		passCheck: Tuple[List[str], int] | None = self.get_year_and_region()
		if passCheck is not None:
			year, region = passCheck
			# Make tests later
			filtered_data: pandas.DataFrame = csv.loc[year[0]:year[1], self.region[region]]
			# filtered_data.fillna(0)

			#pyperclip.copy(filtered_data.to_clipboard)<-- apparently I didn't need pyperclip either
			# filtered_data.to_clipboard()
			return filtered_data
		else:
			return csv.loc[" 1988 Jan ": " 1998 Dec ", self.region[1]] # It is now I realize i shouldve made it start with 0 and not 1 :( # noqa

			#pyperclip.copy(filtered_data.to_clipboard)<-- apparently I didn't need pyperclip either
			# filtered_data.to_clipboard()
	

	def parseData(self, a=None) -> None:
		"""summary parseData

		Returns:
				None: Runs various function to print information to the user
		"""
		if a is None:
			csv_data: pandas.DataFrame = self.filter_by_year_and_region()
		else:
			csv_data: pandas.DataFrame = a
		print("*** Parsed Data (Regions) ***")
		extra_column: pandas.DataFrame = self.add_years(a=csv_data)
		task2: pandas.DataFrame= extra_column
		task2.info()
		print("*** Parsed Data (Years) ***")
		task1 = self.get_years(a=csv_data)
		print(task1.describe())
		return
	
	def add_years(self, a=None) -> pandas.DataFrame:
		if a is None:
			data: pandas.DataFrame = self.filter_by_year_and_region()
		else:
			data: pandas.DataFrame = a
		custom_column = pandas.Series(data.index).copy()
		year_column = custom_column.str.strip(" ")
		year_and_month: pandas.DataFrame = year_column.str.split(" ", expand=True)
		data["years"] = year_and_month[0].values
		# y = data.reset_index(drop=True)
		y = data.astype("int64")
		return y

	def get_years(self, a=None) -> Any:
		"""summary get_years

		Args:
				a (dataframe, optional): [Get a dataframe as the backbone]. Defaults to None.

		Returns:
				None: Splices the csv file to only describe the first column!
		"""
		if a is None:
			data: pandas.DataFrame = self.filter_by_year_and_region()
		else:
			data: pandas.DataFrame = a
		# Well this took long enough to figure out
		data["year"] = data.index
		data.reset_index(inplace=True)
		inject = data["year"].str[:5].astype("int64")
		# data['year'] = data['year'].str.strip()
		# data["year"] = pandas.to_datetime(data['year'], format='%Y %b').astype("int64")
		# data = data.reset_index(level=['   ']).iloc[:, 0].str[:5].astype('int').describe()  # noqa: E501
		# data = data.astype('int').describe()  # noqa: E501
		# remove_index = data.reset_index(drop=True, inplace=True)
		# print(data.describe())
		return inject
	

	def getTop3Countries(self, a=None) -> None:
		"""summary getTop3Countries

		Returns:
				None: Prints the largest five sum of monthly visits	
		"""
		if a is None:
			csv_data: pandas.DataFrame = self.filter_by_year_and_region()
		else:
			csv_data: pandas.DataFrame = a
		print("*** Top 3 countries ***")
		# print(csv_data.head(n=3))
		print(csv_data.sum(axis=0).nlargest(3))
		return


## instantiating class (This means creating a new class and binding it to a variable)
anaylze = VisitorsAnalyticsUtils("Main class", id=1)

## access the class attributes
# test: any = anaylze.__class__.test

## access the instance attributes
# regio: dict[str, list[str]] = anaylze.region

# yr: tuple[int, int] = anaylze.get_year_and_region() # working

# anaylze.get_years() # working
data: pandas.DataFrame = anaylze.filter_by_year_and_region()

data1 = data.copy() # THis is a barbaric way to instantiate a new dataframe.. I know
data2 = data.copy() # but there's no time to figure out a way to make a non static dataframe atm!  # noqa: E501
anaylze.loadDataFile(printData=True, dataframe=data) # working
anaylze.parseData(a=data1) # working
anaylze.getTop3Countries(a=data2)