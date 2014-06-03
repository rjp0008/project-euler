using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace pecs
{
    class e50
    {
        private const int UPPERLIMIT = 1000000;
        static void Main(string[] args)
        {
            int maxLength = 0;
            int theTarget = 0;
            int temp;
            //Console.WriteLine(getSummationListLength(listOfPrimes(1000),953));
            for (int i = UPPERLIMIT; i > 0; i--)
            {
                if (isPrime(i))
                {
                    temp = getSummationListLength(listOfPrimes(UPPERLIMIT), i);
                    if (temp > maxLength)
                    {
                        maxLength = temp;
                        theTarget = i;
                    }
                }
            }
            Console.WriteLine(theTarget);
            Console.ReadLine();

        }

        private static Boolean isPrime(int input)
        {
            //check if two
            if (input == 2)
                return true;
            //check is one or even
            if (input == 1 || input % 2 == 0)
                return false;
            for (int i = 3; i < Math.Sqrt(input) + 1; i += 2)
            {
                if (input % i == 0)
                    return false;
            }
            return true;
        }

        private static List<int> listOfPrimes(int max)
        {
            List<int> output = new List<int>();
            for (int i = 0; i <= max; i++)
            {
                if (isPrime(i))
                {
                    output.Add(i);
                }
            }
            return output;
        }

        private static int getSummationListLength(List<int> primes, int target)
        {
            List<int> primelist = new List<int>();
            foreach (int prime in primes)
            {
                primelist.Add(prime);
            }
            int sum = 0;
            int length = 0;
            int removeCount = 0;
            while (primes.Count > 0)
            {
                sum += primes.First();
                length++;
                primes.RemoveAt(0);
                while (sum > target)
                {
                    sum -= primelist.ElementAt(removeCount);
                    removeCount++;
                    length--;
                }
                if (sum == target)
                {
                    return length;
                }
                if (sum == 0)
                    break;
            }

            return 0;
        }
    }
}
