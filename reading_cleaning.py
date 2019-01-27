import pandas as pd
import geopandas


def read_income_balance():
	#Reading in the files to DataFrames:
	income_yearly = pd.read_csv("IncomeStatementYearly.csv", header = 4, index_col = 0).transpose()[:-2]
	income_monthly = pd.read_csv("IncomeStatementMonthly.csv", header = 4, index_col = 0).transpose()[2:-2]
	trial_balance = pd.read_csv("TrialBalance.csv", header = 4, index_col=0, na_filter=False)
	trial_balance = trial_balance.drop("")

	return income_yearly, income_monthly, trial_balance

def read_ledger():
	general_ledger2018 = pd.read_csv("GeneralLedger2018.csv", header = 4, index_col = 0, na_filter=False)
	general_ledger2017 = pd.read_csv("GeneralLedger2017.csv", header = 4, index_col = 0, na_filter=False)
	general_ledger2016 = pd.read_csv("GeneralLedger2016.csv", header = 4, index_col = 0, na_filter=False)
	general_ledger2015 = pd.read_csv("GeneralLedger2015.csv", header = 4, index_col = 0, na_filter=False)
	general_ledger2014 =pd.read_csv("GeneralLedger2014.csv", header = 4, index_col = 0, na_filter=False)
	#general_ledger2013 = pd.read_csv("GeneralLedger2013.csv", header = 4, index_col = 0, na_filter = False)
	#general_ledger2012 =pd.read_csv("GeneralLedger2012.csv", header = 4, index_col = 0, na_filter=False)
	general_ledger = pd.concat([general_ledger2014,general_ledger2015,general_ledger2016,general_ledger2017,general_ledger2018])
	#Reorganizing General Ledger
	general_ledger["section"] = ""
	general_ledger = general_ledger.drop("")

	indexs = []

	for index, row in general_ledger.iterrows():    
	    try: #the index is a date
	        index = pd.to_datetime(index)
	        row["section"] = section 
	    except:
	        section = str(index)
	        indexs.append(section)
	        
	general_ledger = general_ledger.drop(indexs)
	general_ledger.index = pd.to_datetime(general_ledger.index)
	general_ledger = general_ledger.sort_index(axis=0)

	return general_ledger


def read_sales():
	sales_summary = pd.read_csv("SalesSummary.csv", header= 4, index_col=0, na_filter=False)
	sales_summary = sales_summary.drop("")
	indexs_totals = []
	for index, row in sales_summary.iterrows():
	    try:
	        index = pd.to_datetime(index)      
	    except:
	        indexs_totals.append(index)
	sales_summary = sales_summary.drop(indexs_totals)
	sales_summary.index = pd.to_datetime(sales_summary.index)

	return sales_summary

