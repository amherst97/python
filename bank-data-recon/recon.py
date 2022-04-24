import csv
import re

# global list to hold the new and old files
old_dbname_mapping = {'USDATAMART': 'T24', 'OldDBName': 'NewDbName'}
new_dbname_mapping = {'T24': 'USDATAMART', 'NewDBName': 'OldDbName'}

old_list = []
new_list = []


def print_list_to_file(row_list):
    output_file = 'output.txt'
    with open(output_file, 'wt') as f:
        f.write('\n'.join(row_list))


def read_files(old_file, new_file):
    print(f'process {old_file} {new_file}')
    with open(old_file, 'r') as f:
        file_reader = csv.DictReader(f, skipinitialspace=True, delimiter='|')
        for row in file_reader:
            #print(row)
            old_list.append(row)

    with open(new_file, 'r') as f:
        file_reader = csv.DictReader(f, skipinitialspace=True, delimiter='|')
        for row in file_reader:
            #print(row)
            new_list.append(row)


def compare_old_with_new():
    for old_row in old_list:
        # retrieve database name + table name
        found = False
        old_db_name = old_row['SUBJECTAREA']
        old_table_name = old_row['DATASOURCETABLE']
        new_db_name = old_dbname_mapping[old_db_name]
        new_table_name = old_table_name.replace('_', '.')
        for new_row in new_list:
            if new_db_name == new_row['NEWSQL'] and new_table_name == new_row['DATASOURCETABLE']:
                # not the same table, no need to compare
                if old_row['DATASOURCEFIELD'] == new_row['DATASOURCEFIELD']:
                    # exact match
                    print(f"Exact Match: {old_db_name}, {old_table_name}, {old_row['DATASOURCEFIELD']}")
                    found = True
                    break
        if not found:
            print(f"{old_db_name} {old_table_name} {old_row['DATASOURCEFIELD']} not exist in the new file")


def compare_new_with_old():
    new_unique_schema = []
    for new_row in new_list:
        # retrieve database name + table name
        found = False
        new_db_name = new_row['NEWSQL']
        new_table_name = new_row['DATASOURCETABLE']
        old_db_name = new_dbname_mapping[new_db_name]
        new_table_name = new_table_name.replace('.', '_')

        new_table_datalength = re.findall('[0-9]]', new_row['DATALENGTH'])
        for old_row in old_list:
            old_table_datalength = re.findall('[0-9]]', old_row['DATALENGTH'])
            if old_db_name == old_row['SUBJECTAREA'] and old_table_name == old_row['DATASOURCETABLE']:
                if old_row['DATASOURCEFIELD'] == new_row['DATASOURCEFIELD']:
                    if(new_row['M/S'] == "S"):

                        old_row['DATALENGTH'] = max(new_table_datalength, old_table_datalength)
                        result = f"{old_row['DATALENGTH']}"
                    found = True
                    break
        if not found:
            result = f"{new_db_name},{new_table_name},{new_row['DATASOURCEFIELD']} {new_row['DATATYPE']} {new_row['M/S']} {new_row['DATALENGTH']}"
            print(result)
            new_unique_schema.append(result)
    return new_unique_schema

if __name__ == '__main__':
    print("start recon process")
    old_file_name = 'OldTables.txt'
    new_file_name = 'NewTables.txt'
    read_files(old_file_name, new_file_name)
    # compare_old_with_new()
    print_list_to_file(compare_new_with_old())
