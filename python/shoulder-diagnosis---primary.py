# Romi Haas, Ljoudmila Busija, Alexandra Gorelik, Denise A O'Connor, Christopher Pierce, Danielle Mazza, Rochelle Buchbinder, 2024.

import sys, csv, re

codes = [{"code":"239958005","system":"snomedct"},{"code":"45326000","system":"snomedct"},{"code":"119633005","system":"snomedct"},{"code":"79092002","system":"snomedct"},{"code":"20904001","system":"snomedct"},{"code":"275334004","system":"snomedct"},{"code":"241633004","system":"snomedct"},{"code":"29592009","system":"snomedct"},{"code":"42262007","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('shoulder-diagnosis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["shoulder-diagnosis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["shoulder-diagnosis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["shoulder-diagnosis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
