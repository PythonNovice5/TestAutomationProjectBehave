import logging
import string
import time

from selenium.webdriver.support.ui import *
# from pages.abstract import Abstract
import pickle


class loggedinPage:

    headers = {'NAME':0,'NUMBER OF CASES':1,'IMPACT_SCORE':2,'COMPLEXITY':3}
    def __init__(self,driver):
        self.driver = driver;
        self.sortingDropDown = self.driver.find_element_by_name("sort-select")
        self.tableRows = self.driver.find_elements_by_class_name("table-row")
        self.filter_input = self.driver.find_element_by_id("filter-input")
        self.c_header=self.driver.find_element_by_id("header-complexity")

    #method to select value from dropdown
    def selectFromDropDown(self,value):
        ss = Select(self.sortingDropDown)
        ss.select_by_visible_text(value)

    def fetchAndStoreValues(self):
        print("######################## RETURNING ORIGINAL VALUES ############################")
        # print(self.fetchCurrentValuesFromWebPage())
        with open('outfile', 'wb') as fp:
            pickle.dump(self.fetchCurrentValuesFromWebPage(), fp)
        return self.fetchCurrentValuesFromWebPage()

    def verifySortAfterEnteringFilterValue(self,sortBy):
        time.sleep(1)
        actual_values = self.fetchCurrentValuesFromWebPage();
        to_be_sorted = self.fetchCurrentValuesFromWebPage();
        if sortBy == 'Impact score':
            col_index = 2
            to_be_sorted.sort(key=lambda x: float(x[self.headers['IMPACT_SCORE']]))
            expected_values=to_be_sorted
            actual_values = self.fetchCurrentValuesFromWebPage();
            assert expected_values==actual_values
            print("Sort is working as expected for: " + sortBy.upper())
            return
        elif sortBy == 'Name':
            actual_values=[[j.lower() for j in i] for i in actual_values]
            to_be_sorted = [[j.lower() for j in i] for i in to_be_sorted]
            to_be_sorted.sort(key=lambda x: x[self.headers['NAME']])
            expected_values=to_be_sorted
            assert expected_values==actual_values
            print("Sort is working as expected for: " + sortBy.upper())
            return
        elif sortBy == 'Complexity':
            if self.sortByComplexity(self.headers['COMPLEXITY'],actual_values)==True:
                print("Sort is working as expected for: "+sortBy.upper())
                return
        elif sortBy=='Number of cases':
            if self.sortByNumOfCases(self.headers['NUMBER OF CASES'],actual_values)==True:
                print("Sort is working as expected for: " + sortBy.upper())
                return

    # This method fetches the current values from webpage
    def fetchCurrentValuesFromWebPage(self):
        t_list = []
        p_list = []

        # Adding rows in list
        for t in self.tableRows:
            t_list.append(t.text)

        # Adding rows values in sublists
        for n in t_list:
            k = n.replace('\n', ',')
            k = k.split(',')
            p_list.append(k)
        return p_list

    def sortByComplexity(self,col_index,actual_values):
        # Number of records expected
        expected_records=[]
        actual_values=[[0  if j=='low' else j for j in i] for i in actual_values]
        actual_values = [[1 if j == 'medium' else j for j in i] for i in actual_values]
        actual_values = [[2 if j == 'high' else j for j in i] for i in actual_values]
        to_be_sorted = actual_values
        to_be_sorted.sort(key=lambda x: int(x[col_index]))
        expected_values =to_be_sorted
        assert actual_values == expected_values
        return True

    def sortByNumOfCases(self,col_ind,actual_values):
        for a in actual_values:
            # convert 'M','k' to integer
            a[col_ind]=(self.convert_str_to_number(a[col_ind]))
        # print("-----------ACTUAL VALUES FOR NUMBER OF TEST CASES",actual_values)

    def convert_str_to_number(sel,x):
        total_stars = 0
        num_map = {'K': 1000, 'M': 1000000, 'B': 1000000000}
        if x.isdigit():
            total_stars = int(x)
        else:
            if len(x) > 1:
                total_stars = float(x[:-1]) * num_map.get(x[-1].upper(), 1)
        return int(total_stars)

    def enterIntoFilterData(self,value):
        self.filter_input.send_keys(value)

    # validates if the number of corresponding records returned correctly
    def verifyRecords(self,rec_input):
        expected_records =[]
        actual_records_num = len(self.tableRows)

        # Number of records expected
        with open('outfile', 'rb') as fp:
            org_values = pickle.load(fp)
        # print("ORG VALUES:",org_values)

        for o in org_values:
            if rec_input.lower() in (string.lower() for string in o):
                expected_records.append(o)
        expected_records_num =len(expected_records)
        print("Expected Num of records: ",expected_records_num)
        print("Actual Num of records: ",actual_records_num)
        assert actual_records_num == expected_records_num
        print("ACTUAL AND EXPECTED NUMBER OF SEARCHED RECORD IS SAME")











