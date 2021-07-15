# python-challenge homework

## PyBank

The main.py Python script in the PyBank subfolder will open the 'budget_data.csv' file, which is composed of two columns: `Date` and `Profit/Losses`, from the Resources subfolder.

After skipping the header row, the first month's profit/loss amount is initialized in the variables `last_month` and `total_amount`.

A For loop will go through each row and append the date and profit/losses into the `raw_data` list.  The cumulative profit/losses will be store in the variable `total_amount`.  The monthly change in profit/losses will be stored in the variable `monthly_total`.

An If statement will compare the current month's profit/loss to the values stored in variables.  If the amount is greater or less than the stored amounts, the date and amount will be recorded in the variables.

The following output will be printed on the terminal and saved as a text file, pybank_results.txt, in the Analysis subfolder:

* The total number of months included in the dataset

* The net total amount of "Profit/Losses" over the entire period

* The average change in "Profit/Losses" over the entire period

* The greatest increase in profits (date and amount) over the entire period

* The greatest decrease in profits (date and amount) over the entire period



## PyPoll

The main.py Python script in the PyPoll subfolder will open the 'election_data.csv' file, which is composed of three columns: `Voter ID`, `County`, and `Candidate`, from the Resources subfolder.

After skipping the header row, a For loop will store the `Candidate` value from all remaining rows  into the list `all_candidates`.  An If statement will append all unique candidate names into the list `unique_candidates`.

A For loop will go through each name in the `unique_candidates` list and store each occurrence of the name into the variable `counts`, and store each `counts` value with the candidate name into the list `candidate_votes`.

The total votes cast in the election will be calculated by the length of the `all_candidates` list and stored in the variable `total_votes`.

The `candidate_votes` list will be reverse sorted by the `counts` value to order candidates from highest to lowest votes.

The following output will be printed on the terminal and saved save as the text file, PyPoll_results.txt, in the Analysis subfolder:

* The total number of votes cast from `total_votes`

* A complete list of candidates who received votes and the total number of votes they received from `candidate_votes`

* The percentage of votes each candidate won formatted to three decimal places

* The winner of the election based on popular vote from the first element in the reverse sorted `candidate_votes` list
