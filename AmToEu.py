import re, os, shutil, shelve

date_am = re.compile(r"""^(.*?)((1|0)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$""")
# x = date_am.search('p3python 12-21-2021-ise.xls')   # mm-dd-yyyy

for am_date in os.listdir('.'):
    x = date_am.search(am_date)
    if x is None:                      # to ignore the non date format files
        continue

    prefix = x.group(1)
    month = x.group(2)
    day = x.group(4)
    year = x.group(6)
    suffix = x.group(8)

    date_eu = prefix + day + '-' + month + '-' + year + suffix

    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, am_date)
    euroFilename = os.path.join(absWorkingDir, date_eu)

    print(f'Renaming {amerFilename} to {euroFilename}')
    shutil.move(amerFilename, euroFilename)

# print('{}-{}-{}'.format(day, month, year))
