
## Counting sub-multisets of fixed cardinality

![emmemems](https://github.com/SebastianoF/counting_sub_multisets/mandms.jpg)

How many distinct handfuls of 12 may be drawn from a packet containing 5 blue candies, 9 green ones and 14 red?

The code here provided compute the answer to this one and similar questions. Theoretical grounds about the closed form computations can be found here: http://arxiv.org/abs/1511.06142 . Please cite the paper if you use the code.

#### Python version
Based on python 3.5+. All the methods and main_example.py are back compatible with python 2.7. Use python 3 to have optimal performance (see [xrange](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html#xrange)).

#### Install
To install the required libraries, please install [pip](https://pypi.python.org/pypi/pip) and run 

* `pip install -r requirements.txt`

### Testing

Unit testing with [nosetest](http://pythontesting.net/framework/nose/nose-introduction/):
* `nosetests`

### License
<!--
% [![AGPLv3](https://www.gnu.org/graphics/agplv3-88x31.png)](https://choosealicense.com/licenses/mit/)
-->
Counting_sub_multisets is licensed under the terms of the
[MIT GPLv3](https://choosealicense.com/licenses/mit/) or any later version.