# Quiz_Game
Multi-File "QuizGame" made with Python. Interacts with the Open Trivia DB API to provide a "True/False" quiz game for the user with ever-refreshing questions.

![](https://github.com/rifleben/Quiz_Game/blob/main/quiz_game.gif)


## Summary:

The program requests data from the Open Trivia DB API to build a "deck" of 10 questions. The program then presents a "flashcard" to the user, and two buttons (True/False) are available for the user to select their answer. Once the user selects their response, the program will alert the user of the correctness via changing the background of the canvas (Green for correct, Red for incorrect) and updating their score. Once the user has answered all ten questions, a final "END OF GAME" card will be displayed, and the selector buttons will be disabled.



### Tools Used:
- Python Packages:
  - tkinter (GUI interface)
  - requests (to request data from API)
  - html (to unescape data from the API)
  
- IDE:
  - PyCharm
