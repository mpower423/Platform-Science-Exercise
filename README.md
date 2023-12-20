# Platform-Science-Exercise
# Coding Exercise for Platform Science Interview
# Maria Power
# Dec. 19, 2023

# Caclulate the SS for each combination of drivers and destinations  and determine the best match using the following rules:
# If the length of the shipment's destination street name is even, the base suitability score (SS) is the number of vowels in the driver’s
# name multiplied by 1.5. (#note: I am assuming y as a consonant)
# If the length of the shipment's destination street name is odd, the base SS is the number of consonants in the driver’s name multiplied
# by 1.
# If the length of the shipment's destination street name shares any common factors (besides 1) with the length of the driver’s name, the
# SS is increased by 50% above the base SS.
#

# Run instructions:
# Based on Python 3.12
# can be invoked from the commandline with `python ps_excercise.py <destination list filename> <driver list filename>`
# where <destination list filename> is the filename (in the same directory of the prorgram file) and
#       <driver list filename> is the filename (in the same directory of the program file)
# if the filenames are not given, you will be prompted for them.
