**Answer for Question 1:** Django signals are executed synchronously by default, meaning the signal handlers run in the same thread and process as the signal sender.

**Answer for Question 2:** Django signals run in the same thread as the caller, ensuring that the signal handlers execute within the context of the thread initiating the signal.

**Answer for Question 3:** Django signals run in the same database transaction as the caller by default, meaning any database changes made by signal handlers are part of the same transaction.

**Explanation for Rectangle class :** The Rectangle class creates a rectangle with a given length and width (50 and 25 respectively). You can loop through an instance of this class to get these dimensions. When you do, it shows the length and width one after the other. This example shows how to use Python’s iterator feature to access the rectangle’s details.
