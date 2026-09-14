Summary of AI Assistance

AI was only used where the explicit permission was given and also to summarise for clear and better understanding.

In Part C, AI was used to improve:  book_appointment() function, following the required prompt structure: explain what the code does, identify three limitations, suggest improvements, and ask questions to check understanding, without rewriting the whole application. It correctly explained the function's behaviour and named real issues — no duplicate-booking check, appointment time stored as a plain string, and no unique IDs for referencing appointments later.

In Part D, AI was used to generate an alternative version of the same function, under two explicit constraints: no database and no GUI. It produced a version that split the logic into four smaller functions instead of two, but it also made an unstated assumption that every input would always be valid, so it added no validation for blank names, None values, or duplicate bookings.

Beyond these two sections, AI was not used to write code — the base prototype, the choice of which one improvement to make, the implementation of that improvement, and all verification testing were done independently, with AI's role limited.