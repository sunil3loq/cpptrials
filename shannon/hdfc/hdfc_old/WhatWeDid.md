
1. Generate Cardinality Reports
2. Generate Summarization Reports
3. Create following columns from mnemonics to characterize transactions:
   - CustInterface
   - Mode
   - txnType
   - Association
   - Recurring
   - Reversal
   - ThirdPartyFlag
   - PrematFlag
   - ReturnBounce
   - International
   - RetailForex
   - Bulk
   - Reject
   - SME
   - Bank
	Some of these columns were also made using the credit card transactions for those who have credit cards.
4. Create SuperTypes from few of the above columns.
5. Create product set for each user (for each month which product has been bought and  which has been churned)
6. Create Mastertable on quarterly basis by counting txns, and summing amount
7. Convert the supertype and other column values into unique columns for each quarter -
   This result in the one row for each user with txn count or sum for particular quarter
   under particular column for eg - credit for quarter 1
8. We add more columns based on the demographics (legal entity)
9. From fact txn table, we add more columns based on the type of service requests made
10. Take quarterly difference/quarterly ratios to create feature set for each user
	Many types of features were selected (binned versions of following)
		Sum on Columns (Credits,Debits, etc.)
		Transaction Count (on each of SuperType and overall)
		Difference/Ratio between quarters of above variables
		Binary like having retail forex, premature flag, etc.
		Number of Products/Flags in each of product groups we created (Personal Loan, Savings, Trading, Insurance, etc)
11. Bin them each ratio equally against the population (three bins)
12. Split feature set to test/train dataset - 
	Taking observation period as last quarter 
	Using the features made from the previous three quarters. 
	This method was selected against defining cohorts as we wanted to account for seasonal variations in financial transactions
13. Run train dataset through RandomForest to get some useful feature set.
	Due to limitations on the number of columns that can be input to ARM, we had to select the most important ones
	Random Forest ranks the variables in terms of incremental prediction the variable brings in an out of bag sample
14. On the resulting dataset, run the ARM.
	We are predicting if the user has bought the product in the observation period.
15. Get the model assessment parameters (confusion matrix)
16. Filter dataset for user who have bought product in 4th quarter.
17. Split in test/train.
18. Bin them (3 bins)
19. Run ARM on different combinations of feature sets.
20. Run rule parameter metric.
21. Convert rule from numeric to column name basis.
22. Get mutually exclusive rule set (based on greedy approach)
23. Get lift values.

Other Things We Tried:
1. Grouping mnemonics by kmeans on the variables like totalusers, total amount, min amount, max amount, etc.
2. Categorising the Unknown transactions using the bag of words analysis on the transaction description
3. Bag of Words to infer if the transactions where related to top merchants and other banks.
