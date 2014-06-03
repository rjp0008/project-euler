#include <iostream>

using namespace std;

int FIRST = 1;
int SECOND = 2;
int THIRD = 3;

struct TRIANGLE{
	int firstSide;
	int secondSide;
	int thirdSide;

	int largestSide;
};

void setLargestSide(TRIANGLE &input){
	if (input.thirdSide >= input.firstSide && input.thirdSide >= input.secondSide)
		input.largestSide = THIRD;
	if (input.secondSide >= input.firstSide&& input.secondSide >= input.thirdSide)
		input.largestSide = SECOND;
	if (input.firstSide >= input.secondSide && input.firstSide >= input.thirdSide)
		input.largestSide = FIRST;
}




int squareSide(int input){
	return input * input;
}

bool isValidTriangle(TRIANGLE input){
	if (input.firstSide <= 0 || input.secondSide <= 0 || input.thirdSide <= 0)
		return false;
	switch (input.largestSide){
	case 1:
		if ((input.firstSide) >= (input.secondSide) + (input.thirdSide))
			return false;
		break;
	case 2:
		if ((input.secondSide) >= (input.firstSide) + (input.thirdSide))
			return false;
		break;
	case 3:
		if ((input.thirdSide) >= (input.firstSide) + (input.secondSide))
			return false;
		break;
	}
	return true;
}

bool isRightTriangle(TRIANGLE input){
	switch (input.largestSide){
	case 1:
		if (squareSide(input.firstSide) == squareSide(input.secondSide) + squareSide(input.thirdSide))
			return true;
		break;
	case 2:
		if (squareSide(input.secondSide) == squareSide(input.firstSide) + squareSide(input.thirdSide))
			return true;
		break;
	case 3:
		if (squareSide(input.thirdSide) == squareSide(input.firstSide) + squareSide(input.secondSide))
			return true;
		break;
	}
	return false;
}

bool isValidAndRight(TRIANGLE input){
	return isValidTriangle(input) && isRightTriangle(input);
}

int numberOfRightTrianges(int perimeter){
	int output = 0;
	TRIANGLE test;
	for (int firstSide = 1; firstSide < perimeter; firstSide++){
		for (int secondSide = 1; secondSide < perimeter; secondSide++){
			test.firstSide = firstSide;
			test.secondSide = secondSide;
			test.thirdSide = perimeter - firstSide - secondSide;
			setLargestSide(test);
			if (isValidAndRight(test)){
				output++;
			}
		}
	}
	return output;
}


int main(){
	int p;
	int max = 0;
	int temp;
	for (int i = 1000; i > 3; i--){
		temp = numberOfRightTrianges(i);
		if (temp > max){
			max = temp;
			p = i;
		}
	}
	cout << p;
	int input;
	cin >> input;
	return 0;
}

