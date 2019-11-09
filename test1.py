Objects and Data Structures Assessment Test
Test your knowledge.
Answer the following questions

Write a brief description of all the following Object Types and Data Structures we've learned about:

Numbers: це тип змінюваний тип даних, розділяюється на цілочисельний та з плаваючою комою.використовують для математичних операцій як приклад

Strings: незмінювавий(immutable) тип даних. можна створити як в '' та і в "". Один з основих методів стрінги - len(str) - для визначення довжини стрінги. стрінга є набором символів

Lists: змінювана(mutable) структура даних, аля масив. Може містити різні типи. Створюється через функцію list() та через []. підтримує вложеність тобто в одному лісті може бути ще кілька лісті чи словників чи будь чого і тд.

Tuples: незмінювана структура даних(схожий на ліст). може містити різні типи даних. створюється через () або функцію tuples() або t = 1,...як і лііст чи стрінга - це послідовність(тобто дотримується кожен елемент індексації, індексація починається з 0)

Dictionaries: змінювана структура даних. Це лише відображення а не послідовність(тобто не має індексації, а доступ здійнюється по ключу). Містить пару 'ключ': 'значення'. ствоюється за допомогою функції dict() або {}. Також підтримую вложеність

Numbers
Write an equation that uses multiplication, division, an exponent, addition, and subtraction that is equal to 100.25.
100.25**1
90.25+10
102.25-2
50*2.005
200.50/2

Explain what the cell below will produce and why.
2/3 = 0 (тому що це цілочисельне ділення без остачі, з заокругленням до  меншого)
Can you change it so the answer is correct?
2.00/3

Answer these 3 questions without typing code. Then type code to check your answer.

What is the value of the expression 4 * (6 + 5) = 44

What is the value of the expression 4 * 6 + 5 = 29

What is the value of the expression 4 + 6 * 5 = 34

What is the type of the result of the expression 3 + 1.5 + 4?
3 + 1.5 + 4 = 8.5

What would you use to find a number’s square root, as well as its square?
number’s square root - number**0.5
square - number**2

Strings
Given the string 'hello' give an index command that returns 'e'. Use the code below:
s = 'hello'
# Print out 'e' using indexing
print s[1]

Reverse the string 'hello' using indexing:
s ='hello'

# Reverse the string using indexing
print s[::-1]

Lists
Build this list [0,0,0] two separate ways.
1. s = list('000')
2. s = [0,0,0]
3. s = [0 for i in range(3)]

Reassign 'hello' in this nested list to say 'goodbye' item in this list:
l = [1,2,[3,4,'hello']]
l[2][2] = 'goodbye'

Sort the list below:
l = [5,3,4,6,1]
l.sort()

Dictionaries
Using keys and indexing, grab the 'hello' from the following dictionaries:
d = {'simple_key':'hello'}
print d['simple_key']

d = {'k1':{'k2':'hello'}}
print d['k1']['k2']

d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print d['k1'][0]['nest_key'][1]

Can you sort a dictionary? Why or why not?
Не можу відсортувати словник бо це не послідовність.

Tuples
What is the major difference between tuples and lists?
кортежі не є змінювані

How do you create a tuple?
(); s=1,

Sets
What is unique about a set?
елементи в множині не можуть повторюватись а є унікальними

Use a set to find the unique values of the list below:
l = [1,2,2,33,4,4,11,22,3,3,2]
print set(l)

Final Question: What is the boolean output of the cell block below?
# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

#True or False?
l_one[2][0] >= l_two[2]['k1']
output - false

Booleans
For the following quiz questions, we will get a preview of comparison operators:

Operator	Description	Example
==	If the values of two operands are equal, then the condition becomes true.	(a == b) is not true.
!=	If values of two operands are not equal, then condition becomes true.
<>	If values of two operands are not equal, then condition becomes true.	(a <> b) is true. This is similar to != operator.
>	If the value of left operand is greater than the value of right operand, then condition becomes true.	(a > b) is not true.
<	If the value of left operand is less than the value of right operand, then condition becomes true.	(a < b) is true.
>=	If the value of left operand is greater than or equal to the value of right operand, then condition becomes true.	(a >= b) is not true.
<=	If the value of left operand is less than or equal to the value of right operand, then condition becomes true.	(a <= b) is true.
