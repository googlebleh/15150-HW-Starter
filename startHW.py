#!/usr/bin/env python2
__author__ = "Colin Wee"

import sys, os
import datetime as dt, string
import ConfigParser

DATA_LOC = "resources"
INFO_FNAME = "profile.cfg"
INFO_TITLE = "Student-Specific Information"
INFO_FIELDS = {
    "Name"        : "studentName",
    "Andrew ID"   : "andrewID",
    "Lab Section" : "labSection"
}

def formalDateToday():
    """Return a string representing today's date."""
    return dt.date.today().strftime("%B %d, %Y")

def digitsOnly(s):
    """Return True if s only contains digits only and False otherwise."""
    return (s == ''.join([c for c in s if c in string.digits]))

def YNInput():
    """Robustly accept yes/no input from user."""
    while True:
        cmd = raw_input("Y/N --> ").upper()
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
        proceed = YNInput()
    return i

def initProfile():
    profile = ConfigParser.RawConfigParser()
    profile.add_section(INFO_TITLE)
    for field in INFO_FIELDS:
        profile.set(INFO_TITLE, field, rawInputWithCheck("Enter %s --> " % field))
    with open(os.path.join(DATA_LOC, INFO_FNAME), 'w') as F:
        profile.write(F)

def readProfile():
    profile = ConfigParser.RawConfigParser()
    profile.read(os.path.join(DATA_LOC, INFO_FNAME))
    return tuple([profile.get(field, INFO_FIELDS[field]) for field in INFO_FIELDS])

def main(argc, argv):
    if ((argc != 2) or not(digitsOnly(argv[1]))):
        sys.exit("usage: %s <homework number>" % argv[0])
    
    hwNum = int(argv[1])
    outfile = "hw%02d.tex" % hwNum
    
    # Check all requirements:
        # first time user?
        # resources missing?
        # outfile exists?
    
    with open("resources/template.tex", 'r') as T:
        template = T.read()
        with open(outfile, 'w') as F:
            F.write(template.format(homeworkNumber=hwNum,
                                    currentDate=formalDateToday()))
    return 0

if __name__ == "__main__":
    pass # main(len(sys.argv), sys.argv)
