# CS151 PROGRAMMING ASSIGNMENT #2
50  POINTS (10pts design, 40pts final)                                  			
DESIGN DUE: 09/27/17  
FINAL DUE: 10/04/17

## I. PROBLEM:
You are creating a text adventure game!  In this game, the user gives input that affects the path of the story. You must create a game that meets the requirements in the specification below.

## II. PURPOSE OF THE ASSIGNMENT
The purpose of this assignment is to give you  
1.	practice with input & output  
2.	the opportunity to use decision making  
3.	a chance to be creative

## III. REQUIREMENTS ANALYSIS 
The first stage in your programming assignment is the requirements analysis stage.  You need to make sure you understand the below requirements for what needs to be included in your story's decision making:

1. Your adventure game must ask the user at least 1 question using each of the following types:  
  a. Make a decision based on the value of an integer input.  
  b. Make a decision based on the value of a float input.  
  c. Make a decision based on the value of a string input.  
2. Your adventure game must have a path with at least 2 decisions on it (e.g. I am given the option of choosing A or B. I make choice A which then lets me decide between X and Y; but if I choose B I do not get to choose between X and Y, but instead do something else).   
3. Your adventure game must have at least 1 choice that has at least 3 possible directions (for example, when they enter a number the game takes a different path if their number is <5, between 5 and 10, or > 10).  
4. Your adventure game must use at least 3 different boolean operators throughout the story  
5. Your adventure game must have a decision where it gives the user at least two specific inputs to choose from, and does something different based on which value they input (e.g. "enter 'green', 'red', or 'yellow'")  
6. Your adventure game must use something the user input in part of the output at least once (e.g., asking for their name and then outputting their name every time you address them).

The game must make sense and have an actual story to it. It needs to be understandable. Consider that your professor will be reading the entire story.

**An Example Game:**
An example game can be seen at http://www.youtube.com/watch?v=x0Ksedq3Z5k (from Dr.Olsen). It does not show all of the requirements from above, but does demonstrate a number of them. If you are having trouble understanding what is being asked of you in this assignment, be sure to watch the video.

## IV. DESIGN
The second stage is to design your solution based on the requirements:

1. Write out your algorithm, including input, output, decisions, and calculations.  
  A. Be sure to indent and properly number to show when a decision is nested inside another decision.  
  B. If you have story elements that are used in multiple paths, you can label them as "story part 1","story part 2", etc  and then reference them by that name the next time it's used, instead of writing it all out again. However you must give your full story as part of your design. Don't write your entire algorithm by just saying "story part X".
2. Double check that you included all of the requirements

If you are having trouble coming up with a story, think about a book or movie you enjoyed. Be inspired by its story line or characters and come up with something original.

**DESIGN SUBMISSION: 9/27/17**  
Submit to Moodle and on paper in class: the algorithm for your adventure game in designInitial.txt.

*Remember to double check on github.com that your files pushed. If they didn't, you need to push them. I can only see what is on github.com, not what is only on your computer.*

## V. PROGRAMMING REQUIREMENTS
After your design is complete and correct, it's time to start programming and then testing:

1. Fix design issues: If there were issues with your design, either not meeting requirements or in the format, fix that before you start writing your code.
2. Implementation: Write your program following the requirements and based on your design.
  A. Follow good usability/HCI principles in your input and output (make it clear the type of input you are asking for)
  B. Remember to state the purpose of the program
3. Testing: Make sure it works correctly; give it sample input, and check that the output is correct.
  A. Create a flowchart, label the control paths, and list a test case for each control path.  Test that you can get through each path correctly. You do not need to put the full output in the flowchart, just make it clear what part of the output is there.
  B. Test your program using the input. If it doesn't give the expected output, find the error and fix it.

## VI. EXTRA CREDIT (only if everything else works)
If you choose to do extra credit, it must be submitted in a separate file with "ExtraCredit" in the file name. 
Create a longer story line, with paths where there are at least 3 decisions in a row. At least one of these decisions must use "and" or "or" to combine multiple boolean expressions into a single decision.
Briefly note in your introductory comments what was added for the extra credit.

## VII.	ASSIGNMENT REMINDERS
Follow the programming assignment requirements document for comments, formatting, etc.

## VIII.	FINAL SUBMISSION   
1. To GitHub:  
  A. Your .py file  
  B. Your extra credit .py file if you did the extra credit (make sure "ExtraCredit" is in the filename)  
2. To Moodle:
  A. Your .py file(s)
  B. Your extra credit .py file if you did the extra credit (make sure "ExtraCredit" is in the filename)  
  C. A flowchart of your program with control paths labeled  (as a pdf or picture)
  D. Your test cases based on your flowchart in testcases.txt. You should have at least 1 test case per control path, using boundary values (see ppt slides).  
  E. Your final algorithm, including the changes you made based on the design feedback in designFinal.txt
3. On paper:
  A. Your .py file(s)
  B. Your extra credit .py file if you did the extra credit (make sure "ExtraCredit" is in the filename)  
  C. A flowchart of your program with control paths labeled  (as a pdf or picture)

***Remember to double check on github.com (and Moodle) that your files pushed. If they didn't, you need to push them. I can only see what is on github.com and Moodle, not what is only on your computer.
