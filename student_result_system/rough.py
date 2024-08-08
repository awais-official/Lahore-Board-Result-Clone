import inflect
total_marks = 850
# Convert total marks to words
p = inflect.engine()
total_marks_words = p.number_to_words(total_marks)
print(total_marks_words)