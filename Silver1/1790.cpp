#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int getStart(int num) {
    int i = 1;

    if((0 < num) && (num <= 9)) {
        return 0;
    }

    while(true) {
        if((i*9*pow(10, i-1) < num) && (num <= (9*(i+1)*pow(10, i)))) {
            return i;
        }
        i++;
    }
}

int main(void) {
    int n;
    int k;
    scanf("%d %d", &n, &k);

    int len = 0;

    for(int i=1; i<n+1; i++) {
        len += to_string(i).length();
    }

    if(len < k) {
        printf("-1");
    } else {
        printf("%d", getStart(k));
    }

    return 0;
}