import csv

file1 = "ideas_for_test/work_with_csv/random.csv"
file2 = "ideas_for_test/work_with_csv/random-michaels.csv"
output_file = "result_Doskoch.csv"

data = set()

for file in [file1, file2]:
    with open(file, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            data.add(tuple(row))

with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in sorted(data):
        writer.writerow(row)

print(f"✅ Result saved to {output_file}")