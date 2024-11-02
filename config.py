################################################################################
# SMTP configuration settings.
################################################################################
smtp = {
    'username': 'pierrick_mailserver@mg.blaise.lc',
    'password': 'Moonwalk9-Defraud-Uncertain',
    'host': 'smtp.eu.mailgun.org',
    'port': 587,
    'from_email': 'secretsanta@blaise.lc',
}

################################################################################
# This the secret santa letter template that is used to send everyone the email.
# Note that {santa} and {recipient} are automatically replaced by the secret
# santa's name, and his/her recipient of their gift.
################################################################################
email_template = {
    'from_name': 'Secret Santa',
    'from_email': smtp['from_email'],
    'subject': 'Family Christmas',
    'body': """
Ho Ho Ho!

{santa}, tu es le secret santa de {recipient1}, {recipient2} et {recipient3} !

Merry Christmas!
"""
}

################################################################################
# The complete list of all the secret santa's and their email addresses.
################################################################################
santas = {
    # 'James': 'james@example.com',
    'Pierrick' : 'pierrick@blaise.lc',
    'Siona' : 'siona@blaise.lc',
    'Joyce' : 'joyce@blaise.lc',
    'Genevieve' : 'genevieve@blaise.lc',
    'Emmanuelle' : 'emmanuelle@blaise.lc',
    'Soline' : 'soline@blaise.lc',
    'Hugo' : 'hugo@blaise.lc',
    'Benoit' : 'benoit@blaise.lc'
}

################################################################################
# This contains a dictionary lookup of santa's (keys) who are not allowed to
# have particular recipients (values).
#
# If there are no incompatibles, leave this dictionary empty.
################################################################################
incompatibles = {
    # Do not allow James to be santa for Mary
    # 'James': ('Mary',),

    # Do not allow Mary to be santa for James
    # 'Mary': ('James',),

    # Do not allow Nancy to be santa for John or Mary
    # 'Nancy': ('John', 'Mary',),

    # Something like below is bad, Linda can't be a secret santa for anyone!
#   'Linda': ('James', 'Mary', 'Nancy', 'John', 'Michael', 'Lisa', 'David'),
}

################################################################################
# DON'T PEAK INTO THIS FILE!
#
# This file will contain a record of what was emailed. It will reveal who is
# everyone's secret santa.
################################################################################
secret_santa_record_file = 'secret-santa-record-file.txt'
