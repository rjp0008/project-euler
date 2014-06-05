#include <iostream>
using namespace std;
int main(){
	long long sum = 0LL;
	long long temp = 0LL;
	for (int i = 1; i <= 1000; i++){
		temp = i;
		for (int j = 1; j < i; j++)
		{
			temp *= i;
			temp = temp % 10000000000;
		}
		sum += temp;
	}
	cout << sum % 10000000000;
	int stop;
	cin >> stop;
	return 0;
}