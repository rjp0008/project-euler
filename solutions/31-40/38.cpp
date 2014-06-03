#include <iostream>
#include <sstream>

using namespace std;

int UPPERBOUND = 999999999;
int LOWERBOUND = 100000000;

int PANDIGITAL_PRODUCT = 362880;

bool isPandigital(int input){
	bool oneCheck = false;
	if (input > UPPERBOUND || input < LOWERBOUND){
		return false;
	}
	int placeholder = input % 10;
	while (input != 0){
		input = input / 10;
		if (input == 0){
			break;
		}
		if (input % 10 == 1){
			if (oneCheck){
				return false;
			}
			oneCheck = true;
		}
		placeholder = input % 10 * placeholder;
	}
	if (placeholder == PANDIGITAL_PRODUCT){
		return true;
	}
	return false;
}

bool isPandigital(string input){
	int holding;
	stringstream(input) >> holding;
	return isPandigital(holding);
}

int attemptPandigital(int input){
	string attempt = "";
	int currentTry = 1;
	while (attempt.length() < 10){
		ostringstream converter;
		converter << input * currentTry;
		attempt.append(converter.str());
		currentTry++;
		if (isPandigital(attempt))
		{
			int temp;
			stringstream(attempt) >> temp;
			return temp;
		}
	}
	return 0;
}

int main(){
	int max = 0;
	for (int i = 9999; i >  0; i--)
	{
		int found = attemptPandigital(i);
		if (found > max)
		{
			max = found;
		}
	}
	cout << max;
	int test;
	cin >> test;
	return 0;
}