def read_shipped():
	shipped2015 = pd.read_excel("Shipped Orders 2015.xlsx", index_col=0, na_filter=False)
	shipped2012 = pd.read_excel("Shipped Orders 2012.xlsx", index_col=0, na_filter=False)
	shipped = pd.concat([shipped2012,shipped2015])
	shipped_items = pd.read_excel("Shipped Items.xlsx", index_col=0, na_filter=False)

	#Cleaning files and reorganizing
	shipped = shipped.drop("")
	shipped = shipped.replace(to_replace="New JANE Store", value="JANE Store")
	shipped = shipped.replace(to_replace="Little Sapling Toys, LLC", value="Little Sapling Toys, website")

	shipped_items = shipped_items.replace(to_replace="Age Blocks Photography Prop - Three Woods", value="Age Blocks")
	shipped_items = shipped_items.replace(to_replace="Age Blocks Photography Prop - All Maple (light)", value="Age Blocks")
	shipped_items = shipped_items.replace(to_replace="Age Blocks Photography Prop", value="Age Blocks")
	shipped_items = shipped_items.replace(to_replace="Photo Prop Age Blocks - Three Woods", value="Age Blocks")
	shipped_items = shipped_items.replace(to_replace="Photo Prop Age Blocks, maternity, new baby photography", value="Age Blocks")
	shipped_items = shipped_items.replace(to_replace="4 pc Age Set Maple", value="Age Blocks")
	shipped_items = shipped_items.replace(to_replace="4 pc Age Set 3 Wood", value="Age Blocks")

	shipped_items = shipped_items.replace(to_replace="Stacking Rainbow", value="Stacking Rainbow Toy")
	shipped_items = shipped_items.replace(to_replace="3 woods", value="Stacking Rainbow Toy")
	shipped_items = shipped_items.replace(to_replace="Brainbow wooden natural rainbow stacking toy", value="Stacking Rainbow Toy")
	shipped_items = shipped_items.replace(to_replace="brainbow wooden nesting toy", value="Stacking Rainbow Toy")
	shipped_items = shipped_items.replace(to_replace="personalized brainbow, wooden stacking and nesting toy", value="Stacking Rainbow Toy")
	shipped_items = shipped_items.replace(to_replace="personalized rainbow wooden toy stacking and nesting", value="Stacking Rainbow Toy")
	shipped_items = shipped_items.replace(to_replace="Brainbow wooden toy rainbow stacking toy kids toy puzzle", value="Stacking Rainbow Toy")

	shipped_items = shipped_items.replace(to_replace="Personalized Wood Name Blocks, alphabet baby custom letters wooden toy", value="Baby Name Blocks")
	shipped_items = shipped_items.replace(to_replace="personalized wooden blocks, alphabet letter baby wood name toy", value="Baby Name Blocks")
	shipped_items = shipped_items.replace(to_replace="6 personalized wooden blocks, alphabet letter baby toys modern wood name blocks", value="Baby Name Blocks")
	shipped_items = shipped_items.replace(to_replace="Personalized Name Blocks Wood Toy", value="Baby Name Blocks")
	shipped_items = shipped_items.replace(to_replace="5 personalized wooden blocks, alphabet letter baby toys modern wood name blocks", value="Baby Name Blocks")
	shipped_items = shipped_items.replace(to_replace="7 personalized wooden blocks, alphabet letter baby toys modern wood name blocks", value="Baby Name Blocks")
	shipped_items = shipped_items.replace(to_replace="4 personalized wooden blocks, alphabet letter baby toys modern wood name blocks", value="Baby Name Blocks")
	shipped_items = shipped_items.replace(to_replace="8 personalized wooden blocks, alphabet letter baby toys modern wood name blocks", value="Baby Name Blocks")
	shipped_items = shipped_items.replace(to_replace="Wooden Baby Name Block Toy", value="Baby Name Blocks")
	shipped_items = shipped_items.replace(to_replace="Baby Name Blocks, personalized wooden toy", value="Baby Name Blocks")
	shipped_items = shipped_items.replace(to_replace="Personalized Name Blocks Toy - 5 / uppercase/lowercase", value="Baby Name Blocks")
	shipped_items = shipped_items.replace(to_replace="Personalized Name Blocks Toy - 4 / uppercase/lowercase", value="Baby Name Blocks")
	shipped_items = shipped_items.replace(to_replace="Personalized Name Blocks Toy - 6 / uppercase/lowercase", value="Baby Name Blocks")

	stacker_names = ["personalized wooden toy sapling stacker, stacking blocks organic kids toy","wooden toy sapling stacker, stacking blocks organic kids toy","personalized sapling stacker toy small, organic wooden stacking toy","wooden toy sapling stacker small, personalized stacking toy","Waldorf Toys - Educational Toys - Montessori - Baby First Christmas - Rainbow Stacker - Toddler Toy","personalized wooden toy sapling stacker, stacking blocks organic kids toy","Personalized Sapling Stacker Toy natural wooden kids toy stacking toy","wooden toy sapling stacker, stacking blocks organic kids toy","wooden toy sapling stacker small, stacking blocks eco-friendly kids toy","wooden toy sapling stacker small, stacking blocks eco-friendly kids toy","Wooden Toy Sapling Stacker, stacking blocks organic kids toy","Sapling Stacker Wood Toy - personalize it!","Circle Sapling Stacker Toy","Stacker - Circle","Sapling Stacker Wood Toy","Circle Sapling Stacker Toy - Handmade Wooden Toy - Stacking Toy - Educational Toy - Wood Puzzle - Wood Toy - Toddler Toy - Circle Toy -TY34"]
	shipped_items = shipped_items.replace(to_replace= stacker_names, value="Sapling Stacker Toy")
	toolset_names = ["Wooden Tool Set Toy - Add Personalized Toolbox","Wooden Tool Set Toy - No Thanks","Tool Set Toy","Wooden Tool Set Toy - Add Toolbox","Wooden Tool Set Toy - Add Personalized Toolbox","Birthday Gift - Tool Set Kids - 1st Birthday Gift - Baby Boy","Kid's Tool Set Wooden Toy"]
	shipped_items = shipped_items.replace(to_replace=toolset_names,value="Wooden Tool Set Toy")
	return shipped, shipped_items

def read_maps():
	usa = geopandas.read_file('cb_2017_us_state_500k.shp')
	population = pd.read_csv('population_data.csv')

	population = population.set_index('NAME')
	usa = usa.set_index('NAME')

	usa["Population"] = population['POPESTIMATE2017']

	return usa