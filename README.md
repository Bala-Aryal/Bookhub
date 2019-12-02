Open zip file
In terminal direct to folder
run python main.py keywords.csv books.json

An edge case that I ran into was if the same keyword was part of the same genre and scoring process
at first no score was shown, but when taken into consideration all keyword phrases are added together.
Another edge case that I found was that the program does not search continuously. For example
if 'word worm', 'worm work', 'word worm work' are the key words and the description is  'word worm work', the score for
'worm work' will not be accounted for. In order to resolve this issue, we would have to use an array of continuation points, to store the continuation.

I spent approximately 2.5 hours 
# Bookhub
