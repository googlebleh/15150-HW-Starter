#!/usr/bin/env python2
__author__ = "Colin Wee"
__date__ = "2015-02-17"
__version__ = "0.2"

import sys, os
import datetime as dt, string
import ConfigParser

DATA_DIR = "resources"
TEMPLATE_FNAME = "template_mod.tex"
INFO_FNAME = "profile.cfg"
INFO_TITLE = "Student-Specific Information"
INFO_FIELDS = {
    "Name"        : "studentName",
    "Andrew ID"   : "andrewID",
    "Lab Section" : "labSection"
}

################################## Utilities ##################################

def formalDateToday():
    """Return a string representing today's date."""
    return dt.date.today().strftime("%B %d, %Y")

def digitsOnly(s):
    """Return True if s only contains digits only and False otherwise."""
    return (s == ''.join([c for c in s if c in string.digits]))

def YNInput(prompt=""):
    """Robustly accept yes/no input from user."""
    while True:
        cmd = raw_input("%sY/N --> " % prompt).upper()
        if cmd == "Y": return True
        elif cmd == "N": return False
        print "Invalid input. Try again."

def rawInputWithCheck(prompt):
    """Accept user input while allowing for correction of mistakes."""
    proceed = False
    i = None
    while not(proceed):
        i = raw_input(prompt)
        print "Is this correct?"
        print ' '*3, repr(i)
        proceed = YNInput(' '*2)
    return i

############################# Manage User Profile #############################

def initProfile():
    """
    Completes first-time setup of %s by taking user input.
    """ % os.path.join(DATA_DIR, INFO_FNAME)
    print "First time setup! You will only have to do this once."
    P = ConfigParser.RawConfigParser() # profile is a long word
    P.optionxform = str # preserve case in options
    P.add_section(INFO_TITLE)
    for field in INFO_FIELDS.keys():
        P.set(INFO_TITLE, field, rawInputWithCheck("\nEnter %s --> " % field))
    with open(os.path.join(DATA_DIR, INFO_FNAME), 'w') as F:
        P.write(F)

def readProfile():
    """Reads existing user info from %s""" os.path.join(DATA_DIR, INFO_FNAME)
    P = ConfigParser.RawConfigParser() # profile is a long word
    P.optionxform = str # preserve case in options
    P.read(os.path.join(DATA_DIR, INFO_FNAME))
    return dict(P.items(INFO_TITLE))

################################ Main Routine #################################

def main(argc, argv):
    print '#'*16, "15-150 Homework LaTeX Generator by Colin Wee", '#'*17, '\n'
    
    if ((argc != 2) or not(digitsOnly(argv[1]))):
        sys.exit("usage: %s <homework number>" % argv[0])
    
    hwNum = int(argv[1])
    outfile = "hw%02d.tex" % hwNum
    
    if not(os.access(os.path.join(DATA_DIR, TEMPLATE_FNAME), os.R_OK)):
        sys.exit("Error! Could not find my modded template at %s" %
                 os.path.join(DATA_DIR, TEMPLATE_FNAME))
    elif (os.path.isfile(outfile) and
          not(YNInput("%s already exists. Overwrite? " % outfile))):  
        print "Exiting..."
        return 0
    elif not(os.access(os.path.join(DATA_DIR, INFO_FNAME), os.R_OK)):
        initProfile()
    
    profile = readProfile()
    
    with open(os.path.join(DATA_DIR, TEMPLATE_FNAME), 'r') as T:
        template = T.read()
        with open(outfile, 'w') as F:
            # I apologize for these lines. Python's string
            for field in INFO_FIELDS.keys():
                template = template.replace(INFO_FIELDS[field], profile[field])
            template = template.replace("homeworkNumber", str(hwNum))
            F.write(template.replace("currentDate", formalDateToday()))
    print "File %r successfully generated" % outfile
    return 0

if __name__ == "__main__":
    main(len(sys.argv), sys.argv)
