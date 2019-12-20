# Implementing K MEANS Algorithm

### Files Included:
* **K_MEANS.py**:
    * Implements the K_MEANS unsupervised learning algorithm.
	* Used Jaccard Distance to calculate the distance between various tweets for clustering.
* **datasets.txt**:
    * All the datasets should be inside the same folder.
	
## Requirements
* Python 3
* Command Line Interface

## Steps to run the program
* Open the CLI and run the command, *python K_MEANS.py name_of_dataset staring_value_of_k final_value_of_k difference_between_each_value_of_k*
* Replace the *name_of_dataset* in the above command with the value of the datset, on which we want to run K-MEANS.
* Replace the *staring_value_of_k* in the above command with the value of how many neighbors you want in starting.
* Replace the *final_value_of_k* in the above command with the value of how many neighbors you want in thee end.
* Replace the *difference_between_each_value_of_k* in the above command with the value of the difference between 2 consecutive k

### Example Run commands
* **usnewshealth Dataset**: _python3 K_MEANS.py usnewshealth.txt 5 30 5
* **goodhealth Dataset**: _python3 K_MEANS.py goodhealth.txt 5 30 5
