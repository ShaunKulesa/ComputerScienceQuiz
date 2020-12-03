import sqlite3
import os
import random
 
conn = sqlite3.connect('questions.db')
 
c = conn.cursor()
 
c.execute('''CREATE TABLE questions
             (question text, answers1 text, answers2 text, answers3 text, answers4 text, correct text)''')
 
c.execute("INSERT INTO questions VALUES ('What is 1 megabyte in kilobytes?', '1000', '1024', '1100', '1001', '1024')")
c.execute("INSERT INTO questions VALUES ('What does CPU stand for?', 'Central Programming Unit', 'Computer Processing Unit', 'Central Processing Unit', 'Computer Programming Unit', 'Central Processing Unit')")
c.execute("INSERT INTO questions VALUES ('What is a processor measured in?', ' Hertz', 'Milliseconds', 'Bits', ' Processes', ' Hertz')")
c.execute("INSERT INTO questions VALUES ('What protocol is used to send (outgoing) emails?', 'POP', 'IMAP', 'HTTP', ' SMTP', ' SMTP')")
c.execute("INSERT INTO questions VALUES ('Which is a type of low level language?', 'Machine Code', 'Python', 'PHP', 'JavaScript', 'Machine Code')")
 
# rq_int = random.sample(range(1,5), 3)
# print(rq_int)
 
# for row in c.execute('SELECT question FROM questions WHERE rowid = ?', (rq_int[0],)):
#     print(row)
 
conn.commit()
 
conn.close()
 
# os.remove("questions.db")