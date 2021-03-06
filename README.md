# Advent of Code 2020

Hi! I'm using the Advent of Code (https://adventofcode.com/2020) to learn python and here you will find all of my solutions. I got up to Day 13 before the challeneges became too technical for someone starting out in Python. 13 days is better than none and it was definitly a good early introduction to Python. 

The alternative solutions (day*Alt.py files) are created after I've completed the days challenge by comparing my solution to that of Jonathan Paulson (https://www.youtube.com/channel/UCuWLIm0l4sDpEe28t41WITA/featured)

Below is a diary of the main take-aways from each day and the main things I have learned within python.

  * [Day 1](#day-1)
  * [Day 2](#day-2)
  * [Day 3](#day-3)
  * [Day 4](#day-4)
  * [Day 5](#day-5)
  * [Day 6](#day-6)
  * [Day 7](#day-7)
  * [Day 8](#day-8)
  * [Day 9](#day-9)
  * [Day 10](#day-10)
  * [Day 11](#day-11)
  * [Day 12](#day-12)
  * [Day 13](#day-13)

## Day 1
This challenge mainly consisted of me learning basic python syntax including for loops and if statements. Additionally, finding the correct syntax for importing my data was challenging and then learning how to read this data.

## Day 2
Day 2 consisted of a big learning curve in string manipulation. Being a mainly R user dealing with statistics this isn't something I have much experience in. I also learned about dictionaries and after taking a while to get my head around the setup of deafaultdict this makes more sense and will be useful in the future for key value pairs. Additionally, spent longer than I care to admit trying to come up with the logical statements for one being true but not both - turns out the python xor function is useful here!

## Day 3
Day 3 was a very different style of problem than I've seen before, however noticing the use of the mod function actually meant it wasn't too difficult. The use of the while loop in the alternative solution was cleaner allowed the integration of the different slopes in a way that wasn't constantly cycling through if statements. Really enjoying pythons use of += \*= etc much easier than the cumbersome way in R.

## Day 4
The challenge was rather cumbersome as there was many rules to makes and cycle through. This was a steep learning curve in regrex expressions for finding string expressions. I found getting the basics of regrex from the internet was harder than it should have been and a cheat sheet for regrex may be useful (future side project maybe?). An annoying part was that the passports were over multiple lines and separated by an empty line. Luckily, the alternative solution showed me a nice way around this which I'm sure will be useful in future challenges. Basically having an if statement for each line where if it is NOT empty then you just add it to a data structure (here a dictionary) and then when you have an empty line, that's when you do the analysis on everything you've collected. Again the alternative had a good use of dictionaries (hopefully I'll spot the next time this data structure will be useful!!). Finally, the alternative introduced me to my first function!

First, started using python-mode IDE (https://github.com/python-mode/python-mode) today instead of a jupyter plugin for integrating python into vim. Big fan of vim-python so far, even if adhering to PEP-8 rules can be frustrating.

## Day 5
First, truly annoying challenge! Tried creating some new functions, storing them in a different file and then import them - could I do this for a good hour; no. Eventually, figured out using **from *file* import *func1, func2* ** or you have to specify the file when using the function ie ** file.func1() ** if you just import the file. Managed to struggle though the rest of the challenge using lots of **for loops** and **if** statements. 

The alternative method today made use of some binary trick however I felt this was a bit too niche to focus on here so I just stuck with my implementation. 

## Day 6
Finally spotted a good use for dictionaries! Was really happy with my solution to this challenge as I made use of tricks learned for earlier challenges; namely using a dictionary and how to deal with line separated data. 

Turns out a could have done this without a dictionary but ah well! The alternative code was interesting and introduced me to sets. I particularly liked how you can do **and** and **or** statements on sets which is a nice new trick that could speed up future problems like this. If you have a 2 sets and do ** set1 & set2** then you get a set with just the elements that are in both.

## Day 7
First, failure day :'( 

Spent a long time trying to learn some tree structure to try and implement this problem however it just wasn't happening. The trick I found was using a **deque** along with **dictionaries**. Took me a while to figure these out but once I got my head around it I feel I could answer a similar problem now. Also, saw a function which calls the function within itself in order to loop backwards. Still not entirely comfortable with this and need to fully understand how these work and are implemented at a deeper level to trust them.

## Day 8
Our first day where our solution was similar enough to the alternative that I didn't need to code up the alternative! Found this challenge surprisingly easy especially compared to Day 7. One annoyance was trying to keep an original list and recursively altering parts of it. Turns out you have to slice the original list in order to stop it being altered itself. Apart from this an easier challenge!


## Day 9
First day where I feel my solution was more elegant than the alternative. I made use of **deque** which was nice after learning about these in Day 7. Maybe need to find a way of having less checking variables to break code more subtly once the answer has been found. The alternative was less lines of code however a lot slower as it looped though the data more than our. Found a neat solution to finding 2 numbers from a list that add to a target number which doesn't need to look though the data multiple times. I learned a lot about list slicing using the alternative including the **a:b** style where** a** is inclusive while **b** is exclusive. This should be helpful for future challenges.

## Day 10
First part of day 10 was super easy; sort the data and count the difference sizes. However, part 2 was a nightmare. The aim was to count the number of possible combinations of adapters that still worked. I had a thought about using a recursive function and should have continued down this path - instead I tried coming up with all possible combinations of adapters and checking how many were valid. This caused me to run out of memory and so we had to look to the alternative. 

This brought me to dynamic programming. I've come across DPs quite a bit in my PhD for solving changepoint problems however coding one using a recursive function I haven't done - learning time. So if you are looking at the code in the day10Alt.py file you will see what I'm going to explain. The key part is we for each position we want to see how many ways there are to get to the end. So we start with the first entry and then cycle though the possible next steps. In this case it will be the second entry, now however we want all the paths from the second entry to the end so again we cycle through these. What ends up happening is we cycle through all the way to the last entry (we then hit the **return 1**) now we start cycling backwards through the data. So we almost retreat or i a step and then look for the next j that we haven't already looked at. Now if we finish all the possible j's for that i then we know all the possible paths from i to the end so we can store this for future reference. We will then move back another i and start looking through all the j's past i that we haven't already looked at (making use of the stored number of paths to the end if that j appears.

This took me a while to get my head around but I feel I could now code one myself for a similar project. In the end a disappointing day that I didn't finish without help but a good learning day for DPs!

## Day  11
First part was do-able although long. Had to write out lots of rules, meaning loads of nested **for** and **while** loops and **if** statements. I took a long time to figure out about deepcopys in python. In R using *=* just assigns one thing to another object, easy. In python it is used as a pointer. This makes performing lots of operations before updating the whole grid more difficult; which was the case here. However I was pleased to see in the alternative this was the correct way to do this!

Part 2 I read and then thought I will come back to this another day (it was Xmas party day tbf!). In the end I think I over complicated part 2 in my head and showed I need to become more comfortable with **while** loops. Looking at the alternative for the answer I found it was actually vary similar to part 1 with a few extra (you guessed it) **while** loops. Take-aways from day 11 are **deepcopy** and utilize while loops more!

## Day 12
We finished a day in a reasonable time!! Lot of **if** and **elif** statements and got there using a list [North, East] for the ships position. Then saw in the alternative it is much easier to just use two variables. Additionally, the alternative showed me its probably nicer to have a for loop repeating the direction changes rather than 3 if statements - definitely looks cleaner. Also, was nice how the set directions were used DX and DY rather than writing out again 4 different if statements. 

Overall a good day and alternative provided us with some tricks for making our code more neat.

## Day 13
First true failure day. Part one was very easy using basic mods and just remembering to be careful about which way around the wait time is (not the time since the last bus but the time until the next bus). 

Part 2 I had no idea how to go about this and imagined it would be some trick with mods. I was right and the alternative was done using the Chinese Remainder Theorem. However, after listening to the explanation of this I deemed it wasn't worth the extensive time needed to understand all this and code it up. Sometimes its better to just move on and save a lesson for another day when it might be more relevant - I struggle to see myself using the Chinese remainder theorem anytime soon!
