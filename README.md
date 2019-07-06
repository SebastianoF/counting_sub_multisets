
## Counting sub-multisets of fixed cardinality


<p align="center"> 
<img src="https://github.com/SebastianoF/counting_sub_multisets/blob/master/mandms.jpg" width="350">
</p>

<!---
![emmemems](https://github.com/SebastianoF/counting_sub_multisets/blob/master/mandms.jpg)
--> 

**How many distinct handfuls of 7 may be drawn from a packet containing 4 blue candies, 3 green ones, 3 red, 2 orange and 1 yellow?**


The code here provided is a tool to compute the answer to this one and similar questions, both with brute force and with an enumerative combinatorics 
 closed form formula. 
Theoretical grounds about the closed form computations can be found here: http://arxiv.org/abs/1511.06142 . 
Use the same link to cite the code.

### Python version
Based on python 3.5+. All the methods and main_example.py are back compatible with python 2.7. Use python 3 to have optimal performance (see [xrange](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html#xrange)).

### Install
To install the required libraries, please install [pip](https://pypi.python.org/pypi/pip) and run 

* `pip install -r requirements.txt`

### Testing
Unit testing with [pytest](https://docs.pytest.org/en/latest/):

* `pytest .`

### License
Counting_sub_multisets is licensed under the terms of the
[MIT](https://choosealicense.com/licenses/mit/) or any later version.