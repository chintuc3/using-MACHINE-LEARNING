Autocorrection, also known as text replacement, replace-as-you- type or simply autocorrect, is an automatic data validation function commonly found in word processors and text editing interfaces for smartphones and tablet computers.
Its principal purpose is as part of the spell checker to correct common spelling or typing errors, saving time for the user. 
It is also used to automatically format text or insert special characters by recognizing particular character usage, saving the user from having to use more tedious functions. For any type of text processing or analysis, 
checking the spelling of the word is one of the basic requirements.
To achieve the best quality while making spelling corrections dictionary-based methods are not enough. In the backdrop of machine learning, autocorrect is purely based on Natural Language Processing.

![image](https://github.com/chintuc3/using-MACHINE-LEARNING/assets/141393677/723ff260-b002-457a-9aef-976b98fd9fc1)

![image](https://github.com/chintuc3/using-MACHINE-LEARNING/assets/141393677/76657df7-76c8-450d-bf0b-e46089558f5e)
requirements : pip install pyspellchecker==0.7.2

PySpellChecker: PySpellChecker is a Python library that provides spell-checking capabilities. 
It uses the SymSpell algorithm, which efficiently handles spelling mistakes, including insertion, deletion, substitution, and transposition errors. 
PySpellChecker offers a simple and straightforward way to perform spell checking and suggest corrections in Python.

 N Gram technique: An n-gram is considered to be a collection of ensuing characters of length N.N-gram analysis is a process to detect whether the entered words in the document are wrong spelled or not.
 Here we do not compare each word with the dictionary instead we use the N-gram method. If the place is said to be empty or deficient n-gram is found, Itis assumed as an incorrect, or it is assumed to be correct.
 If N is found to be 1 then it is a unigram, if N is 2
 then it is a Bigram, if N is 3 then it is a trigram etc. The n-grams algorithm is also referred as or a “neutral string-matching algorithm”

