def is_safe(report):
    prev_change = 0
    for i, level in enumerate(report[1:]):
        change = level - report[i]
        if abs(change) not in range(1, 4) or change * prev_change < 0:
            return i
        prev_change = change

    return -1


with open('input.txt') as file:
    safe_reports = 0
    results = []
    for line in file.readlines():
        report = [int(level) for level in line.split()]
        fail_pos = is_safe(report)
        fail_pos_mod_1 = fail_pos_mod_2 = fail_pos_mod_3 = None

        if fail_pos >= 0:
            modified_report_1 = report.copy()
            modified_report_2 = report.copy()
            modified_report_1.pop(fail_pos)
            modified_report_2.pop(fail_pos + 1)
            fail_pos_mod_1 = is_safe(modified_report_1)
            fail_pos_mod_2 = is_safe(modified_report_2)

            if fail_pos - 1 >= 0:
                modified_report_3 = report.copy()
                modified_report_3.pop(fail_pos - 1)
                fail_pos_mod_3 = is_safe(modified_report_3)

        if fail_pos == -1 or fail_pos_mod_1 == -1 or fail_pos_mod_2 == -1 or fail_pos_mod_3 == -1:
            safe_reports += 1
            results.append(f'{report} - safe')
        else:
            results.append(f'{report} - NOT safe')

    # print('\n'.join(results))
    print(safe_reports)
