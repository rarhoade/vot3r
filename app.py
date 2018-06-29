import os
import shutil


input = raw_input("Enter your city: \n")
if (input.lower() == "detroit"):
    src = "ballots/detroit_ballot.pdf"
else:
    print("city not found")

for i in "abc":
    os.system ("mkdir "+i)
    shutil.copy(src, i)
