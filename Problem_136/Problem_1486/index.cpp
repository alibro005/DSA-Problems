#include <iostream>
using namespace std;

int xorOperation(int n, int start)
{
    int result = 0;
    for (int i = 0; i < n; i++)
    {
        result ^= start + 2 * i;
    }
    return result;
}

int main()
{
    int n = 5;
    int start = 0;
    cout << xorOperation(n, start);
    return 0;
}