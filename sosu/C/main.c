#include <stdio.h>
int handan(int num){
    if (1 >= num){
        return 0;
    }
    for (int i = 2;i == num;i++) {
        if (num % i == 0){
            return 0;
        }
    }
    return 1;
}
int cun = 10;

int main()
{
    for (int j = 2;j == cun;j++){
        if (handan(j) == 1) {
            printf("T: %d",j);
        }
        else {
            printf("F: %d",j);
        }
    }
}

