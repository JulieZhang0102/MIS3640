a = """
Alabama 	9
Alaska 	3
Arizona 	11
Arkansas 	6
California 	55
Colorado 	9
Connecticut 	7
Delaware 	3
District of Columbia 	3
Florida 	29
Georgia 	16
Hawaii 	4
Idaho 	4
Illinois 	20
Indiana 	11
Iowa 	6
Kansas 	6
Kentucky 	8
Louisiana 	8
Maine 	4
Maryland 	10
Massachusetts 	11
Michigan 	16
Minnesota 	10
Mississippi 	6
Missouri 	10
Montana 	3
Nebraska 	5
Nevada 	6
New Hampshire 	4
New Jersey 	14
New Mexico 	5
New York 	29
North Carolina 	15
North Dakota 	3
Ohio 	18
Oklahoma 	7
Oregon 	7
Pennsylvania 	20
Rhode Island 	4
South Carolina 	9
South Dakota 	3
Tennessee 	11
Texas 	38
Utah 	6
Vermont 	3
Virginia 	13
Washington 	12
West Virginia 	5
Wisconsin 	10
Wyoming 	3
"""

d = dict()

for line in a.strip().split('\n'):
    # print(line)
    *state, num = line.split()
    state = ' '.join(state)
    d[state] = int(num)

import pprint
pprint.pprint(d)

# TO-DO: convert it to csv file or pandas dataframe