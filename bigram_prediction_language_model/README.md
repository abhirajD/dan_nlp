guage Model - Prediction 
### Bigram Model and smoothing

Hola, People! 
One application of building a language model is that you can predicting new Sentences or Text Block learnt from that language. [This](https://github.com/abhirajD/dan_nlp/blob/master/bigram_predictor/bigram_langmodel.py) sub-repo does exactly that. 

*Note:* The bigram model also supports plus-one smoothing.

## Getting Started

**bigram_langmodel.py** takes:
* *Corpus.txt* which is a raw dump of apple news here, can be replaced by any corpus.
* *sentence1* and *sentence2* for testing the predictablity of model. The model will throw probabilities of belonging of these sentences to the language model. 

Once downloaded and ready hit:
```bash
python bigram_langmodel.py <Corpus.txt> <Sentence1> <Sentence2>
```


### Prerequisites

To Draw those pretty pretty tables: [Tabulate](https://pypi.python.org/pypi/tabulate)

```python
pip install tabulate
```

## Sample output
For:
```bash 
python bigram_langmodel.py Corpus.txt  'Apple inc is launching iphone' 'An apple a day keeps doctor away'
```
Following predictions are generated:
```
+++::SMOOTHING::FALSE+++
===========================================================================================
::SENTENCE =  <s> apple inc is launching iphone <\s>
___________________________________________________________________________
:WORD COUNT TABLE
*            <s>    apple    inc    is    launching    iphone    <\s>
---------  -----  -------  -----  ----  -----------  --------  ------
<s>            0       61      0     0            0         0       0
apple          0        0      7     7            0         2       8
inc            0        0      0     2            0         0       0
is             0        0      0     0            0         0       0
launching      0        0      0     0            0         0       0
iphone         0        1      0     0            0         0       2
<\s>           0        0      0     0            0         0       0
___________________________________________________________________________
:WORD PROBABILITY TABLE
*            <s>     apple        inc         is    launching     iphone       <\s>
---------  -----  --------  ---------  ---------  -----------  ---------  ---------
<s>            0  0         0          0                    0  0          0
apple          0  0         0.0153846  0.0153846            0  0.0043956  0.0175824
inc            0  0         0          0.153846             0  0          0
is             0  0         0          0                    0  0          0
launching      0  0         0          0                    0  0          0
iphone         0  0.016129  0          0                    0  0          0.0322581
<\s>           0  0         0          0                    0  0          0
___________________________________________________________________________
::PROBABILITY =  0.20148883374689827 

===========================================================================================
::SENTENCE =  <s> an apple a day keeps doctor away <\s>
___________________________________________________________________________
:WORD COUNT TABLE
*         <s>    an    apple    a    day    keeps    doctor    away    <\s>
------  -----  ----  -------  ---  -----  -------  --------  ------  ------
<s>         0     3       61   11      0        0         0       0       0
an          0     0        9    0      0        0         0       0       0
apple       0     0        0    1      0        0         0       0       8
a           0     0        0    0      1        0         0       0       0
day         0     0        0    0      0        0         0       0       0
keeps       0     0        0    0      0        0         0       0       0
doctor      0     0        0    0      0        0         0       0       0
away        0     0        0    1      0        0         0       0       0
<\s>        0     0        0    0      0        0         0       0       0
___________________________________________________________________________
:WORD PROBABILITY TABLE
*         <s>    an     apple          a         day    keeps    doctor    away       <\s>
------  -----  ----  --------  ---------  ----------  -------  --------  ------  ---------
<s>         0     0  0         0          0                 0         0       0  0
an          0     0  0.118421  0          0                 0         0       0  0
apple       0     0  0         0.0021978  0                 0         0       0  0.0175824
a           0     0  0         0          0.00318471        0         0       0  0
day         0     0  0         0          0                 0         0       0  0
keeps       0     0  0         0          0                 0         0       0  0
doctor      0     0  0         0          0                 0         0       0  0
away        0     0  0         0.142857   0                 0         0       0  0
<\s>        0     0  0         0          0                 0         0       0  0
___________________________________________________________________________
::PROBABILITY =  0.12380356820517732 

+++::SMOOTHING::TRUE+++
===========================================================================================
::SENTENCE =  <s> apple inc is launching iphone <\s>
___________________________________________________________________________
:WORD COUNT TABLE
*            <s>    apple    inc    is    launching    iphone    <\s>
---------  -----  -------  -----  ----  -----------  --------  ------
<s>            1       62      1     1            1         1       1
apple          1        1      8     8            1         3       9
inc            1        1      1     3            1         1       1
is             1        1      1     1            1         1       1
launching      1        1      1     1            1         1       1
iphone         1        2      1     1            1         1       3
<\s>           1        1      1     1            1         1       1
___________________________________________________________________________
:WORD PROBABILITY TABLE
*                  <s>        apple          inc           is    launching       iphone         <\s>
---------  -----------  -----------  -----------  -----------  -----------  -----------  -----------
<s>        0.00031348   0.0194357    0.00031348   0.00031348   0.00031348   0.00031348   0.00031348
apple      0.000274348  0.000274348  0.00219479   0.00219479   0.000274348  0.000823045  0.00246914
inc        0.000312207  0.000312207  0.000312207  0.000936622  0.000312207  0.000312207  0.000312207
is         0.000308356  0.000308356  0.000308356  0.000308356  0.000308356  0.000308356  0.000308356
launching  0.00031348   0.00031348   0.00031348   0.00031348   0.00031348   0.00031348   0.00031348
iphone     0.000307503  0.000615006  0.000307503  0.000307503  0.000307503  0.000307503  0.000922509
<\s>       0.00031348   0.00031348   0.00031348   0.00031348   0.00031348   0.00031348   0.00031348
___________________________________________________________________________
::PROBABILITY =  0.02411149128302595 

===========================================================================================
::SENTENCE =  <s> an apple a day keeps doctor away <\s>
___________________________________________________________________________
:WORD COUNT TABLE
*         <s>    an    apple    a    day    keeps    doctor    away    <\s>
------  -----  ----  -------  ---  -----  -------  --------  ------  ------
<s>         1     4       62   12      1        1         1       1       1
an          1     1       10    1      1        1         1       1       1
apple       1     1        1    2      1        1         1       1       9
a           1     1        1    1      2        1         1       1       1
day         1     1        1    1      1        1         1       1       1
keeps       1     1        1    1      1        1         1       1       1
doctor      1     1        1    1      1        1         1       1       1
away        1     1        1    2      1        1         1       1       1
<\s>        1     1        1    1      1        1         1       1       1
___________________________________________________________________________
:WORD PROBABILITY TABLE
*               <s>           an        apple            a          day        keeps       doctor         away         <\s>
------  -----------  -----------  -----------  -----------  -----------  -----------  -----------  -----------  -----------
<s>     0.00031348   0.00125392   0.0194357    0.00376176   0.00031348   0.00031348   0.00031348   0.00031348   0.00031348
an      0.000306185  0.000306185  0.00306185   0.000306185  0.000306185  0.000306185  0.000306185  0.000306185  0.000306185
apple   0.000274348  0.000274348  0.000274348  0.000548697  0.000274348  0.000274348  0.000274348  0.000274348  0.00246914
a       0.000285388  0.000285388  0.000285388  0.000285388  0.000570776  0.000285388  0.000285388  0.000285388  0.000285388
day     0.000313087  0.000313087  0.000313087  0.000313087  0.000313087  0.000313087  0.000313087  0.000313087  0.000313087
keeps   0.00031348   0.00031348   0.00031348   0.00031348   0.00031348   0.00031348   0.00031348   0.00031348   0.00031348
doctor  0.00031348   0.00031348   0.00031348   0.00031348   0.00031348   0.00031348   0.00031348   0.00031348   0.00031348
away    0.000312793  0.000312793  0.000312793  0.000625586  0.000312793  0.000312793  0.000312793  0.000312793  0.000312793
<\s>    0.00031348   0.00031348   0.00031348   0.00031348   0.00031348   0.00031348   0.00031348   0.00031348   0.00031348
___________________________________________________________________________
::PROBABILITY =  0.006688080482521803 
```

## Authors
**Abhiraj Darshankar** - [abhirajd](https://github.com/abhirajd)



Report bugs/issues/suggestions to abhirajd (abhiraj.darshankar@gmail.com)


