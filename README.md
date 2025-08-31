# Qualifier for Code Jam 12 Python Discord
## By mhasanali2010 (discord: ryushison)


## About the project
For the qualifier of the Python Discord Community's Code Jam 12, we were required to make an imitation of Javascript's querySelectorAll in Python.

## My take on the project
Since I was new to Python and coding in general at the time, I did not know of RegEx (Regular Expressions) which was used by most of my peers to solve the problem and qualify. I used a nest of IF and ELIF statements to select the nodes which matched the selector(s). Each of the conditional statements were based on my understanding of what the possible combinations of selectors could be.

## How to use
Example usage is shown in `./example_usage.py`. Just clone the repository and try it for yourself if you want to. The query_selector_all is in the `./qualifier.py` file. Node class is in `./node.py` and test cases which were provided by Python Discord can be found in `./tests.py`.

### Setup and Usage
- To clone the repository: `git clone https://github.com/mhasanali2010/code-jam-12-qualifier`
- Example Usage:
```python
from qualifier import query_selector_all
from node import Node

node = Node() # details of the node go here
selector = '#home-link' # css selector
matched_nodes = query_selector_all(node, selector) # returns a list
```

## Notes
- This has only been tested using `Python 3.13`.
- No external library is required. Only Python stdlib functions are used.
- All other needed files are already given.
- This is not the exact version that I used to qualify, some changes have been made.
- CSS selector can be a mix of tag, ID and class(es).
- There can be multiple selectors (comma separated)
