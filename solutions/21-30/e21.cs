using System;
using System.Collections.Generic;

namespace PE
{
    class e21
    {
        static void Main(string[] args)
        {
            var dList = new int[10000];
            int sum = 0;
            for (int i = 0; i < dList.Length; i++)
            {
                dList[i] = d(i);
            }

            for (int i = 0; i <= dList.Length; i++)
            {
                try
                {
                    if (i == dList[dList[i]] && dList[i] != i)
                    {
                        sum += i;
                    }
                }
                catch (IndexOutOfRangeException)
                {
                    //The numbers were not amicable, as d(number) is larger than 10k.
                }
            }
            Console.WriteLine(sum);
        }

        static int d(int number)
        {
            int sum = 0;

            foreach (int divisor in Divisors(number))
            {
                sum += divisor;
            }

            return sum;
        }

        static List<int> Divisors(int numberToDivide)
        {
            var output = new List<int>();

            for (int i = 1; i <= numberToDivide / 2; i++)
            {
                if (numberToDivide % i == 0)
                {
                    output.Add(i);
                }
            }

            return output;
        }
    }
}
