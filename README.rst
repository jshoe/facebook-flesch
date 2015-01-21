===================
Facebook Flesch-Kincaid tester
===================

This Hackathon project was intended to calculate and present Facebook users with their personal Flesch-Kincaid writing grade level, calculated from a sample of the user's messages on Facebook.

The application would leverage Facebook's Python API to authenticate over OAuth. Then the application would download user messages in JSON format and parse the messages to produce a tally of total words, total sentences, and total syllables (from a word list). Finally the application would present the calculated score to the user and allow them to share it on their profile or compare it to the stored scores of their friends.

The Flesch-Kincaid Grade Level formula we would implement is roughly Grade_Level = 0.39(total_words / total_sentences) + 11.8(total_syllables / total_words) - 15.59.

More info: http://en.wikipedia.org/wiki/Flesch%E2%80%93Kincaid_readability_tests