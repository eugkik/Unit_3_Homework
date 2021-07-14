# python-challenge homework







## PyPoll

The main.py Python script in the PyPoll subfolder will open the 'election_data.csv' file, which is composed of three columns: `Voter ID`, `County`, and `Candidate`, from the Resources subfolder.

After skipping the header row, a For loop will store the `Candidate` value from all remaining rows  into the list `all_candidates`.  An If statement will append all unique candidate names into the list `unique_candidates`.

A For loop will go through each name in the `unique_candidates` list and store each occurrence of the name into the variable `counts`, and store each `counts` value with the candidate name into the list `candidate_votes`.

The total votes cast in the election will be calculated by the length of the `all_candidates` list and stored in the variable `total_votes`.

The `candidate_votes` list will be reverse sorted by the `counts` value to order candidates from highest to lowest votes.

The following output will be written to the terminal and saved save as the text file, PyPoll_results.txt, in the Analysis subfolder:

* The total number of votes cast from `total_votes`

* A complete list of candidates who received votes and the total number of votes they received from `candidate_votes`

* The percentage of votes each candidate won formatted to three decimal places

* The winner of the election based on popular vote from the first element in the reverse sorted `candidate_votes` list
