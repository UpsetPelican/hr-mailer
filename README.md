# SMTP Kromailer
Simple Mailer from template and using Excel as "database".

## But whyyy?
Because we needed a simple way of sending mails to candidates using a template and a .xlsx document.

### Yes, but whyyyyy xlsx when you could've use a database?
For simplicity sake! I only had two days (and a weekend) to code this pilot and I'm super bad at coding.

### Ok, how does it work?
Ok, so you have the template which is a simple .txt which is loaded and replaced with the information from the "database".

Then, you have your "database" which has 4 columns.
- email
- name
- position
- sent

The first three are self-explanatory; name, email and position are the fields about your candidate, then the 
"sent" field, when you run `python mailer.py` there is a loop that checks if "sent" is empty, if true, sends the email
to that entry and add a timestamp in there so the user can track when the email was sent, else, it will skip that row. 
Simple huh?


### Ok, so how did you do it?
Found two great libraries of which I fell in love with.
- [Yagmail](https://github.com/kootenpv/yagmail). Which is the thing that sends emails and makes it soooo easy.
- [Pyexcel](https://github.com/pyexcel/pyexcel). A Python wrapper for spreasheet manipulation.

### You convinced me, I want to give it a try.
Awesome, First clone the repo, and give the "database" some true data.

Then change the email in `mailer.py` for your own.

And lastly run `python mailer.py`

### Troubleshooting
So it worked with my SMTP Google company email just fine, but had trouble with another account of the .com address book.

- First I was directed [here](https://support.google.com/mail/answer/7126229?visit_id=1-636316842412718237-1180349011&rd=2#cantsignin) from the exception raised in the code.
  - Troubled user does not have 2FA enabled so this was a far shot.
- Then found [this](http://joequery.me/guides/python-smtp-authenticationerror/) which is the same error code I was having.
  - Didn't work.
- Finally contacted the IT who had the answer all along.
  - You have to allow "less secure" applications, you can do it [here](https://support.google.com/accounts/answer/6010255?hl=en)!
  
