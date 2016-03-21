#!/usr/bin/env python3

import pandas as pd
from pandas import DatanoFrame
import matplotlib.pyplot as plt
import matplotlib
#matplotlib.style.use('ggplot')


def input_growth_rate(rate,amount):
	amount = rate * amount
	return amount

#Initial User Request
user_input = input("Build by Product?: ")
if user_input == "Yes":
    print("I will build this later.")
else: 

#Input Revenue Forecast
	rev_1 = 100
	rev_2 = 110
	rev_3 = 120
	rev_4 = 130
	rev_5 = 140

#Input COGS Forecast
	cogs_1 = 50
	cogs_2 = 55
	cogs_3 = 60
	cogs_4 = 65
	cogs_5 = 70

#Input Sales & Marketing Forecast
	sm_1 = 20
	sm_2 = 20
	sm_3 = 20
	sm_4 = 20
	sm_5 = 20

#Input Research & Development Forecast
	rd_1 = 15
	rd_2 = 15
	rd_3 = 15
	rd_4 = 15
	rd_5 = 15

#Input G&A Forecast
	ga_1 = 10
	ga_2 = 10
	ga_3 = 10
	ga_4 = 10
	ga_5 = 10

#Set Rev Growth Rate Input
	rev_g_rate_1 = 1.00
	rev_g_rate_2 = 1.10
	rev_g_rate_3 = 1.08
	rev_g_rate_4 = 1.05
	rev_g_rate_5 = 1.03

#Set Rev Growth Rate Input
	cogs_g_rate_1 = 1.00
	cogs_g_rate_2 = 1.010
	cogs_g_rate_3 = 1.08
	cogs_g_rate_4 = 1.05
	cogs_g_rate_5 = 1.03

#Set Rev Growth Rate Input
	sm_g_rate_1 = 1.00
	sm_g_rate_2 = 1.03
	sm_g_rate_3 = 1.03
	sm_g_rate_4 = 1.03
	sm_g_rate_5 = 1.03

#Set Rev Growth Rate Input
	rd_g_rate_1 = 1.00
	rd_g_rate_2 = 1.03
	rd_g_rate_3 = 1.03
	rd_g_rate_4 = 1.03
	rd_g_rate_5 = 1.03

#Set Rev Growth Rate Input
	ga_g_rate_1 = 1.00
	ga_g_rate_2 = 1.03
	ga_g_rate_3 = 1.03
	ga_g_rate_4 = 1.03
	ga_g_rate_5 = 1.03

#Set tax rate
	trate_1 = .3
	trate_2 = .3
	trate_3 = .3
	trate_4 = .3
	trate_5 = .3

#Build the forecast based on a growth rate per year
	rev_1 = input_growth_rate(rev_g_rate_1,rev_1)
	rev_2 = input_growth_rate(rev_g_rate_2,rev_2)
	rev_3 = input_growth_rate(rev_g_rate_3,rev_3)
	rev_4 = input_growth_rate(rev_g_rate_4,rev_4)
	rev_5 = input_growth_rate(rev_g_rate_5,rev_5)

	cogs_1 = input_growth_rate(cogs_g_rate_1,cogs_1)
	cogs_2 = input_growth_rate(cogs_g_rate_2,cogs_2)
	cogs_3 = input_growth_rate(cogs_g_rate_3,cogs_3)
	cogs_4 = input_growth_rate(cogs_g_rate_4,cogs_4)
	cogs_5 = input_growth_rate(cogs_g_rate_5,cogs_5)

	gm_1 = rev_1 - cogs_1
	gm_2 = rev_2 - cogs_2
	gm_3 = rev_3 - cogs_3
	gm_4 = rev_4 - cogs_4
	gm_5 = rev_5 - cogs_5

	sm_1 = input_growth_rate(sm_g_rate_1,sm_1)
	sm_2 = input_growth_rate(sm_g_rate_2,sm_2)
	sm_3 = input_growth_rate(sm_g_rate_3,sm_3)
	sm_4 = input_growth_rate(sm_g_rate_4,sm_4)
	sm_5 = input_growth_rate(sm_g_rate_5,sm_5)

	rd_1 = input_growth_rate(rd_g_rate_1,rd_1)
	rd_2 = input_growth_rate(rd_g_rate_2,rd_2)
	rd_3 = input_growth_rate(rd_g_rate_3,rd_3)
	rd_4 = input_growth_rate(rd_g_rate_4,rd_4)
	rd_5 = input_growth_rate(rd_g_rate_5,rd_5)

	ga_1 = input_growth_rate(ga_g_rate_1,ga_1)
	ga_2 = input_growth_rate(ga_g_rate_2,ga_2)
	ga_3 = input_growth_rate(ga_g_rate_3,ga_3)
	ga_4 = input_growth_rate(ga_g_rate_4,ga_4)
	ga_5 = input_growth_rate(ga_g_rate_5,ga_5)

	opex_1 = sm_1 + rd_1 + ga_1
	opex_2 = sm_2 + rd_2 + ga_2
	opex_3 = sm_3 + rd_3 + ga_3
	opex_4 = sm_4 + rd_4 + ga_4
	opex_5 = sm_5 + rd_5 + ga_5

	btaxp_1 = gm_1 - opex_1
	btaxp_2 = gm_2 - opex_2
	btaxp_3 = gm_3 - opex_3
	btaxp_4 = gm_4 - opex_4
	btaxp_5 = gm_5 - opex_5

#Build lists to pass to the DataFrame
	rev = [rev_1, rev_2, rev_3, rev_4, rev_5]
	cogs = [cogs_1, cogs_2, cogs_3, cogs_4, cogs_5]
	gm = [gm_1, gm_2, gm_3, gm_4, gm_5]
	sm = [sm_1, sm_2, sm_3, sm_4, sm_5]
	rd = [rd_1, rd_2, rd_3, rd_4, rd_5]
	ga = [ga_1, ga_2, ga_3, ga_4, ga_5]
	opex = [opex_1, opex_2, opex_3, opex_4, opex_5]
	btaxp = [btaxp_1, btaxp_2,btaxp_3,btaxp_4,btaxp_5] 

	rows = ["Revenue","COGS","GM","Sales & Marketing","Research & Development","General & Admin","OPEX","Before Tax Profit"]
	columns = ["2015","2016","2017","2018","2019"]

#Create the DataFrame
	df = pd.DataFrame([rev,cogs,gm,sm,rd,ga,opex,btaxp], index = rows, columns = columns)
	print (df)
	df.head()

#Chart the data
#ts = pd.Series(rev, index=columns)
#ts = ts.cumsum()
#ts.plot()
