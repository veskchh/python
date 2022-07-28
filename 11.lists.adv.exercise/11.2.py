def version_upgrade(ver):
    ver[-1] += 1
    if ver[-1] == 10:
        ver[-1] = 0
        ver[-2] += 1
        if ver[-2] == 10:
            ver[-2] = 0
            ver[-3] += 1
    print('.'.join(str(s) for s in ver))


version_num = [int(a) for a in input().split('.')]

version_upgrade(version_num)