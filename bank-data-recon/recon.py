import csv
import re

# global list to hold the new and old files
old_dbname_mapping = {'USDATAMART': 'T24', 'OldDBName': 'NewDbName'}
new_dbname_mapping = {'T24': 'USDATAMART', 'NewDBName': 'OldDbName'}

old_list = []
new_list = []


def print_list_to_file(row_list, filename):
    with open(filename, 'wt') as f:
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
    new_unique_result = []
    exact_match_result = []

    for new_row in new_list:
        # retrieve database name + table name
        found = False
        new_db_name = new_row['NEWSQL']
        new_table_name = new_row['DATASOURCETABLE']
        old_db_name = new_dbname_mapping[new_db_name]
        old_table_name = new_table_name.replace('.', '_')


        for old_row in old_list:
            print(old_row)
            old_table_datalength = re.findall(r'\d+|$', old_row['DATALENGTH'])[0]
            new_table_datalength = re.findall(r'\d+|$', new_row['DATALENGTH'])[0]

            if old_db_name == old_row['SUBJECTAREA'] and old_table_name == old_row['DATASOURCETABLE']:
                if old_row['DATASOURCEFIELD'] == new_row['DATASOURCEFIELD']:
                    if(new_row['M/S'] == "S"):
                        temp = max(new_table_datalength, old_table_datalength)
                        result1 = f"{old_db_name},{old_table_name},{old_row['DATASOURCEFIELD']}, {old_row['DATATYPE']},{temp}"
                        exact_match_result.append(result1)
                    if(new_row['M/S'] == "M" and new_row['DATATYPE']!='decimal'):
                        temp1 = max((3*int(new_table_datalength))+3, int(old_table_datalength))
                        result2 = f"{old_db_name},{old_table_name},{old_row['DATASOURCEFIELD']}, {old_row['DATATYPE']},{temp1}"
                        exact_match_result.append(result2)
                    found = True
                    break
        if not found:
            result = f"{new_db_name},{new_table_name},{new_row['DATASOURCEFIELD']} {new_row['DATATYPE']} {new_row['M/S']} {new_row['DATALENGTH']}"
            print(result)
            new_unique_result.append(result)
    return new_unique_result, exact_match_result


if __name__ == '__main__':
    print("start recon process")
    old_file_name = 'OldTables.txt'
    new_file_name = 'NewTables.txt'
    read_files(old_file_name, new_file_name)
    # compare_old_with_new()

    unique_match, exact_match = compare_new_with_old()
    print(f"UNIQUE FILE")
    print_list_to_file(unique_match, "unique.txt")
    print(f"EXACT FILE")
    print_list_to_file(exact_match, "exact.txt")