#include <iostream>
#include <math.h>
using namespace std;

int upper_bound = 1000000;

bool isPrime(int input){
	if (input == 2)
		return true;
	if (input % 2 == 0 || input == 1)
		return false;
	for (int i = 2; i < sqrt(input) + 1; i++)
		if (input % i == 0)
			return false;
	return true;
}

int intLength(int input){
	int length = 0;
	while (input / 10 != 0){
		length++;
		input /= 10;
	}
	return length;
}

bool isCircularPrime(int input){
	if (!isPrime(input))
		return false;
	int tensDigit = intLength(input);
	int placeHolder = input;
	do{
		int temp = placeHolder % 10;
		placeHolder /= 10;
		placeHolder = (pow(10, tensDigit) * temp) + placeHolder;
		if (!isPrime(placeHolder))
			return false;
	} while (placeHolder != input);
	return true;
}

int main(){
	int counter = 0;
	for (int i = 0; i < upper_bound; i++){
		if (isCircularPrime(i))
			counter++;
	}
	cout << counter;
	int in;
	cin >> in;
	return 0;
}