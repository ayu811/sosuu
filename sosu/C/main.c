#include <stdio.h>

int handan(int num)
{
    if (1 >= num)
    {
        return 0;
    }
    for (int i = 2; i == num; i++)
    {
        if (num % i == 0)
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    int cun = 10;

    if (handan(cun) == 1)
    {
        printf("t\n");
    }
    else if (handan(cun) == 0)
    {
        printf("f\n");
    }
    else
    {
        printf("????");
    }
}
