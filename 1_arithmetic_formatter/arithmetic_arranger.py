def arithmetic_arranger(problems, opt=False):
    dash = ''
    l1, l2, l3 = zip(*[(st.split()[0], st.split()[1], st.split()[2]) for st in problems])

    l_dash = []
    l_up = []
    l_bottom = []

    for i in l2:
        if i == '/' or i == '*':
            return "Error: Operator must be '+' or '-'."

    if len(problems) > 5:
        return 'Error: Too many problems.'

    for i, j in zip(l1, l3):
        if i.isdigit() is False or j.isdigit() is False:
            return 'Error: Numbers must only contain digits.'

    for i, j in zip(l1, l3):
        if len(i) > 4 or len(j) > 4:
            return 'Error: Numbers cannot be more than four digits.'

    if opt is False:
        for i, s, j in zip(l1, l2, l3):
            if len(j) > len(i):
                dash = dash + ('-' * (len(j) + 2))
                l_dash.append(dash)
                l_bottom.append(s + ' ' + j)
            elif len(i) > len(j):
                dash = dash + ('-' * (len(i) + 2))
                l_dash.append(dash)
                l_bottom.append(s + (' ' * (len(dash) - len(j) - 1)) + j)
            else:
                dash = dash + ('-' * (len(i) + 2))
                l_dash.append(dash)
                l_bottom.append(s + ' ' + j)
            l_up.append(' ' * (len(dash) - len(i)) + i)
            dash = ''

        s1 = '    '.join(l_up)
        s2 = '    '.join(l_bottom)
        s3 = '    '.join(l_dash)
        arranged_problems = '\n'.join((s1, s2, s3))
        return arranged_problems

    elif opt is True:
        l4 = [int(e1) + int(e2) for e1, e2 in zip(l1, l3)]
        l_sum = []

        for i, s, j, k in zip(l1, l2, l3, l4):
            if len(j) > len(i):
                dash = dash + ('-' * (len(j) + 2))
                l_dash.append(dash)
                l_bottom.append(s + ' ' + j)
            elif len(i) > len(j):
                dash = dash + ('-' * (len(i) + 2))
                l_dash.append(dash)
                l_bottom.append(s + (' ' * (len(dash) - len(j) - 1)) + j)
            else:
                dash = dash + ('-' * (len(i) + 2))
                l_dash.append(dash)
                l_bottom.append(s + ' ' + j)
            l_sum.append(' ' * (len(dash) - len(str(k))) + str(k))
            l_up.append(' ' * (len(dash) - len(i)) + i)
            dash = ''

        s1 = '    '.join(l_up)
        s2 = '    '.join(l_bottom)
        s3 = '    '.join(l_dash)
        s4 = '    '.join(l_sum)
        arranged_problems = '\n'.join((s1, s2, s3, s4))
        return arranged_problems