'''
input: 5
output:
    * 
   * * 
  *   * 
 *     * 
*       * 
 *     * 
  *   * 
   * * 
    * 
'''

num = int(input().strip())
for i in range(num):
    for k in range(num - i, 1, -1): print(' ', end = '')
    for j in range(i + 1): 
        if not j or j == i: print('*', end = ' ')
        else: print(' ', end = ' ')
    print()
for i in range(num, 0, -1):
    for k in range(num - i + 1): print(' ', end = '')
    for j in range(i - 1): 
        if not j or j == i - 2: print('*', end = ' ')
        else: print(' ', end = ' ')
    print()